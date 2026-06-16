from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserGameVoteResponse")


@_attrs_define
class UserGameVoteResponse:
    """
    Attributes:
        can_vote (bool | Unset):
        user_vote (bool | None | Unset):
        reason_for_not_voteable (None | str | Unset):
    """

    can_vote: bool | Unset = UNSET
    user_vote: bool | None | Unset = UNSET
    reason_for_not_voteable: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        can_vote = self.can_vote

        user_vote: bool | None | Unset
        if isinstance(self.user_vote, Unset):
            user_vote = UNSET
        else:
            user_vote = self.user_vote

        reason_for_not_voteable: None | str | Unset
        if isinstance(self.reason_for_not_voteable, Unset):
            reason_for_not_voteable = UNSET
        else:
            reason_for_not_voteable = self.reason_for_not_voteable

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if can_vote is not UNSET:
            field_dict["canVote"] = can_vote
        if user_vote is not UNSET:
            field_dict["userVote"] = user_vote
        if reason_for_not_voteable is not UNSET:
            field_dict["reasonForNotVoteable"] = reason_for_not_voteable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_vote = d.pop("canVote", UNSET)

        def _parse_user_vote(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        user_vote = _parse_user_vote(d.pop("userVote", UNSET))

        def _parse_reason_for_not_voteable(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason_for_not_voteable = _parse_reason_for_not_voteable(d.pop("reasonForNotVoteable", UNSET))

        user_game_vote_response = cls(
            can_vote=can_vote,
            user_vote=user_vote,
            reason_for_not_voteable=reason_for_not_voteable,
        )

        return user_game_vote_response
