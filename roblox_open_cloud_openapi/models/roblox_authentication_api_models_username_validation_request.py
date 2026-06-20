from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_authentication_api_models_username_validation_request_context import (
    RobloxAuthenticationApiModelsUsernameValidationRequestContext,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsUsernameValidationRequest")


@_attrs_define
class RobloxAuthenticationApiModelsUsernameValidationRequest:
    """
    Attributes:
        username (str | Unset):
        birthday (datetime.datetime | Unset):
        context (RobloxAuthenticationApiModelsUsernameValidationRequestContext | Unset):
    """

    username: str | Unset = UNSET
    birthday: datetime.datetime | Unset = UNSET
    context: RobloxAuthenticationApiModelsUsernameValidationRequestContext | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        birthday: str | Unset = UNSET
        if not isinstance(self.birthday, Unset):
            birthday = self.birthday.isoformat()

        context: int | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if birthday is not UNSET:
            field_dict["birthday"] = birthday
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        username = d.pop("username", UNSET)

        _birthday = d.pop("birthday", UNSET)
        birthday: datetime.datetime | Unset
        if isinstance(_birthday, Unset):
            birthday = UNSET
        else:
            birthday = datetime.datetime.fromisoformat(_birthday)

        _context = d.pop("context", UNSET)
        context: RobloxAuthenticationApiModelsUsernameValidationRequestContext | Unset
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = RobloxAuthenticationApiModelsUsernameValidationRequestContext(_context)

        roblox_authentication_api_models_username_validation_request = cls(
            username=username,
            birthday=birthday,
            context=context,
        )

        return roblox_authentication_api_models_username_validation_request
