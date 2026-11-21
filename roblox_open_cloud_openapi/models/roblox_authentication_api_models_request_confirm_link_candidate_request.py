from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsRequestConfirmLinkCandidateRequest")


@_attrs_define
class RobloxAuthenticationApiModelsRequestConfirmLinkCandidateRequest:
    """
    Attributes:
        link_candidate_token_id (str | Unset):
        user_id (int | Unset):
        create_new (bool | Unset):
    """

    link_candidate_token_id: str | Unset = UNSET
    user_id: int | Unset = UNSET
    create_new: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        link_candidate_token_id = self.link_candidate_token_id

        user_id = self.user_id

        create_new = self.create_new

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if link_candidate_token_id is not UNSET:
            field_dict["linkCandidateTokenId"] = link_candidate_token_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if create_new is not UNSET:
            field_dict["createNew"] = create_new

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        link_candidate_token_id = d.pop("linkCandidateTokenId", UNSET)

        user_id = d.pop("userId", UNSET)

        create_new = d.pop("createNew", UNSET)

        roblox_authentication_api_models_request_confirm_link_candidate_request = cls(
            link_candidate_token_id=link_candidate_token_id,
            user_id=user_id,
            create_new=create_new,
        )

        return roblox_authentication_api_models_request_confirm_link_candidate_request
