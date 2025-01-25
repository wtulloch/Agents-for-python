import jwt

from .bot_auth_configuration import BotAuthConfiguration

class JwtTokenValidation():
    def __init__(self, configuration: BotAuthConfiguration):
        self.configuration = configuration

    def validate_token(self, token: str):
        pass
    
    def _get_public_key_or_secret(self, token: str):
        decoded_token = jwt.decode(token, options={"verify_signature": False})
        if 'appid' in decoded_token:
            return decoded_token['appid']
        return None