from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectMeshSummaryType0")


@_attrs_define
class ObjectMeshSummaryType0:
    """Provides a summary of the mesh characteristics of an object, such as triangle and vertex counts.

    Attributes:
        triangles (int | Unset): The total number of triangles in the object's mesh.
        vertices (int | Unset): The total number of vertices in the object's mesh.
    """

    triangles: int | Unset = UNSET
    vertices: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        triangles = self.triangles

        vertices = self.vertices

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if triangles is not UNSET:
            field_dict["triangles"] = triangles
        if vertices is not UNSET:
            field_dict["vertices"] = vertices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        triangles = d.pop("triangles", UNSET)

        vertices = d.pop("vertices", UNSET)

        object_mesh_summary_type_0 = cls(
            triangles=triangles,
            vertices=vertices,
        )

        return object_mesh_summary_type_0
