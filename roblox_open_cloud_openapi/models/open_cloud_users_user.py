from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_cloud_users_user_social_network_profiles import OpenCloudUsersUserSocialNetworkProfiles


T = TypeVar("T", bound="OpenCloudUsersUser")


@_attrs_define
class OpenCloudUsersUser:
    """Represents any registered user of Roblox.

    Attributes:
        path (None | str | Unset): The resource path of the user.

            Format: `users/{user_id}`
        create_time (datetime.datetime | None | Unset): The timestamp at which the user was created.
        id (None | str | Unset): Unique ID that identifies a user in Roblox.
        name (None | str | Unset): Unique username for a user in Roblox.
        display_name (None | str | Unset): Display name for the user.
        about (None | str | Unset): User-defined information about themselves.
        locale (None | str | Unset): Current locale selected by the user. Returns IETF language code.
        premium (bool | Unset): Whether the user is a premium user.
        id_verified (bool | None | Unset): Specifies if the user is identity-verified. Verification includes, but
            isn't limited to, non-VoIP phone numbers or government IDs.

            To access this data, you need an API key / OAuth token with the following
            scope: user.advanced:read. The field is omitted from the response when the
            caller is not authorized to read it.
        social_network_profiles (None | OpenCloudUsersUserSocialNetworkProfiles | Unset): User's social network profiles
            and visibility.
    """

    path: None | str | Unset = UNSET
    create_time: datetime.datetime | None | Unset = UNSET
    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    about: None | str | Unset = UNSET
    locale: None | str | Unset = UNSET
    premium: bool | Unset = UNSET
    id_verified: bool | None | Unset = UNSET
    social_network_profiles: None | OpenCloudUsersUserSocialNetworkProfiles | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.open_cloud_users_user_social_network_profiles import OpenCloudUsersUserSocialNetworkProfiles

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        create_time: None | str | Unset
        if isinstance(self.create_time, Unset):
            create_time = UNSET
        elif isinstance(self.create_time, datetime.datetime):
            create_time = self.create_time.isoformat()
        else:
            create_time = self.create_time

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        about: None | str | Unset
        if isinstance(self.about, Unset):
            about = UNSET
        else:
            about = self.about

        locale: None | str | Unset
        if isinstance(self.locale, Unset):
            locale = UNSET
        else:
            locale = self.locale

        premium = self.premium

        id_verified: bool | None | Unset
        if isinstance(self.id_verified, Unset):
            id_verified = UNSET
        else:
            id_verified = self.id_verified

        social_network_profiles: dict[str, Any] | None | Unset
        if isinstance(self.social_network_profiles, Unset):
            social_network_profiles = UNSET
        elif isinstance(self.social_network_profiles, OpenCloudUsersUserSocialNetworkProfiles):
            social_network_profiles = self.social_network_profiles.to_dict()
        else:
            social_network_profiles = self.social_network_profiles

        field_dict: dict[str, Any] = {}

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
        from ..models.open_cloud_users_user_social_network_profiles import OpenCloudUsersUserSocialNetworkProfiles

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_create_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                create_time_type_0 = datetime.datetime.fromisoformat(data)

                return create_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        create_time = _parse_create_time(d.pop("createTime", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        def _parse_about(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        about = _parse_about(d.pop("about", UNSET))

        def _parse_locale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locale = _parse_locale(d.pop("locale", UNSET))

        premium = d.pop("premium", UNSET)

        def _parse_id_verified(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        id_verified = _parse_id_verified(d.pop("idVerified", UNSET))

        def _parse_social_network_profiles(data: object) -> None | OpenCloudUsersUserSocialNetworkProfiles | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                social_network_profiles_type_1 = OpenCloudUsersUserSocialNetworkProfiles.from_dict(data)

                return social_network_profiles_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OpenCloudUsersUserSocialNetworkProfiles | Unset, data)

        social_network_profiles = _parse_social_network_profiles(d.pop("socialNetworkProfiles", UNSET))

        open_cloud_users_user = cls(
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

        return open_cloud_users_user
