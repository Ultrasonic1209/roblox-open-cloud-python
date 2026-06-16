from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.matchmaking_signal_curve_type import MatchmakingSignalCurveType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matchmaking_attribute_reference import MatchmakingAttributeReference


T = TypeVar("T", bound="PlayerCategoricalSignalConfiguration")


@_attrs_define
class PlayerCategoricalSignalConfiguration:
    """The player categorical signal configuration.

    Attributes:
        player_attribute (MatchmakingAttributeReference | Unset): Matchmaking attribute reference object for matchmaking
            rules.
        curve_type (MatchmakingSignalCurveType | Unset): The signal curve type for matchmaking.
    """

    player_attribute: MatchmakingAttributeReference | Unset = UNSET
    curve_type: MatchmakingSignalCurveType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        player_attribute: dict[str, Any] | Unset = UNSET
        if not isinstance(self.player_attribute, Unset):
            player_attribute = self.player_attribute.to_dict()

        curve_type: str | Unset = UNSET
        if not isinstance(self.curve_type, Unset):
            curve_type = self.curve_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if player_attribute is not UNSET:
            field_dict["playerAttribute"] = player_attribute
        if curve_type is not UNSET:
            field_dict["curveType"] = curve_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matchmaking_attribute_reference import MatchmakingAttributeReference

        d = dict(src_dict)
        _player_attribute = d.pop("playerAttribute", UNSET)
        player_attribute: MatchmakingAttributeReference | Unset
        if isinstance(_player_attribute, Unset):
            player_attribute = UNSET
        else:
            player_attribute = MatchmakingAttributeReference.from_dict(_player_attribute)

        _curve_type = d.pop("curveType", UNSET)
        curve_type: MatchmakingSignalCurveType | Unset
        if isinstance(_curve_type, Unset):
            curve_type = UNSET
        else:
            curve_type = MatchmakingSignalCurveType(_curve_type)

        player_categorical_signal_configuration = cls(
            player_attribute=player_attribute,
            curve_type=curve_type,
        )

        return player_categorical_signal_configuration
