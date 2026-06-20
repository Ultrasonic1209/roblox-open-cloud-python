from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserGameVoteRequest")


@_attrs_define
class UserGameVoteRequest:
    """
    Attributes:
        vote (bool | None | Unset):
    """

    vote: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        vote: bool | None | Unset
        if isinstance(self.vote, Unset):
            vote = UNSET
        else:
            vote = self.vote

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if vote is not UNSET:
            field_dict["vote"] = vote

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_vote(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        vote = _parse_vote(d.pop("vote", UNSET))

        user_game_vote_request = cls(
            vote=vote,
        )

        return user_game_vote_request
