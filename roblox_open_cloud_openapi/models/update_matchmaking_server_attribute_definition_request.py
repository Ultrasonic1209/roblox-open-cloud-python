from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matchmaking_server_attribute_default_value import MatchmakingServerAttributeDefaultValue


T = TypeVar("T", bound="UpdateMatchmakingServerAttributeDefinitionRequest")


@_attrs_define
class UpdateMatchmakingServerAttributeDefinitionRequest:
    """Request model to update an exising ServerAttributeDefinition.

    Attributes:
        attribute_id (None | str | Unset): Id of the attribute to update.
        default_value (MatchmakingServerAttributeDefaultValue | Unset): Describes how the server attribute value should
            be derived
    """

    attribute_id: None | str | Unset = UNSET
    default_value: MatchmakingServerAttributeDefaultValue | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        attribute_id: None | str | Unset
        if isinstance(self.attribute_id, Unset):
            attribute_id = UNSET
        else:
            attribute_id = self.attribute_id

        default_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_value, Unset):
            default_value = self.default_value.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if attribute_id is not UNSET:
            field_dict["attributeId"] = attribute_id
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matchmaking_server_attribute_default_value import MatchmakingServerAttributeDefaultValue

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_attribute_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        attribute_id = _parse_attribute_id(d.pop("attributeId", UNSET))

        _default_value = d.pop("defaultValue", UNSET)
        default_value: MatchmakingServerAttributeDefaultValue | Unset
        if isinstance(_default_value, Unset):
            default_value = UNSET
        else:
            default_value = MatchmakingServerAttributeDefaultValue.from_dict(_default_value)

        update_matchmaking_server_attribute_definition_request = cls(
            attribute_id=attribute_id,
            default_value=default_value,
        )

        return update_matchmaking_server_attribute_definition_request
