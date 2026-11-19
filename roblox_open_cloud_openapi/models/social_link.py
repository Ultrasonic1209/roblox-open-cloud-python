from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialLink")


@_attrs_define
class SocialLink:
    """A social media link for the asset. Maximum of three per asset. Object name can be any of: <ul><li>`facebookSocialLin
    k`</li><li>`twitterSocialLink`</li><li>`youtubeSocialLink`</li><li>`twitchSocialLink`</li><li>`discordSocialLink`</l
    i><li>`githubSocialLink`</li><li>`robloxSocialLink`</li><li>`guildedSocialLink`</li><li>`devForumSocialLink`</li></u
    l>For syntax, see the sample request under [Update Asset](#Assets_UpdateAsset).

        Attributes:
            title (None | str | Unset): An optional title for the social media link. Not used on the Creator Hub.
            uri (None | str | Unset): The URI for the social media link. Must match the expected format for the type of
                link. For example, the URI for a `twitchSocialLink` object must be of the format `https://twitch.tv/your-
                channel`.
    """

    title: None | str | Unset = UNSET
    uri: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        uri: None | str | Unset
        if isinstance(self.uri, Unset):
            uri = UNSET
        else:
            uri = self.uri

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uri = _parse_uri(d.pop("uri", UNSET))

        social_link = cls(
            title=title,
            uri=uri,
        )

        return social_link
