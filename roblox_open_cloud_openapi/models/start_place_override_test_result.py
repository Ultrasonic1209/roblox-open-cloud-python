from enum import Enum


class StartPlaceOverrideTestResult(str, Enum):
    DATASTOREENTRYNOTFOUND = "DataStoreEntryNotFound"
    DATASTOREERROR = "DataStoreError"
    DATASTORENOTFOUND = "DataStoreNotFound"
    FIELDMISSING = "FieldMissing"
    FOUND = "Found"
    INVALID = "Invalid"
    NOOVERRIDECONFIGURED = "NoOverrideConfigured"
    PLACENOTINEXPERIENCE = "PlaceNotInExperience"
    PLACENOTPUBLISHED = "PlaceNotPublished"
    VALUEPARSEFAILURE = "ValueParseFailure"

    def __str__(self) -> str:
        return str(self.value)
