from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matchmaking_attribute_value import MatchmakingAttributeValue
    from ..models.matchmaking_attribute_value_location import MatchmakingAttributeValueLocation


T = TypeVar("T", bound="UpdateMatchmakingPlayerAttributeDefinitionRequest")


@_attrs_define
class UpdateMatchmakingPlayerAttributeDefinitionRequest:
    """Request model for updating a PlayerAttributeDefinition.

    Attributes:
        attribute_id (None | str | Unset): Id of the attribute to update.
        default_value (MatchmakingAttributeValue | Unset): Matchmaking attribute value object for matchmaking rules.
        attribute_value_location (MatchmakingAttributeValueLocation | Unset): Describes where an attribute value exists.
    """

    attribute_id: None | str | Unset = UNSET
    default_value: MatchmakingAttributeValue | Unset = UNSET
    attribute_value_location: MatchmakingAttributeValueLocation | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        attribute_id: None | str | Unset
        if isinstance(self.attribute_id, Unset):
            attribute_id = UNSET
        else:
            attribute_id = self.attribute_id

        default_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_value, Unset):
            default_value = self.default_value.to_dict()

        attribute_value_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attribute_value_location, Unset):
            attribute_value_location = self.attribute_value_location.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if attribute_id is not UNSET:
            field_dict["attributeId"] = attribute_id
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if attribute_value_location is not UNSET:
            field_dict["attributeValueLocation"] = attribute_value_location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matchmaking_attribute_value import MatchmakingAttributeValue
        from ..models.matchmaking_attribute_value_location import MatchmakingAttributeValueLocation

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_attribute_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        attribute_id = _parse_attribute_id(d.pop("attributeId", UNSET))

        _default_value = d.pop("defaultValue", UNSET)
        default_value: MatchmakingAttributeValue | Unset
        if isinstance(_default_value, Unset):
            default_value = UNSET
        else:
            default_value = MatchmakingAttributeValue.from_dict(_default_value)

        _attribute_value_location = d.pop("attributeValueLocation", UNSET)
        attribute_value_location: MatchmakingAttributeValueLocation | Unset
        if isinstance(_attribute_value_location, Unset):
            attribute_value_location = UNSET
        else:
            attribute_value_location = MatchmakingAttributeValueLocation.from_dict(_attribute_value_location)

        update_matchmaking_player_attribute_definition_request = cls(
            attribute_id=attribute_id,
            default_value=default_value,
            attribute_value_location=attribute_value_location,
        )

        return update_matchmaking_player_attribute_definition_request
