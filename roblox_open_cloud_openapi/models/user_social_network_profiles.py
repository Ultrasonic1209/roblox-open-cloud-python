from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_social_network_profiles_visibility import UserSocialNetworkProfilesVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserSocialNetworkProfiles")


@_attrs_define
class UserSocialNetworkProfiles:
    """Social network profiles of a user.

    Attributes:
        facebook (str | Unset): Facebook profile URI.
        twitter (str | Unset): Twitter profile URI.
        youtube (str | Unset): YouTube profile URI.
        twitch (str | Unset): Twitch profile URI.
        guilded (str | Unset): Guilded profile URI.
        visibility (UserSocialNetworkProfilesVisibility | Unset): Visibility of the social network profiles.

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
              | EVERYONE | Everyone | Example: SOCIAL_NETWORK_VISIBILITY_UNSPECIFIED.
    """

    facebook: str | Unset = UNSET
    twitter: str | Unset = UNSET
    youtube: str | Unset = UNSET
    twitch: str | Unset = UNSET
    guilded: str | Unset = UNSET
    visibility: UserSocialNetworkProfilesVisibility | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        facebook = self.facebook

        twitter = self.twitter

        youtube = self.youtube

        twitch = self.twitch

        guilded = self.guilded

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        facebook = d.pop("facebook", UNSET)

        twitter = d.pop("twitter", UNSET)

        youtube = d.pop("youtube", UNSET)

        twitch = d.pop("twitch", UNSET)

        guilded = d.pop("guilded", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: UserSocialNetworkProfilesVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = UserSocialNetworkProfilesVisibility(_visibility)

        user_social_network_profiles = cls(
            facebook=facebook,
            twitter=twitter,
            youtube=youtube,
            twitch=twitch,
            guilded=guilded,
            visibility=visibility,
        )

        user_social_network_profiles.additional_properties = d
        return user_social_network_profiles

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
