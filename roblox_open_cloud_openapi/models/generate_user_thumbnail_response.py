from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GenerateUserThumbnailResponse")


@_attrs_define
class GenerateUserThumbnailResponse:
    """Returns the URL for the user's avatar thumbnail.

    Attributes:
        image_uri (str | Unset): URI for the generated thumbnail.
    """

    image_uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_uri = self.image_uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image_uri is not UNSET:
            field_dict["imageUri"] = image_uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image_uri = d.pop("imageUri", UNSET)

        generate_user_thumbnail_response = cls(
            image_uri=image_uri,
        )

        generate_user_thumbnail_response.additional_properties = d
        return generate_user_thumbnail_response

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
