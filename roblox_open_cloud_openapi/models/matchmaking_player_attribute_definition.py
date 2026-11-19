from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.matchmaking_attribute_data_type import MatchmakingAttributeDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matchmaking_attribute_value import MatchmakingAttributeValue
    from ..models.matchmaking_attribute_value_location import MatchmakingAttributeValueLocation


T = TypeVar("T", bound="MatchmakingPlayerAttributeDefinition")


@_attrs_define
class MatchmakingPlayerAttributeDefinition:
    """Describes a player attribute definition for matchmaking.

    Attributes:
        id (None | str): The id of the attribute.
        name (None | str): The name of the attribute.
        attribute_value_location (MatchmakingAttributeValueLocation): Describes where an attribute value exists.
        universe_id (int | Unset): The universe id of the attribute.
        data_type (MatchmakingAttributeDataType | Unset): Data type of a matchmaking attribute. Can be a bool, number,
            or string.
        default_value (MatchmakingAttributeValue | Unset): Matchmaking attribute value object for matchmaking rules.
        created_time (datetime.datetime | Unset): The aggregation function of the attribute.
        updated_time (datetime.datetime | Unset): The time the attribute was last updated.
    """

    id: None | str
    name: None | str
    attribute_value_location: MatchmakingAttributeValueLocation
    universe_id: int | Unset = UNSET
    data_type: MatchmakingAttributeDataType | Unset = UNSET
    default_value: MatchmakingAttributeValue | Unset = UNSET
    created_time: datetime.datetime | Unset = UNSET
    updated_time: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str
        id = self.id

        name: None | str
        name = self.name

        attribute_value_location = self.attribute_value_location.to_dict()

        universe_id = self.universe_id

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

        field_dict.update(
            {
                "id": id,
                "name": name,
                "attributeValueLocation": attribute_value_location,
            }
        )
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
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
        from ..models.matchmaking_attribute_value import MatchmakingAttributeValue  # noqa: PLC0415
        from ..models.matchmaking_attribute_value_location import MatchmakingAttributeValueLocation  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        id = _parse_id(d.pop("id"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        attribute_value_location = MatchmakingAttributeValueLocation.from_dict(d.pop("attributeValueLocation"))

        universe_id = d.pop("universeId", UNSET)

        _data_type = d.pop("dataType", UNSET)
        data_type: MatchmakingAttributeDataType | Unset
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = MatchmakingAttributeDataType(_data_type)

        _default_value = d.pop("defaultValue", UNSET)
        default_value: MatchmakingAttributeValue | Unset
        if isinstance(_default_value, Unset):
            default_value = UNSET
        else:
            default_value = MatchmakingAttributeValue.from_dict(_default_value)

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

        matchmaking_player_attribute_definition = cls(
            id=id,
            name=name,
            attribute_value_location=attribute_value_location,
            universe_id=universe_id,
            data_type=data_type,
            default_value=default_value,
            created_time=created_time,
            updated_time=updated_time,
        )

        return matchmaking_player_attribute_definition
