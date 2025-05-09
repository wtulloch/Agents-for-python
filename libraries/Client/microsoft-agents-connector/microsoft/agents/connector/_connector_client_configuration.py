# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.10.3, generator: @autorest/python@6.27.0)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any

from azure.core.pipeline import policies
from azure.core.credentials_async import AsyncTokenCredential

VERSION = "unknown"


class ConnectorConfiguration:  # pylint: disable=too-many-instance-attributes
    """Configuration for Connector.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async import AsyncTokenCredential
    """

    def __init__(self, credential: AsyncTokenCredential, **kwargs: Any) -> None:
        self.credential = credential
        self.credential_scopes = kwargs.pop("credential_scopes", [])
        kwargs.setdefault("sdk_moniker", "connector/{}".format(VERSION))
        self.polling_interval = kwargs.get("polling_interval", 30)
        self._configure(**kwargs)

    def _configure(self, **kwargs: Any) -> None:
        self.user_agent_policy = kwargs.get(
            "user_agent_policy"
        ) or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(
            **kwargs
        )
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get(
            "logging_policy"
        ) or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get(
            "http_logging_policy"
        ) or policies.HttpLoggingPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get(
            "custom_hook_policy"
        ) or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get(
            "redirect_policy"
        ) or policies.AsyncRedirectPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.AsyncRetryPolicy(
            **kwargs
        )
        self.authentication_policy = kwargs.get("authentication_policy")
        """
        if not self.credential_scopes and not self.authentication_policy:
            raise ValueError(
                "You must provide either credential_scopes or authentication_policy as kwargs"
            )
        """
        if self.credential and not self.authentication_policy:
            scopes = self.credential_scopes or []
            self.authentication_policy = policies.AsyncBearerTokenCredentialPolicy(
                self.credential, *scopes, **kwargs
            )
