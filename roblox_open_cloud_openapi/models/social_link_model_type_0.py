from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.link_type import LinkType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialLinkModelType0")


@_attrs_define
class SocialLinkModelType0:
    """Model for a Social Link.

    Attributes:
        link_type (LinkType | Unset):
        url (None | str | Unset): Gets or sets the Url.
        title (None | str | Unset): Gets or sets the title.
    """

    link_type: LinkType | Unset = UNSET
    url: None | str | Unset = UNSET
    title: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        link_type: int | Unset = UNSET
        if not isinstance(self.link_type, Unset):
            link_type = self.link_type.value

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if link_type is not UNSET:
            field_dict["linkType"] = link_type
        if url is not UNSET:
            field_dict["url"] = url
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _link_type = d.pop("linkType", UNSET)
        link_type: LinkType | Unset
        if isinstance(_link_type, Unset):
            link_type = UNSET
        else:
            link_type = LinkType(_link_type)

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        social_link_model_type_0 = cls(
            link_type=link_type,
            url=url,
            title=title,
        )

        return social_link_model_type_0
