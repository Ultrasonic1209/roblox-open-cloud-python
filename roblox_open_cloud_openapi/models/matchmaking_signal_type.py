from enum import StrEnum


class MatchmakingSignalType(StrEnum):
    AGE = "Age"
    DEVICETYPE = "DeviceType"
    INVALID = "Invalid"
    LANGUAGE = "Language"
    LATENCY = "Latency"
    OCCUPANCY = "Occupancy"
    PLAYHISTORY = "PlayHistory"
    PREFERREDPLAYERS = "PreferredPlayers"
    TEXTCHAT = "TextChat"
    VOICECHAT = "VoiceChat"

    def __str__(self) -> str:
        return str(self.value)
