from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_notifications_analytics_response_campaigns_type_0_item import (
        GetNotificationsAnalyticsResponseCampaignsType0Item,
    )
    from ..models.get_notifications_analytics_response_overview_type_0 import (
        GetNotificationsAnalyticsResponseOverviewType0,
    )


T = TypeVar("T", bound="GetNotificationsAnalyticsResponse")


@_attrs_define
class GetNotificationsAnalyticsResponse:
    """
    Attributes:
        overview (GetNotificationsAnalyticsResponseOverviewType0 | None):
        campaigns (list[GetNotificationsAnalyticsResponseCampaignsType0Item] | None):
    """

    overview: GetNotificationsAnalyticsResponseOverviewType0 | None
    campaigns: list[GetNotificationsAnalyticsResponseCampaignsType0Item] | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_notifications_analytics_response_overview_type_0 import (
            GetNotificationsAnalyticsResponseOverviewType0,  # noqa: PLC0415
        )

        overview: dict[str, Any] | None
        if isinstance(self.overview, GetNotificationsAnalyticsResponseOverviewType0):
            overview = self.overview.to_dict()
        else:
            overview = self.overview

        campaigns: list[dict[str, Any]] | None
        if isinstance(self.campaigns, list):
            campaigns = []
            for campaigns_type_0_item_data in self.campaigns:
                campaigns_type_0_item = campaigns_type_0_item_data.to_dict()
                campaigns.append(campaigns_type_0_item)

        else:
            campaigns = self.campaigns

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "overview": overview,
                "campaigns": campaigns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_notifications_analytics_response_campaigns_type_0_item import (
            GetNotificationsAnalyticsResponseCampaignsType0Item,  # noqa: PLC0415
        )
        from ..models.get_notifications_analytics_response_overview_type_0 import (
            GetNotificationsAnalyticsResponseOverviewType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_overview(data: object) -> GetNotificationsAnalyticsResponseOverviewType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                overview_type_0 = GetNotificationsAnalyticsResponseOverviewType0.from_dict(data)

                return overview_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetNotificationsAnalyticsResponseOverviewType0 | None, data)

        overview = _parse_overview(d.pop("overview"))

        def _parse_campaigns(data: object) -> list[GetNotificationsAnalyticsResponseCampaignsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                campaigns_type_0 = []
                _campaigns_type_0 = data
                for campaigns_type_0_item_data in _campaigns_type_0:
                    campaigns_type_0_item = GetNotificationsAnalyticsResponseCampaignsType0Item.from_dict(
                        campaigns_type_0_item_data
                    )

                    campaigns_type_0.append(campaigns_type_0_item)

                return campaigns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GetNotificationsAnalyticsResponseCampaignsType0Item] | None, data)

        campaigns = _parse_campaigns(d.pop("campaigns"))

        get_notifications_analytics_response = cls(
            overview=overview,
            campaigns=campaigns,
        )

        return get_notifications_analytics_response
