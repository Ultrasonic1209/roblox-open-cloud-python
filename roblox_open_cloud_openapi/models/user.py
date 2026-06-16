from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_social_network_profiles import UserSocialNetworkProfiles


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """Represents any registered user of Roblox.

    Attributes:
        path (str | Unset): The resource path of the user.

            Format: `users/{user_id}` Example: users/123.
        create_time (datetime.datetime | Unset): The timestamp at which the user was created. Example:
            2023-07-05T12:34:56Z.
        id (str | Unset): Unique ID that identifies a user in Roblox. Example: 123456.
        name (str | Unset): Unique username for a user in Roblox. Example: exampleUser.
        display_name (str | Unset): Display name for the user. Example: userDefinedName.
        about (str | Unset): User-defined information about themselves. Example: Example User's bio.
        locale (str | Unset): Current locale selected by the user. Returns IETF language code. Example: en-US.
        premium (bool | Unset): Whether the user is a premium user. Example: True.
        id_verified (bool | Unset): Specifies if the user is identity-verified. Verification includes, but
            isn't limited to, non-VoIP phone numbers or government IDs.

            To access this data, you need an API key / OAuth token with the following
            scope: user.advanced:read Example: True.
        social_network_profiles (UserSocialNetworkProfiles | Unset): Social network profiles of a user.
    """

    path: str | Unset = UNSET
    create_time: datetime.datetime | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    display_name: str | Unset = UNSET
    about: str | Unset = UNSET
    locale: str | Unset = UNSET
    premium: bool | Unset = UNSET
    id_verified: bool | Unset = UNSET
    social_network_profiles: UserSocialNetworkProfiles | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        id = self.id

        name = self.name

        display_name = self.display_name

        about = self.about

        locale = self.locale

        premium = self.premium

        id_verified = self.id_verified

        social_network_profiles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.social_network_profiles, Unset):
            social_network_profiles = self.social_network_profiles.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if about is not UNSET:
            field_dict["about"] = about
        if locale is not UNSET:
            field_dict["locale"] = locale
        if premium is not UNSET:
            field_dict["premium"] = premium
        if id_verified is not UNSET:
            field_dict["idVerified"] = id_verified
        if social_network_profiles is not UNSET:
            field_dict["socialNetworkProfiles"] = social_network_profiles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_social_network_profiles import UserSocialNetworkProfiles

        d = dict(src_dict)
        path = d.pop("path", UNSET)

        _create_time = d.pop("createTime", UNSET)
        create_time: datetime.datetime | Unset
        if isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = datetime.datetime.fromisoformat(_create_time)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        about = d.pop("about", UNSET)

        locale = d.pop("locale", UNSET)

        premium = d.pop("premium", UNSET)

        id_verified = d.pop("idVerified", UNSET)

        _social_network_profiles = d.pop("socialNetworkProfiles", UNSET)
        social_network_profiles: UserSocialNetworkProfiles | Unset
        if isinstance(_social_network_profiles, Unset):
            social_network_profiles = UNSET
        else:
            social_network_profiles = UserSocialNetworkProfiles.from_dict(_social_network_profiles)

        user = cls(
            path=path,
            create_time=create_time,
            id=id,
            name=name,
            display_name=display_name,
            about=about,
            locale=locale,
            premium=premium,
            id_verified=id_verified,
            social_network_profiles=social_network_profiles,
        )

        user.additional_properties = d
        return user

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
