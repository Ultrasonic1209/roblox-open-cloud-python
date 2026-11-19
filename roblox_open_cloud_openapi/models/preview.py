from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Preview")


@_attrs_define
class Preview:
    """An asset preview.

    Attributes:
        asset (None | str | Unset): The preview asset path.
        alt_text (None | str | Unset): Alt text for the preview asset.
    """

    asset: None | str | Unset = UNSET
    alt_text: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset: None | str | Unset
        if isinstance(self.asset, Unset):
            asset = UNSET
        else:
            asset = self.asset

        alt_text: None | str | Unset
        if isinstance(self.alt_text, Unset):
            alt_text = UNSET
        else:
            alt_text = self.alt_text

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset is not UNSET:
            field_dict["asset"] = asset
        if alt_text is not UNSET:
            field_dict["altText"] = alt_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_asset(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asset = _parse_asset(d.pop("asset", UNSET))

        def _parse_alt_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alt_text = _parse_alt_text(d.pop("altText", UNSET))

        preview = cls(
            asset=asset,
            alt_text=alt_text,
        )

        return preview
