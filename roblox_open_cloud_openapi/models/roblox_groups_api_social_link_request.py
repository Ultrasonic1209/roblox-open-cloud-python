from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_groups_api_social_link_request_type import RobloxGroupsApiSocialLinkRequestType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiSocialLinkRequest")


@_attrs_define
class RobloxGroupsApiSocialLinkRequest:
    """An update request for a social link

    Attributes:
        type_ (RobloxGroupsApiSocialLinkRequestType | Unset): What type of social media this points to
        url (str | Unset): The url of the link
        title (str | Unset): The title of the link
    """

    type_: RobloxGroupsApiSocialLinkRequestType | Unset = UNSET
    url: str | Unset = UNSET
    title: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: int | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        url = self.url

        title = self.title

        field_dict: dict[str, Any] = {}

        field_dict.update({})
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
        _type_ = d.pop("type", UNSET)
        type_: RobloxGroupsApiSocialLinkRequestType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RobloxGroupsApiSocialLinkRequestType(_type_)

        url = d.pop("url", UNSET)

        title = d.pop("title", UNSET)

        roblox_groups_api_social_link_request = cls(
            type_=type_,
            url=url,
            title=title,
        )

        return roblox_groups_api_social_link_request
