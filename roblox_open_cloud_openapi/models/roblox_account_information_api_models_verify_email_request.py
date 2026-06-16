from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAccountInformationApiModelsVerifyEmailRequest")


@_attrs_define
class RobloxAccountInformationApiModelsVerifyEmailRequest:
    """Verify Email Request

    Attributes:
        ticket (str | Unset): Ticket to verify email
    """

    ticket: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        ticket = self.ticket

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if ticket is not UNSET:
            field_dict["ticket"] = ticket

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ticket = d.pop("ticket", UNSET)

        roblox_account_information_api_models_verify_email_request = cls(
            ticket=ticket,
        )

        return roblox_account_information_api_models_verify_email_request
