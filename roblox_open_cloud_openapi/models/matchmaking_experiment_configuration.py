from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matchmaking_experiment_variant import MatchmakingExperimentVariant


T = TypeVar("T", bound="MatchmakingExperimentConfiguration")


@_attrs_define
class MatchmakingExperimentConfiguration:
    """Configuration for a matchmaking experiment.

    Attributes:
        variants (list[MatchmakingExperimentVariant] | None | Unset): Variants participating in the experiment.
    """

    variants: list[MatchmakingExperimentVariant] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        variants: list[dict[str, Any]] | None | Unset
        if isinstance(self.variants, Unset):
            variants = UNSET
        elif isinstance(self.variants, list):
            variants = []
            for variants_type_0_item_data in self.variants:
                variants_type_0_item = variants_type_0_item_data.to_dict()
                variants.append(variants_type_0_item)

        else:
            variants = self.variants

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if variants is not UNSET:
            field_dict["variants"] = variants

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matchmaking_experiment_variant import MatchmakingExperimentVariant

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_variants(data: object) -> list[MatchmakingExperimentVariant] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                variants_type_0 = []
                _variants_type_0 = data
                for variants_type_0_item_data in _variants_type_0:
                    variants_type_0_item = MatchmakingExperimentVariant.from_dict(variants_type_0_item_data)

                    variants_type_0.append(variants_type_0_item)

                return variants_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MatchmakingExperimentVariant] | None | Unset, data)

        variants = _parse_variants(d.pop("variants", UNSET))

        matchmaking_experiment_configuration = cls(
            variants=variants,
        )

        return matchmaking_experiment_configuration
