from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiGroupEconomyPermissionsModel")


@_attrs_define
class RobloxGroupsApiGroupEconomyPermissionsModel:
    """A model representing data about an Roblox.Platform.Membership.IUser

    Attributes:
        spend_group_funds (bool | Unset): Spend group funds permission
        advertise_group (bool | Unset): Advertise group permission
        create_items (bool | Unset): Create items permission
        manage_items (bool | Unset): Manage items permission
        add_group_places (bool | Unset): Add group places permission
        manage_group_games (bool | Unset): Manage group games permission
        view_group_payouts (bool | Unset): Manage group games permission
        view_analytics (bool | Unset): Permission to view universe analytics from the creator dashboard.
    """

    spend_group_funds: bool | Unset = UNSET
    advertise_group: bool | Unset = UNSET
    create_items: bool | Unset = UNSET
    manage_items: bool | Unset = UNSET
    add_group_places: bool | Unset = UNSET
    manage_group_games: bool | Unset = UNSET
    view_group_payouts: bool | Unset = UNSET
    view_analytics: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        spend_group_funds = self.spend_group_funds

        advertise_group = self.advertise_group

        create_items = self.create_items

        manage_items = self.manage_items

        add_group_places = self.add_group_places

        manage_group_games = self.manage_group_games

        view_group_payouts = self.view_group_payouts

        view_analytics = self.view_analytics

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if spend_group_funds is not UNSET:
            field_dict["spendGroupFunds"] = spend_group_funds
        if advertise_group is not UNSET:
            field_dict["advertiseGroup"] = advertise_group
        if create_items is not UNSET:
            field_dict["createItems"] = create_items
        if manage_items is not UNSET:
            field_dict["manageItems"] = manage_items
        if add_group_places is not UNSET:
            field_dict["addGroupPlaces"] = add_group_places
        if manage_group_games is not UNSET:
            field_dict["manageGroupGames"] = manage_group_games
        if view_group_payouts is not UNSET:
            field_dict["viewGroupPayouts"] = view_group_payouts
        if view_analytics is not UNSET:
            field_dict["viewAnalytics"] = view_analytics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        spend_group_funds = d.pop("spendGroupFunds", UNSET)

        advertise_group = d.pop("advertiseGroup", UNSET)

        create_items = d.pop("createItems", UNSET)

        manage_items = d.pop("manageItems", UNSET)

        add_group_places = d.pop("addGroupPlaces", UNSET)

        manage_group_games = d.pop("manageGroupGames", UNSET)

        view_group_payouts = d.pop("viewGroupPayouts", UNSET)

        view_analytics = d.pop("viewAnalytics", UNSET)

        roblox_groups_api_group_economy_permissions_model = cls(
            spend_group_funds=spend_group_funds,
            advertise_group=advertise_group,
            create_items=create_items,
            manage_items=manage_items,
            add_group_places=add_group_places,
            manage_group_games=manage_group_games,
            view_group_payouts=view_group_payouts,
            view_analytics=view_analytics,
        )

        return roblox_groups_api_group_economy_permissions_model
