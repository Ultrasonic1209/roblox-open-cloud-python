from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalControllerHttpControllerResearcherRoleData")


@_attrs_define
class InternalControllerHttpControllerResearcherRoleData:
    """
    Attributes:
        expires_at (str | Unset): ExpiresAt is when an APPROVED grant's access ends, RFC 3339; absent when the
            grant has no expiry. Example: 2028-09-18T23:59:59Z.
        granted_at (str | Unset): GrantedAt is when the grant was first recorded, RFC 3339. Example:
            2026-06-27T09:05:00Z.
        role (str | Unset): Role is the granted tier: QR (qualified) or VR (vetted). Example: QR.
        state (str | Unset): State is the grant's lifecycle state. Example: APPROVED.
    """

    expires_at: str | Unset = UNSET
    granted_at: str | Unset = UNSET
    role: str | Unset = UNSET
    state: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_at = self.expires_at

        granted_at = self.granted_at

        role = self.role

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if granted_at is not UNSET:
            field_dict["granted_at"] = granted_at
        if role is not UNSET:
            field_dict["role"] = role
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expires_at = d.pop("expires_at", UNSET)

        granted_at = d.pop("granted_at", UNSET)

        role = d.pop("role", UNSET)

        state = d.pop("state", UNSET)

        internal_controller_http_controller_researcher_role_data = cls(
            expires_at=expires_at,
            granted_at=granted_at,
            role=role,
            state=state,
        )

        internal_controller_http_controller_researcher_role_data.additional_properties = d
        return internal_controller_http_controller_researcher_role_data

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
