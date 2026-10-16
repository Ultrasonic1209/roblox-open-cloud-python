from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxLocalizationTablesApiIngestContentMetadataPlaceInformation")


@_attrs_define
class RobloxLocalizationTablesApiIngestContentMetadataPlaceInformation:
    """The place information metadata of an ingest content request.

    Attributes:
        place_id (int | Unset): The place id of an ingest content request.
        place_version_number (int | Unset): The place version number of an ingest content request.
    """

    place_id: int | Unset = UNSET
    place_version_number: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        place_id = self.place_id

        place_version_number = self.place_version_number

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if place_id is not UNSET:
            field_dict["placeId"] = place_id
        if place_version_number is not UNSET:
            field_dict["placeVersionNumber"] = place_version_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        place_id = d.pop("placeId", UNSET)

        place_version_number = d.pop("placeVersionNumber", UNSET)

        roblox_localization_tables_api_ingest_content_metadata_place_information = cls(
            place_id=place_id,
            place_version_number=place_version_number,
        )

        return roblox_localization_tables_api_ingest_content_metadata_place_information
