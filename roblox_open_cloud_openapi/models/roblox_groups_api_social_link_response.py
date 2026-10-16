from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_groups_api_social_link_response_type import RobloxGroupsApiSocialLinkResponseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiSocialLinkResponse")


@_attrs_define
class RobloxGroupsApiSocialLinkResponse:
    """A social link response from a create request

    Attributes:
        id (int | Unset): The id of the social link
        type_ (RobloxGroupsApiSocialLinkResponseType | Unset): What type of social media (including Roblox Group) this
            points to ['Facebook' = 0, 'Twitter' = 1, 'YouTube' = 2, 'Twitch' = 3, 'GooglePlus' = 4, 'Discord' = 5,
            'RobloxGroup' = 6, 'Amazon' = 7, 'Guilded' = 8]
        url (str | Unset): The url of the link
        title (str | Unset): The title of the link
    """

    id: int | Unset = UNSET
    type_: RobloxGroupsApiSocialLinkResponseType | Unset = UNSET
    url: str | Unset = UNSET
    title: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: int | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        url = self.url

        title = self.title

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RobloxGroupsApiSocialLinkResponseType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RobloxGroupsApiSocialLinkResponseType(_type_)

        url = d.pop("url", UNSET)

        title = d.pop("title", UNSET)

        roblox_groups_api_social_link_response = cls(
            id=id,
            type_=type_,
            url=url,
            title=title,
        )

        return roblox_groups_api_social_link_response
