from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.instance import Instance


T = TypeVar("T", bound="ListInstanceChildrenResponse")


@_attrs_define
class ListInstanceChildrenResponse:
    """Returns a list of the instance's children.

    Attributes:
        instances (list[Instance] | Unset): A list of children instances.

        next_page_token (str | Unset): A token, which can be sent as `page_token` to retrieve the next page.
            If this field is omitted, there are no subsequent pages.
    """

    instances: list[Instance] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instances: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.instances, Unset):
            instances = []
            for instances_item_data in self.instances:
                instances_item = instances_item_data.to_dict()
                instances.append(instances_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instances is not UNSET:
            field_dict["instances"] = instances
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.instance import Instance

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _instances = d.pop("instances", UNSET)
        instances: list[Instance] | Unset = UNSET
        if _instances is not UNSET:
            instances = []
            for instances_item_data in _instances:
                instances_item = Instance.from_dict(instances_item_data)

                instances.append(instances_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_instance_children_response = cls(
            instances=instances,
            next_page_token=next_page_token,
        )

        list_instance_children_response.additional_properties = d
        return list_instance_children_response

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
