from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VariantMeta")


@_attrs_define
class VariantMeta:
    """Metadata shared by every experiment variant.

    Attributes:
        variant_id (None | str | Unset): Unique identifier for the variant. Only assigned once the experiment starts
            running;
            empty or null for draft variants.
        label (None | str | Unset): Human-readable label for the variant, e.g. `Control`, `Treatment A`. Non-empty,
            at most 50 characters; must start with a letter and contain only letters, digits, spaces,
            underscores, or hyphens.
        is_baseline (bool | Unset): True iff this variant is the baseline. Exactly one variant must be the baseline.
        weight (int | Unset): Relative traffic weight for this variant. The platform normalizes across all variants,
            so weights do not have to sum to 100.
    """

    variant_id: None | str | Unset = UNSET
    label: None | str | Unset = UNSET
    is_baseline: bool | Unset = UNSET
    weight: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        variant_id: None | str | Unset
        if isinstance(self.variant_id, Unset):
            variant_id = UNSET
        else:
            variant_id = self.variant_id

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        is_baseline = self.is_baseline

        weight = self.weight

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if variant_id is not UNSET:
            field_dict["variantId"] = variant_id
        if label is not UNSET:
            field_dict["label"] = label
        if is_baseline is not UNSET:
            field_dict["isBaseline"] = is_baseline
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_variant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variant_id = _parse_variant_id(d.pop("variantId", UNSET))

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        is_baseline = d.pop("isBaseline", UNSET)

        weight = d.pop("weight", UNSET)

        variant_meta = cls(
            variant_id=variant_id,
            label=label,
            is_baseline=is_baseline,
            weight=weight,
        )

        return variant_meta
