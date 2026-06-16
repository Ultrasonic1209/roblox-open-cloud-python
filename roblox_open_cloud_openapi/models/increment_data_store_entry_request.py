from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.increment_data_store_entry_request_attributes import IncrementDataStoreEntryRequestAttributes


T = TypeVar("T", bound="IncrementDataStoreEntryRequest")


@_attrs_define
class IncrementDataStoreEntryRequest:
    """Increments the entry value.

    If the value is not numeric, this request fails.

        Attributes:
            amount (float | Unset): The amount by which to increment the entry value. Both the existing value
                and the increment amount must be integers.
            users (list[str] | Unset): Users associated with the entry.

                If this is not provided, existing user IDs are cleared.
            attributes (IncrementDataStoreEntryRequestAttributes | Unset): An arbitrary set of attributes associated with
                the entry.

                If this is not provided, existing attributes are cleared.
    """

    amount: float | Unset = UNSET
    users: list[str] | Unset = UNSET
    attributes: IncrementDataStoreEntryRequestAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        users: list[str] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = self.users

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if users is not UNSET:
            field_dict["users"] = users
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.increment_data_store_entry_request_attributes import IncrementDataStoreEntryRequestAttributes

        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        users = cast(list[str], d.pop("users", UNSET))

        _attributes = d.pop("attributes", UNSET)
        attributes: IncrementDataStoreEntryRequestAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = IncrementDataStoreEntryRequestAttributes.from_dict(_attributes)

        increment_data_store_entry_request = cls(
            amount=amount,
            users=users,
            attributes=attributes,
        )

        increment_data_store_entry_request.additional_properties = d
        return increment_data_store_entry_request

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
