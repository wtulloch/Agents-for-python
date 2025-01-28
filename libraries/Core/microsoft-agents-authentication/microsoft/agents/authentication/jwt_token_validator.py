import jwt

from jwt import PyJWKClient, PyJWK, decode, get_unverified_header

from .bot_auth_configuration import BotAuthConfiguration


class JwtTokenValidator:
    def __init__(self, configuration: BotAuthConfiguration):
        self.configuration = configuration

    def validate_token(self, token: str):
        key = self._get_public_key_or_secret()
        decoded_token = jwt.decode(
            token, key=key, algorithms=["RS256"], options={"verify_audience": False}
        )
        if decoded_token["aud"] != self.configuration.CLIENT_ID:
            raise ValueError("Invalid audience.")
        return decoded_token

    def _get_public_key_or_secret(self, token: str) -> PyJWK:
        header = get_unverified_header(token)
        unverified_payload: dict = decode(token, options={"verify_signature": False})

        jwksUri = (
            "https://login.botframework.com/v1/.well-known/keys"
            if unverified_payload.get("iss") == "https://api.botframework.com"
            else f"https://login.microsoftonline.com/{self.configuration.TENANT_ID}/discovery/v2.0/keys"
        )

        jwks_client = PyJWKClient(jwksUri)

        key = jwks_client.get_signing_key(header["kid"])
        return key
