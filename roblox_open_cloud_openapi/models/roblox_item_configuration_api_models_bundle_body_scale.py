from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsBundleBodyScale")


@_attrs_define
class RobloxItemConfigurationApiModelsBundleBodyScale:
    """The body scale of the bundle.

    Attributes:
        height (float | Unset): Determines by what factor the height (top-to-bottom distance) is scaled.
            Range 0.9-1.05.
        width (float | Unset): Determines by what factor the width (left-to-right distance) is
            scaled. Range: 0.7-1.0.
        head (float | Unset): Determines by what factor the Head is scaled. Range 0.95-1.0.
        body_type (float | Unset): Determines by which the shape of a Humanoid rig is interpolated. Range
            0.0-1.0.
        proportion (float | Unset): Determines how wide (0) or narrow (1) a Humanoid rig. Range 0.0-1.0.
    """

    height: float | Unset = UNSET
    width: float | Unset = UNSET
    head: float | Unset = UNSET
    body_type: float | Unset = UNSET
    proportion: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        height = self.height

        width = self.width

        head = self.head

        body_type = self.body_type

        proportion = self.proportion

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if height is not UNSET:
            field_dict["height"] = height
        if width is not UNSET:
            field_dict["width"] = width
        if head is not UNSET:
            field_dict["head"] = head
        if body_type is not UNSET:
            field_dict["bodyType"] = body_type
        if proportion is not UNSET:
            field_dict["proportion"] = proportion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        height = d.pop("height", UNSET)

        width = d.pop("width", UNSET)

        head = d.pop("head", UNSET)

        body_type = d.pop("bodyType", UNSET)

        proportion = d.pop("proportion", UNSET)

        roblox_item_configuration_api_models_bundle_body_scale = cls(
            height=height,
            width=width,
            head=head,
            body_type=body_type,
            proportion=proportion,
        )

        return roblox_item_configuration_api_models_bundle_body_scale
