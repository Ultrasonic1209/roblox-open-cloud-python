from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.asset_type import AssetType
from ..models.state import State
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.creation_context import CreationContext
    from ..models.moderation_result import ModerationResult
    from ..models.preview import Preview
    from ..models.social_link import SocialLink


T = TypeVar("T", bound="AssetsUploadApiAsset")


@_attrs_define
class AssetsUploadApiAsset:
    """Represents an asset.

    Attributes:
        path (None | str | Unset): The returned resource path of the asset. Format: `assets/{assetId}`. Example:
            `assets/2205400862`. Example: assets/123.
        revision_id (None | str | Unset): Revision ID of the asset. Equivalent to `versionNumber`. Every change of the
            asset automatically commits a new version. The format is an integer string. Example: `1`.
        revision_create_time (datetime.datetime | None | Unset): The creation timestamp of the current revision.
        asset_id (str | Unset): The unique identifier of the asset. Required for [Update Asset](#Assets_UpdateAsset).
        display_name (None | str | Unset): Display name of the asset. Required for [Create Asset](#Assets_CreateAsset).
        description (None | str | Unset): The description of the asset. Limit to 1000 characters. Required for [Create
            Asset](#Assets_CreateAsset).
        asset_type (AssetType | Unset): Type of the Asset.
        creation_context (CreationContext | Unset): The context of creation that is not part of the asset content, such
            as metadata and creator information. Required for [Create Asset](#Assets_CreateAsset).
        moderation_result (ModerationResult | Unset): The moderation result of the asset.
        published (bool | Unset): Whether to publish the asset version created by the request. To check whether the
            current revision is published, see `isPublished`.
        icon (None | str | Unset): The resource path for the icon. The icon must be an image set to [Open
            Use](https://create.roblox.com/docs/projects/assets/privacy). To create an Open Use image, set
            `creationContext.assetPrivacy` to `OpenUse` in [Create Asset](#Assets_CreateAsset).
        previews (list[Preview] | None | Unset): A list of previews, each with an asset path and alt text. Previews must
            be **Image** assets, except for Place assets, which can have one **GamePreviewVideo**, and for Model, MeshPart,
            and Plugin assets, which can have one **StorePreviewVideo**. Image previews must be set to [Open
            Use](https://create.roblox.com/docs/projects/assets/privacy). To create an Open Use image, set
            `creationContext.assetPrivacy` to `OpenUse` in [Create Asset](#Assets_CreateAsset).
        state (State | Unset): Whether the asset is active or archived. Unspecified isn't used.
        facebook_social_link (SocialLink | Unset): A social media link for the asset. Maximum of three per asset. Object
            name can be any of: <ul><li>`facebookSocialLink`</li><li>`twitterSocialLink`</li><li>`youtubeSocialLink`</li><li
            >`twitchSocialLink`</li><li>`discordSocialLink`</li><li>`githubSocialLink`</li><li>`robloxSocialLink`</li><li>`g
            uildedSocialLink`</li><li>`devForumSocialLink`</li></ul>For syntax, see the sample request under [Update
            Asset](#Assets_UpdateAsset).
        twitter_social_link (SocialLink | Unset): A social media link for the asset. Maximum of three per asset. Object
            name can be any of: <ul><li>`facebookSocialLink`</li><li>`twitterSocialLink`</li><li>`youtubeSocialLink`</li><li
            >`twitchSocialLink`</li><li>`discordSocialLink`</li><li>`githubSocialLink`</li><li>`robloxSocialLink`</li><li>`g
            uildedSocialLink`</li><li>`devForumSocialLink`</li></ul>For syntax, see the sample request under [Update
            Asset](#Assets_UpdateAsset).
        youtube_social_link (SocialLink | Unset): A social media link for the asset. Maximum of three per asset. Object
            name can be any of: <ul><li>`facebookSocialLink`</li><li>`twitterSocialLink`</li><li>`youtubeSocialLink`</li><li
            >`twitchSocialLink`</li><li>`discordSocialLink`</li><li>`githubSocialLink`</li><li>`robloxSocialLink`</li><li>`g
            uildedSocialLink`</li><li>`devForumSocialLink`</li></ul>For syntax, see the sample request under [Update
            Asset](#Assets_UpdateAsset).
        twitch_social_link (SocialLink | Unset): A social media link for the asset. Maximum of three per asset. Object
            name can be any of: <ul><li>`facebookSocialLink`</li><li>`twitterSocialLink`</li><li>`youtubeSocialLink`</li><li
            >`twitchSocialLink`</li><li>`discordSocialLink`</li><li>`githubSocialLink`</li><li>`robloxSocialLink`</li><li>`g
            uildedSocialLink`</li><li>`devForumSocialLink`</li></ul>For syntax, see the sample request under [Update
            Asset](#Assets_UpdateAsset).
        discord_social_link (SocialLink | Unset): A social media link for the asset. Maximum of three per asset. Object
            name can be any of: <ul><li>`facebookSocialLink`</li><li>`twitterSocialLink`</li><li>`youtubeSocialLink`</li><li
            >`twitchSocialLink`</li><li>`discordSocialLink`</li><li>`githubSocialLink`</li><li>`robloxSocialLink`</li><li>`g
            uildedSocialLink`</li><li>`devForumSocialLink`</li></ul>For syntax, see the sample request under [Update
            Asset](#Assets_UpdateAsset).
        github_social_link (SocialLink | Unset): A social media link for the asset. Maximum of three per asset. Object
            name can be any of: <ul><li>`facebookSocialLink`</li><li>`twitterSocialLink`</li><li>`youtubeSocialLink`</li><li
            >`twitchSocialLink`</li><li>`discordSocialLink`</li><li>`githubSocialLink`</li><li>`robloxSocialLink`</li><li>`g
            uildedSocialLink`</li><li>`devForumSocialLink`</li></ul>For syntax, see the sample request under [Update
            Asset](#Assets_UpdateAsset).
        roblox_social_link (SocialLink | Unset): A social media link for the asset. Maximum of three per asset. Object
            name can be any of: <ul><li>`facebookSocialLink`</li><li>`twitterSocialLink`</li><li>`youtubeSocialLink`</li><li
            >`twitchSocialLink`</li><li>`discordSocialLink`</li><li>`githubSocialLink`</li><li>`robloxSocialLink`</li><li>`g
            uildedSocialLink`</li><li>`devForumSocialLink`</li></ul>For syntax, see the sample request under [Update
            Asset](#Assets_UpdateAsset).
        guilded_social_link (SocialLink | Unset): A social media link for the asset. Maximum of three per asset. Object
            name can be any of: <ul><li>`facebookSocialLink`</li><li>`twitterSocialLink`</li><li>`youtubeSocialLink`</li><li
            >`twitchSocialLink`</li><li>`discordSocialLink`</li><li>`githubSocialLink`</li><li>`robloxSocialLink`</li><li>`g
            uildedSocialLink`</li><li>`devForumSocialLink`</li></ul>For syntax, see the sample request under [Update
            Asset](#Assets_UpdateAsset).
        dev_forum_social_link (SocialLink | Unset): A social media link for the asset. Maximum of three per asset.
            Object name can be any of: <ul><li>`facebookSocialLink`</li><li>`twitterSocialLink`</li><li>`youtubeSocialLink`<
            /li><li>`twitchSocialLink`</li><li>`discordSocialLink`</li><li>`githubSocialLink`</li><li>`robloxSocialLink`</li
            ><li>`guildedSocialLink`</li><li>`devForumSocialLink`</li></ul>For syntax, see the sample request under [Update
            Asset](#Assets_UpdateAsset).
        try_asset_social_link (SocialLink | Unset): A social media link for the asset. Maximum of three per asset.
            Object name can be any of: <ul><li>`facebookSocialLink`</li><li>`twitterSocialLink`</li><li>`youtubeSocialLink`<
            /li><li>`twitchSocialLink`</li><li>`discordSocialLink`</li><li>`githubSocialLink`</li><li>`robloxSocialLink`</li
            ><li>`guildedSocialLink`</li><li>`devForumSocialLink`</li></ul>For syntax, see the sample request under [Update
            Asset](#Assets_UpdateAsset).
        is_published (bool | Unset): Whether the current revision of the asset is published.
    """

    path: None | str | Unset = UNSET
    revision_id: None | str | Unset = UNSET
    revision_create_time: datetime.datetime | None | Unset = UNSET
    asset_id: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    asset_type: AssetType | Unset = UNSET
    creation_context: CreationContext | Unset = UNSET
    moderation_result: ModerationResult | Unset = UNSET
    published: bool | Unset = UNSET
    icon: None | str | Unset = UNSET
    previews: list[Preview] | None | Unset = UNSET
    state: State | Unset = UNSET
    facebook_social_link: SocialLink | Unset = UNSET
    twitter_social_link: SocialLink | Unset = UNSET
    youtube_social_link: SocialLink | Unset = UNSET
    twitch_social_link: SocialLink | Unset = UNSET
    discord_social_link: SocialLink | Unset = UNSET
    github_social_link: SocialLink | Unset = UNSET
    roblox_social_link: SocialLink | Unset = UNSET
    guilded_social_link: SocialLink | Unset = UNSET
    dev_forum_social_link: SocialLink | Unset = UNSET
    try_asset_social_link: SocialLink | Unset = UNSET
    is_published: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        revision_id: None | str | Unset
        if isinstance(self.revision_id, Unset):
            revision_id = UNSET
        else:
            revision_id = self.revision_id

        revision_create_time: None | str | Unset
        if isinstance(self.revision_create_time, Unset):
            revision_create_time = UNSET
        elif isinstance(self.revision_create_time, datetime.datetime):
            revision_create_time = self.revision_create_time.isoformat()
        else:
            revision_create_time = self.revision_create_time

        asset_id = self.asset_id

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        asset_type: str | Unset = UNSET
        if not isinstance(self.asset_type, Unset):
            asset_type = self.asset_type.value

        creation_context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creation_context, Unset):
            creation_context = self.creation_context.to_dict()

        moderation_result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.moderation_result, Unset):
            moderation_result = self.moderation_result.to_dict()

        published = self.published

        icon: None | str | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        previews: list[dict[str, Any]] | None | Unset
        if isinstance(self.previews, Unset):
            previews = UNSET
        elif isinstance(self.previews, list):
            previews = []
            for previews_type_0_item_data in self.previews:
                previews_type_0_item = previews_type_0_item_data.to_dict()
                previews.append(previews_type_0_item)

        else:
            previews = self.previews

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        facebook_social_link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.facebook_social_link, Unset):
            facebook_social_link = self.facebook_social_link.to_dict()

        twitter_social_link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.twitter_social_link, Unset):
            twitter_social_link = self.twitter_social_link.to_dict()

        youtube_social_link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.youtube_social_link, Unset):
            youtube_social_link = self.youtube_social_link.to_dict()

        twitch_social_link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.twitch_social_link, Unset):
            twitch_social_link = self.twitch_social_link.to_dict()

        discord_social_link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.discord_social_link, Unset):
            discord_social_link = self.discord_social_link.to_dict()

        github_social_link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.github_social_link, Unset):
            github_social_link = self.github_social_link.to_dict()

        roblox_social_link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.roblox_social_link, Unset):
            roblox_social_link = self.roblox_social_link.to_dict()

        guilded_social_link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guilded_social_link, Unset):
            guilded_social_link = self.guilded_social_link.to_dict()

        dev_forum_social_link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dev_forum_social_link, Unset):
            dev_forum_social_link = self.dev_forum_social_link.to_dict()

        try_asset_social_link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.try_asset_social_link, Unset):
            try_asset_social_link = self.try_asset_social_link.to_dict()

        is_published = self.is_published

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if revision_id is not UNSET:
            field_dict["revisionId"] = revision_id
        if revision_create_time is not UNSET:
            field_dict["revisionCreateTime"] = revision_create_time
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if asset_type is not UNSET:
            field_dict["assetType"] = asset_type
        if creation_context is not UNSET:
            field_dict["creationContext"] = creation_context
        if moderation_result is not UNSET:
            field_dict["moderationResult"] = moderation_result
        if published is not UNSET:
            field_dict["published"] = published
        if icon is not UNSET:
            field_dict["icon"] = icon
        if previews is not UNSET:
            field_dict["previews"] = previews
        if state is not UNSET:
            field_dict["state"] = state
        if facebook_social_link is not UNSET:
            field_dict["facebookSocialLink"] = facebook_social_link
        if twitter_social_link is not UNSET:
            field_dict["twitterSocialLink"] = twitter_social_link
        if youtube_social_link is not UNSET:
            field_dict["youtubeSocialLink"] = youtube_social_link
        if twitch_social_link is not UNSET:
            field_dict["twitchSocialLink"] = twitch_social_link
        if discord_social_link is not UNSET:
            field_dict["discordSocialLink"] = discord_social_link
        if github_social_link is not UNSET:
            field_dict["githubSocialLink"] = github_social_link
        if roblox_social_link is not UNSET:
            field_dict["robloxSocialLink"] = roblox_social_link
        if guilded_social_link is not UNSET:
            field_dict["guildedSocialLink"] = guilded_social_link
        if dev_forum_social_link is not UNSET:
            field_dict["devForumSocialLink"] = dev_forum_social_link
        if try_asset_social_link is not UNSET:
            field_dict["tryAssetSocialLink"] = try_asset_social_link
        if is_published is not UNSET:
            field_dict["isPublished"] = is_published

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.creation_context import CreationContext  # noqa: PLC0415
        from ..models.moderation_result import ModerationResult  # noqa: PLC0415
        from ..models.preview import Preview  # noqa: PLC0415
        from ..models.social_link import SocialLink  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_revision_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        revision_id = _parse_revision_id(d.pop("revisionId", UNSET))

        def _parse_revision_create_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revision_create_time_type_0 = datetime.datetime.fromisoformat(data)

                return revision_create_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        revision_create_time = _parse_revision_create_time(d.pop("revisionCreateTime", UNSET))

        asset_id = d.pop("assetId", UNSET)

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _asset_type = d.pop("assetType", UNSET)
        asset_type: AssetType | Unset
        if isinstance(_asset_type, Unset):
            asset_type = UNSET
        else:
            asset_type = AssetType(_asset_type)

        _creation_context = d.pop("creationContext", UNSET)
        creation_context: CreationContext | Unset
        if isinstance(_creation_context, Unset):
            creation_context = UNSET
        else:
            creation_context = CreationContext.from_dict(_creation_context)

        _moderation_result = d.pop("moderationResult", UNSET)
        moderation_result: ModerationResult | Unset
        if isinstance(_moderation_result, Unset):
            moderation_result = UNSET
        else:
            moderation_result = ModerationResult.from_dict(_moderation_result)

        published = d.pop("published", UNSET)

        def _parse_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))

        def _parse_previews(data: object) -> list[Preview] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                previews_type_0 = []
                _previews_type_0 = data
                for previews_type_0_item_data in _previews_type_0:
                    previews_type_0_item = Preview.from_dict(previews_type_0_item_data)

                    previews_type_0.append(previews_type_0_item)

                return previews_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Preview] | None | Unset, data)

        previews = _parse_previews(d.pop("previews", UNSET))

        _state = d.pop("state", UNSET)
        state: State | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = State(_state)

        _facebook_social_link = d.pop("facebookSocialLink", UNSET)
        facebook_social_link: SocialLink | Unset
        if isinstance(_facebook_social_link, Unset):
            facebook_social_link = UNSET
        else:
            facebook_social_link = SocialLink.from_dict(_facebook_social_link)

        _twitter_social_link = d.pop("twitterSocialLink", UNSET)
        twitter_social_link: SocialLink | Unset
        if isinstance(_twitter_social_link, Unset):
            twitter_social_link = UNSET
        else:
            twitter_social_link = SocialLink.from_dict(_twitter_social_link)

        _youtube_social_link = d.pop("youtubeSocialLink", UNSET)
        youtube_social_link: SocialLink | Unset
        if isinstance(_youtube_social_link, Unset):
            youtube_social_link = UNSET
        else:
            youtube_social_link = SocialLink.from_dict(_youtube_social_link)

        _twitch_social_link = d.pop("twitchSocialLink", UNSET)
        twitch_social_link: SocialLink | Unset
        if isinstance(_twitch_social_link, Unset):
            twitch_social_link = UNSET
        else:
            twitch_social_link = SocialLink.from_dict(_twitch_social_link)

        _discord_social_link = d.pop("discordSocialLink", UNSET)
        discord_social_link: SocialLink | Unset
        if isinstance(_discord_social_link, Unset):
            discord_social_link = UNSET
        else:
            discord_social_link = SocialLink.from_dict(_discord_social_link)

        _github_social_link = d.pop("githubSocialLink", UNSET)
        github_social_link: SocialLink | Unset
        if isinstance(_github_social_link, Unset):
            github_social_link = UNSET
        else:
            github_social_link = SocialLink.from_dict(_github_social_link)

        _roblox_social_link = d.pop("robloxSocialLink", UNSET)
        roblox_social_link: SocialLink | Unset
        if isinstance(_roblox_social_link, Unset):
            roblox_social_link = UNSET
        else:
            roblox_social_link = SocialLink.from_dict(_roblox_social_link)

        _guilded_social_link = d.pop("guildedSocialLink", UNSET)
        guilded_social_link: SocialLink | Unset
        if isinstance(_guilded_social_link, Unset):
            guilded_social_link = UNSET
        else:
            guilded_social_link = SocialLink.from_dict(_guilded_social_link)

        _dev_forum_social_link = d.pop("devForumSocialLink", UNSET)
        dev_forum_social_link: SocialLink | Unset
        if isinstance(_dev_forum_social_link, Unset):
            dev_forum_social_link = UNSET
        else:
            dev_forum_social_link = SocialLink.from_dict(_dev_forum_social_link)

        _try_asset_social_link = d.pop("tryAssetSocialLink", UNSET)
        try_asset_social_link: SocialLink | Unset
        if isinstance(_try_asset_social_link, Unset):
            try_asset_social_link = UNSET
        else:
            try_asset_social_link = SocialLink.from_dict(_try_asset_social_link)

        is_published = d.pop("isPublished", UNSET)

        assets_upload_api_asset = cls(
            path=path,
            revision_id=revision_id,
            revision_create_time=revision_create_time,
            asset_id=asset_id,
            display_name=display_name,
            description=description,
            asset_type=asset_type,
            creation_context=creation_context,
            moderation_result=moderation_result,
            published=published,
            icon=icon,
            previews=previews,
            state=state,
            facebook_social_link=facebook_social_link,
            twitter_social_link=twitter_social_link,
            youtube_social_link=youtube_social_link,
            twitch_social_link=twitch_social_link,
            discord_social_link=discord_social_link,
            github_social_link=github_social_link,
            roblox_social_link=roblox_social_link,
            guilded_social_link=guilded_social_link,
            dev_forum_social_link=dev_forum_social_link,
            try_asset_social_link=try_asset_social_link,
            is_published=is_published,
        )

        return assets_upload_api_asset
