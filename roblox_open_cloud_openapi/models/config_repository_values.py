from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conditional_rules_payload import ConditionalRulesPayload
    from ..models.config_repository_metadata import ConfigRepositoryMetadata
    from ..models.config_repository_values_entries_type_0 import ConfigRepositoryValuesEntriesType0


T = TypeVar("T", bound="ConfigRepositoryValues")


@_attrs_define
class ConfigRepositoryValues:
    """A representation of a configuration repository with just the values (no metadata or decorators).
    This response can be used as a direct copy-and-paste to the draft update endpoints.

        Attributes:
            metadata (ConfigRepositoryMetadata | None | Unset): Metadata about the configuration repository.
            entries (ConfigRepositoryValuesEntriesType0 | None | Unset): The configuration entries (key-value pairs) in the
                repository.
            conditional_rules (ConditionalRulesPayload | None | Unset): Conditional RPN rules and evaluation order, when any
                exist.
    """

    metadata: ConfigRepositoryMetadata | None | Unset = UNSET
    entries: ConfigRepositoryValuesEntriesType0 | None | Unset = UNSET
    conditional_rules: ConditionalRulesPayload | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.conditional_rules_payload import ConditionalRulesPayload
        from ..models.config_repository_metadata import ConfigRepositoryMetadata
        from ..models.config_repository_values_entries_type_0 import ConfigRepositoryValuesEntriesType0

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, ConfigRepositoryMetadata):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        entries: dict[str, Any] | None | Unset
        if isinstance(self.entries, Unset):
            entries = UNSET
        elif isinstance(self.entries, ConfigRepositoryValuesEntriesType0):
            entries = self.entries.to_dict()
        else:
            entries = self.entries

        conditional_rules: dict[str, Any] | None | Unset
        if isinstance(self.conditional_rules, Unset):
            conditional_rules = UNSET
        elif isinstance(self.conditional_rules, ConditionalRulesPayload):
            conditional_rules = self.conditional_rules.to_dict()
        else:
            conditional_rules = self.conditional_rules

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if entries is not UNSET:
            field_dict["entries"] = entries
        if conditional_rules is not UNSET:
            field_dict["conditionalRules"] = conditional_rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conditional_rules_payload import ConditionalRulesPayload
        from ..models.config_repository_metadata import ConfigRepositoryMetadata
        from ..models.config_repository_values_entries_type_0 import ConfigRepositoryValuesEntriesType0

        d = dict(src_dict)

        def _parse_metadata(data: object) -> ConfigRepositoryMetadata | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_1 = ConfigRepositoryMetadata.from_dict(data)

                return metadata_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConfigRepositoryMetadata | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_entries(data: object) -> ConfigRepositoryValuesEntriesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entries_type_0 = ConfigRepositoryValuesEntriesType0.from_dict(data)

                return entries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConfigRepositoryValuesEntriesType0 | None | Unset, data)

        entries = _parse_entries(d.pop("entries", UNSET))

        def _parse_conditional_rules(data: object) -> ConditionalRulesPayload | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                conditional_rules_type_1 = ConditionalRulesPayload.from_dict(data)

                return conditional_rules_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConditionalRulesPayload | None | Unset, data)

        conditional_rules = _parse_conditional_rules(d.pop("conditionalRules", UNSET))

        config_repository_values = cls(
            metadata=metadata,
            entries=entries,
            conditional_rules=conditional_rules,
        )

        return config_repository_values
