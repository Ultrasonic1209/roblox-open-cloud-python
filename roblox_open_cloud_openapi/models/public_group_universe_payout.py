from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicGroupUniversePayout")


@_attrs_define
class PublicGroupUniversePayout:
    """A recurring payout in the public groups API contract.

    Attributes:
        user_id (int | Unset):
        percentage (int | Unset):
    """

    user_id: int | Unset = UNSET
    percentage: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        percentage = self.percentage

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if percentage is not UNSET:
            field_dict["percentage"] = percentage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        user_id = d.pop("userId", UNSET)

        percentage = d.pop("percentage", UNSET)

        public_group_universe_payout = cls(
            user_id=user_id,
            percentage=percentage,
        )

        return public_group_universe_payout
