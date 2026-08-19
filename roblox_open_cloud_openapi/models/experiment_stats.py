from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExperimentStats")


@_attrs_define
class ExperimentStats:
    """Computed stats for a running experiment.

    Attributes:
        is_srm_detected (bool | Unset): True if Sample Ratio Mismatch (SRM) was detected for the experiment.
    """

    is_srm_detected: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_srm_detected = self.is_srm_detected

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_srm_detected is not UNSET:
            field_dict["isSrmDetected"] = is_srm_detected

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        is_srm_detected = d.pop("isSrmDetected", UNSET)

        experiment_stats = cls(
            is_srm_detected=is_srm_detected,
        )

        return experiment_stats
