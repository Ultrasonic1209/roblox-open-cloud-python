from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_engine_instance import RobloxEngineInstance


T = TypeVar("T", bound="Instance")


@_attrs_define
class Instance:
    """Represents a data model instance.

    Attributes:
        path (str | Unset): The resource path of the instance.

            Format: `universes/{universe_id}/places/{place_id}/instances/{instance_id}` Example:
            universes/123/places/123/instances/0123456789abcdef0123456789abcdef.
        has_children (bool | Unset): whether the instance has any children instance Example: True.
        engine_instance (RobloxEngineInstance | Unset): Instance is the base class for all classes in the Roblox class
            hierarchy.
    """

    path: str | Unset = UNSET
    has_children: bool | Unset = UNSET
    engine_instance: RobloxEngineInstance | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        has_children = self.has_children

        engine_instance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.engine_instance, Unset):
            engine_instance = self.engine_instance.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if has_children is not UNSET:
            field_dict["hasChildren"] = has_children
        if engine_instance is not UNSET:
            field_dict["engineInstance"] = engine_instance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_engine_instance import RobloxEngineInstance

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        path = d.pop("path", UNSET)

        has_children = d.pop("hasChildren", UNSET)

        _engine_instance = d.pop("engineInstance", UNSET)
        engine_instance: RobloxEngineInstance | Unset
        if isinstance(_engine_instance, Unset):
            engine_instance = UNSET
        else:
            engine_instance = RobloxEngineInstance.from_dict(_engine_instance)

        instance = cls(
            path=path,
            has_children=has_children,
            engine_instance=engine_instance,
        )

        instance.additional_properties = d
        return instance

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
