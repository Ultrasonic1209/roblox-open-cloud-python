from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.game_vote_response import GameVoteResponse


T = TypeVar("T", bound="GameVoteResponseApiArrayResponse")


@_attrs_define
class GameVoteResponseApiArrayResponse:
    """
    Attributes:
        data (list[GameVoteResponse] | None | Unset):
    """

    data: list[GameVoteResponse] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, list):
            data = []
            for data_type_0_item_data in self.data:
                data_type_0_item = data_type_0_item_data.to_dict()
                data.append(data_type_0_item)

        else:
            data = self.data

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.game_vote_response import GameVoteResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_data(data: object) -> list[GameVoteResponse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = []
                _data_type_0 = data
                for data_type_0_item_data in _data_type_0:
                    data_type_0_item = GameVoteResponse.from_dict(data_type_0_item_data)

                    data_type_0.append(data_type_0_item)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GameVoteResponse] | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        game_vote_response_api_array_response = cls(
            data=data,
        )

        return game_vote_response_api_array_response
