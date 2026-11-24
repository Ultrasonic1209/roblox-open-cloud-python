from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UniverseSocialLink")


@_attrs_define
class UniverseSocialLink:
    """A social link that may be associated with the universe.

    Can only be removed when using a field mask.

        Attributes:
            title (str | Unset): The title of the social link.
            uri (str | Unset): The uri of the social link.
    """

    title: str | Unset = UNSET
    uri: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        uri = self.uri

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        uri = d.pop("uri", UNSET)

        universe_social_link = cls(
            title=title,
            uri=uri,
        )

        return universe_social_link
