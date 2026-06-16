from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_engine_instance_details import RobloxEngineInstanceDetails


T = TypeVar("T", bound="RobloxEngineInstance")


@_attrs_define
class RobloxEngineInstance:
    """Instance is the base class for all classes in the Roblox class hierarchy.

    Attributes:
        id (str | Unset): The unique identifier for an instance.
            Format: lower-case hexadecimal characters
            Example: 44b188da-ce63-2b47-02e9-c68d004b5664
        parent (str | Unset): The parent of the Instance.
            Format: lower-case hexadecimal characters
            Example: 44b188da-ce63-2b47-02e9-c68d004b5664
        name (str | Unset): A non-unique identifier of the Instance.
        details (RobloxEngineInstanceDetails | Unset): Contains instance type-specific details about a data model
            instance.
    """

    id: str | Unset = UNSET
    parent: str | Unset = UNSET
    name: str | Unset = UNSET
    details: RobloxEngineInstanceDetails | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        parent = self.parent

        name = self.name

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if parent is not UNSET:
            field_dict["Parent"] = parent
        if name is not UNSET:
            field_dict["Name"] = name
        if details is not UNSET:
            field_dict["Details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_engine_instance_details import RobloxEngineInstanceDetails

        d = dict(src_dict)
        id = d.pop("Id", UNSET)

        parent = d.pop("Parent", UNSET)

        name = d.pop("Name", UNSET)

        _details = d.pop("Details", UNSET)
        details: RobloxEngineInstanceDetails | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = RobloxEngineInstanceDetails.from_dict(_details)

        roblox_engine_instance = cls(
            id=id,
            parent=parent,
            name=name,
            details=details,
        )

        roblox_engine_instance.additional_properties = d
        return roblox_engine_instance

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
