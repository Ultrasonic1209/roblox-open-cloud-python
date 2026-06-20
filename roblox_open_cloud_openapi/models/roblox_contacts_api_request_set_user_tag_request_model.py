from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxContactsApiRequestSetUserTagRequestModel")


@_attrs_define
class RobloxContactsApiRequestSetUserTagRequestModel:
    """
    Attributes:
        target_user_id (int | Unset): The userId of the target of the userTag.
        user_tag (str | Unset): The userTag to be set
    """

    target_user_id: int | Unset = UNSET
    user_tag: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        target_user_id = self.target_user_id

        user_tag = self.user_tag

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if target_user_id is not UNSET:
            field_dict["targetUserId"] = target_user_id
        if user_tag is not UNSET:
            field_dict["userTag"] = user_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        target_user_id = d.pop("targetUserId", UNSET)

        user_tag = d.pop("userTag", UNSET)

        roblox_contacts_api_request_set_user_tag_request_model = cls(
            target_user_id=target_user_id,
            user_tag=user_tag,
        )

        return roblox_contacts_api_request_set_user_tag_request_model
