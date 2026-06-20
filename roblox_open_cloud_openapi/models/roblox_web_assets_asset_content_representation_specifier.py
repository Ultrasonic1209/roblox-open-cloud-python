from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxWebAssetsAssetContentRepresentationSpecifier")


@_attrs_define
class RobloxWebAssetsAssetContentRepresentationSpecifier:
    """
    Attributes:
        format_ (str | Unset):
        major_version (str | Unset):
        fidelity (str | Unset):
        skip_generation_if_not_exist (bool | Unset):
    """

    format_: str | Unset = UNSET
    major_version: str | Unset = UNSET
    fidelity: str | Unset = UNSET
    skip_generation_if_not_exist: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_

        major_version = self.major_version

        fidelity = self.fidelity

        skip_generation_if_not_exist = self.skip_generation_if_not_exist

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if format_ is not UNSET:
            field_dict["format"] = format_
        if major_version is not UNSET:
            field_dict["majorVersion"] = major_version
        if fidelity is not UNSET:
            field_dict["fidelity"] = fidelity
        if skip_generation_if_not_exist is not UNSET:
            field_dict["skipGenerationIfNotExist"] = skip_generation_if_not_exist

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        format_ = d.pop("format", UNSET)

        major_version = d.pop("majorVersion", UNSET)

        fidelity = d.pop("fidelity", UNSET)

        skip_generation_if_not_exist = d.pop("skipGenerationIfNotExist", UNSET)

        roblox_web_assets_asset_content_representation_specifier = cls(
            format_=format_,
            major_version=major_version,
            fidelity=fidelity,
            skip_generation_if_not_exist=skip_generation_if_not_exist,
        )

        return roblox_web_assets_asset_content_representation_specifier
