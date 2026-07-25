from enum import Enum


class InternalPublicV1TargetingDimensionsDevicesItem(str, Enum):
    CONSOLE = "CONSOLE"
    DESKTOP = "DESKTOP"
    PHONE = "PHONE"
    TABLET = "TABLET"

    def __str__(self) -> str:
        return str(self.value)
