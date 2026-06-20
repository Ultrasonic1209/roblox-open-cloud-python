from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.matchmaking_attribute_data_type import MatchmakingAttributeDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matchmaking_server_attribute_default_value import MatchmakingServerAttributeDefaultValue


T = TypeVar("T", bound="CreateMatchmakingServerAttributeDefinitionRequest")


@_attrs_define
class CreateMatchmakingServerAttributeDefinitionRequest:
    """Request to create a new ServerAttributeDefinition.

    Attributes:
        universe_id (int | Unset): UniverseId for the new PlayerAttributeDefinition.
        name (None | str | Unset): Name of the new rule.
        data_type (MatchmakingAttributeDataType | Unset): Data type of a matchmaking attribute. Can be a bool, number,
            or string.
        default_value (MatchmakingServerAttributeDefaultValue | Unset): Describes how the server attribute value should
            be derived
    """

    universe_id: int | Unset = UNSET
    name: None | str | Unset = UNSET
    data_type: MatchmakingAttributeDataType | Unset = UNSET
    default_value: MatchmakingServerAttributeDefaultValue | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        universe_id = self.universe_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        data_type: str | Unset = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.value

        default_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_value, Unset):
            default_value = self.default_value.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if name is not UNSET:
            field_dict["name"] = name
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matchmaking_server_attribute_default_value import MatchmakingServerAttributeDefaultValue

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        universe_id = d.pop("universeId", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _data_type = d.pop("dataType", UNSET)
        data_type: MatchmakingAttributeDataType | Unset
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = MatchmakingAttributeDataType(_data_type)

        _default_value = d.pop("defaultValue", UNSET)
        default_value: MatchmakingServerAttributeDefaultValue | Unset
        if isinstance(_default_value, Unset):
            default_value = UNSET
        else:
            default_value = MatchmakingServerAttributeDefaultValue.from_dict(_default_value)

        create_matchmaking_server_attribute_definition_request = cls(
            universe_id=universe_id,
            name=name,
            data_type=data_type,
            default_value=default_value,
        )

        return create_matchmaking_server_attribute_definition_request
