from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_groups_api_get_social_link_response_social_links_verification_status import (
    RobloxGroupsApiGetSocialLinkResponseSocialLinksVerificationStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_social_link_response import RobloxGroupsApiSocialLinkResponse


T = TypeVar("T", bound="RobloxGroupsApiGetSocialLinkResponse")


@_attrs_define
class RobloxGroupsApiGetSocialLinkResponse:
    """A social link response from a create request

    Attributes:
        data (list[RobloxGroupsApiSocialLinkResponse] | Unset):
        social_links_verification_status (RobloxGroupsApiGetSocialLinkResponseSocialLinksVerificationStatus | Unset):
    """

    data: list[RobloxGroupsApiSocialLinkResponse] | Unset = UNSET
    social_links_verification_status: RobloxGroupsApiGetSocialLinkResponseSocialLinksVerificationStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        social_links_verification_status: int | Unset = UNSET
        if not isinstance(self.social_links_verification_status, Unset):
            social_links_verification_status = self.social_links_verification_status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if social_links_verification_status is not UNSET:
            field_dict["socialLinksVerificationStatus"] = social_links_verification_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_social_link_response import RobloxGroupsApiSocialLinkResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _data = d.pop("data", UNSET)
        data: list[RobloxGroupsApiSocialLinkResponse] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = RobloxGroupsApiSocialLinkResponse.from_dict(data_item_data)

                data.append(data_item)

        _social_links_verification_status = d.pop("socialLinksVerificationStatus", UNSET)
        social_links_verification_status: RobloxGroupsApiGetSocialLinkResponseSocialLinksVerificationStatus | Unset
        if isinstance(_social_links_verification_status, Unset):
            social_links_verification_status = UNSET
        else:
            social_links_verification_status = RobloxGroupsApiGetSocialLinkResponseSocialLinksVerificationStatus(
                _social_links_verification_status
            )

        roblox_groups_api_get_social_link_response = cls(
            data=data,
            social_links_verification_status=social_links_verification_status,
        )

        return roblox_groups_api_get_social_link_response
