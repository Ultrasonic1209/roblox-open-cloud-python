from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationAuthorizationsApiModelsResponseScopeConfigurationEntry")


@_attrs_define
class ApplicationAuthorizationsApiModelsResponseScopeConfigurationEntry:
    """
    Attributes:
        scope_type (str):
        operation (str):
        target_type (None | str | Unset):
        translation_key (None | str | Unset):
        description (None | str | Unset):
        risk_level (None | str | Unset):
        group_allowed (bool | Unset):
        first_party_o_auth_only (bool | Unset):
        categories (list[str] | None | Unset):
    """

    scope_type: str
    operation: str
    target_type: None | str | Unset = UNSET
    translation_key: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    risk_level: None | str | Unset = UNSET
    group_allowed: bool | Unset = UNSET
    first_party_o_auth_only: bool | Unset = UNSET
    categories: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        scope_type = self.scope_type

        operation = self.operation

        target_type: None | str | Unset
        if isinstance(self.target_type, Unset):
            target_type = UNSET
        else:
            target_type = self.target_type

        translation_key: None | str | Unset
        if isinstance(self.translation_key, Unset):
            translation_key = UNSET
        else:
            translation_key = self.translation_key

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        risk_level: None | str | Unset
        if isinstance(self.risk_level, Unset):
            risk_level = UNSET
        else:
            risk_level = self.risk_level

        group_allowed = self.group_allowed

        first_party_o_auth_only = self.first_party_o_auth_only

        categories: list[str] | None | Unset
        if isinstance(self.categories, Unset):
            categories = UNSET
        elif isinstance(self.categories, list):
            categories = self.categories

        else:
            categories = self.categories

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "scopeType": scope_type,
                "operation": operation,
            }
        )
        if target_type is not UNSET:
            field_dict["targetType"] = target_type
        if translation_key is not UNSET:
            field_dict["translationKey"] = translation_key
        if description is not UNSET:
            field_dict["description"] = description
        if risk_level is not UNSET:
            field_dict["riskLevel"] = risk_level
        if group_allowed is not UNSET:
            field_dict["groupAllowed"] = group_allowed
        if first_party_o_auth_only is not UNSET:
            field_dict["firstPartyOAuthOnly"] = first_party_o_auth_only
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scope_type = d.pop("scopeType")

        operation = d.pop("operation")

        def _parse_target_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_type = _parse_target_type(d.pop("targetType", UNSET))

        def _parse_translation_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        translation_key = _parse_translation_key(d.pop("translationKey", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_risk_level(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        risk_level = _parse_risk_level(d.pop("riskLevel", UNSET))

        group_allowed = d.pop("groupAllowed", UNSET)

        first_party_o_auth_only = d.pop("firstPartyOAuthOnly", UNSET)

        def _parse_categories(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                categories_type_0 = cast(list[str], data)

                return categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        categories = _parse_categories(d.pop("categories", UNSET))

        application_authorizations_api_models_response_scope_configuration_entry = cls(
            scope_type=scope_type,
            operation=operation,
            target_type=target_type,
            translation_key=translation_key,
            description=description,
            risk_level=risk_level,
            group_allowed=group_allowed,
            first_party_o_auth_only=first_party_o_auth_only,
            categories=categories,
        )

        return application_authorizations_api_models_response_scope_configuration_entry
