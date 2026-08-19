from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExperimentConfigEntry")


@_attrs_define
class ExperimentConfigEntry:
    """
    Attributes:
        key (None | str | Unset): The config key this variant overrides. Must match across variants in the same
            experiment.
        entry_value (Any | Unset): The value assigned to Key for this variant. Can be a string, number, bool, array,
            object,
            or null.
        description (None | str | Unset): Optional human-readable description carried alongside the value.
    """

    key: None | str | Unset = UNSET
    entry_value: Any | Unset = UNSET
    description: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        entry_value = self.entry_value

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if entry_value is not UNSET:
            field_dict["entryValue"] = entry_value
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))

        entry_value = d.pop("entryValue", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        experiment_config_entry = cls(
            key=key,
            entry_value=entry_value,
            description=description,
        )

        return experiment_config_entry
