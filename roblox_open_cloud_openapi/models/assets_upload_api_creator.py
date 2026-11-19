from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetsUploadApiCreator")


@_attrs_define
class AssetsUploadApiCreator:
    """Represents a creator. Only one creator ID is set, according to the creator type.

    Attributes:
        user_id (None | str | Unset): The user ID as a decimal string. Set when the asset is owned by a user.
        group_id (None | str | Unset): The group ID as a decimal string. Set when the asset is owned by a group.
        experience_id (None | str | Unset):
    """

    user_id: None | str | Unset = UNSET
    group_id: None | str | Unset = UNSET
    experience_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        else:
            group_id = self.group_id

        experience_id: None | str | Unset
        if isinstance(self.experience_id, Unset):
            experience_id = UNSET
        else:
            experience_id = self.experience_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if experience_id is not UNSET:
            field_dict["experienceId"] = experience_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("userId", UNSET))

        def _parse_group_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_id = _parse_group_id(d.pop("groupId", UNSET))

        def _parse_experience_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        experience_id = _parse_experience_id(d.pop("experienceId", UNSET))

        assets_upload_api_creator = cls(
            user_id=user_id,
            group_id=group_id,
            experience_id=experience_id,
        )

        return assets_upload_api_creator
