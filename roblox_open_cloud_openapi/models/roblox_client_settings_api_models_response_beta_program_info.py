from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxClientSettingsApiModelsResponseBetaProgramInfo")


@_attrs_define
class RobloxClientSettingsApiModelsResponseBetaProgramInfo:
    """Beta program information included in the user channel response.

    Attributes:
        name (str | Unset): The display name of the beta program.
        id (str | Unset): The ID of the beta program.
    """

    name: str | Unset = UNSET
    id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        roblox_client_settings_api_models_response_beta_program_info = cls(
            name=name,
            id=id,
        )

        return roblox_client_settings_api_models_response_beta_program_info
