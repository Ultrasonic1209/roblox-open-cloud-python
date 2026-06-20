from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.state import State
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.creation_context import CreationContext
    from ..models.moderation_result import ModerationResult
    from ..models.preview import Preview
    from ..models.social_link import SocialLink


T = TypeVar("T", bound="Asset")


@_attrs_define
class Asset:
    """Represents an asset.

    Attributes:
        asset_type (str | Unset): The asset type. Required for [Create Asset](#POST-v1-assets).
        asset_id (int | Unset): The unique identifier of the asset. Required for [Update Asset](#PATCH-v1-assets-
            _asset_).
        creation_context (CreationContext | Unset): The context of creation that is not part of the asset content, such
            as metadata and creator information. Required for [Create Asset](#POST-v1-assets).
        description (str | Unset): The description of the asset. Limit to 1000 characters. Required for [Create
            Asset](#POST-v1-assets).
        display_name (str | Unset): Display name of the asset. Required for [Create Asset](#POST-v1-assets).
        path (str | Unset): The returned resource path of the asset. Format: `assets/{assetId}`. Example:
            `assets/2205400862`.
        revision_id (str | Unset): Revision ID of the asset. Equivalent to `versionNumber`. Every change of the asset
            automatically commits a new version. The format is an integer string. Example: `1`.
        revision_create_time (datetime.datetime | Unset): The creation timestamp of the current revision.
        moderation_result (ModerationResult | Unset): The moderation result of the asset.
        icon (str | Unset): The resource path for the icon.
        previews (list[Preview] | Unset): A list of previews, each with an asset path and alt text. Previews must be
            **Image** assets.
        state (State | Unset): Whether the asset is active or archived. Unspecified isn't used.
        social_link (SocialLink | Unset): A social media link for the asset. Maximum of three per asset. Object name can
            be any of: <ul><li>`facebookSocialLink`</li><li>`twitterSocialLink`</li><li>`youtubeSocialLink`</li><li>`twitchS
            ocialLink`</li><li>`discordSocialLink`</li><li>`githubSocialLink`</li><li>`robloxSocialLink`</li><li>`guildedSoc
            ialLink`</li><li>`devForumSocialLink`</li></ul>For syntax, see the sample request under [Update
            Asset](#PATCH-v1-assets-_assetId_).
    """

    asset_type: str | Unset = UNSET
    asset_id: int | Unset = UNSET
    creation_context: CreationContext | Unset = UNSET
    description: str | Unset = UNSET
    display_name: str | Unset = UNSET
    path: str | Unset = UNSET
    revision_id: str | Unset = UNSET
    revision_create_time: datetime.datetime | Unset = UNSET
    moderation_result: ModerationResult | Unset = UNSET
    icon: str | Unset = UNSET
    previews: list[Preview] | Unset = UNSET
    state: State | Unset = UNSET
    social_link: SocialLink | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_type = self.asset_type

        asset_id = self.asset_id

        creation_context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creation_context, Unset):
            creation_context = self.creation_context.to_dict()

        description = self.description

        display_name = self.display_name

        path = self.path

        revision_id = self.revision_id

        revision_create_time: str | Unset = UNSET
        if not isinstance(self.revision_create_time, Unset):
            revision_create_time = self.revision_create_time.isoformat()

        moderation_result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.moderation_result, Unset):
            moderation_result = self.moderation_result.to_dict()

        icon = self.icon

        previews: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.previews, Unset):
            previews = []
            for previews_item_data in self.previews:
                previews_item = previews_item_data.to_dict()
                previews.append(previews_item)

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        social_link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.social_link, Unset):
            social_link = self.social_link.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_type is not UNSET:
            field_dict["assetType"] = asset_type
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if creation_context is not UNSET:
            field_dict["creationContext"] = creation_context
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if path is not UNSET:
            field_dict["path"] = path
        if revision_id is not UNSET:
            field_dict["revisionId"] = revision_id
        if revision_create_time is not UNSET:
            field_dict["revisionCreateTime"] = revision_create_time
        if moderation_result is not UNSET:
            field_dict["moderationResult"] = moderation_result
        if icon is not UNSET:
            field_dict["icon"] = icon
        if previews is not UNSET:
            field_dict["previews"] = previews
        if state is not UNSET:
            field_dict["state"] = state
        if social_link is not UNSET:
            field_dict["socialLink"] = social_link

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.creation_context import CreationContext
        from ..models.moderation_result import ModerationResult
        from ..models.preview import Preview
        from ..models.social_link import SocialLink

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        asset_type = d.pop("assetType", UNSET)

        asset_id = d.pop("assetId", UNSET)

        _creation_context = d.pop("creationContext", UNSET)
        creation_context: CreationContext | Unset
        if isinstance(_creation_context, Unset):
            creation_context = UNSET
        else:
            creation_context = CreationContext.from_dict(_creation_context)

        description = d.pop("description", UNSET)

        display_name = d.pop("displayName", UNSET)

        path = d.pop("path", UNSET)

        revision_id = d.pop("revisionId", UNSET)

        _revision_create_time = d.pop("revisionCreateTime", UNSET)
        revision_create_time: datetime.datetime | Unset
        if isinstance(_revision_create_time, Unset):
            revision_create_time = UNSET
        else:
            revision_create_time = datetime.datetime.fromisoformat(_revision_create_time)

        _moderation_result = d.pop("moderationResult", UNSET)
        moderation_result: ModerationResult | Unset
        if isinstance(_moderation_result, Unset):
            moderation_result = UNSET
        else:
            moderation_result = ModerationResult.from_dict(_moderation_result)

        icon = d.pop("icon", UNSET)

        _previews = d.pop("previews", UNSET)
        previews: list[Preview] | Unset = UNSET
        if _previews is not UNSET:
            previews = []
            for previews_item_data in _previews:
                previews_item = Preview.from_dict(previews_item_data)

                previews.append(previews_item)

        _state = d.pop("state", UNSET)
        state: State | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = State(_state)

        _social_link = d.pop("socialLink", UNSET)
        social_link: SocialLink | Unset
        if isinstance(_social_link, Unset):
            social_link = UNSET
        else:
            social_link = SocialLink.from_dict(_social_link)

        asset = cls(
            asset_type=asset_type,
            asset_id=asset_id,
            creation_context=creation_context,
            description=description,
            display_name=display_name,
            path=path,
            revision_id=revision_id,
            revision_create_time=revision_create_time,
            moderation_result=moderation_result,
            icon=icon,
            previews=previews,
            state=state,
            social_link=social_link,
        )

        asset.additional_properties = d
        return asset

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
