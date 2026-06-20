from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_badges_api_badge_creator_response import RobloxBadgesApiBadgeCreatorResponse
    from ..models.roblox_web_responses_badges_badge_award_statistics_response import (
        RobloxWebResponsesBadgesBadgeAwardStatisticsResponse,
    )
    from ..models.roblox_web_responses_related_entity_type_response_roblox_platform_badges_badge_awarder_type import (
        RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformBadgesBadgeAwarderType,
    )


T = TypeVar("T", bound="RobloxBadgesApiGetBadgesByUserResponse")


@_attrs_define
class RobloxBadgesApiGetBadgesByUserResponse:
    """Response for the GetBadgesByUser endpoint.

    Attributes:
        creator (RobloxBadgesApiBadgeCreatorResponse | Unset): Represents information about the badge creator. (Creator
            of the place that awarded the badge)
        id (int | Unset):
        name (str | Unset):
        description (str | Unset):
        display_name (str | Unset):
        display_description (str | Unset):
        enabled (bool | Unset):
        icon_image_id (int | Unset):
        display_icon_image_id (int | Unset):
        awarder (RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformBadgesBadgeAwarderType | Unset):
        statistics (RobloxWebResponsesBadgesBadgeAwardStatisticsResponse | Unset):
        created (datetime.datetime | Unset):
        updated (datetime.datetime | Unset):
    """

    creator: RobloxBadgesApiBadgeCreatorResponse | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    display_name: str | Unset = UNSET
    display_description: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    icon_image_id: int | Unset = UNSET
    display_icon_image_id: int | Unset = UNSET
    awarder: RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformBadgesBadgeAwarderType | Unset = UNSET
    statistics: RobloxWebResponsesBadgesBadgeAwardStatisticsResponse | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    updated: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        id = self.id

        name = self.name

        description = self.description

        display_name = self.display_name

        display_description = self.display_description

        enabled = self.enabled

        icon_image_id = self.icon_image_id

        display_icon_image_id = self.display_icon_image_id

        awarder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.awarder, Unset):
            awarder = self.awarder.to_dict()

        statistics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if creator is not UNSET:
            field_dict["creator"] = creator
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_description is not UNSET:
            field_dict["displayDescription"] = display_description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if icon_image_id is not UNSET:
            field_dict["iconImageId"] = icon_image_id
        if display_icon_image_id is not UNSET:
            field_dict["displayIconImageId"] = display_icon_image_id
        if awarder is not UNSET:
            field_dict["awarder"] = awarder
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_badges_api_badge_creator_response import RobloxBadgesApiBadgeCreatorResponse
        from ..models.roblox_web_responses_badges_badge_award_statistics_response import (
            RobloxWebResponsesBadgesBadgeAwardStatisticsResponse,
        )
        from ..models.roblox_web_responses_related_entity_type_response_roblox_platform_badges_badge_awarder_type import (
            RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformBadgesBadgeAwarderType,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _creator = d.pop("creator", UNSET)
        creator: RobloxBadgesApiBadgeCreatorResponse | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = RobloxBadgesApiBadgeCreatorResponse.from_dict(_creator)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_description = d.pop("displayDescription", UNSET)

        enabled = d.pop("enabled", UNSET)

        icon_image_id = d.pop("iconImageId", UNSET)

        display_icon_image_id = d.pop("displayIconImageId", UNSET)

        _awarder = d.pop("awarder", UNSET)
        awarder: RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformBadgesBadgeAwarderType | Unset
        if isinstance(_awarder, Unset):
            awarder = UNSET
        else:
            awarder = RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformBadgesBadgeAwarderType.from_dict(
                _awarder
            )

        _statistics = d.pop("statistics", UNSET)
        statistics: RobloxWebResponsesBadgesBadgeAwardStatisticsResponse | Unset
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = RobloxWebResponsesBadgesBadgeAwardStatisticsResponse.from_dict(_statistics)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        _updated = d.pop("updated", UNSET)
        updated: datetime.datetime | Unset
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = datetime.datetime.fromisoformat(_updated)

        roblox_badges_api_get_badges_by_user_response = cls(
            creator=creator,
            id=id,
            name=name,
            description=description,
            display_name=display_name,
            display_description=display_description,
            enabled=enabled,
            icon_image_id=icon_image_id,
            display_icon_image_id=display_icon_image_id,
            awarder=awarder,
            statistics=statistics,
            created=created,
            updated=updated,
        )

        return roblox_badges_api_get_badges_by_user_response
