from typing import Optional

from microsoft.agents.authentication import ClaimsIdentity
from microsoft.agents.connector import ConnectorClientBase

from .channel_service_client_factory_base import ChannelServiceClientFactoryBase


class RestChannelServiceClientFactory(ChannelServiceClientFactoryBase):
    async def create_connector_client(
        self,
        claims_identity: ClaimsIdentity,
        service_url: str,
        audience: str,
        scopes: Optional[list[str]] = None,
        use_anonymous: bool = False,
    ) -> ConnectorClientBase:
        pass
