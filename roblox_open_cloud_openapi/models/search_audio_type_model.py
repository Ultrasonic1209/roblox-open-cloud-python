from enum import Enum


class SearchAudioTypeModel(str, Enum):
    MUSIC = "Music"
    SOUND_EFFECT = "SoundEffect"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
