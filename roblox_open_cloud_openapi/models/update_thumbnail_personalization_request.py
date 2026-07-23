from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="UpdateThumbnailPersonalizationRequest")


@_attrs_define
class UpdateThumbnailPersonalizationRequest:
    """
    Attributes:
        homepage_thumbnail_ids (list[str]):
        id (str):
    """

    homepage_thumbnail_ids: list[str]
    id: str

    def to_dict(self) -> dict[str, Any]:
        homepage_thumbnail_ids = self.homepage_thumbnail_ids

        id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "homepageThumbnailIds": homepage_thumbnail_ids,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        homepage_thumbnail_ids = cast(list[str], d.pop("homepageThumbnailIds"))

        id = d.pop("id")

        update_thumbnail_personalization_request = cls(
            homepage_thumbnail_ids=homepage_thumbnail_ids,
            id=id,
        )

        return update_thumbnail_personalization_request
