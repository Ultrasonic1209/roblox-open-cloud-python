from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiAvatarModelsBodyColorsModelV4")


@_attrs_define
class RobloxApiAvatarModelsBodyColorsModelV4:
    """A model containing RGB hex colors for each body part.

    Attributes:
        head_color (str | Unset): The RGB hex color for head color, e.g. #FFFFFF
        torso_color (str | Unset): The RGB hex color for torso color, e.g. #FFFFFF
        right_arm_color (str | Unset): The RGB hex color for right arm color, e.g. #FFFFFF
        left_arm_color (str | Unset): The RGB hex color for left arm color, e.g. #FFFFFF
        right_leg_color (str | Unset): The RGB hex color for right leg color, e.g. #FFFFFF
        left_leg_color (str | Unset): The RGB hex color for left leg color, e.g. #FFFFFF
    """

    head_color: str | Unset = UNSET
    torso_color: str | Unset = UNSET
    right_arm_color: str | Unset = UNSET
    left_arm_color: str | Unset = UNSET
    right_leg_color: str | Unset = UNSET
    left_leg_color: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        head_color = self.head_color

        torso_color = self.torso_color

        right_arm_color = self.right_arm_color

        left_arm_color = self.left_arm_color

        right_leg_color = self.right_leg_color

        left_leg_color = self.left_leg_color

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if head_color is not UNSET:
            field_dict["headColor"] = head_color
        if torso_color is not UNSET:
            field_dict["torsoColor"] = torso_color
        if right_arm_color is not UNSET:
            field_dict["rightArmColor"] = right_arm_color
        if left_arm_color is not UNSET:
            field_dict["leftArmColor"] = left_arm_color
        if right_leg_color is not UNSET:
            field_dict["rightLegColor"] = right_leg_color
        if left_leg_color is not UNSET:
            field_dict["leftLegColor"] = left_leg_color

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        head_color = d.pop("headColor", UNSET)

        torso_color = d.pop("torsoColor", UNSET)

        right_arm_color = d.pop("rightArmColor", UNSET)

        left_arm_color = d.pop("leftArmColor", UNSET)

        right_leg_color = d.pop("rightLegColor", UNSET)

        left_leg_color = d.pop("leftLegColor", UNSET)

        roblox_api_avatar_models_body_colors_model_v4 = cls(
            head_color=head_color,
            torso_color=torso_color,
            right_arm_color=right_arm_color,
            left_arm_color=left_arm_color,
            right_leg_color=right_leg_color,
            left_leg_color=left_leg_color,
        )

        return roblox_api_avatar_models_body_colors_model_v4
