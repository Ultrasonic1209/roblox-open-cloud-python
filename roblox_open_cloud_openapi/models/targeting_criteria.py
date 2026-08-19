from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conditional_rule_definition import ConditionalRuleDefinition


T = TypeVar("T", bound="TargetingCriteria")


@_attrs_define
class TargetingCriteria:
    """Eligibility criteria scoping which users an experiment can apply to.

    Attributes:
        rule (ConditionalRuleDefinition | None | Unset): RPN rule that decides whether an evaluator (user, request,
            etc.) is eligible for the
            experiment. `null` means no targeting (every otherwise-eligible user is in scope).
    """

    rule: ConditionalRuleDefinition | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.conditional_rule_definition import ConditionalRuleDefinition

        rule: dict[str, Any] | None | Unset
        if isinstance(self.rule, Unset):
            rule = UNSET
        elif isinstance(self.rule, ConditionalRuleDefinition):
            rule = self.rule.to_dict()
        else:
            rule = self.rule

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if rule is not UNSET:
            field_dict["rule"] = rule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conditional_rule_definition import ConditionalRuleDefinition

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_rule(data: object) -> ConditionalRuleDefinition | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rule_type_1 = ConditionalRuleDefinition.from_dict(data)

                return rule_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConditionalRuleDefinition | None | Unset, data)

        rule = _parse_rule(d.pop("rule", UNSET))

        targeting_criteria = cls(
            rule=rule,
        )

        return targeting_criteria
