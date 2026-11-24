from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_opencloud_scopeconfiguration_v2_risk_level import RobloxOpencloudScopeconfigurationV2RiskLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxOpencloudScopeconfigurationV2Scope")


@_attrs_define
class RobloxOpencloudScopeconfigurationV2Scope:
    """The primary unit of the v2 configuration, identified by (scope_type, operation).

    Attributes:
        scope_type (str | Unset):
        operation (str | Unset):
        target_type (str | Unset):
        translation_key (str | Unset): Scope-specific description translation key (replaces the legacy operation
            override description key).
        risk_level (RobloxOpencloudScopeconfigurationV2RiskLevel | Unset): Risk level associated with a scope. Consumed
            by the front end.
        group_allowed (bool | Unset): Whether this scope is allowed on group-owned API keys.
        first_party_oauth_only (bool | Unset): Whether this scope may only be granted via first-party OAuth access. When
            true and the scope supports OAuth2,
            OAuth consumers must reject the scope unless the requesting client is a first-party client.
        description (str | Unset): Localized scope description for the requested locale, falling back to English. Unset
            when unavailable.
        display_section (str | Unset): UI section this scope is listed under in permission dialogs. Unset when the scope
            has none.
    """

    scope_type: str | Unset = UNSET
    operation: str | Unset = UNSET
    target_type: str | Unset = UNSET
    translation_key: str | Unset = UNSET
    risk_level: RobloxOpencloudScopeconfigurationV2RiskLevel | Unset = UNSET
    group_allowed: bool | Unset = UNSET
    first_party_oauth_only: bool | Unset = UNSET
    description: str | Unset = UNSET
    display_section: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        scope_type = self.scope_type

        operation = self.operation

        target_type = self.target_type

        translation_key = self.translation_key

        risk_level: str | Unset = UNSET
        if not isinstance(self.risk_level, Unset):
            risk_level = self.risk_level.value

        group_allowed = self.group_allowed

        first_party_oauth_only = self.first_party_oauth_only

        description = self.description

        display_section = self.display_section

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if scope_type is not UNSET:
            field_dict["scopeType"] = scope_type
        if operation is not UNSET:
            field_dict["operation"] = operation
        if target_type is not UNSET:
            field_dict["targetType"] = target_type
        if translation_key is not UNSET:
            field_dict["translationKey"] = translation_key
        if risk_level is not UNSET:
            field_dict["riskLevel"] = risk_level
        if group_allowed is not UNSET:
            field_dict["groupAllowed"] = group_allowed
        if first_party_oauth_only is not UNSET:
            field_dict["firstPartyOauthOnly"] = first_party_oauth_only
        if description is not UNSET:
            field_dict["description"] = description
        if display_section is not UNSET:
            field_dict["displaySection"] = display_section

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scope_type = d.pop("scopeType", UNSET)

        operation = d.pop("operation", UNSET)

        target_type = d.pop("targetType", UNSET)

        translation_key = d.pop("translationKey", UNSET)

        _risk_level = d.pop("riskLevel", UNSET)
        risk_level: RobloxOpencloudScopeconfigurationV2RiskLevel | Unset
        if isinstance(_risk_level, Unset):
            risk_level = UNSET
        else:
            risk_level = RobloxOpencloudScopeconfigurationV2RiskLevel(_risk_level)

        group_allowed = d.pop("groupAllowed", UNSET)

        first_party_oauth_only = d.pop("firstPartyOauthOnly", UNSET)

        description = d.pop("description", UNSET)

        display_section = d.pop("displaySection", UNSET)

        roblox_opencloud_scopeconfiguration_v2_scope = cls(
            scope_type=scope_type,
            operation=operation,
            target_type=target_type,
            translation_key=translation_key,
            risk_level=risk_level,
            group_allowed=group_allowed,
            first_party_oauth_only=first_party_oauth_only,
            description=description,
            display_section=display_section,
        )

        return roblox_opencloud_scopeconfiguration_v2_scope
