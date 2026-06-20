from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.literal_value_dto import LiteralValueDto


T = TypeVar("T", bound="RpnOperandDto")


@_attrs_define
class RpnOperandDto:
    """RPN operand: attribute reference or literal value (same concepts as the proto `RpnOperand` oneof).

    Attributes:
        attribute_reference (None | str | Unset):
        literal_value (LiteralValueDto | None | Unset): Literal constant for an RPN operand (proto `LiteralValue` oneof
            as independent fields for JSON).
    """

    attribute_reference: None | str | Unset = UNSET
    literal_value: LiteralValueDto | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.literal_value_dto import LiteralValueDto

        attribute_reference: None | str | Unset
        if isinstance(self.attribute_reference, Unset):
            attribute_reference = UNSET
        else:
            attribute_reference = self.attribute_reference

        literal_value: dict[str, Any] | None | Unset
        if isinstance(self.literal_value, Unset):
            literal_value = UNSET
        elif isinstance(self.literal_value, LiteralValueDto):
            literal_value = self.literal_value.to_dict()
        else:
            literal_value = self.literal_value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if attribute_reference is not UNSET:
            field_dict["attributeReference"] = attribute_reference
        if literal_value is not UNSET:
            field_dict["literalValue"] = literal_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.literal_value_dto import LiteralValueDto

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_attribute_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        attribute_reference = _parse_attribute_reference(d.pop("attributeReference", UNSET))

        def _parse_literal_value(data: object) -> LiteralValueDto | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                literal_value_type_1 = LiteralValueDto.from_dict(data)

                return literal_value_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteralValueDto | None | Unset, data)

        literal_value = _parse_literal_value(d.pop("literalValue", UNSET))

        rpn_operand_dto = cls(
            attribute_reference=attribute_reference,
            literal_value=literal_value,
        )

        return rpn_operand_dto
