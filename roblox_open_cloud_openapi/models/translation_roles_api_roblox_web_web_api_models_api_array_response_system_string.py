from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranslationRolesApiRobloxWebWebAPIModelsApiArrayResponseSystemString")


@_attrs_define
class TranslationRolesApiRobloxWebWebAPIModelsApiArrayResponseSystemString:
    """
    Attributes:
        data (list[str] | Unset):
    """

    data: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[str] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        data = cast(list[str], d.pop("data", UNSET))

        translation_roles_api_roblox_web_web_api_models_api_array_response_system_string = cls(
            data=data,
        )

        translation_roles_api_roblox_web_web_api_models_api_array_response_system_string.additional_properties = d
        return translation_roles_api_roblox_web_web_api_models_api_array_response_system_string

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
