from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationAuthorizationsApiModelsResponseOperationConfigurationEntry")


@_attrs_define
class ApplicationAuthorizationsApiModelsResponseOperationConfigurationEntry:
    """
    Attributes:
        name (str):
        translation_key (None | str | Unset):
    """

    name: str
    translation_key: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        translation_key: None | str | Unset
        if isinstance(self.translation_key, Unset):
            translation_key = UNSET
        else:
            translation_key = self.translation_key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if translation_key is not UNSET:
            field_dict["translationKey"] = translation_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_translation_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        translation_key = _parse_translation_key(d.pop("translationKey", UNSET))

        application_authorizations_api_models_response_operation_configuration_entry = cls(
            name=name,
            translation_key=translation_key,
        )

        return application_authorizations_api_models_response_operation_configuration_entry
