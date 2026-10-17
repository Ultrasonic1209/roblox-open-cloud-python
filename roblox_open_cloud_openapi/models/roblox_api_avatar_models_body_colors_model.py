from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiAvatarModelsBodyColorsModel")


@_attrs_define
class RobloxApiAvatarModelsBodyColorsModel:
    """A model container BrickColor ids for each body part.

    Attributes:
        head_color_id (int | Unset): The BrickColor id for head color
        torso_color_id (int | Unset): The BrickColor id for torso color
        right_arm_color_id (int | Unset): The BrickColor id for right arm color
        left_arm_color_id (int | Unset): The BrickColor id for left arm color
        right_leg_color_id (int | Unset): The BrickColor id for right leg color
        left_leg_color_id (int | Unset): The BrickColor id for left leg color
    """

    head_color_id: int | Unset = UNSET
    torso_color_id: int | Unset = UNSET
    right_arm_color_id: int | Unset = UNSET
    left_arm_color_id: int | Unset = UNSET
    right_leg_color_id: int | Unset = UNSET
    left_leg_color_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        head_color_id = self.head_color_id

        torso_color_id = self.torso_color_id

        right_arm_color_id = self.right_arm_color_id

        left_arm_color_id = self.left_arm_color_id

        right_leg_color_id = self.right_leg_color_id

        left_leg_color_id = self.left_leg_color_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if head_color_id is not UNSET:
            field_dict["headColorId"] = head_color_id
        if torso_color_id is not UNSET:
            field_dict["torsoColorId"] = torso_color_id
        if right_arm_color_id is not UNSET:
            field_dict["rightArmColorId"] = right_arm_color_id
        if left_arm_color_id is not UNSET:
            field_dict["leftArmColorId"] = left_arm_color_id
        if right_leg_color_id is not UNSET:
            field_dict["rightLegColorId"] = right_leg_color_id
        if left_leg_color_id is not UNSET:
            field_dict["leftLegColorId"] = left_leg_color_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        head_color_id = d.pop("headColorId", UNSET)

        torso_color_id = d.pop("torsoColorId", UNSET)

        right_arm_color_id = d.pop("rightArmColorId", UNSET)

        left_arm_color_id = d.pop("leftArmColorId", UNSET)

        right_leg_color_id = d.pop("rightLegColorId", UNSET)

        left_leg_color_id = d.pop("leftLegColorId", UNSET)

        roblox_api_avatar_models_body_colors_model = cls(
            head_color_id=head_color_id,
            torso_color_id=torso_color_id,
            right_arm_color_id=right_arm_color_id,
            left_arm_color_id=left_arm_color_id,
            right_leg_color_id=right_leg_color_id,
            left_leg_color_id=left_leg_color_id,
        )

        return roblox_api_avatar_models_body_colors_model
