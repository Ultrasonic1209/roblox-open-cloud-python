from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiDevelopModelsResponseAssetVotingModel")


@_attrs_define
class RobloxApiDevelopModelsResponseAssetVotingModel:
    """Asset voting information

    Attributes:
        asset_id (int | Unset): The !:IAsset's id.
        has_user_voted (bool | Unset): Whether the user has voted on this !:IAsset.
        can_user_vote (bool | Unset): Whether the user can vote on this !:IAsset.
        should_show_votes (bool | Unset): Whether votes should be shown.
        up_votes (int | Unset): The number of up votes.
        down_votes (int | Unset): The number of down votes.
        reason_for_not_able_to_vote (str | Unset): The reason this !:IAsset cannot be voted on.
    """

    asset_id: int | Unset = UNSET
    has_user_voted: bool | Unset = UNSET
    can_user_vote: bool | Unset = UNSET
    should_show_votes: bool | Unset = UNSET
    up_votes: int | Unset = UNSET
    down_votes: int | Unset = UNSET
    reason_for_not_able_to_vote: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        has_user_voted = self.has_user_voted

        can_user_vote = self.can_user_vote

        should_show_votes = self.should_show_votes

        up_votes = self.up_votes

        down_votes = self.down_votes

        reason_for_not_able_to_vote = self.reason_for_not_able_to_vote

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if has_user_voted is not UNSET:
            field_dict["hasUserVoted"] = has_user_voted
        if can_user_vote is not UNSET:
            field_dict["canUserVote"] = can_user_vote
        if should_show_votes is not UNSET:
            field_dict["shouldShowVotes"] = should_show_votes
        if up_votes is not UNSET:
            field_dict["upVotes"] = up_votes
        if down_votes is not UNSET:
            field_dict["downVotes"] = down_votes
        if reason_for_not_able_to_vote is not UNSET:
            field_dict["reasonForNotAbleToVote"] = reason_for_not_able_to_vote

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = d.pop("assetId", UNSET)

        has_user_voted = d.pop("hasUserVoted", UNSET)

        can_user_vote = d.pop("canUserVote", UNSET)

        should_show_votes = d.pop("shouldShowVotes", UNSET)

        up_votes = d.pop("upVotes", UNSET)

        down_votes = d.pop("downVotes", UNSET)

        reason_for_not_able_to_vote = d.pop("reasonForNotAbleToVote", UNSET)

        roblox_api_develop_models_response_asset_voting_model = cls(
            asset_id=asset_id,
            has_user_voted=has_user_voted,
            can_user_vote=can_user_vote,
            should_show_votes=should_show_votes,
            up_votes=up_votes,
            down_votes=down_votes,
            reason_for_not_able_to_vote=reason_for_not_able_to_vote,
        )

        return roblox_api_develop_models_response_asset_voting_model
