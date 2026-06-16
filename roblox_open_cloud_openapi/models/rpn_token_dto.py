from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rpn_operand_dto import RpnOperandDto


T = TypeVar("T", bound="RpnTokenDto")


@_attrs_define
class RpnTokenDto:
    """One RPN token: either a logical/comparison CreatorConfigsPublicApi.Models.ConditionalRuleOperator (proto JSON
    `OPERATOR_*`) or an operand object.

        Attributes:
            operator (None | str | Unset):
            operand (None | RpnOperandDto | Unset): RPN operand: attribute reference or literal value (same concepts as the
                proto `RpnOperand` oneof).
    """

    operator: None | str | Unset = UNSET
    operand: None | RpnOperandDto | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.rpn_operand_dto import RpnOperandDto

        operator: None | str | Unset
        if isinstance(self.operator, Unset):
            operator = UNSET
        else:
            operator = self.operator

        operand: dict[str, Any] | None | Unset
        if isinstance(self.operand, Unset):
            operand = UNSET
        elif isinstance(self.operand, RpnOperandDto):
            operand = self.operand.to_dict()
        else:
            operand = self.operand

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if operator is not UNSET:
            field_dict["operator"] = operator
        if operand is not UNSET:
            field_dict["operand"] = operand

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rpn_operand_dto import RpnOperandDto

        d = dict(src_dict)

        def _parse_operator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operator = _parse_operator(d.pop("operator", UNSET))

        def _parse_operand(data: object) -> None | RpnOperandDto | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                operand_type_1 = RpnOperandDto.from_dict(data)

                return operand_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RpnOperandDto | Unset, data)

        operand = _parse_operand(d.pop("operand", UNSET))

        rpn_token_dto = cls(
            operator=operator,
            operand=operand,
        )

        return rpn_token_dto
