from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conditional_rules_payload import ConditionalRulesPayload
    from ..models.config_repository_draft_entries_type_0 import ConfigRepositoryDraftEntriesType0


T = TypeVar("T", bound="ConfigRepositoryDraft")


@_attrs_define
class ConfigRepositoryDraft:
    """A representation of the current draft changes for a configuration repository.

    Attributes:
        draft_hash (None | str | Unset): The hash of the draft for concurrency control.
        entries (ConfigRepositoryDraftEntriesType0 | None | Unset): The configuration entries in the draft (key to value
            and optional description).
        conditional_rules (ConditionalRulesPayload | None | Unset): Conditional rules staged on the draft, when any
            exist.
    """

    draft_hash: None | str | Unset = UNSET
    entries: ConfigRepositoryDraftEntriesType0 | None | Unset = UNSET
    conditional_rules: ConditionalRulesPayload | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.conditional_rules_payload import ConditionalRulesPayload
        from ..models.config_repository_draft_entries_type_0 import ConfigRepositoryDraftEntriesType0

        draft_hash: None | str | Unset
        if isinstance(self.draft_hash, Unset):
            draft_hash = UNSET
        else:
            draft_hash = self.draft_hash

        entries: dict[str, Any] | None | Unset
        if isinstance(self.entries, Unset):
            entries = UNSET
        elif isinstance(self.entries, ConfigRepositoryDraftEntriesType0):
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
        if draft_hash is not UNSET:
            field_dict["draftHash"] = draft_hash
        if entries is not UNSET:
            field_dict["entries"] = entries
        if conditional_rules is not UNSET:
            field_dict["conditionalRules"] = conditional_rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conditional_rules_payload import ConditionalRulesPayload
        from ..models.config_repository_draft_entries_type_0 import ConfigRepositoryDraftEntriesType0

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_draft_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        draft_hash = _parse_draft_hash(d.pop("draftHash", UNSET))

        def _parse_entries(data: object) -> ConfigRepositoryDraftEntriesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entries_type_0 = ConfigRepositoryDraftEntriesType0.from_dict(data)

                return entries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConfigRepositoryDraftEntriesType0 | None | Unset, data)

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

        config_repository_draft = cls(
            draft_hash=draft_hash,
            entries=entries,
            conditional_rules=conditional_rules,
        )

        return config_repository_draft
