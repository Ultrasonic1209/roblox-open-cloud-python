from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalPublicV1PerformanceTotals")


@_attrs_define
class InternalPublicV1PerformanceTotals:
    """
    Attributes:
        clicks (int | Unset): The number of clicks on an ad.
        cpm_micros (str | Unset): Cost per 1,000 impressions in micro-USD, as a decimal string.
        cpp_micros (str | Unset): Cost per play in micro-USD, as a decimal string.
        ctr (float | Unset): The click-through rate: clicks divided by impressions, from 0 to 1.
        impressions (int | Unset): The number of times an ad was shown.
        play_rate (float | Unset): The play rate: plays divided by impressions, from 0 to 1.
        plays (int | Unset): The number of resulting experience plays.
        spend_micros (str | Unset): Total spend in micro-USD, as a decimal string (for example, `5000000` = $5.00).
    """

    clicks: int | Unset = UNSET
    cpm_micros: str | Unset = UNSET
    cpp_micros: str | Unset = UNSET
    ctr: float | Unset = UNSET
    impressions: int | Unset = UNSET
    play_rate: float | Unset = UNSET
    plays: int | Unset = UNSET
    spend_micros: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clicks = self.clicks

        cpm_micros = self.cpm_micros

        cpp_micros = self.cpp_micros

        ctr = self.ctr

        impressions = self.impressions

        play_rate = self.play_rate

        plays = self.plays

        spend_micros = self.spend_micros

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if clicks is not UNSET:
            field_dict["clicks"] = clicks
        if cpm_micros is not UNSET:
            field_dict["cpmMicros"] = cpm_micros
        if cpp_micros is not UNSET:
            field_dict["cppMicros"] = cpp_micros
        if ctr is not UNSET:
            field_dict["ctr"] = ctr
        if impressions is not UNSET:
            field_dict["impressions"] = impressions
        if play_rate is not UNSET:
            field_dict["playRate"] = play_rate
        if plays is not UNSET:
            field_dict["plays"] = plays
        if spend_micros is not UNSET:
            field_dict["spendMicros"] = spend_micros

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        clicks = d.pop("clicks", UNSET)

        cpm_micros = d.pop("cpmMicros", UNSET)

        cpp_micros = d.pop("cppMicros", UNSET)

        ctr = d.pop("ctr", UNSET)

        impressions = d.pop("impressions", UNSET)

        play_rate = d.pop("playRate", UNSET)

        plays = d.pop("plays", UNSET)

        spend_micros = d.pop("spendMicros", UNSET)

        internal_public_v1_performance_totals = cls(
            clicks=clicks,
            cpm_micros=cpm_micros,
            cpp_micros=cpp_micros,
            ctr=ctr,
            impressions=impressions,
            play_rate=play_rate,
            plays=plays,
            spend_micros=spend_micros,
        )

        internal_public_v1_performance_totals.additional_properties = d
        return internal_public_v1_performance_totals

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
