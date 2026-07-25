from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalPublicV1AdFormat")


@_attrs_define
class InternalPublicV1AdFormat:
    """
    Attributes:
        format_ (str | Unset): The ad format name.
        height (int | Unset): The format height in pixels.
        width (int | Unset): The format width in pixels.
    """

    format_: str | Unset = UNSET
    height: int | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_

        height = self.height

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if format_ is not UNSET:
            field_dict["format"] = format_
        if height is not UNSET:
            field_dict["height"] = height
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        format_ = d.pop("format", UNSET)

        height = d.pop("height", UNSET)

        width = d.pop("width", UNSET)

        internal_public_v1_ad_format = cls(
            format_=format_,
            height=height,
            width=width,
        )

        internal_public_v1_ad_format.additional_properties = d
        return internal_public_v1_ad_format

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
