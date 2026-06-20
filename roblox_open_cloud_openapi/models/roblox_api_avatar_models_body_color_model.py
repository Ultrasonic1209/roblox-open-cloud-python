from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiAvatarModelsBodyColorModel")


@_attrs_define
class RobloxApiAvatarModelsBodyColorModel:
    """A model container BrickColor ids for each body part.

    Attributes:
        brick_color_id (int | Unset): The BrickColor id
        hex_color (str | Unset): The hex color, e.g. #FFFFFF
        name (str | Unset): The name of the BrickColor
    """

    brick_color_id: int | Unset = UNSET
    hex_color: str | Unset = UNSET
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        brick_color_id = self.brick_color_id

        hex_color = self.hex_color

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if brick_color_id is not UNSET:
            field_dict["brickColorId"] = brick_color_id
        if hex_color is not UNSET:
            field_dict["hexColor"] = hex_color
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        brick_color_id = d.pop("brickColorId", UNSET)

        hex_color = d.pop("hexColor", UNSET)

        name = d.pop("name", UNSET)

        roblox_api_avatar_models_body_color_model = cls(
            brick_color_id=brick_color_id,
            hex_color=hex_color,
            name=name,
        )

        return roblox_api_avatar_models_body_color_model
