from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiUpdatePermissionsRequestPermissions")


@_attrs_define
class RobloxGroupsApiUpdatePermissionsRequestPermissions:
    """The permission-value pairs to be updated.

    Attributes:
        delete_from_wall (bool | Unset):
        post_to_wall (bool | Unset):
        invite_members (bool | Unset):
        post_to_status (bool | Unset):
        remove_members (bool | Unset):
        ban_members (bool | Unset):
        view_status (bool | Unset):
        view_wall (bool | Unset):
        change_rank (bool | Unset):
        advertise_group (bool | Unset):
        manage_relationships (bool | Unset):
        add_group_places (bool | Unset):
        view_audit_logs (bool | Unset):
        create_items (bool | Unset):
        manage_items (bool | Unset):
        spend_group_funds (bool | Unset):
        manage_clan (bool | Unset):
        manage_group_games (bool | Unset):
        use_cloud_authentication (bool | Unset):
        administer_cloud_authentication (bool | Unset):
        view_analytics (bool | Unset):
        view_forums (bool | Unset):
        manage_categories (bool | Unset):
        create_posts (bool | Unset):
        remove_posts (bool | Unset):
        lock_posts (bool | Unset):
        pin_posts (bool | Unset):
        create_comments (bool | Unset):
        remove_comments (bool | Unset):
        manage_keyword_block_list (bool | Unset):
        view_keyword_block_list (bool | Unset):
        bypass_slowmode (bool | Unset):
        view_community_analytics (bool | Unset):
    """

    delete_from_wall: bool | Unset = UNSET
    post_to_wall: bool | Unset = UNSET
    invite_members: bool | Unset = UNSET
    post_to_status: bool | Unset = UNSET
    remove_members: bool | Unset = UNSET
    ban_members: bool | Unset = UNSET
    view_status: bool | Unset = UNSET
    view_wall: bool | Unset = UNSET
    change_rank: bool | Unset = UNSET
    advertise_group: bool | Unset = UNSET
    manage_relationships: bool | Unset = UNSET
    add_group_places: bool | Unset = UNSET
    view_audit_logs: bool | Unset = UNSET
    create_items: bool | Unset = UNSET
    manage_items: bool | Unset = UNSET
    spend_group_funds: bool | Unset = UNSET
    manage_clan: bool | Unset = UNSET
    manage_group_games: bool | Unset = UNSET
    use_cloud_authentication: bool | Unset = UNSET
    administer_cloud_authentication: bool | Unset = UNSET
    view_analytics: bool | Unset = UNSET
    view_forums: bool | Unset = UNSET
    manage_categories: bool | Unset = UNSET
    create_posts: bool | Unset = UNSET
    remove_posts: bool | Unset = UNSET
    lock_posts: bool | Unset = UNSET
    pin_posts: bool | Unset = UNSET
    create_comments: bool | Unset = UNSET
    remove_comments: bool | Unset = UNSET
    manage_keyword_block_list: bool | Unset = UNSET
    view_keyword_block_list: bool | Unset = UNSET
    bypass_slowmode: bool | Unset = UNSET
    view_community_analytics: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        delete_from_wall = self.delete_from_wall

        post_to_wall = self.post_to_wall

        invite_members = self.invite_members

        post_to_status = self.post_to_status

        remove_members = self.remove_members

        ban_members = self.ban_members

        view_status = self.view_status

        view_wall = self.view_wall

        change_rank = self.change_rank

        advertise_group = self.advertise_group

        manage_relationships = self.manage_relationships

        add_group_places = self.add_group_places

        view_audit_logs = self.view_audit_logs

        create_items = self.create_items

        manage_items = self.manage_items

        spend_group_funds = self.spend_group_funds

        manage_clan = self.manage_clan

        manage_group_games = self.manage_group_games

        use_cloud_authentication = self.use_cloud_authentication

        administer_cloud_authentication = self.administer_cloud_authentication

        view_analytics = self.view_analytics

        view_forums = self.view_forums

        manage_categories = self.manage_categories

        create_posts = self.create_posts

        remove_posts = self.remove_posts

        lock_posts = self.lock_posts

        pin_posts = self.pin_posts

        create_comments = self.create_comments

        remove_comments = self.remove_comments

        manage_keyword_block_list = self.manage_keyword_block_list

        view_keyword_block_list = self.view_keyword_block_list

        bypass_slowmode = self.bypass_slowmode

        view_community_analytics = self.view_community_analytics

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if delete_from_wall is not UNSET:
            field_dict["DeleteFromWall"] = delete_from_wall
        if post_to_wall is not UNSET:
            field_dict["PostToWall"] = post_to_wall
        if invite_members is not UNSET:
            field_dict["InviteMembers"] = invite_members
        if post_to_status is not UNSET:
            field_dict["PostToStatus"] = post_to_status
        if remove_members is not UNSET:
            field_dict["RemoveMembers"] = remove_members
        if ban_members is not UNSET:
            field_dict["BanMembers"] = ban_members
        if view_status is not UNSET:
            field_dict["ViewStatus"] = view_status
        if view_wall is not UNSET:
            field_dict["ViewWall"] = view_wall
        if change_rank is not UNSET:
            field_dict["ChangeRank"] = change_rank
        if advertise_group is not UNSET:
            field_dict["AdvertiseGroup"] = advertise_group
        if manage_relationships is not UNSET:
            field_dict["ManageRelationships"] = manage_relationships
        if add_group_places is not UNSET:
            field_dict["AddGroupPlaces"] = add_group_places
        if view_audit_logs is not UNSET:
            field_dict["ViewAuditLogs"] = view_audit_logs
        if create_items is not UNSET:
            field_dict["CreateItems"] = create_items
        if manage_items is not UNSET:
            field_dict["ManageItems"] = manage_items
        if spend_group_funds is not UNSET:
            field_dict["SpendGroupFunds"] = spend_group_funds
        if manage_clan is not UNSET:
            field_dict["ManageClan"] = manage_clan
        if manage_group_games is not UNSET:
            field_dict["ManageGroupGames"] = manage_group_games
        if use_cloud_authentication is not UNSET:
            field_dict["UseCloudAuthentication"] = use_cloud_authentication
        if administer_cloud_authentication is not UNSET:
            field_dict["AdministerCloudAuthentication"] = administer_cloud_authentication
        if view_analytics is not UNSET:
            field_dict["ViewAnalytics"] = view_analytics
        if view_forums is not UNSET:
            field_dict["ViewForums"] = view_forums
        if manage_categories is not UNSET:
            field_dict["ManageCategories"] = manage_categories
        if create_posts is not UNSET:
            field_dict["CreatePosts"] = create_posts
        if remove_posts is not UNSET:
            field_dict["RemovePosts"] = remove_posts
        if lock_posts is not UNSET:
            field_dict["LockPosts"] = lock_posts
        if pin_posts is not UNSET:
            field_dict["PinPosts"] = pin_posts
        if create_comments is not UNSET:
            field_dict["CreateComments"] = create_comments
        if remove_comments is not UNSET:
            field_dict["RemoveComments"] = remove_comments
        if manage_keyword_block_list is not UNSET:
            field_dict["ManageKeywordBlockList"] = manage_keyword_block_list
        if view_keyword_block_list is not UNSET:
            field_dict["ViewKeywordBlockList"] = view_keyword_block_list
        if bypass_slowmode is not UNSET:
            field_dict["BypassSlowmode"] = bypass_slowmode
        if view_community_analytics is not UNSET:
            field_dict["ViewCommunityAnalytics"] = view_community_analytics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        delete_from_wall = d.pop("DeleteFromWall", UNSET)

        post_to_wall = d.pop("PostToWall", UNSET)

        invite_members = d.pop("InviteMembers", UNSET)

        post_to_status = d.pop("PostToStatus", UNSET)

        remove_members = d.pop("RemoveMembers", UNSET)

        ban_members = d.pop("BanMembers", UNSET)

        view_status = d.pop("ViewStatus", UNSET)

        view_wall = d.pop("ViewWall", UNSET)

        change_rank = d.pop("ChangeRank", UNSET)

        advertise_group = d.pop("AdvertiseGroup", UNSET)

        manage_relationships = d.pop("ManageRelationships", UNSET)

        add_group_places = d.pop("AddGroupPlaces", UNSET)

        view_audit_logs = d.pop("ViewAuditLogs", UNSET)

        create_items = d.pop("CreateItems", UNSET)

        manage_items = d.pop("ManageItems", UNSET)

        spend_group_funds = d.pop("SpendGroupFunds", UNSET)

        manage_clan = d.pop("ManageClan", UNSET)

        manage_group_games = d.pop("ManageGroupGames", UNSET)

        use_cloud_authentication = d.pop("UseCloudAuthentication", UNSET)

        administer_cloud_authentication = d.pop("AdministerCloudAuthentication", UNSET)

        view_analytics = d.pop("ViewAnalytics", UNSET)

        view_forums = d.pop("ViewForums", UNSET)

        manage_categories = d.pop("ManageCategories", UNSET)

        create_posts = d.pop("CreatePosts", UNSET)

        remove_posts = d.pop("RemovePosts", UNSET)

        lock_posts = d.pop("LockPosts", UNSET)

        pin_posts = d.pop("PinPosts", UNSET)

        create_comments = d.pop("CreateComments", UNSET)

        remove_comments = d.pop("RemoveComments", UNSET)

        manage_keyword_block_list = d.pop("ManageKeywordBlockList", UNSET)

        view_keyword_block_list = d.pop("ViewKeywordBlockList", UNSET)

        bypass_slowmode = d.pop("BypassSlowmode", UNSET)

        view_community_analytics = d.pop("ViewCommunityAnalytics", UNSET)

        roblox_groups_api_update_permissions_request_permissions = cls(
            delete_from_wall=delete_from_wall,
            post_to_wall=post_to_wall,
            invite_members=invite_members,
            post_to_status=post_to_status,
            remove_members=remove_members,
            ban_members=ban_members,
            view_status=view_status,
            view_wall=view_wall,
            change_rank=change_rank,
            advertise_group=advertise_group,
            manage_relationships=manage_relationships,
            add_group_places=add_group_places,
            view_audit_logs=view_audit_logs,
            create_items=create_items,
            manage_items=manage_items,
            spend_group_funds=spend_group_funds,
            manage_clan=manage_clan,
            manage_group_games=manage_group_games,
            use_cloud_authentication=use_cloud_authentication,
            administer_cloud_authentication=administer_cloud_authentication,
            view_analytics=view_analytics,
            view_forums=view_forums,
            manage_categories=manage_categories,
            create_posts=create_posts,
            remove_posts=remove_posts,
            lock_posts=lock_posts,
            pin_posts=pin_posts,
            create_comments=create_comments,
            remove_comments=remove_comments,
            manage_keyword_block_list=manage_keyword_block_list,
            view_keyword_block_list=view_keyword_block_list,
            bypass_slowmode=bypass_slowmode,
            view_community_analytics=view_community_analytics,
        )

        return roblox_groups_api_update_permissions_request_permissions
