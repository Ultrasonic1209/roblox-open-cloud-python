from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_contacts_api_response_set_user_tag_response_model_status import (
    RobloxContactsApiResponseSetUserTagResponseModelStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxContactsApiResponseSetUserTagResponseModel")


@_attrs_define
class RobloxContactsApiResponseSetUserTagResponseModel:
    """
    Attributes:
        status (RobloxContactsApiResponseSetUserTagResponseModelStatus | Unset): Status message to be sent to the setter
            of the userTag ['Success' = 0, 'Moderated' = 1]
    """

    status: RobloxContactsApiResponseSetUserTagResponseModelStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: RobloxContactsApiResponseSetUserTagResponseModelStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RobloxContactsApiResponseSetUserTagResponseModelStatus(_status)

        roblox_contacts_api_response_set_user_tag_response_model = cls(
            status=status,
        )

        return roblox_contacts_api_response_set_user_tag_response_model
