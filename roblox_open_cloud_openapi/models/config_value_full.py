from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_variant_dto import ConfigVariantDto


T = TypeVar("T", bound="ConfigValueFull")


@_attrs_define
class ConfigValueFull:
    """A full representation of a configuration value, including its metadata.

    Attributes:
        variants (list[ConfigVariantDto] | None | Unset): Non-default branches (e.g. conditional), when present.
        value (Any | Unset): The value of the configuration entry.
        description (None | str | Unset): A description of the configuration entry.
        last_modified_time (datetime.datetime | Unset): The time when the configuration entry was last modified.
        last_accessed_time (datetime.datetime | Unset): The time when the configuration entry was last accessed.
    """

    variants: list[ConfigVariantDto] | None | Unset = UNSET
    value: Any | Unset = UNSET
    description: None | str | Unset = UNSET
    last_modified_time: datetime.datetime | Unset = UNSET
    last_accessed_time: datetime.datetime | Unset = UNSET

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

        value = self.value

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        last_modified_time: str | Unset = UNSET
        if not isinstance(self.last_modified_time, Unset):
            last_modified_time = self.last_modified_time.isoformat()

        last_accessed_time: str | Unset = UNSET
        if not isinstance(self.last_accessed_time, Unset):
            last_accessed_time = self.last_accessed_time.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if variants is not UNSET:
            field_dict["variants"] = variants
        if value is not UNSET:
            field_dict["value"] = value
        if description is not UNSET:
            field_dict["description"] = description
        if last_modified_time is not UNSET:
            field_dict["lastModifiedTime"] = last_modified_time
        if last_accessed_time is not UNSET:
            field_dict["lastAccessedTime"] = last_accessed_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_variant_dto import ConfigVariantDto

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_variants(data: object) -> list[ConfigVariantDto] | None | Unset:
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
                    variants_type_0_item = ConfigVariantDto.from_dict(variants_type_0_item_data)

                    variants_type_0.append(variants_type_0_item)

                return variants_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ConfigVariantDto] | None | Unset, data)

        variants = _parse_variants(d.pop("variants", UNSET))

        value = d.pop("value", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _last_modified_time = d.pop("lastModifiedTime", UNSET)
        last_modified_time: datetime.datetime | Unset
        if isinstance(_last_modified_time, Unset):
            last_modified_time = UNSET
        else:
            last_modified_time = datetime.datetime.fromisoformat(_last_modified_time)

        _last_accessed_time = d.pop("lastAccessedTime", UNSET)
        last_accessed_time: datetime.datetime | Unset
        if isinstance(_last_accessed_time, Unset):
            last_accessed_time = UNSET
        else:
            last_accessed_time = datetime.datetime.fromisoformat(_last_accessed_time)

        config_value_full = cls(
            variants=variants,
            value=value,
            description=description,
            last_modified_time=last_modified_time,
            last_accessed_time=last_accessed_time,
        )

        return config_value_full
