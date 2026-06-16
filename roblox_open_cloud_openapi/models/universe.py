from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.universe_age_rating import UniverseAgeRating
from ..models.universe_visibility import UniverseVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.universe_social_link import UniverseSocialLink


T = TypeVar("T", bound="Universe")


@_attrs_define
class Universe:
    """Represents a Roblox experience.

    Attributes:
        template_root_place (str): The resource path of the template place, used for CreateUniverse.
            The root place of the newly-created universe will be a clone of this
            template. A list of the valid template places can be obtained from
            ListTemplatePlaces. Format: universes/{universe_id}/places/{place_id} Example:
            universes/{universe_id}/places/{place_id}.
        path (str | Unset): The resource path of the universe.

            Format: `universes/{universe_id}` Example: universes/123.
        create_time (datetime.datetime | Unset): The timestamp when the universe was created. Example:
            2023-07-05T12:34:56Z.
        update_time (datetime.datetime | Unset): The timestamp when the universe was last updated. Example:
            2023-07-05T12:34:56Z.
        display_name (str | Unset): The name of the universe.

            This field can be updated by updating the root place's name. Example: ROBLOX Battle [OPEN].
        description (str | Unset): The description of the universe.

            This field can be updated by updating the root place's description. Example: OPEN SOURCE!
             Feel free to check out how we made this game and ask us about it!.
        user (str | Unset): The universe is user-owned.
        group (str | Unset): The universe is group-owned.
        visibility (UniverseVisibility | Unset): Whether or not the universe is publicly accessible.

            Possible values:

              | Value | Description |
              | --- | --- |
              | VISIBILITY_UNSPECIFIED | Updates using this value will throw an error on the backend. |
              | PUBLIC | The universe is public. |
              | PRIVATE | The universe is private.  If a universe's visibility is set to PRIVATE, all active players will
            immediately be removed from all running servers. | Example: VISIBILITY_UNSPECIFIED.
        facebook_social_link (UniverseSocialLink | Unset): A social link that may be associated with the universe.

            Can only be removed when using a field mask.
        twitter_social_link (UniverseSocialLink | Unset): A social link that may be associated with the universe.

            Can only be removed when using a field mask.
        youtube_social_link (UniverseSocialLink | Unset): A social link that may be associated with the universe.

            Can only be removed when using a field mask.
        twitch_social_link (UniverseSocialLink | Unset): A social link that may be associated with the universe.

            Can only be removed when using a field mask.
        discord_social_link (UniverseSocialLink | Unset): A social link that may be associated with the universe.

            Can only be removed when using a field mask.
        roblox_group_social_link (UniverseSocialLink | Unset): A social link that may be associated with the universe.

            Can only be removed when using a field mask.
        guilded_social_link (UniverseSocialLink | Unset): A social link that may be associated with the universe.

            Can only be removed when using a field mask.
        voice_chat_enabled (bool | Unset): Whether or not voice chat is enabled for users in the Experience.

            Updating this value will not affect active servers. Example: True.
        age_rating (UniverseAgeRating | Unset): The age rating of this universe.

            Possible values:

              | Value | Description |
              | --- | --- |
              | AGE_RATING_UNSPECIFIED | The age rating is not set. |
              | AGE_RATING_ALL | Supported for all users. |
              | AGE_RATING_9_PLUS | Supported for users aged 9 and up. |
              | AGE_RATING_13_PLUS | Supported for users aged 13 and up. |
              | AGE_RATING_17_PLUS | Supported for users aged 17 and up. | Example: AGE_RATING_UNSPECIFIED.
        private_server_price_robux (int | Unset): Represents the price in Robux of private servers.

            If unset, private servers are not supported for this universe.

            Can only be disabled when using a field mask.

            Setting to null will disable all active private servers.

            Changing the price will cancel all private server subscriptions.
        desktop_enabled (bool | Unset): Whether or not players can join the Experience via Desktop. Example: True.
        mobile_enabled (bool | Unset): Whether or not players can join the Experience via Mobile. Example: True.
        tablet_enabled (bool | Unset): Whether or not players can join the Experience via Tablet. Example: True.
        console_enabled (bool | Unset): Whether or not players can join the Experience via Console. Example: True.
        vr_enabled (bool | Unset): Whether or not players can join the Experience via VR. Example: True.
        root_place (str | Unset): The resource path of the root place of this universe
            Format: universes/{universe_id}/places/{place_id}
    """

    template_root_place: str
    path: str | Unset = UNSET
    create_time: datetime.datetime | Unset = UNSET
    update_time: datetime.datetime | Unset = UNSET
    display_name: str | Unset = UNSET
    description: str | Unset = UNSET
    user: str | Unset = UNSET
    group: str | Unset = UNSET
    visibility: UniverseVisibility | Unset = UNSET
    facebook_social_link: UniverseSocialLink | Unset = UNSET
    twitter_social_link: UniverseSocialLink | Unset = UNSET
    youtube_social_link: UniverseSocialLink | Unset = UNSET
    twitch_social_link: UniverseSocialLink | Unset = UNSET
    discord_social_link: UniverseSocialLink | Unset = UNSET
    roblox_group_social_link: UniverseSocialLink | Unset = UNSET
    guilded_social_link: UniverseSocialLink | Unset = UNSET
    voice_chat_enabled: bool | Unset = UNSET
    age_rating: UniverseAgeRating | Unset = UNSET
    private_server_price_robux: int | Unset = UNSET
    desktop_enabled: bool | Unset = UNSET
    mobile_enabled: bool | Unset = UNSET
    tablet_enabled: bool | Unset = UNSET
    console_enabled: bool | Unset = UNSET
    vr_enabled: bool | Unset = UNSET
    root_place: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_root_place = self.template_root_place

        path = self.path

        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        update_time: str | Unset = UNSET
        if not isinstance(self.update_time, Unset):
            update_time = self.update_time.isoformat()

        display_name = self.display_name

        description = self.description

        user = self.user

        group = self.group

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

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

        roblox_group_social_link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.roblox_group_social_link, Unset):
            roblox_group_social_link = self.roblox_group_social_link.to_dict()

        guilded_social_link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guilded_social_link, Unset):
            guilded_social_link = self.guilded_social_link.to_dict()

        voice_chat_enabled = self.voice_chat_enabled

        age_rating: str | Unset = UNSET
        if not isinstance(self.age_rating, Unset):
            age_rating = self.age_rating.value

        private_server_price_robux = self.private_server_price_robux

        desktop_enabled = self.desktop_enabled

        mobile_enabled = self.mobile_enabled

        tablet_enabled = self.tablet_enabled

        console_enabled = self.console_enabled

        vr_enabled = self.vr_enabled

        root_place = self.root_place

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "templateRootPlace": template_root_place,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if update_time is not UNSET:
            field_dict["updateTime"] = update_time
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if user is not UNSET:
            field_dict["user"] = user
        if group is not UNSET:
            field_dict["group"] = group
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
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
        if roblox_group_social_link is not UNSET:
            field_dict["robloxGroupSocialLink"] = roblox_group_social_link
        if guilded_social_link is not UNSET:
            field_dict["guildedSocialLink"] = guilded_social_link
        if voice_chat_enabled is not UNSET:
            field_dict["voiceChatEnabled"] = voice_chat_enabled
        if age_rating is not UNSET:
            field_dict["ageRating"] = age_rating
        if private_server_price_robux is not UNSET:
            field_dict["privateServerPriceRobux"] = private_server_price_robux
        if desktop_enabled is not UNSET:
            field_dict["desktopEnabled"] = desktop_enabled
        if mobile_enabled is not UNSET:
            field_dict["mobileEnabled"] = mobile_enabled
        if tablet_enabled is not UNSET:
            field_dict["tabletEnabled"] = tablet_enabled
        if console_enabled is not UNSET:
            field_dict["consoleEnabled"] = console_enabled
        if vr_enabled is not UNSET:
            field_dict["vrEnabled"] = vr_enabled
        if root_place is not UNSET:
            field_dict["rootPlace"] = root_place

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.universe_social_link import UniverseSocialLink

        d = dict(src_dict)
        template_root_place = d.pop("templateRootPlace")

        path = d.pop("path", UNSET)

        _create_time = d.pop("createTime", UNSET)
        create_time: datetime.datetime | Unset
        if isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = datetime.datetime.fromisoformat(_create_time)

        _update_time = d.pop("updateTime", UNSET)
        update_time: datetime.datetime | Unset
        if isinstance(_update_time, Unset):
            update_time = UNSET
        else:
            update_time = datetime.datetime.fromisoformat(_update_time)

        display_name = d.pop("displayName", UNSET)

        description = d.pop("description", UNSET)

        user = d.pop("user", UNSET)

        group = d.pop("group", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: UniverseVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = UniverseVisibility(_visibility)

        _facebook_social_link = d.pop("facebookSocialLink", UNSET)
        facebook_social_link: UniverseSocialLink | Unset
        if isinstance(_facebook_social_link, Unset):
            facebook_social_link = UNSET
        else:
            facebook_social_link = UniverseSocialLink.from_dict(_facebook_social_link)

        _twitter_social_link = d.pop("twitterSocialLink", UNSET)
        twitter_social_link: UniverseSocialLink | Unset
        if isinstance(_twitter_social_link, Unset):
            twitter_social_link = UNSET
        else:
            twitter_social_link = UniverseSocialLink.from_dict(_twitter_social_link)

        _youtube_social_link = d.pop("youtubeSocialLink", UNSET)
        youtube_social_link: UniverseSocialLink | Unset
        if isinstance(_youtube_social_link, Unset):
            youtube_social_link = UNSET
        else:
            youtube_social_link = UniverseSocialLink.from_dict(_youtube_social_link)

        _twitch_social_link = d.pop("twitchSocialLink", UNSET)
        twitch_social_link: UniverseSocialLink | Unset
        if isinstance(_twitch_social_link, Unset):
            twitch_social_link = UNSET
        else:
            twitch_social_link = UniverseSocialLink.from_dict(_twitch_social_link)

        _discord_social_link = d.pop("discordSocialLink", UNSET)
        discord_social_link: UniverseSocialLink | Unset
        if isinstance(_discord_social_link, Unset):
            discord_social_link = UNSET
        else:
            discord_social_link = UniverseSocialLink.from_dict(_discord_social_link)

        _roblox_group_social_link = d.pop("robloxGroupSocialLink", UNSET)
        roblox_group_social_link: UniverseSocialLink | Unset
        if isinstance(_roblox_group_social_link, Unset):
            roblox_group_social_link = UNSET
        else:
            roblox_group_social_link = UniverseSocialLink.from_dict(_roblox_group_social_link)

        _guilded_social_link = d.pop("guildedSocialLink", UNSET)
        guilded_social_link: UniverseSocialLink | Unset
        if isinstance(_guilded_social_link, Unset):
            guilded_social_link = UNSET
        else:
            guilded_social_link = UniverseSocialLink.from_dict(_guilded_social_link)

        voice_chat_enabled = d.pop("voiceChatEnabled", UNSET)

        _age_rating = d.pop("ageRating", UNSET)
        age_rating: UniverseAgeRating | Unset
        if isinstance(_age_rating, Unset):
            age_rating = UNSET
        else:
            age_rating = UniverseAgeRating(_age_rating)

        private_server_price_robux = d.pop("privateServerPriceRobux", UNSET)

        desktop_enabled = d.pop("desktopEnabled", UNSET)

        mobile_enabled = d.pop("mobileEnabled", UNSET)

        tablet_enabled = d.pop("tabletEnabled", UNSET)

        console_enabled = d.pop("consoleEnabled", UNSET)

        vr_enabled = d.pop("vrEnabled", UNSET)

        root_place = d.pop("rootPlace", UNSET)

        universe = cls(
            template_root_place=template_root_place,
            path=path,
            create_time=create_time,
            update_time=update_time,
            display_name=display_name,
            description=description,
            user=user,
            group=group,
            visibility=visibility,
            facebook_social_link=facebook_social_link,
            twitter_social_link=twitter_social_link,
            youtube_social_link=youtube_social_link,
            twitch_social_link=twitch_social_link,
            discord_social_link=discord_social_link,
            roblox_group_social_link=roblox_group_social_link,
            guilded_social_link=guilded_social_link,
            voice_chat_enabled=voice_chat_enabled,
            age_rating=age_rating,
            private_server_price_robux=private_server_price_robux,
            desktop_enabled=desktop_enabled,
            mobile_enabled=mobile_enabled,
            tablet_enabled=tablet_enabled,
            console_enabled=console_enabled,
            vr_enabled=vr_enabled,
            root_place=root_place,
        )

        universe.additional_properties = d
        return universe

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
