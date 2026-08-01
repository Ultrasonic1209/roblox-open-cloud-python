from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ThumbnailResponse")


@_attrs_define
class ThumbnailResponse:
    """
    Attributes:
        media_id (int | Unset):
        rank (int | Unset):
    """

    media_id: int | Unset = UNSET
    rank: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        media_id = self.media_id

        rank = self.rank

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if media_id is not UNSET:
            field_dict["mediaId"] = media_id
        if rank is not UNSET:
            field_dict["rank"] = rank

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        media_id = d.pop("mediaId", UNSET)

        rank = d.pop("rank", UNSET)

        thumbnail_response = cls(
            media_id=media_id,
            rank=rank,
        )

        return thumbnail_response
