from enum import Enum


class GetV1DeveloperProductsIconsSize(str, Enum):
    VALUE_0 = "150x150"
    VALUE_1 = "420x420"

    def __str__(self) -> str:
        return str(self.value)
