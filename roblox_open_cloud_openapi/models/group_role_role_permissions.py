from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupRoleRolePermissions")


@_attrs_define
class GroupRoleRolePermissions:
    """Represents the permissions on a role.

    Attributes:
        view_wall_posts (bool | Unset): View group wall. Example: True.
        create_wall_posts (bool | Unset): Post on group wall. Example: True.
        delete_wall_posts (bool | Unset): Delete group wall posts. Example: True.
        view_group_shout (bool | Unset): View group shout. Example: True.
        create_group_shout (bool | Unset): Post group shout. Example: True.
        change_rank (bool | Unset): Manage lower-ranked member ranks. Example: True.
        accept_requests (bool | Unset): Accept join requests. Example: True.
        exile_members (bool | Unset): Kick lower-ranked members. Example: True.
        manage_relationships (bool | Unset): Manage allies and enemies. Example: True.
        view_audit_log (bool | Unset): View audit log. Example: True.
        spend_group_funds (bool | Unset): Spend group funds. Example: True.
        advertise_group (bool | Unset): Advertise group. Example: True.
        create_avatar_items (bool | Unset): Create avatar items. Example: True.
        manage_avatar_items (bool | Unset): Manage avatar items. Example: True.
        manage_group_universes (bool | Unset): Manage group universes. Example: True.
        view_universe_analytics (bool | Unset): View universe analytics. Example: True.
        create_api_keys (bool | Unset): Create group API Keys. Example: True.
        manage_api_keys (bool | Unset): Manage all group API keys. Example: True.
        ban_members (bool | Unset): Ban lower-ranked members. Example: True.
        view_forums (bool | Unset): Can view forums Example: True.
        manage_categories (bool | Unset): Can change forum categories Example: True.
        create_posts (bool | Unset): Can create forum post Example: True.
        lock_posts (bool | Unset): Can lock forum post Example: True.
        pin_posts (bool | Unset): Can pin forum post Example: True.
        remove_posts (bool | Unset): Can remove forum post Example: True.
        create_comments (bool | Unset): Can create forum comment Example: True.
        remove_comments (bool | Unset): Can remove forum comment Example: True.
        manage_blocked_words (bool | Unset): Can manage blocked words Example: True.
        view_blocked_words (bool | Unset): Can view blocked words Example: True.
        bypass_slow_mode (bool | Unset): can bypass slow mode Example: True.
    """

    view_wall_posts: bool | Unset = UNSET
    create_wall_posts: bool | Unset = UNSET
    delete_wall_posts: bool | Unset = UNSET
    view_group_shout: bool | Unset = UNSET
    create_group_shout: bool | Unset = UNSET
    change_rank: bool | Unset = UNSET
    accept_requests: bool | Unset = UNSET
    exile_members: bool | Unset = UNSET
    manage_relationships: bool | Unset = UNSET
    view_audit_log: bool | Unset = UNSET
    spend_group_funds: bool | Unset = UNSET
    advertise_group: bool | Unset = UNSET
    create_avatar_items: bool | Unset = UNSET
    manage_avatar_items: bool | Unset = UNSET
    manage_group_universes: bool | Unset = UNSET
    view_universe_analytics: bool | Unset = UNSET
    create_api_keys: bool | Unset = UNSET
    manage_api_keys: bool | Unset = UNSET
    ban_members: bool | Unset = UNSET
    view_forums: bool | Unset = UNSET
    manage_categories: bool | Unset = UNSET
    create_posts: bool | Unset = UNSET
    lock_posts: bool | Unset = UNSET
    pin_posts: bool | Unset = UNSET
    remove_posts: bool | Unset = UNSET
    create_comments: bool | Unset = UNSET
    remove_comments: bool | Unset = UNSET
    manage_blocked_words: bool | Unset = UNSET
    view_blocked_words: bool | Unset = UNSET
    bypass_slow_mode: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        view_wall_posts = self.view_wall_posts

        create_wall_posts = self.create_wall_posts

        delete_wall_posts = self.delete_wall_posts

        view_group_shout = self.view_group_shout

        create_group_shout = self.create_group_shout

        change_rank = self.change_rank

        accept_requests = self.accept_requests

        exile_members = self.exile_members

        manage_relationships = self.manage_relationships

        view_audit_log = self.view_audit_log

        spend_group_funds = self.spend_group_funds

        advertise_group = self.advertise_group

        create_avatar_items = self.create_avatar_items

        manage_avatar_items = self.manage_avatar_items

        manage_group_universes = self.manage_group_universes

        view_universe_analytics = self.view_universe_analytics

        create_api_keys = self.create_api_keys

        manage_api_keys = self.manage_api_keys

        ban_members = self.ban_members

        view_forums = self.view_forums

        manage_categories = self.manage_categories

        create_posts = self.create_posts

        lock_posts = self.lock_posts

        pin_posts = self.pin_posts

        remove_posts = self.remove_posts

        create_comments = self.create_comments

        remove_comments = self.remove_comments

        manage_blocked_words = self.manage_blocked_words

        view_blocked_words = self.view_blocked_words

        bypass_slow_mode = self.bypass_slow_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if view_wall_posts is not UNSET:
            field_dict["viewWallPosts"] = view_wall_posts
        if create_wall_posts is not UNSET:
            field_dict["createWallPosts"] = create_wall_posts
        if delete_wall_posts is not UNSET:
            field_dict["deleteWallPosts"] = delete_wall_posts
        if view_group_shout is not UNSET:
            field_dict["viewGroupShout"] = view_group_shout
        if create_group_shout is not UNSET:
            field_dict["createGroupShout"] = create_group_shout
        if change_rank is not UNSET:
            field_dict["changeRank"] = change_rank
        if accept_requests is not UNSET:
            field_dict["acceptRequests"] = accept_requests
        if exile_members is not UNSET:
            field_dict["exileMembers"] = exile_members
        if manage_relationships is not UNSET:
            field_dict["manageRelationships"] = manage_relationships
        if view_audit_log is not UNSET:
            field_dict["viewAuditLog"] = view_audit_log
        if spend_group_funds is not UNSET:
            field_dict["spendGroupFunds"] = spend_group_funds
        if advertise_group is not UNSET:
            field_dict["advertiseGroup"] = advertise_group
        if create_avatar_items is not UNSET:
            field_dict["createAvatarItems"] = create_avatar_items
        if manage_avatar_items is not UNSET:
            field_dict["manageAvatarItems"] = manage_avatar_items
        if manage_group_universes is not UNSET:
            field_dict["manageGroupUniverses"] = manage_group_universes
        if view_universe_analytics is not UNSET:
            field_dict["viewUniverseAnalytics"] = view_universe_analytics
        if create_api_keys is not UNSET:
            field_dict["createApiKeys"] = create_api_keys
        if manage_api_keys is not UNSET:
            field_dict["manageApiKeys"] = manage_api_keys
        if ban_members is not UNSET:
            field_dict["banMembers"] = ban_members
        if view_forums is not UNSET:
            field_dict["viewForums"] = view_forums
        if manage_categories is not UNSET:
            field_dict["manageCategories"] = manage_categories
        if create_posts is not UNSET:
            field_dict["createPosts"] = create_posts
        if lock_posts is not UNSET:
            field_dict["lockPosts"] = lock_posts
        if pin_posts is not UNSET:
            field_dict["pinPosts"] = pin_posts
        if remove_posts is not UNSET:
            field_dict["removePosts"] = remove_posts
        if create_comments is not UNSET:
            field_dict["createComments"] = create_comments
        if remove_comments is not UNSET:
            field_dict["removeComments"] = remove_comments
        if manage_blocked_words is not UNSET:
            field_dict["manageBlockedWords"] = manage_blocked_words
        if view_blocked_words is not UNSET:
            field_dict["viewBlockedWords"] = view_blocked_words
        if bypass_slow_mode is not UNSET:
            field_dict["bypassSlowMode"] = bypass_slow_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        view_wall_posts = d.pop("viewWallPosts", UNSET)

        create_wall_posts = d.pop("createWallPosts", UNSET)

        delete_wall_posts = d.pop("deleteWallPosts", UNSET)

        view_group_shout = d.pop("viewGroupShout", UNSET)

        create_group_shout = d.pop("createGroupShout", UNSET)

        change_rank = d.pop("changeRank", UNSET)

        accept_requests = d.pop("acceptRequests", UNSET)

        exile_members = d.pop("exileMembers", UNSET)

        manage_relationships = d.pop("manageRelationships", UNSET)

        view_audit_log = d.pop("viewAuditLog", UNSET)

        spend_group_funds = d.pop("spendGroupFunds", UNSET)

        advertise_group = d.pop("advertiseGroup", UNSET)

        create_avatar_items = d.pop("createAvatarItems", UNSET)

        manage_avatar_items = d.pop("manageAvatarItems", UNSET)

        manage_group_universes = d.pop("manageGroupUniverses", UNSET)

        view_universe_analytics = d.pop("viewUniverseAnalytics", UNSET)

        create_api_keys = d.pop("createApiKeys", UNSET)

        manage_api_keys = d.pop("manageApiKeys", UNSET)

        ban_members = d.pop("banMembers", UNSET)

        view_forums = d.pop("viewForums", UNSET)

        manage_categories = d.pop("manageCategories", UNSET)

        create_posts = d.pop("createPosts", UNSET)

        lock_posts = d.pop("lockPosts", UNSET)

        pin_posts = d.pop("pinPosts", UNSET)

        remove_posts = d.pop("removePosts", UNSET)

        create_comments = d.pop("createComments", UNSET)

        remove_comments = d.pop("removeComments", UNSET)

        manage_blocked_words = d.pop("manageBlockedWords", UNSET)

        view_blocked_words = d.pop("viewBlockedWords", UNSET)

        bypass_slow_mode = d.pop("bypassSlowMode", UNSET)

        group_role_role_permissions = cls(
            view_wall_posts=view_wall_posts,
            create_wall_posts=create_wall_posts,
            delete_wall_posts=delete_wall_posts,
            view_group_shout=view_group_shout,
            create_group_shout=create_group_shout,
            change_rank=change_rank,
            accept_requests=accept_requests,
            exile_members=exile_members,
            manage_relationships=manage_relationships,
            view_audit_log=view_audit_log,
            spend_group_funds=spend_group_funds,
            advertise_group=advertise_group,
            create_avatar_items=create_avatar_items,
            manage_avatar_items=manage_avatar_items,
            manage_group_universes=manage_group_universes,
            view_universe_analytics=view_universe_analytics,
            create_api_keys=create_api_keys,
            manage_api_keys=manage_api_keys,
            ban_members=ban_members,
            view_forums=view_forums,
            manage_categories=manage_categories,
            create_posts=create_posts,
            lock_posts=lock_posts,
            pin_posts=pin_posts,
            remove_posts=remove_posts,
            create_comments=create_comments,
            remove_comments=remove_comments,
            manage_blocked_words=manage_blocked_words,
            view_blocked_words=view_blocked_words,
            bypass_slow_mode=bypass_slow_mode,
        )

        group_role_role_permissions.additional_properties = d
        return group_role_role_permissions

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
