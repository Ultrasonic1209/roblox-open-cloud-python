from enum import Enum


class RobloxItemConfigurationApiReleaseConfigurationResponseModelSaleAvailabilityLocationsItem(str, Enum):
    ALLUNIVERSES = "AllUniverses"
    CATALOG = "Catalog"
    MYUNIVERSES = "MyUniverses"
    UNDEFINED = "Undefined"

    def __str__(self) -> str:
        return str(self.value)
