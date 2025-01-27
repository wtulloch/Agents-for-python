import jwt

from jwt import PyJWKClient

from .bot_auth_configuration import BotAuthConfiguration


class JwtTokenValidation:
    def __init__(self, configuration: BotAuthConfiguration):
        self.configuration = configuration

    def validate_token(self, token: str):

        key = self._get_public_key_or_secret()
        pass

    def _get_public_key_or_secret(self, token: str):
        header = jwt.get_unverified_header(token)
        unverified_payload: dict = jwt.decode(token, options={"verify_signature": False})

        jwksUri = (
            "https://login.botframework.com/v1/.well-known/keys"
            if unverified_payload.get("iss") == "https://api.botframework.com"
            else f"https://login.microsoftonline.com/{self.configuration.TENANT_ID}/discovery/v2.0/keys"
        )
        
        jwks_client = PyJWKClient(jwksUri)
        
        key = jwks_client.get_signing_key(header["kid"])
        if "appid" in unverified_payload:
            return unverified_payload["appid"]
        return None
