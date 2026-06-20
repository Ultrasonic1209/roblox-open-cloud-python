from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_authentication_api_models_forgot_password_user_response import (
        RobloxAuthenticationApiModelsForgotPasswordUserResponse,
    )


T = TypeVar("T", bound="RobloxAuthenticationApiModelsPasswordResetVerificationResponse")


@_attrs_define
class RobloxAuthenticationApiModelsPasswordResetVerificationResponse:
    """
    Attributes:
        user_tickets (list[RobloxAuthenticationApiModelsForgotPasswordUserResponse] | Unset):
    """

    user_tickets: list[RobloxAuthenticationApiModelsForgotPasswordUserResponse] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_tickets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user_tickets, Unset):
            user_tickets = []
            for user_tickets_item_data in self.user_tickets:
                user_tickets_item = user_tickets_item_data.to_dict()
                user_tickets.append(user_tickets_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_tickets is not UNSET:
            field_dict["userTickets"] = user_tickets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_authentication_api_models_forgot_password_user_response import (
            RobloxAuthenticationApiModelsForgotPasswordUserResponse,
        )

        d = dict(src_dict)
        _user_tickets = d.pop("userTickets", UNSET)
        user_tickets: list[RobloxAuthenticationApiModelsForgotPasswordUserResponse] | Unset = UNSET
        if _user_tickets is not UNSET:
            user_tickets = []
            for user_tickets_item_data in _user_tickets:
                user_tickets_item = RobloxAuthenticationApiModelsForgotPasswordUserResponse.from_dict(
                    user_tickets_item_data
                )

                user_tickets.append(user_tickets_item)

        roblox_authentication_api_models_password_reset_verification_response = cls(
            user_tickets=user_tickets,
        )

        return roblox_authentication_api_models_password_reset_verification_response
