from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Roblox2AssetdeliveryV3RepresentationItem")


@_attrs_define
class Roblox2AssetdeliveryV3RepresentationItem:
    """
    Attributes:
        format_ (str | Unset):
        major_version (str | Unset):
        fidelity (str | Unset):
    """

    format_: str | Unset = UNSET
    major_version: str | Unset = UNSET
    fidelity: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_

        major_version = self.major_version

        fidelity = self.fidelity

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if format_ is not UNSET:
            field_dict["format"] = format_
        if major_version is not UNSET:
            field_dict["majorVersion"] = major_version
        if fidelity is not UNSET:
            field_dict["fidelity"] = fidelity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        format_ = d.pop("format", UNSET)

        major_version = d.pop("majorVersion", UNSET)

        fidelity = d.pop("fidelity", UNSET)

        roblox_2_assetdelivery_v3_representation_item = cls(
            format_=format_,
            major_version=major_version,
            fidelity=fidelity,
        )

        return roblox_2_assetdelivery_v3_representation_item
