from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_trades_api_user_asset_response import RobloxTradesApiUserAssetResponse
    from ..models.roblox_web_responses_users_skinny_user_response import RobloxWebResponsesUsersSkinnyUserResponse


T = TypeVar("T", bound="RobloxTradesApiTradeOfferResponse")


@_attrs_define
class RobloxTradesApiTradeOfferResponse:
    """
    Attributes:
        user (RobloxWebResponsesUsersSkinnyUserResponse | Unset):
        user_assets (list[RobloxTradesApiUserAssetResponse] | Unset):
        robux (int | Unset):
    """

    user: RobloxWebResponsesUsersSkinnyUserResponse | Unset = UNSET
    user_assets: list[RobloxTradesApiUserAssetResponse] | Unset = UNSET
    robux: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        user_assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user_assets, Unset):
            user_assets = []
            for user_assets_item_data in self.user_assets:
                user_assets_item = user_assets_item_data.to_dict()
                user_assets.append(user_assets_item)

        robux = self.robux

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if user_assets is not UNSET:
            field_dict["userAssets"] = user_assets
        if robux is not UNSET:
            field_dict["robux"] = robux

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_trades_api_user_asset_response import RobloxTradesApiUserAssetResponse
        from ..models.roblox_web_responses_users_skinny_user_response import RobloxWebResponsesUsersSkinnyUserResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _user = d.pop("user", UNSET)
        user: RobloxWebResponsesUsersSkinnyUserResponse | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = RobloxWebResponsesUsersSkinnyUserResponse.from_dict(_user)

        _user_assets = d.pop("userAssets", UNSET)
        user_assets: list[RobloxTradesApiUserAssetResponse] | Unset = UNSET
        if _user_assets is not UNSET:
            user_assets = []
            for user_assets_item_data in _user_assets:
                user_assets_item = RobloxTradesApiUserAssetResponse.from_dict(user_assets_item_data)

                user_assets.append(user_assets_item)

        robux = d.pop("robux", UNSET)

        roblox_trades_api_trade_offer_response = cls(
            user=user,
            user_assets=user_assets,
            robux=robux,
        )

        return roblox_trades_api_trade_offer_response
