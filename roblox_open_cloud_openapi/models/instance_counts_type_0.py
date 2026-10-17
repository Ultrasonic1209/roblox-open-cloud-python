from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstanceCountsType0")


@_attrs_define
class InstanceCountsType0:
    """Represents the count of various instance types within an asset.
    See [Instance](https://create.roblox.com/docs/reference/engine/classes/Instance).

        Attributes:
            script (int | Unset): The number of Script instances.
            mesh_part (int | Unset): The number of MeshPart instances.
            animation (int | Unset): The number of Animation instances.
            decal (int | Unset): The number of Decal instances.
            audio (int | Unset): The number of Audio instances.
            tool (int | Unset): The number of Tool instances.
    """

    script: int | Unset = UNSET
    mesh_part: int | Unset = UNSET
    animation: int | Unset = UNSET
    decal: int | Unset = UNSET
    audio: int | Unset = UNSET
    tool: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        script = self.script

        mesh_part = self.mesh_part

        animation = self.animation

        decal = self.decal

        audio = self.audio

        tool = self.tool

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if script is not UNSET:
            field_dict["script"] = script
        if mesh_part is not UNSET:
            field_dict["meshPart"] = mesh_part
        if animation is not UNSET:
            field_dict["animation"] = animation
        if decal is not UNSET:
            field_dict["decal"] = decal
        if audio is not UNSET:
            field_dict["audio"] = audio
        if tool is not UNSET:
            field_dict["tool"] = tool

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        script = d.pop("script", UNSET)

        mesh_part = d.pop("meshPart", UNSET)

        animation = d.pop("animation", UNSET)

        decal = d.pop("decal", UNSET)

        audio = d.pop("audio", UNSET)

        tool = d.pop("tool", UNSET)

        instance_counts_type_0 = cls(
            script=script,
            mesh_part=mesh_part,
            animation=animation,
            decal=decal,
            audio=audio,
            tool=tool,
        )

        return instance_counts_type_0
