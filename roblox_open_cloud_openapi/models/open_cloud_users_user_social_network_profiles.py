from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.open_cloud_users_user_social_network_profiles_visibility import (
    OpenCloudUsersUserSocialNetworkProfilesVisibility,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenCloudUsersUserSocialNetworkProfiles")


@_attrs_define
class OpenCloudUsersUserSocialNetworkProfiles:
    """Social network profiles of a user.

    Attributes:
        facebook (None | str | Unset): Facebook profile URI.
        twitter (None | str | Unset): Twitter profile URI.
        youtube (None | str | Unset): YouTube profile URI.
        twitch (None | str | Unset): Twitch profile URI.
        guilded (None | str | Unset): Guilded profile URI.
        visibility (OpenCloudUsersUserSocialNetworkProfilesVisibility | Unset): Visibility of the social network
            profiles.

            To access this data, you need an API key / OAuth token with the following
            scope: user.social:read

            Possible values:

              | Value | Description |
              | --- | --- |
              | SOCIAL_NETWORK_VISIBILITY_UNSPECIFIED | Default SocialNetworkVisibility. |
              | NO_ONE | No one |
              | FRIENDS | Friends only |
              | FRIENDS_AND_FOLLOWING | Friends and other users the user follows |
              | FRIENDS_FOLLOWING_AND_FOLLOWERS | Friends, other users the user follows, and other users who follow the user
            |
              | EVERYONE | Everyone |
    """

    facebook: None | str | Unset = UNSET
    twitter: None | str | Unset = UNSET
    youtube: None | str | Unset = UNSET
    twitch: None | str | Unset = UNSET
    guilded: None | str | Unset = UNSET
    visibility: OpenCloudUsersUserSocialNetworkProfilesVisibility | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        facebook: None | str | Unset
        if isinstance(self.facebook, Unset):
            facebook = UNSET
        else:
            facebook = self.facebook

        twitter: None | str | Unset
        if isinstance(self.twitter, Unset):
            twitter = UNSET
        else:
            twitter = self.twitter

        youtube: None | str | Unset
        if isinstance(self.youtube, Unset):
            youtube = UNSET
        else:
            youtube = self.youtube

        twitch: None | str | Unset
        if isinstance(self.twitch, Unset):
            twitch = UNSET
        else:
            twitch = self.twitch

        guilded: None | str | Unset
        if isinstance(self.guilded, Unset):
            guilded = UNSET
        else:
            guilded = self.guilded

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if facebook is not UNSET:
            field_dict["facebook"] = facebook
        if twitter is not UNSET:
            field_dict["twitter"] = twitter
        if youtube is not UNSET:
            field_dict["youtube"] = youtube
        if twitch is not UNSET:
            field_dict["twitch"] = twitch
        if guilded is not UNSET:
            field_dict["guilded"] = guilded
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_facebook(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facebook = _parse_facebook(d.pop("facebook", UNSET))

        def _parse_twitter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        twitter = _parse_twitter(d.pop("twitter", UNSET))

        def _parse_youtube(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        youtube = _parse_youtube(d.pop("youtube", UNSET))

        def _parse_twitch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        twitch = _parse_twitch(d.pop("twitch", UNSET))

        def _parse_guilded(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guilded = _parse_guilded(d.pop("guilded", UNSET))

        _visibility = d.pop("visibility", UNSET)
        visibility: OpenCloudUsersUserSocialNetworkProfilesVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = OpenCloudUsersUserSocialNetworkProfilesVisibility(_visibility)

        open_cloud_users_user_social_network_profiles = cls(
            facebook=facebook,
            twitter=twitter,
            youtube=youtube,
            twitch=twitch,
            guilded=guilded,
            visibility=visibility,
        )

        return open_cloud_users_user_social_network_profiles
