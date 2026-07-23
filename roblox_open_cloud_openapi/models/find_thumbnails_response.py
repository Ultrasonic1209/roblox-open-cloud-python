from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.homepage_thumbnail import HomepageThumbnail


T = TypeVar("T", bound="FindThumbnailsResponse")


@_attrs_define
class FindThumbnailsResponse:
    """
    Attributes:
        homepage_thumbnails (list[HomepageThumbnail]):
        next_cursor (None | str | Unset):
    """

    homepage_thumbnails: list[HomepageThumbnail]
    next_cursor: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        homepage_thumbnails = []
        for homepage_thumbnails_item_data in self.homepage_thumbnails:
            homepage_thumbnails_item = homepage_thumbnails_item_data.to_dict()
            homepage_thumbnails.append(homepage_thumbnails_item)

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "homepageThumbnails": homepage_thumbnails,
            }
        )
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.homepage_thumbnail import HomepageThumbnail

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        homepage_thumbnails = []
        _homepage_thumbnails = d.pop("homepageThumbnails")
        for homepage_thumbnails_item_data in _homepage_thumbnails:
            homepage_thumbnails_item = HomepageThumbnail.from_dict(homepage_thumbnails_item_data)

            homepage_thumbnails.append(homepage_thumbnails_item)

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))

        find_thumbnails_response = cls(
            homepage_thumbnails=homepage_thumbnails,
            next_cursor=next_cursor,
        )

        return find_thumbnails_response
