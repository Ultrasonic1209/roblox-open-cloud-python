from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardMetricVariantSelection")


@_attrs_define
class DashboardMetricVariantSelection:
    """DashboardMetricVariantSelection selects one metric variant for a pseudo-dimension.
    Keep this message wire-compatible with ComputedMetricVariantSelection for
    schema-v1 computed sources.

        Attributes:
            pseudo_dimension_key (None | str | Unset):  Default: ''.
            variant_key (None | str | Unset): Schema v3 uses AFC's stable key (e.g. SUM, COUNT_USER, AVERAGE), not its
                catalog
                value (e.g. Sum, CountUser, AVG). Older documents are normalized on migration. Default: ''.
    """

    pseudo_dimension_key: None | str | Unset = ""
    variant_key: None | str | Unset = ""

    def to_dict(self) -> dict[str, Any]:
        pseudo_dimension_key: None | str | Unset
        if isinstance(self.pseudo_dimension_key, Unset):
            pseudo_dimension_key = UNSET
        else:
            pseudo_dimension_key = self.pseudo_dimension_key

        variant_key: None | str | Unset
        if isinstance(self.variant_key, Unset):
            variant_key = UNSET
        else:
            variant_key = self.variant_key

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if pseudo_dimension_key is not UNSET:
            field_dict["pseudoDimensionKey"] = pseudo_dimension_key
        if variant_key is not UNSET:
            field_dict["variantKey"] = variant_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_pseudo_dimension_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pseudo_dimension_key = _parse_pseudo_dimension_key(d.pop("pseudoDimensionKey", UNSET))

        def _parse_variant_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variant_key = _parse_variant_key(d.pop("variantKey", UNSET))

        dashboard_metric_variant_selection = cls(
            pseudo_dimension_key=pseudo_dimension_key,
            variant_key=variant_key,
        )

        return dashboard_metric_variant_selection
