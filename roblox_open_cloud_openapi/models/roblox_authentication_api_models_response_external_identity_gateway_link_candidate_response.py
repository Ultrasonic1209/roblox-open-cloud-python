from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsResponseExternalIdentityGatewayLinkCandidateResponse")


@_attrs_define
class RobloxAuthenticationApiModelsResponseExternalIdentityGatewayLinkCandidateResponse:
    """
    Attributes:
        user_ids (list[int] | Unset):
        email (str | Unset):
    """

    user_ids: list[int] | Unset = UNSET
    email: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_ids: list[int] | Unset = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        email = self.email

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_ids is not UNSET:
            field_dict["userIds"] = user_ids
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_ids = cast(list[int], d.pop("userIds", UNSET))

        email = d.pop("email", UNSET)

        roblox_authentication_api_models_response_external_identity_gateway_link_candidate_response = cls(
            user_ids=user_ids,
            email=email,
        )

        return roblox_authentication_api_models_response_external_identity_gateway_link_candidate_response
