from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiAvatarModelsAvatarThumbnailCustomizationCameraModel")


@_attrs_define
class RobloxApiAvatarModelsAvatarThumbnailCustomizationCameraModel:
    """A model describing a the camera details for a single avatar thumbnail customization.

    Attributes:
        field_of_view_deg (float | Unset): Field of view for the camera, in degrees.
        y_rot_deg (float | Unset): Rotation around y axis, in degrees.
        distance_scale (float | Unset): There's a natural camera distance we calculate based on avatar size. Apply this
            scale to that distance.
    """

    field_of_view_deg: float | Unset = UNSET
    y_rot_deg: float | Unset = UNSET
    distance_scale: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        field_of_view_deg = self.field_of_view_deg

        y_rot_deg = self.y_rot_deg

        distance_scale = self.distance_scale

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if field_of_view_deg is not UNSET:
            field_dict["fieldOfViewDeg"] = field_of_view_deg
        if y_rot_deg is not UNSET:
            field_dict["yRotDeg"] = y_rot_deg
        if distance_scale is not UNSET:
            field_dict["distanceScale"] = distance_scale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        field_of_view_deg = d.pop("fieldOfViewDeg", UNSET)

        y_rot_deg = d.pop("yRotDeg", UNSET)

        distance_scale = d.pop("distanceScale", UNSET)

        roblox_api_avatar_models_avatar_thumbnail_customization_camera_model = cls(
            field_of_view_deg=field_of_view_deg,
            y_rot_deg=y_rot_deg,
            distance_scale=distance_scale,
        )

        return roblox_api_avatar_models_avatar_thumbnail_customization_camera_model
