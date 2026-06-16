from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.matchmaking_attribute_data_type import MatchmakingAttributeDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matchmaking_server_attribute_default_value import MatchmakingServerAttributeDefaultValue


T = TypeVar("T", bound="MatchmakingServerAttributeDefinition")


@_attrs_define
class MatchmakingServerAttributeDefinition:
    """Describes a player attribute definition for matchmaking.

    Attributes:
        id (None | str | Unset): The id of the attribute.
        universe_id (int | Unset): The universe id of the attribute.
        name (None | str | Unset): The name of the attribute.
        data_type (MatchmakingAttributeDataType | Unset): Data type of a matchmaking attribute. Can be a bool, number,
            or string.
        default_value (MatchmakingServerAttributeDefaultValue | Unset): Describes how the server attribute value should
            be derived
        created_time (datetime.datetime | Unset): The aggregation function of the attribute.
        updated_time (datetime.datetime | Unset): The time the attribute was last updated.
    """

    id: None | str | Unset = UNSET
    universe_id: int | Unset = UNSET
    name: None | str | Unset = UNSET
    data_type: MatchmakingAttributeDataType | Unset = UNSET
    default_value: MatchmakingServerAttributeDefaultValue | Unset = UNSET
    created_time: datetime.datetime | Unset = UNSET
    updated_time: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

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

        created_time: str | Unset = UNSET
        if not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        updated_time: str | Unset = UNSET
        if not isinstance(self.updated_time, Unset):
            updated_time = self.updated_time.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if name is not UNSET:
            field_dict["name"] = name
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if updated_time is not UNSET:
            field_dict["updatedTime"] = updated_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matchmaking_server_attribute_default_value import MatchmakingServerAttributeDefaultValue

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

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

        _created_time = d.pop("createdTime", UNSET)
        created_time: datetime.datetime | Unset
        if isinstance(_created_time, Unset):
            created_time = UNSET
        else:
            created_time = datetime.datetime.fromisoformat(_created_time)

        _updated_time = d.pop("updatedTime", UNSET)
        updated_time: datetime.datetime | Unset
        if isinstance(_updated_time, Unset):
            updated_time = UNSET
        else:
            updated_time = datetime.datetime.fromisoformat(_updated_time)

        matchmaking_server_attribute_definition = cls(
            id=id,
            universe_id=universe_id,
            name=name,
            data_type=data_type,
            default_value=default_value,
            created_time=created_time,
            updated_time=updated_time,
        )

        return matchmaking_server_attribute_definition
