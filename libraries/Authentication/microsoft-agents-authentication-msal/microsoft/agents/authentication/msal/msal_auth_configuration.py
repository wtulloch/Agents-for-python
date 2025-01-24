from typing import Protocol, Optional

from .auth_types import AuthTypes


class MsalAuthConfiguration(Protocol):
    """
    Configuration for MSAL authentication.
    """

    AUTH_TYPE: AuthTypes
    TENANT_ID: Optional[str]
    CLIENT_ID: Optional[str]
    CLIENT_SECRET: Optional[str]
    CERT_PEM_FILE: Optional[str]
    CERT_KEY_FILE: Optional[str]
    CONNECTION_NAME: Optional[str]
    SCOPES: Optional[list[str]]
    AUTHORITY: Optional[str]

    @property
    def ISSUERS(self) -> list[str]:
        """
        Gets the list of issuers.
        """
        return [
            "https://api.botframework.com",
            f"https://sts.windows.net/{self.TENANT_ID}/",
            f"https://login.microsoftonline.com/{self.TENANT_ID}/v2.0",
        ]
