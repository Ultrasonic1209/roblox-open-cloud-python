from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conditional_rules_payload import ConditionalRulesPayload
    from ..models.config_repository_full_entries_type_0 import ConfigRepositoryFullEntriesType0
    from ..models.config_repository_metadata import ConfigRepositoryMetadata


T = TypeVar("T", bound="ConfigRepositoryFull")


@_attrs_define
class ConfigRepositoryFull:
    """A full representation of a configuration repository, including all entries and their metadata.

    Attributes:
        entries (ConfigRepositoryFullEntriesType0 | None | Unset): The configuration entries (key-value with metadata
            such as description, last modified/accessed times).
        metadata (ConfigRepositoryMetadata | None | Unset): Metadata about the configuration repository.
        conditional_rules (ConditionalRulesPayload | None | Unset): Conditional RPN rules and evaluation order, when any
            exist.
    """

    entries: ConfigRepositoryFullEntriesType0 | None | Unset = UNSET
    metadata: ConfigRepositoryMetadata | None | Unset = UNSET
    conditional_rules: ConditionalRulesPayload | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.conditional_rules_payload import ConditionalRulesPayload
        from ..models.config_repository_full_entries_type_0 import ConfigRepositoryFullEntriesType0
        from ..models.config_repository_metadata import ConfigRepositoryMetadata

        entries: dict[str, Any] | None | Unset
        if isinstance(self.entries, Unset):
            entries = UNSET
        elif isinstance(self.entries, ConfigRepositoryFullEntriesType0):
            entries = self.entries.to_dict()
        else:
            entries = self.entries

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, ConfigRepositoryMetadata):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        conditional_rules: dict[str, Any] | None | Unset
        if isinstance(self.conditional_rules, Unset):
            conditional_rules = UNSET
        elif isinstance(self.conditional_rules, ConditionalRulesPayload):
            conditional_rules = self.conditional_rules.to_dict()
        else:
            conditional_rules = self.conditional_rules

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if entries is not UNSET:
            field_dict["entries"] = entries
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if conditional_rules is not UNSET:
            field_dict["conditionalRules"] = conditional_rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conditional_rules_payload import ConditionalRulesPayload
        from ..models.config_repository_full_entries_type_0 import ConfigRepositoryFullEntriesType0
        from ..models.config_repository_metadata import ConfigRepositoryMetadata

        d = dict(src_dict)

        def _parse_entries(data: object) -> ConfigRepositoryFullEntriesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entries_type_0 = ConfigRepositoryFullEntriesType0.from_dict(data)

                return entries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConfigRepositoryFullEntriesType0 | None | Unset, data)

        entries = _parse_entries(d.pop("entries", UNSET))

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

        config_repository_full = cls(
            entries=entries,
            metadata=metadata,
            conditional_rules=conditional_rules,
        )

        return config_repository_full
