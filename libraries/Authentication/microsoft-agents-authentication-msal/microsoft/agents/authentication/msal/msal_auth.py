from microsoft.agents.authentication import AccessTokenProviderBase
from typing import Optional
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from collections import defaultdict
from datetime import datetime, timedelta
from urllib.parse import urlparse

class MsalAuth(AccessTokenProviderBase):
    def __init__(self, msal_configuration_section):
        pass

    async def get_access_token(self, resource_url: str, scopes: list[str], force_refresh: bool = False) -> str:
        if not urlparse(resource_url).scheme:
            raise ValueError("Invalid instance URL")

        instance_uri = urlparse(resource_url)
        local_scopes = self._resolve_scopes_list(instance_uri, scopes)

        if instance_uri in self._cache_list:
            if not force_refresh:
                access_token = self._cache_list[instance_uri].msal_auth_result.access_token
                token_expires_on = self._cache_list[instance_uri].msal_auth_result.expires_on
                if token_expires_on and token_expires_on < datetime.utcnow() - timedelta(seconds=30):
                    access_token = ""
                    del self._cache_list[instance_uri]

                if access_token:
                    return access_token
            else:
                del self._cache_list[instance_uri]

        msal_auth_client = self._create_client_application()

        auth_result_payload = None
        if isinstance(msal_auth_client, IConfidentialClientApplication):
            auth_result = await msal_auth_client.acquire_token_for_client(local_scopes).with_force_refresh(True).execute_async()
            auth_result_payload = ExecuteAuthenticationResults(
                msal_auth_result=auth_result,
                target_service_url=instance_uri,
                msal_auth_client=msal_auth_client
            )
        elif isinstance(msal_auth_client, IManagedIdentityApplication):
            auth_result = await msal_auth_client.acquire_token_for_managed_identity(resource_url).with_force_refresh(True).execute_async()
            auth_result_payload = ExecuteAuthenticationResults(
                msal_auth_result=auth_result,
                target_service_url=instance_uri,
                msal_auth_client=msal_auth_client
            )
        else:
            raise NotImplementedError()

        self._cache_list[instance_uri] = auth_result_payload

        return auth_result_payload.msal_auth_result.access_token

    def _create_client_application(self):
        msal_auth_client = None

        if self._connection_settings.auth_type == AuthTypes.SystemManagedIdentity:
            msal_auth_client = ManagedIdentityApplicationBuilder.create(ManagedIdentityId.SystemAssigned) \
                .with_logging(IdentityLoggerAdapter(self._logger), self._system_service_provider.get_service(MsalAuthConfigurationOptions).MSALEnabledLogPII) \
                .with_http_client_factory(self._msal_http_client) \
                .build()
        elif self._connection_settings.auth_type == AuthTypes.UserManagedIdentity:
            msal_auth_client = ManagedIdentityApplicationBuilder.create(ManagedIdentityId.with_user_assigned_client_id(self._connection_settings.client_id)) \
                .with_logging(IdentityLoggerAdapter(self._logger), self._system_service_provider.get_service(MsalAuthConfigurationOptions).MSALEnabledLogPII) \
                .with_http_client_factory(self._msal_http_client) \
                .build()
        else:
            c_app_builder = ConfidentialClientApplicationBuilder.create_with_application_options(
                ConfidentialClientApplicationOptions(
                    client_id=self._connection_settings.client_id,
                    enable_pii_logging=self._system_service_provider.get_service(MsalAuthConfigurationOptions).MSALEnabledLogPII,
                    log_level=Identity.Client.LogLevel.Verbose,
                )
            ).with_logging(IdentityLoggerAdapter(self._logger), self._system_service_provider.get_service(MsalAuthConfigurationOptions).MSALEnabledLogPII) \
                .with_legacy_cache_compatibility(False) \
                .with_cache_options(CacheOptions(True)) \
                .with_http_client_factory(self._msal_http_client)

            if self._connection_settings.authority:
                c_app_builder.with_authority(self._connection_settings.authority)
            else:
                c_app_builder.with_tenant_id(self._connection_settings.tenant_id)

            if self._connection_settings.auth_type in [AuthTypes.Certificate, AuthTypes.CertificateSubjectName]:
                c_app_builder.with_certificate(self._certificate_provider.get_certificate(), self._connection_settings.send_x5c)
            elif self._connection_settings.auth_type == AuthTypes.ClientSecret:
                c_app_builder.with_client_secret(self._connection_settings.client_secret)
            else:
                raise NotImplementedError()

            msal_auth_client = c_app_builder.build()

        return msal_auth_client

    def _resolve_scopes_list(self, instance_url, scopes=None):
        if scopes:
            return scopes

        templist = []
        for scope in self._connection_settings.scopes:
            scope_placeholder = scope
            if "{instance}" in scope_placeholder.lower():
                scope_placeholder = scope_placeholder.replace("{instance}", f"{instance_url.scheme}://{instance_url.netloc}")
            templist.append(scope_placeholder)
        return templist