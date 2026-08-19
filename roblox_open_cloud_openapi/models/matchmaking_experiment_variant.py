from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.place_scoring_config import PlaceScoringConfig
    from ..models.variant_meta import VariantMeta


T = TypeVar("T", bound="MatchmakingExperimentVariant")


@_attrs_define
class MatchmakingExperimentVariant:
    """Variant definition for a matchmaking experiment.

    Attributes:
        variant_meta (None | Unset | VariantMeta): Metadata common to all variants.
        place_matchmaking_configs (list[PlaceScoringConfig] | None | Unset): Per-place matchmaking scoring
            configurations applied when this variant is selected.
    """

    variant_meta: None | Unset | VariantMeta = UNSET
    place_matchmaking_configs: list[PlaceScoringConfig] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.variant_meta import VariantMeta

        variant_meta: dict[str, Any] | None | Unset
        if isinstance(self.variant_meta, Unset):
            variant_meta = UNSET
        elif isinstance(self.variant_meta, VariantMeta):
            variant_meta = self.variant_meta.to_dict()
        else:
            variant_meta = self.variant_meta

        place_matchmaking_configs: list[dict[str, Any]] | None | Unset
        if isinstance(self.place_matchmaking_configs, Unset):
            place_matchmaking_configs = UNSET
        elif isinstance(self.place_matchmaking_configs, list):
            place_matchmaking_configs = []
            for place_matchmaking_configs_type_0_item_data in self.place_matchmaking_configs:
                place_matchmaking_configs_type_0_item = place_matchmaking_configs_type_0_item_data.to_dict()
                place_matchmaking_configs.append(place_matchmaking_configs_type_0_item)

        else:
            place_matchmaking_configs = self.place_matchmaking_configs

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if variant_meta is not UNSET:
            field_dict["variantMeta"] = variant_meta
        if place_matchmaking_configs is not UNSET:
            field_dict["placeMatchmakingConfigs"] = place_matchmaking_configs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.place_scoring_config import PlaceScoringConfig
        from ..models.variant_meta import VariantMeta

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_variant_meta(data: object) -> None | Unset | VariantMeta:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                variant_meta_type_1 = VariantMeta.from_dict(data)

                return variant_meta_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VariantMeta, data)

        variant_meta = _parse_variant_meta(d.pop("variantMeta", UNSET))

        def _parse_place_matchmaking_configs(data: object) -> list[PlaceScoringConfig] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                place_matchmaking_configs_type_0 = []
                _place_matchmaking_configs_type_0 = data
                for place_matchmaking_configs_type_0_item_data in _place_matchmaking_configs_type_0:
                    place_matchmaking_configs_type_0_item = PlaceScoringConfig.from_dict(
                        place_matchmaking_configs_type_0_item_data
                    )

                    place_matchmaking_configs_type_0.append(place_matchmaking_configs_type_0_item)

                return place_matchmaking_configs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PlaceScoringConfig] | None | Unset, data)

        place_matchmaking_configs = _parse_place_matchmaking_configs(d.pop("placeMatchmakingConfigs", UNSET))

        matchmaking_experiment_variant = cls(
            variant_meta=variant_meta,
            place_matchmaking_configs=place_matchmaking_configs,
        )

        return matchmaking_experiment_variant
