from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.experiment_config_entry import ExperimentConfigEntry
    from ..models.variant_meta import VariantMeta


T = TypeVar("T", bound="SingleConfigExperimentVariant")


@_attrs_define
class SingleConfigExperimentVariant:
    """Variant definition for an in-game-config experiment
    (CreatorConfigsPublicApi.Models.Experimentation.InGameConfigExperimentConfiguration).

        Attributes:
            variant_meta (None | Unset | VariantMeta): Metadata common to all variants.
            config_entry (ExperimentConfigEntry | None | Unset): The config entry value for this variant. Required for
                non-`IsBaseline` variants.
    """

    variant_meta: None | Unset | VariantMeta = UNSET
    config_entry: ExperimentConfigEntry | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.experiment_config_entry import ExperimentConfigEntry
        from ..models.variant_meta import VariantMeta

        variant_meta: dict[str, Any] | None | Unset
        if isinstance(self.variant_meta, Unset):
            variant_meta = UNSET
        elif isinstance(self.variant_meta, VariantMeta):
            variant_meta = self.variant_meta.to_dict()
        else:
            variant_meta = self.variant_meta

        config_entry: dict[str, Any] | None | Unset
        if isinstance(self.config_entry, Unset):
            config_entry = UNSET
        elif isinstance(self.config_entry, ExperimentConfigEntry):
            config_entry = self.config_entry.to_dict()
        else:
            config_entry = self.config_entry

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if variant_meta is not UNSET:
            field_dict["variantMeta"] = variant_meta
        if config_entry is not UNSET:
            field_dict["configEntry"] = config_entry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.experiment_config_entry import ExperimentConfigEntry
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

        def _parse_config_entry(data: object) -> ExperimentConfigEntry | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_entry_type_1 = ExperimentConfigEntry.from_dict(data)

                return config_entry_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExperimentConfigEntry | None | Unset, data)

        config_entry = _parse_config_entry(d.pop("configEntry", UNSET))

        single_config_experiment_variant = cls(
            variant_meta=variant_meta,
            config_entry=config_entry,
        )

        return single_config_experiment_variant
