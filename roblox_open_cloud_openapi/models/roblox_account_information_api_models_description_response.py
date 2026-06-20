from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAccountInformationApiModelsDescriptionResponse")


@_attrs_define
class RobloxAccountInformationApiModelsDescriptionResponse:
    """The description response

    Attributes:
        description (str | Unset): The description
    """

    description: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        description = d.pop("description", UNSET)

        roblox_account_information_api_models_description_response = cls(
            description=description,
        )

        return roblox_account_information_api_models_description_response
