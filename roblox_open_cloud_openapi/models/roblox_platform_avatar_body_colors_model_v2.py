from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxPlatformAvatarBodyColorsModelV2")


@_attrs_define
class RobloxPlatformAvatarBodyColorsModelV2:
    """
    Attributes:
        head_color_3 (str | Unset):
        torso_color_3 (str | Unset):
        right_arm_color_3 (str | Unset):
        left_arm_color_3 (str | Unset):
        right_leg_color_3 (str | Unset):
        left_leg_color_3 (str | Unset):
    """

    head_color_3: str | Unset = UNSET
    torso_color_3: str | Unset = UNSET
    right_arm_color_3: str | Unset = UNSET
    left_arm_color_3: str | Unset = UNSET
    right_leg_color_3: str | Unset = UNSET
    left_leg_color_3: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        head_color_3 = self.head_color_3

        torso_color_3 = self.torso_color_3

        right_arm_color_3 = self.right_arm_color_3

        left_arm_color_3 = self.left_arm_color_3

        right_leg_color_3 = self.right_leg_color_3

        left_leg_color_3 = self.left_leg_color_3

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if head_color_3 is not UNSET:
            field_dict["headColor3"] = head_color_3
        if torso_color_3 is not UNSET:
            field_dict["torsoColor3"] = torso_color_3
        if right_arm_color_3 is not UNSET:
            field_dict["rightArmColor3"] = right_arm_color_3
        if left_arm_color_3 is not UNSET:
            field_dict["leftArmColor3"] = left_arm_color_3
        if right_leg_color_3 is not UNSET:
            field_dict["rightLegColor3"] = right_leg_color_3
        if left_leg_color_3 is not UNSET:
            field_dict["leftLegColor3"] = left_leg_color_3

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        head_color_3 = d.pop("headColor3", UNSET)

        torso_color_3 = d.pop("torsoColor3", UNSET)

        right_arm_color_3 = d.pop("rightArmColor3", UNSET)

        left_arm_color_3 = d.pop("leftArmColor3", UNSET)

        right_leg_color_3 = d.pop("rightLegColor3", UNSET)

        left_leg_color_3 = d.pop("leftLegColor3", UNSET)

        roblox_platform_avatar_body_colors_model_v2 = cls(
            head_color_3=head_color_3,
            torso_color_3=torso_color_3,
            right_arm_color_3=right_arm_color_3,
            left_arm_color_3=left_arm_color_3,
            right_leg_color_3=right_leg_color_3,
            left_leg_color_3=left_leg_color_3,
        )

        return roblox_platform_avatar_body_colors_model_v2
