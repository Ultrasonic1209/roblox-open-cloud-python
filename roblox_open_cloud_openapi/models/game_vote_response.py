from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GameVoteResponse")


@_attrs_define
class GameVoteResponse:
    """
    Attributes:
        id (int | Unset):
        up_votes (int | Unset):
        down_votes (int | Unset):
    """

    id: int | Unset = UNSET
    up_votes: int | Unset = UNSET
    down_votes: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        up_votes = self.up_votes

        down_votes = self.down_votes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if up_votes is not UNSET:
            field_dict["upVotes"] = up_votes
        if down_votes is not UNSET:
            field_dict["downVotes"] = down_votes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        up_votes = d.pop("upVotes", UNSET)

        down_votes = d.pop("downVotes", UNSET)

        game_vote_response = cls(
            id=id,
            up_votes=up_votes,
            down_votes=down_votes,
        )

        return game_vote_response
