from enum import StrEnum


class InternalPublicV1TargetingDimensionsDevicesItem(StrEnum):
    CONSOLE = "CONSOLE"
    DESKTOP = "DESKTOP"
    PHONE = "PHONE"
    TABLET = "TABLET"

    def __str__(self) -> str:
        return str(self.value)
