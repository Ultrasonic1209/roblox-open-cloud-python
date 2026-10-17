from enum import StrEnum


class SearchAudioTypeModel(StrEnum):
    MUSIC = "Music"
    SOUND_EFFECT = "SoundEffect"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
