from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rpn_token_dto import RpnTokenDto


T = TypeVar("T", bound="ConditionalRuleDefinition")


@_attrs_define
class ConditionalRuleDefinition:
    """JSON shape of an RPN conditional rule in public API requests, aligned with
    `roblox.creatorexperienceconfig.conditionrules.v1.RpnRule`.

        Attributes:
            tokens (list[RpnTokenDto] | None | Unset): Postfix RPN token sequence.
    """

    tokens: list[RpnTokenDto] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tokens: list[dict[str, Any]] | None | Unset
        if isinstance(self.tokens, Unset):
            tokens = UNSET
        elif isinstance(self.tokens, list):
            tokens = []
            for tokens_type_0_item_data in self.tokens:
                tokens_type_0_item = tokens_type_0_item_data.to_dict()
                tokens.append(tokens_type_0_item)

        else:
            tokens = self.tokens

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if tokens is not UNSET:
            field_dict["tokens"] = tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rpn_token_dto import RpnTokenDto

        d = dict(src_dict)

        def _parse_tokens(data: object) -> list[RpnTokenDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tokens_type_0 = []
                _tokens_type_0 = data
                for tokens_type_0_item_data in _tokens_type_0:
                    tokens_type_0_item = RpnTokenDto.from_dict(tokens_type_0_item_data)

                    tokens_type_0.append(tokens_type_0_item)

                return tokens_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RpnTokenDto] | None | Unset, data)

        tokens = _parse_tokens(d.pop("tokens", UNSET))

        conditional_rule_definition = cls(
            tokens=tokens,
        )

        return conditional_rule_definition
