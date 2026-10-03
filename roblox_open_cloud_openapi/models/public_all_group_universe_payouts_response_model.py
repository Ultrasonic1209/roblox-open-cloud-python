from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_group_universe_payout import PublicGroupUniversePayout


T = TypeVar("T", bound="PublicAllGroupUniversePayoutsResponseModel")


@_attrs_define
class PublicAllGroupUniversePayoutsResponseModel:
    """Public response for recurring payouts.

    Attributes:
        payouts (list[PublicGroupUniversePayout] | None | Unset):
    """

    payouts: list[PublicGroupUniversePayout] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        payouts: list[dict[str, Any]] | None | Unset
        if isinstance(self.payouts, Unset):
            payouts = UNSET
        elif isinstance(self.payouts, list):
            payouts = []
            for payouts_type_0_item_data in self.payouts:
                payouts_type_0_item = payouts_type_0_item_data.to_dict()
                payouts.append(payouts_type_0_item)

        else:
            payouts = self.payouts

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if payouts is not UNSET:
            field_dict["payouts"] = payouts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_group_universe_payout import PublicGroupUniversePayout

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_payouts(data: object) -> list[PublicGroupUniversePayout] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                payouts_type_0 = []
                _payouts_type_0 = data
                for payouts_type_0_item_data in _payouts_type_0:
                    payouts_type_0_item = PublicGroupUniversePayout.from_dict(payouts_type_0_item_data)

                    payouts_type_0.append(payouts_type_0_item)

                return payouts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PublicGroupUniversePayout] | None | Unset, data)

        payouts = _parse_payouts(d.pop("payouts", UNSET))

        public_all_group_universe_payouts_response_model = cls(
            payouts=payouts,
        )

        return public_all_group_universe_payouts_response_model
