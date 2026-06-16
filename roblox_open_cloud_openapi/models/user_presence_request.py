from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserPresenceRequest")


@_attrs_define
class UserPresenceRequest:
    """
    Attributes:
        user_ids (list[int] | None | Unset):
    """

    user_ids: list[int] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_ids: list[int] | None | Unset
        if isinstance(self.user_ids, Unset):
            user_ids = UNSET
        elif isinstance(self.user_ids, list):
            user_ids = self.user_ids

        else:
            user_ids = self.user_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_ids is not UNSET:
            field_dict["userIds"] = user_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_user_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_ids_type_0 = cast(list[int], data)

                return user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        user_ids = _parse_user_ids(d.pop("userIds", UNSET))

        user_presence_request = cls(
            user_ids=user_ids,
        )

        return user_presence_request
