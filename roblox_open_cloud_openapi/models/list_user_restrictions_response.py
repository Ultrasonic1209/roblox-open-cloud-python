from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_restriction import UserRestriction


T = TypeVar("T", bound="ListUserRestrictionsResponse")


@_attrs_define
class ListUserRestrictionsResponse:
    """A list of UserRestrictions in the parent collection.

    Attributes:
        user_restrictions (list[UserRestriction] | Unset): The UserRestrictions from the specified Universe or Place.
        next_page_token (str | Unset): A token that you can send as a `pageToken` parameter to retrieve the next
            page. If this field is omitted, there are no subsequent pages.
    """

    user_restrictions: list[UserRestriction] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_restrictions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user_restrictions, Unset):
            user_restrictions = []
            for user_restrictions_item_data in self.user_restrictions:
                user_restrictions_item = user_restrictions_item_data.to_dict()
                user_restrictions.append(user_restrictions_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_restrictions is not UNSET:
            field_dict["userRestrictions"] = user_restrictions
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_restriction import UserRestriction

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _user_restrictions = d.pop("userRestrictions", UNSET)
        user_restrictions: list[UserRestriction] | Unset = UNSET
        if _user_restrictions is not UNSET:
            user_restrictions = []
            for user_restrictions_item_data in _user_restrictions:
                user_restrictions_item = UserRestriction.from_dict(user_restrictions_item_data)

                user_restrictions.append(user_restrictions_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_user_restrictions_response = cls(
            user_restrictions=user_restrictions,
            next_page_token=next_page_token,
        )

        list_user_restrictions_response.additional_properties = d
        return list_user_restrictions_response

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
