from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="RobloxClientSettingsApiModelsResponseBetaProgramInfo")


@_attrs_define
class RobloxClientSettingsApiModelsResponseBetaProgramInfo:
    """Beta program information included in the user channel response.

    Attributes:
        name (str): The display name of the beta program.
        id (str): The ID of the beta program.
    """

    name: str
    id: str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name = d.pop("name")

        id = d.pop("id")

        roblox_client_settings_api_models_response_beta_program_info = cls(
            name=name,
            id=id,
        )

        return roblox_client_settings_api_models_response_beta_program_info
