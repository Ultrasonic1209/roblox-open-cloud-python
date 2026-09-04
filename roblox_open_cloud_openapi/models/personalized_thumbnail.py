from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.homepage_thumbnail_status import HomepageThumbnailStatus
from ..models.personalized_thumbnail_status import PersonalizedThumbnailStatus

T = TypeVar("T", bound="PersonalizedThumbnail")


@_attrs_define
class PersonalizedThumbnail:
    """A homepage thumbnail and its status within a personalization configuration.

    Attributes:
        homepage_thumbnail_id (str): The unique identifier of the homepage thumbnail.
        asset_id (int): The identifier of the image asset used by the thumbnail.
        personalized_thumbnail_status (PersonalizedThumbnailStatus): The status of a thumbnail within a personalization
            configuration.
        homepage_thumbnail_status (HomepageThumbnailStatus): The availability status of a homepage thumbnail.
    """

    homepage_thumbnail_id: str
    asset_id: int
    personalized_thumbnail_status: PersonalizedThumbnailStatus
    homepage_thumbnail_status: HomepageThumbnailStatus

    def to_dict(self) -> dict[str, Any]:
        homepage_thumbnail_id = self.homepage_thumbnail_id

        asset_id = self.asset_id

        personalized_thumbnail_status = self.personalized_thumbnail_status.value

        homepage_thumbnail_status = self.homepage_thumbnail_status.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "homepageThumbnailId": homepage_thumbnail_id,
                "assetId": asset_id,
                "personalizedThumbnailStatus": personalized_thumbnail_status,
                "homepageThumbnailStatus": homepage_thumbnail_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        homepage_thumbnail_id = d.pop("homepageThumbnailId")

        asset_id = d.pop("assetId")

        personalized_thumbnail_status = PersonalizedThumbnailStatus(d.pop("personalizedThumbnailStatus"))

        homepage_thumbnail_status = HomepageThumbnailStatus(d.pop("homepageThumbnailStatus"))

        personalized_thumbnail = cls(
            homepage_thumbnail_id=homepage_thumbnail_id,
            asset_id=asset_id,
            personalized_thumbnail_status=personalized_thumbnail_status,
            homepage_thumbnail_status=homepage_thumbnail_status,
        )

        return personalized_thumbnail
