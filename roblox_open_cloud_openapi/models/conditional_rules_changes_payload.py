from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conditional_rules_changes_payload_rules_type_0 import ConditionalRulesChangesPayloadRulesType0
    from ..models.rules_order_delta_payload import RulesOrderDeltaPayload


T = TypeVar("T", bound="ConditionalRulesChangesPayload")


@_attrs_define
class ConditionalRulesChangesPayload:
    """Minimal delta for conditional rules on a revision (optional extension on list revisions).

    Attributes:
        rules_order (None | RulesOrderDeltaPayload | Unset):
        rules (ConditionalRulesChangesPayloadRulesType0 | None | Unset):
    """

    rules_order: None | RulesOrderDeltaPayload | Unset = UNSET
    rules: ConditionalRulesChangesPayloadRulesType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.conditional_rules_changes_payload_rules_type_0 import ConditionalRulesChangesPayloadRulesType0
        from ..models.rules_order_delta_payload import RulesOrderDeltaPayload

        rules_order: dict[str, Any] | None | Unset
        if isinstance(self.rules_order, Unset):
            rules_order = UNSET
        elif isinstance(self.rules_order, RulesOrderDeltaPayload):
            rules_order = self.rules_order.to_dict()
        else:
            rules_order = self.rules_order

        rules: dict[str, Any] | None | Unset
        if isinstance(self.rules, Unset):
            rules = UNSET
        elif isinstance(self.rules, ConditionalRulesChangesPayloadRulesType0):
            rules = self.rules.to_dict()
        else:
            rules = self.rules

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if rules_order is not UNSET:
            field_dict["rulesOrder"] = rules_order
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conditional_rules_changes_payload_rules_type_0 import ConditionalRulesChangesPayloadRulesType0
        from ..models.rules_order_delta_payload import RulesOrderDeltaPayload

        d = dict(src_dict)

        def _parse_rules_order(data: object) -> None | RulesOrderDeltaPayload | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rules_order_type_1 = RulesOrderDeltaPayload.from_dict(data)

                return rules_order_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RulesOrderDeltaPayload | Unset, data)

        rules_order = _parse_rules_order(d.pop("rulesOrder", UNSET))

        def _parse_rules(data: object) -> ConditionalRulesChangesPayloadRulesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rules_type_0 = ConditionalRulesChangesPayloadRulesType0.from_dict(data)

                return rules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConditionalRulesChangesPayloadRulesType0 | None | Unset, data)

        rules = _parse_rules(d.pop("rules", UNSET))

        conditional_rules_changes_payload = cls(
            rules_order=rules_order,
            rules=rules,
        )

        return conditional_rules_changes_payload
