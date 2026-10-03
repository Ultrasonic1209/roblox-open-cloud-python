from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicUserUniversePayout")


@_attrs_define
class PublicUserUniversePayout:
    """A payout-visible universe in the public groups API contract.

    Attributes:
        universe_id (int | Unset):
        percentage (int | Unset):
    """

    universe_id: int | Unset = UNSET
    percentage: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        universe_id = self.universe_id

        percentage = self.percentage

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if percentage is not UNSET:
            field_dict["percentage"] = percentage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        universe_id = d.pop("universeId", UNSET)

        percentage = d.pop("percentage", UNSET)

        public_user_universe_payout = cls(
            universe_id=universe_id,
            percentage=percentage,
        )

        return public_user_universe_payout
