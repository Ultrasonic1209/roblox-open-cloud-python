from enum import StrEnum


class RobloxOpencloudScopeconfigurationV2TargetPartTypesValueType(StrEnum):
    VALUE_TYPE_INT64 = "VALUE_TYPE_INT64"
    VALUE_TYPE_INVALID = "VALUE_TYPE_INVALID"
    VALUE_TYPE_STRING = "VALUE_TYPE_STRING"

    def __str__(self) -> str:
        return str(self.value)
