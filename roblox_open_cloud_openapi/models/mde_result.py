from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MdeResult")


@_attrs_define
class MdeResult:
    """MDE calculation result. Returned in the `operation.result` field on a successful
    `POST .../experiments:calculateMde` call.

        Attributes:
            total_sample_size (int | Unset): Estimated total sample size required for the experiment.
            mde_relative_percentages (list[float] | None | Unset): MDE expressed as a relative percentage of the goal
                metric, per non-baseline variant.
            minimum_sample_size_threshold (int | Unset): Below this sample-size threshold the MDE estimate is unreliable.
    """

    total_sample_size: int | Unset = UNSET
    mde_relative_percentages: list[float] | None | Unset = UNSET
    minimum_sample_size_threshold: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        total_sample_size = self.total_sample_size

        mde_relative_percentages: list[float] | None | Unset
        if isinstance(self.mde_relative_percentages, Unset):
            mde_relative_percentages = UNSET
        elif isinstance(self.mde_relative_percentages, list):
            mde_relative_percentages = self.mde_relative_percentages

        else:
            mde_relative_percentages = self.mde_relative_percentages

        minimum_sample_size_threshold = self.minimum_sample_size_threshold

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if total_sample_size is not UNSET:
            field_dict["totalSampleSize"] = total_sample_size
        if mde_relative_percentages is not UNSET:
            field_dict["mdeRelativePercentages"] = mde_relative_percentages
        if minimum_sample_size_threshold is not UNSET:
            field_dict["minimumSampleSizeThreshold"] = minimum_sample_size_threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        total_sample_size = d.pop("totalSampleSize", UNSET)

        def _parse_mde_relative_percentages(data: object) -> list[float] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mde_relative_percentages_type_0 = cast(list[float], data)

                return mde_relative_percentages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[float] | None | Unset, data)

        mde_relative_percentages = _parse_mde_relative_percentages(d.pop("mdeRelativePercentages", UNSET))

        minimum_sample_size_threshold = d.pop("minimumSampleSizeThreshold", UNSET)

        mde_result = cls(
            total_sample_size=total_sample_size,
            mde_relative_percentages=mde_relative_percentages,
            minimum_sample_size_threshold=minimum_sample_size_threshold,
        )

        return mde_result
