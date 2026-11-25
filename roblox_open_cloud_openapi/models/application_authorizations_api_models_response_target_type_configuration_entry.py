from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationAuthorizationsApiModelsResponseTargetTypeConfigurationEntry")


@_attrs_define
class ApplicationAuthorizationsApiModelsResponseTargetTypeConfigurationEntry:
    """
    Attributes:
        name (str):
        required_parts (list[str] | None | Unset):
        optional_parts (list[str] | None | Unset):
        translation_key (None | str | Unset):
    """

    name: str
    required_parts: list[str] | None | Unset = UNSET
    optional_parts: list[str] | None | Unset = UNSET
    translation_key: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        required_parts: list[str] | None | Unset
        if isinstance(self.required_parts, Unset):
            required_parts = UNSET
        elif isinstance(self.required_parts, list):
            required_parts = self.required_parts

        else:
            required_parts = self.required_parts

        optional_parts: list[str] | None | Unset
        if isinstance(self.optional_parts, Unset):
            optional_parts = UNSET
        elif isinstance(self.optional_parts, list):
            optional_parts = self.optional_parts

        else:
            optional_parts = self.optional_parts

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
        if required_parts is not UNSET:
            field_dict["requiredParts"] = required_parts
        if optional_parts is not UNSET:
            field_dict["optionalParts"] = optional_parts
        if translation_key is not UNSET:
            field_dict["translationKey"] = translation_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_required_parts(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                required_parts_type_0 = cast(list[str], data)

                return required_parts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        required_parts = _parse_required_parts(d.pop("requiredParts", UNSET))

        def _parse_optional_parts(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                optional_parts_type_0 = cast(list[str], data)

                return optional_parts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        optional_parts = _parse_optional_parts(d.pop("optionalParts", UNSET))

        def _parse_translation_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        translation_key = _parse_translation_key(d.pop("translationKey", UNSET))

        application_authorizations_api_models_response_target_type_configuration_entry = cls(
            name=name,
            required_parts=required_parts,
            optional_parts=optional_parts,
            translation_key=translation_key,
        )

        return application_authorizations_api_models_response_target_type_configuration_entry
