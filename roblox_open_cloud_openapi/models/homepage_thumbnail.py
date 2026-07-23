from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.homepage_thumbnail_status import HomepageThumbnailStatus
from ..models.personalized_config_status import PersonalizedConfigStatus
from ..models.thumbnail_personalization_api_moderation_status import ThumbnailPersonalizationApiModerationStatus

T = TypeVar("T", bound="HomepageThumbnail")


@_attrs_define
class HomepageThumbnail:
    """
    Attributes:
        homepage_thumbnail_id (str):
        asset_id (int):
        moderation_status (ThumbnailPersonalizationApiModerationStatus):
        personalized_config_status (PersonalizedConfigStatus):
        homepage_thumbnail_status (HomepageThumbnailStatus):
    """

    homepage_thumbnail_id: str
    asset_id: int
    moderation_status: ThumbnailPersonalizationApiModerationStatus
    personalized_config_status: PersonalizedConfigStatus
    homepage_thumbnail_status: HomepageThumbnailStatus

    def to_dict(self) -> dict[str, Any]:
        homepage_thumbnail_id = self.homepage_thumbnail_id

        asset_id = self.asset_id

        moderation_status = self.moderation_status.value

        personalized_config_status = self.personalized_config_status.value

        homepage_thumbnail_status = self.homepage_thumbnail_status.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "homepageThumbnailId": homepage_thumbnail_id,
                "assetId": asset_id,
                "moderationStatus": moderation_status,
                "personalizedConfigStatus": personalized_config_status,
                "homepageThumbnailStatus": homepage_thumbnail_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        homepage_thumbnail_id = d.pop("homepageThumbnailId")

        asset_id = d.pop("assetId")

        moderation_status = ThumbnailPersonalizationApiModerationStatus(d.pop("moderationStatus"))

        personalized_config_status = PersonalizedConfigStatus(d.pop("personalizedConfigStatus"))

        homepage_thumbnail_status = HomepageThumbnailStatus(d.pop("homepageThumbnailStatus"))

        homepage_thumbnail = cls(
            homepage_thumbnail_id=homepage_thumbnail_id,
            asset_id=asset_id,
            moderation_status=moderation_status,
            personalized_config_status=personalized_config_status,
            homepage_thumbnail_status=homepage_thumbnail_status,
        )

        return homepage_thumbnail
