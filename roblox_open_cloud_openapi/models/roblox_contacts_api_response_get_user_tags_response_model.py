from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxContactsApiResponseGetUserTagsResponseModel")


@_attrs_define
class RobloxContactsApiResponseGetUserTagsResponseModel:
    """
    Attributes:
        target_user_id (int | Unset):
        target_user_tag (str | Unset):
    """

    target_user_id: int | Unset = UNSET
    target_user_tag: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        target_user_id = self.target_user_id

        target_user_tag = self.target_user_tag

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if target_user_id is not UNSET:
            field_dict["targetUserId"] = target_user_id
        if target_user_tag is not UNSET:
            field_dict["targetUserTag"] = target_user_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_user_id = d.pop("targetUserId", UNSET)

        target_user_tag = d.pop("targetUserTag", UNSET)

        roblox_contacts_api_response_get_user_tags_response_model = cls(
            target_user_id=target_user_id,
            target_user_tag=target_user_tag,
        )

        return roblox_contacts_api_response_get_user_tags_response_model
