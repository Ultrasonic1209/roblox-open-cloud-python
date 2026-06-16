from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_badges_api_universe_response import RobloxBadgesApiUniverseResponse
    from ..models.roblox_web_responses_badges_badge_award_statistics_response import (
        RobloxWebResponsesBadgesBadgeAwardStatisticsResponse,
    )


T = TypeVar("T", bound="RobloxBadgesApiBadgeResponse")


@_attrs_define
class RobloxBadgesApiBadgeResponse:
    """A response containing badge information.

    Attributes:
        id (int | Unset): The badge Id.
        name (str | Unset): The name of the badge.
        description (str | Unset): The badge description.
        display_name (str | Unset): The localized name of the badge.
        display_description (str | Unset): The localized badge description.
        enabled (bool | Unset): Whether or not the badge is enabled.
        icon_image_id (int | Unset): The badge icon asset Id.
        display_icon_image_id (int | Unset): The localized badge icon asset Id.
        created (datetime.datetime | Unset): When the badge was created.
        updated (datetime.datetime | Unset): When the badge was updated.
        statistics (RobloxWebResponsesBadgesBadgeAwardStatisticsResponse | Unset):
        awarding_universe (RobloxBadgesApiUniverseResponse | Unset): A response containing universe information.
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    display_name: str | Unset = UNSET
    display_description: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    icon_image_id: int | Unset = UNSET
    display_icon_image_id: int | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    updated: datetime.datetime | Unset = UNSET
    statistics: RobloxWebResponsesBadgesBadgeAwardStatisticsResponse | Unset = UNSET
    awarding_universe: RobloxBadgesApiUniverseResponse | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        display_name = self.display_name

        display_description = self.display_description

        enabled = self.enabled

        icon_image_id = self.icon_image_id

        display_icon_image_id = self.display_icon_image_id

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        statistics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        awarding_universe: dict[str, Any] | Unset = UNSET
        if not isinstance(self.awarding_universe, Unset):
            awarding_universe = self.awarding_universe.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
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
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if awarding_universe is not UNSET:
            field_dict["awardingUniverse"] = awarding_universe

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_badges_api_universe_response import RobloxBadgesApiUniverseResponse
        from ..models.roblox_web_responses_badges_badge_award_statistics_response import (
            RobloxWebResponsesBadgesBadgeAwardStatisticsResponse,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_description = d.pop("displayDescription", UNSET)

        enabled = d.pop("enabled", UNSET)

        icon_image_id = d.pop("iconImageId", UNSET)

        display_icon_image_id = d.pop("displayIconImageId", UNSET)

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

        _statistics = d.pop("statistics", UNSET)
        statistics: RobloxWebResponsesBadgesBadgeAwardStatisticsResponse | Unset
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = RobloxWebResponsesBadgesBadgeAwardStatisticsResponse.from_dict(_statistics)

        _awarding_universe = d.pop("awardingUniverse", UNSET)
        awarding_universe: RobloxBadgesApiUniverseResponse | Unset
        if isinstance(_awarding_universe, Unset):
            awarding_universe = UNSET
        else:
            awarding_universe = RobloxBadgesApiUniverseResponse.from_dict(_awarding_universe)

        roblox_badges_api_badge_response = cls(
            id=id,
            name=name,
            description=description,
            display_name=display_name,
            display_description=display_description,
            enabled=enabled,
            icon_image_id=icon_image_id,
            display_icon_image_id=display_icon_image_id,
            created=created,
            updated=updated,
            statistics=statistics,
            awarding_universe=awarding_universe,
        )

        return roblox_badges_api_badge_response
