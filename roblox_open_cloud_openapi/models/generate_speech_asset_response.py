from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GenerateSpeechAssetResponse")


@_attrs_define
class GenerateSpeechAssetResponse:
    """Contains a generated audio asset in MPEG-2 Audio Layer III (MP3) format.

    Attributes:
        asset_id (str | Unset): The generated audio asset ID.
        remaining_quota (int | Unset): The remaining quota (the remaining number of requests available
            to the user this calendar month).
    """

    asset_id: str | Unset = UNSET
    remaining_quota: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        remaining_quota = self.remaining_quota

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if remaining_quota is not UNSET:
            field_dict["remainingQuota"] = remaining_quota

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = d.pop("assetId", UNSET)

        remaining_quota = d.pop("remainingQuota", UNSET)

        generate_speech_asset_response = cls(
            asset_id=asset_id,
            remaining_quota=remaining_quota,
        )

        generate_speech_asset_response.additional_properties = d
        return generate_speech_asset_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
