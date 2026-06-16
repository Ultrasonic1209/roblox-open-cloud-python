from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conditional_rules_payload import ConditionalRulesPayload
    from ..models.update_draft_request_entries_type_0 import UpdateDraftRequestEntriesType0


T = TypeVar("T", bound="UpdateDraftRequest")


@_attrs_define
class UpdateDraftRequest:
    """Request model for draft updates: PATCH uses a partial merge; PUT `draft:overwrite` treats the body as the full
    intended configuration after publish.

        Attributes:
            draft_hash (None | str | Unset): The previous draft hash for concurrency control. If provided, the update will
                fail if it doesn't match.
            entries (None | Unset | UpdateDraftRequestEntriesType0): On PATCH, keys not included are unchanged; set a key to
                null to delete a branch or entry per merge rules.
                On PUT `draft:overwrite`, this map is the authoritative final entry set: any key present on the latest published
                configuration but omitted here is removed, and any conditional branch omitted for a key that remains is removed.
            conditional_rules (ConditionalRulesPayload | None | Unset): Optional conditional rules. On PATCH, merges with
                the current draft rules when this payload is non-empty (any rule id or `rulesOrder` entry).
                Omit the property or send an empty object `{}` to leave rules unchanged (draft rules, or latest published rules
                if the draft has none yet).
                On PUT `draft:overwrite`, when this property is present,
                CreatorConfigsPublicApi.Models.ConditionalRulesPayload.Rules is the full intended rule set after publish: rules
                that exist on the latest published configuration but are omitted are removed.
                When omitted on overwrite, all published conditional rules are cleared (entries must not reference conditionals
                unless you provide this object).
    """

    draft_hash: None | str | Unset = UNSET
    entries: None | Unset | UpdateDraftRequestEntriesType0 = UNSET
    conditional_rules: ConditionalRulesPayload | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.conditional_rules_payload import ConditionalRulesPayload
        from ..models.update_draft_request_entries_type_0 import UpdateDraftRequestEntriesType0

        draft_hash: None | str | Unset
        if isinstance(self.draft_hash, Unset):
            draft_hash = UNSET
        else:
            draft_hash = self.draft_hash

        entries: dict[str, Any] | None | Unset
        if isinstance(self.entries, Unset):
            entries = UNSET
        elif isinstance(self.entries, UpdateDraftRequestEntriesType0):
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
        from ..models.update_draft_request_entries_type_0 import UpdateDraftRequestEntriesType0

        d = dict(src_dict)

        def _parse_draft_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        draft_hash = _parse_draft_hash(d.pop("draftHash", UNSET))

        def _parse_entries(data: object) -> None | Unset | UpdateDraftRequestEntriesType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entries_type_0 = UpdateDraftRequestEntriesType0.from_dict(data)

                return entries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateDraftRequestEntriesType0, data)

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

        update_draft_request = cls(
            draft_hash=draft_hash,
            entries=entries,
            conditional_rules=conditional_rules,
        )

        return update_draft_request
