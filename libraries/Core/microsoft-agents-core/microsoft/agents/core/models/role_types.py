from enum import Enum

class RoleTypes(str, Enum):
    user = "user"
    bot = "bot"
    skill = "skill"
