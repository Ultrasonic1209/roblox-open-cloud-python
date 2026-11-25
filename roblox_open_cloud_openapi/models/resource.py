from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.resource_type import ResourceType

T = TypeVar("T", bound="Resource")


@_attrs_define
class Resource:
    """
    Attributes:
        resource_type (ResourceType):
        resource_id (int):
    """

    resource_type: ResourceType
    resource_id: int

    def to_dict(self) -> dict[str, Any]:
        resource_type = self.resource_type.value

        resource_id = self.resource_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "resourceType": resource_type,
                "resourceId": resource_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_type = ResourceType(d.pop("resourceType"))

        resource_id = d.pop("resourceId")

        resource = cls(
            resource_type=resource_type,
            resource_id=resource_id,
        )

        return resource
