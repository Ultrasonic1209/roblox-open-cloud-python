from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VotingModelType0")


@_attrs_define
class VotingModelType0:
    """model for voting.

    Attributes:
        show_votes (bool | Unset): Gets or sets show votes.
        up_votes (int | Unset): Gets or sets success.
        down_votes (int | Unset): Gets or sets down votes.
        can_vote (bool | Unset): Gets or sets can vote.
        user_vote (bool | None | Unset): Gets or sets user vote.
        has_voted (bool | Unset): Gets UserVote.
        vote_count (int | Unset): The total number of votes
        up_vote_percent (int | Unset): The percentage of total votes that have been UpVotes
    """

    show_votes: bool | Unset = UNSET
    up_votes: int | Unset = UNSET
    down_votes: int | Unset = UNSET
    can_vote: bool | Unset = UNSET
    user_vote: bool | None | Unset = UNSET
    has_voted: bool | Unset = UNSET
    vote_count: int | Unset = UNSET
    up_vote_percent: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        show_votes = self.show_votes

        up_votes = self.up_votes

        down_votes = self.down_votes

        can_vote = self.can_vote

        user_vote: bool | None | Unset
        if isinstance(self.user_vote, Unset):
            user_vote = UNSET
        else:
            user_vote = self.user_vote

        has_voted = self.has_voted

        vote_count = self.vote_count

        up_vote_percent = self.up_vote_percent

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if show_votes is not UNSET:
            field_dict["showVotes"] = show_votes
        if up_votes is not UNSET:
            field_dict["upVotes"] = up_votes
        if down_votes is not UNSET:
            field_dict["downVotes"] = down_votes
        if can_vote is not UNSET:
            field_dict["canVote"] = can_vote
        if user_vote is not UNSET:
            field_dict["userVote"] = user_vote
        if has_voted is not UNSET:
            field_dict["hasVoted"] = has_voted
        if vote_count is not UNSET:
            field_dict["voteCount"] = vote_count
        if up_vote_percent is not UNSET:
            field_dict["upVotePercent"] = up_vote_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        show_votes = d.pop("showVotes", UNSET)

        up_votes = d.pop("upVotes", UNSET)

        down_votes = d.pop("downVotes", UNSET)

        can_vote = d.pop("canVote", UNSET)

        def _parse_user_vote(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        user_vote = _parse_user_vote(d.pop("userVote", UNSET))

        has_voted = d.pop("hasVoted", UNSET)

        vote_count = d.pop("voteCount", UNSET)

        up_vote_percent = d.pop("upVotePercent", UNSET)

        voting_model_type_0 = cls(
            show_votes=show_votes,
            up_votes=up_votes,
            down_votes=down_votes,
            can_vote=can_vote,
            user_vote=user_vote,
            has_voted=has_voted,
            vote_count=vote_count,
            up_vote_percent=up_vote_percent,
        )

        return voting_model_type_0
