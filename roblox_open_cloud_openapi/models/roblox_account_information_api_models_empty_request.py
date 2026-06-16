from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="RobloxAccountInformationApiModelsEmptyRequest")


@_attrs_define
class RobloxAccountInformationApiModelsEmptyRequest:
    """For API calls without a request body."""

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        roblox_account_information_api_models_empty_request = cls()

        return roblox_account_information_api_models_empty_request
