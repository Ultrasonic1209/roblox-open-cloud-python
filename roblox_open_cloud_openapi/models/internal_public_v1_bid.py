from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.internal_public_v1_bid_strategy import InternalPublicV1BidStrategy
from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalPublicV1Bid")


@_attrs_define
class InternalPublicV1Bid:
    """
    Attributes:
        strategy (InternalPublicV1BidStrategy | Unset): The bidding strategy. v1 campaigns are always `AUTOMATED`.
    """

    strategy: InternalPublicV1BidStrategy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strategy: str | Unset = UNSET
        if not isinstance(self.strategy, Unset):
            strategy = self.strategy.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if strategy is not UNSET:
            field_dict["strategy"] = strategy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _strategy = d.pop("strategy", UNSET)
        strategy: InternalPublicV1BidStrategy | Unset
        if isinstance(_strategy, Unset):
            strategy = UNSET
        else:
            strategy = InternalPublicV1BidStrategy(_strategy)

        internal_public_v1_bid = cls(
            strategy=strategy,
        )

        internal_public_v1_bid.additional_properties = d
        return internal_public_v1_bid

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
