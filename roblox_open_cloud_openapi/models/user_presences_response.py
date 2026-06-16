from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_presence import UserPresence


T = TypeVar("T", bound="UserPresencesResponse")


@_attrs_define
class UserPresencesResponse:
    """
    Attributes:
        user_presences (list[UserPresence] | None | Unset):
    """

    user_presences: list[UserPresence] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_presences: list[dict[str, Any]] | None | Unset
        if isinstance(self.user_presences, Unset):
            user_presences = UNSET
        elif isinstance(self.user_presences, list):
            user_presences = []
            for user_presences_type_0_item_data in self.user_presences:
                user_presences_type_0_item = user_presences_type_0_item_data.to_dict()
                user_presences.append(user_presences_type_0_item)

        else:
            user_presences = self.user_presences

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_presences is not UNSET:
            field_dict["userPresences"] = user_presences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_presence import UserPresence

        d = dict(src_dict)

        def _parse_user_presences(data: object) -> list[UserPresence] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_presences_type_0 = []
                _user_presences_type_0 = data
                for user_presences_type_0_item_data in _user_presences_type_0:
                    user_presences_type_0_item = UserPresence.from_dict(user_presences_type_0_item_data)

                    user_presences_type_0.append(user_presences_type_0_item)

                return user_presences_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UserPresence] | None | Unset, data)

        user_presences = _parse_user_presences(d.pop("userPresences", UNSET))

        user_presences_response = cls(
            user_presences=user_presences,
        )

        return user_presences_response
