from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_localization_tables_api_ingest_content_metadata_place_information import (
        RobloxLocalizationTablesApiIngestContentMetadataPlaceInformation,
    )


T = TypeVar("T", bound="RobloxLocalizationTablesApiIngestContentMetadata")


@_attrs_define
class RobloxLocalizationTablesApiIngestContentMetadata:
    """The metadata of an ingest content request.

    Attributes:
        place_information (RobloxLocalizationTablesApiIngestContentMetadataPlaceInformation | Unset): The place
            information metadata of an ingest content request.
    """

    place_information: RobloxLocalizationTablesApiIngestContentMetadataPlaceInformation | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        place_information: dict[str, Any] | Unset = UNSET
        if not isinstance(self.place_information, Unset):
            place_information = self.place_information.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if place_information is not UNSET:
            field_dict["placeInformation"] = place_information

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_localization_tables_api_ingest_content_metadata_place_information import (
            RobloxLocalizationTablesApiIngestContentMetadataPlaceInformation,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _place_information = d.pop("placeInformation", UNSET)
        place_information: RobloxLocalizationTablesApiIngestContentMetadataPlaceInformation | Unset
        if isinstance(_place_information, Unset):
            place_information = UNSET
        else:
            place_information = RobloxLocalizationTablesApiIngestContentMetadataPlaceInformation.from_dict(
                _place_information
            )

        roblox_localization_tables_api_ingest_content_metadata = cls(
            place_information=place_information,
        )

        return roblox_localization_tables_api_ingest_content_metadata
