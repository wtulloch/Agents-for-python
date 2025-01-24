from enum import Enum


class EndOfConversationCodes(str, Enum):
    unknown = "unknown"
    completed_successfully = "completedSuccessfully"
    user_cancelled = "userCancelled"
    bot_timed_out = "botTimedOut"
    bot_issued_invalid_message = "botIssuedInvalidMessage"
    channel_failed = "channelFailed"
