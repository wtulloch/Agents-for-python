from abc import abstractmethod
from typing import Protocol

from .bot_sign_in_base import BotSignInBase
from .user_token_base import UserTokenBase

class UserTokenClientBase(Protocol):
    @property
    @abstractmethod
    def bot_sign_in(self) -> BotSignInBase:
        pass

    @property
    @abstractmethod
    def user_token(self) -> UserTokenBase:
        pass