from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_authentication_api_models_request_audit_content_value_parameters import (
        RobloxAuthenticationApiModelsRequestAuditContentValueParameters,
    )


T = TypeVar("T", bound="RobloxAuthenticationApiModelsRequestAuditContentValue")


@_attrs_define
class RobloxAuthenticationApiModelsRequestAuditContentValue:
    """
    Attributes:
        translation_key (str | Unset):
        translation_namespace (str | Unset):
        translated_source_string (str | Unset):
        parameters (RobloxAuthenticationApiModelsRequestAuditContentValueParameters | Unset):
    """

    translation_key: str | Unset = UNSET
    translation_namespace: str | Unset = UNSET
    translated_source_string: str | Unset = UNSET
    parameters: RobloxAuthenticationApiModelsRequestAuditContentValueParameters | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        translation_key = self.translation_key

        translation_namespace = self.translation_namespace

        translated_source_string = self.translated_source_string

        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if translation_key is not UNSET:
            field_dict["translationKey"] = translation_key
        if translation_namespace is not UNSET:
            field_dict["translationNamespace"] = translation_namespace
        if translated_source_string is not UNSET:
            field_dict["translatedSourceString"] = translated_source_string
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_authentication_api_models_request_audit_content_value_parameters import (
            RobloxAuthenticationApiModelsRequestAuditContentValueParameters,
        )

        d = dict(src_dict)
        translation_key = d.pop("translationKey", UNSET)

        translation_namespace = d.pop("translationNamespace", UNSET)

        translated_source_string = d.pop("translatedSourceString", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: RobloxAuthenticationApiModelsRequestAuditContentValueParameters | Unset
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = RobloxAuthenticationApiModelsRequestAuditContentValueParameters.from_dict(_parameters)

        roblox_authentication_api_models_request_audit_content_value = cls(
            translation_key=translation_key,
            translation_namespace=translation_namespace,
            translated_source_string=translated_source_string,
            parameters=parameters,
        )

        return roblox_authentication_api_models_request_audit_content_value
