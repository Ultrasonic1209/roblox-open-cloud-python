from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_badges_api_badge_response import RobloxBadgesApiBadgeResponse


T = TypeVar("T", bound="RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiBadgeResponse")


@_attrs_define
class RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiBadgeResponse:
    """
    Attributes:
        previous_page_cursor (str | Unset):
        next_page_cursor (str | Unset):
        data (list[RobloxBadgesApiBadgeResponse] | Unset):
    """

    previous_page_cursor: str | Unset = UNSET
    next_page_cursor: str | Unset = UNSET
    data: list[RobloxBadgesApiBadgeResponse] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        previous_page_cursor = self.previous_page_cursor

        next_page_cursor = self.next_page_cursor

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if previous_page_cursor is not UNSET:
            field_dict["previousPageCursor"] = previous_page_cursor
        if next_page_cursor is not UNSET:
            field_dict["nextPageCursor"] = next_page_cursor
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_badges_api_badge_response import RobloxBadgesApiBadgeResponse

        d = dict(src_dict)
        previous_page_cursor = d.pop("previousPageCursor", UNSET)

        next_page_cursor = d.pop("nextPageCursor", UNSET)

        _data = d.pop("data", UNSET)
        data: list[RobloxBadgesApiBadgeResponse] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = RobloxBadgesApiBadgeResponse.from_dict(data_item_data)

                data.append(data_item)

        roblox_web_web_api_models_api_page_response_roblox_badges_api_badge_response = cls(
            previous_page_cursor=previous_page_cursor,
            next_page_cursor=next_page_cursor,
            data=data,
        )

        return roblox_web_web_api_models_api_page_response_roblox_badges_api_badge_response
