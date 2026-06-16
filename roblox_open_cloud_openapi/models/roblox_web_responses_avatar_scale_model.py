from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxWebResponsesAvatarScaleModel")


@_attrs_define
class RobloxWebResponsesAvatarScaleModel:
    """
    Attributes:
        height (float | Unset):
        width (float | Unset):
        head (float | Unset):
        depth (float | Unset):
        proportion (float | Unset):
        body_type (float | Unset):
    """

    height: float | Unset = UNSET
    width: float | Unset = UNSET
    head: float | Unset = UNSET
    depth: float | Unset = UNSET
    proportion: float | Unset = UNSET
    body_type: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        height = self.height

        width = self.width

        head = self.head

        depth = self.depth

        proportion = self.proportion

        body_type = self.body_type

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if height is not UNSET:
            field_dict["height"] = height
        if width is not UNSET:
            field_dict["width"] = width
        if head is not UNSET:
            field_dict["head"] = head
        if depth is not UNSET:
            field_dict["depth"] = depth
        if proportion is not UNSET:
            field_dict["proportion"] = proportion
        if body_type is not UNSET:
            field_dict["bodyType"] = body_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        height = d.pop("height", UNSET)

        width = d.pop("width", UNSET)

        head = d.pop("head", UNSET)

        depth = d.pop("depth", UNSET)

        proportion = d.pop("proportion", UNSET)

        body_type = d.pop("bodyType", UNSET)

        roblox_web_responses_avatar_scale_model = cls(
            height=height,
            width=width,
            head=head,
            depth=depth,
            proportion=proportion,
            body_type=body_type,
        )

        return roblox_web_responses_avatar_scale_model
