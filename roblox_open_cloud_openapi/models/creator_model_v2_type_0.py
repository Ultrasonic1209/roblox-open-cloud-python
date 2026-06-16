from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatorModelV2Type0")


@_attrs_define
class CreatorModelV2Type0:
    """Model representing a creator.

    Attributes:
        creator (None | str | Unset): Deprecated: Please refer to the 'userId' and 'groupId' properties instead.
            The creator type and ID. E.g. user/123 or group/456.
        user_id (int | None | Unset): The User ID of the creator. Required if the asset is individual-user-owned.
        group_id (int | None | Unset): The Group ID. Required if the asset is group-owned.
        name (None | str | Unset): The creator's name.
        verified (bool | None | Unset): Whether the creator is verified.
        latest_group_updater_user_id (int | None | Unset): This value only exists for group-based creators and
            represents the User ID of the creator who most recently updated the asset.
        latest_group_updater_user_name (None | str | Unset): This value only exists for group-based creators and
            represents the name of the creator who most recently updated the asset.
    """

    creator: None | str | Unset = UNSET
    user_id: int | None | Unset = UNSET
    group_id: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    verified: bool | None | Unset = UNSET
    latest_group_updater_user_id: int | None | Unset = UNSET
    latest_group_updater_user_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        creator: None | str | Unset
        if isinstance(self.creator, Unset):
            creator = UNSET
        else:
            creator = self.creator

        user_id: int | None | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        group_id: int | None | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        else:
            group_id = self.group_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        verified: bool | None | Unset
        if isinstance(self.verified, Unset):
            verified = UNSET
        else:
            verified = self.verified

        latest_group_updater_user_id: int | None | Unset
        if isinstance(self.latest_group_updater_user_id, Unset):
            latest_group_updater_user_id = UNSET
        else:
            latest_group_updater_user_id = self.latest_group_updater_user_id

        latest_group_updater_user_name: None | str | Unset
        if isinstance(self.latest_group_updater_user_name, Unset):
            latest_group_updater_user_name = UNSET
        else:
            latest_group_updater_user_name = self.latest_group_updater_user_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if creator is not UNSET:
            field_dict["creator"] = creator
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if name is not UNSET:
            field_dict["name"] = name
        if verified is not UNSET:
            field_dict["verified"] = verified
        if latest_group_updater_user_id is not UNSET:
            field_dict["latestGroupUpdaterUserId"] = latest_group_updater_user_id
        if latest_group_updater_user_name is not UNSET:
            field_dict["latestGroupUpdaterUserName"] = latest_group_updater_user_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_creator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        creator = _parse_creator(d.pop("creator", UNSET))

        def _parse_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_id = _parse_user_id(d.pop("userId", UNSET))

        def _parse_group_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        group_id = _parse_group_id(d.pop("groupId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_verified(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        verified = _parse_verified(d.pop("verified", UNSET))

        def _parse_latest_group_updater_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        latest_group_updater_user_id = _parse_latest_group_updater_user_id(d.pop("latestGroupUpdaterUserId", UNSET))

        def _parse_latest_group_updater_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_group_updater_user_name = _parse_latest_group_updater_user_name(
            d.pop("latestGroupUpdaterUserName", UNSET)
        )

        creator_model_v2_type_0 = cls(
            creator=creator,
            user_id=user_id,
            group_id=group_id,
            name=name,
            verified=verified,
            latest_group_updater_user_id=latest_group_updater_user_id,
            latest_group_updater_user_name=latest_group_updater_user_name,
        )

        return creator_model_v2_type_0
