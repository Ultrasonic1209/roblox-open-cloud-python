from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_controller_http_controller_researcher_role_data import (
        InternalControllerHttpControllerResearcherRoleData,
    )


T = TypeVar("T", bound="InternalControllerHttpControllerResearcherRolesData")


@_attrs_define
class InternalControllerHttpControllerResearcherRolesData:
    """
    Attributes:
        roles (list[InternalControllerHttpControllerResearcherRoleData] | Unset): Roles is every grant held by the
            caller; empty when they hold none.
    """

    roles: list[InternalControllerHttpControllerResearcherRoleData] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        roles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()
                roles.append(roles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_controller_http_controller_researcher_role_data import (
            InternalControllerHttpControllerResearcherRoleData,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _roles = d.pop("roles", UNSET)
        roles: list[InternalControllerHttpControllerResearcherRoleData] | Unset = UNSET
        if _roles is not UNSET:
            roles = []
            for roles_item_data in _roles:
                roles_item = InternalControllerHttpControllerResearcherRoleData.from_dict(roles_item_data)

                roles.append(roles_item)

        internal_controller_http_controller_researcher_roles_data = cls(
            roles=roles,
        )

        internal_controller_http_controller_researcher_roles_data.additional_properties = d
        return internal_controller_http_controller_researcher_roles_data

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
