from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conditional_rules_payload_rules_type_0 import ConditionalRulesPayloadRulesType0


T = TypeVar("T", bound="ConditionalRulesPayload")


@_attrs_define
class ConditionalRulesPayload:
    """Public JSON shape for conditional rules (`rules` + `rulesOrder`), aligned with CMS `ConditionalRules`.

    Attributes:
        rules (ConditionalRulesPayloadRulesType0 | None | Unset): RPN rules keyed by condition id. On `draft:overwrite`,
            omitting a rule id that exists on published removes that rule; JSON `null` tombstones;
            `{ "tokens": [] }` is an explicit empty rule.
        rules_order (list[str] | None | Unset): Evaluation order (condition ids).
    """

    rules: ConditionalRulesPayloadRulesType0 | None | Unset = UNSET
    rules_order: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.conditional_rules_payload_rules_type_0 import ConditionalRulesPayloadRulesType0

        rules: dict[str, Any] | None | Unset
        if isinstance(self.rules, Unset):
            rules = UNSET
        elif isinstance(self.rules, ConditionalRulesPayloadRulesType0):
            rules = self.rules.to_dict()
        else:
            rules = self.rules

        rules_order: list[str] | None | Unset
        if isinstance(self.rules_order, Unset):
            rules_order = UNSET
        elif isinstance(self.rules_order, list):
            rules_order = self.rules_order

        else:
            rules_order = self.rules_order

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if rules is not UNSET:
            field_dict["rules"] = rules
        if rules_order is not UNSET:
            field_dict["rulesOrder"] = rules_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conditional_rules_payload_rules_type_0 import ConditionalRulesPayloadRulesType0

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_rules(data: object) -> ConditionalRulesPayloadRulesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rules_type_0 = ConditionalRulesPayloadRulesType0.from_dict(data)

                return rules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConditionalRulesPayloadRulesType0 | None | Unset, data)

        rules = _parse_rules(d.pop("rules", UNSET))

        def _parse_rules_order(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rules_order_type_0 = cast(list[str], data)

                return rules_order_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        rules_order = _parse_rules_order(d.pop("rulesOrder", UNSET))

        conditional_rules_payload = cls(
            rules=rules,
            rules_order=rules_order,
        )

        return conditional_rules_payload
