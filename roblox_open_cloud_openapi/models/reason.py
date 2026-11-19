from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Reason")


@_attrs_define
class Reason:
    """
    Attributes:
        code (str): A stable, machine-readable code.
        message (str): A human-readable explanation.
        remediation (str | Unset): What the caller can do to resolve it.
        resource (str | Unset): The related resource, for example `billing-accounts/123`.
    """

    code: str
    message: str
    remediation: str | Unset = UNSET
    resource: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        remediation = self.remediation

        resource = self.resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if remediation is not UNSET:
            field_dict["remediation"] = remediation
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        remediation = d.pop("remediation", UNSET)

        resource = d.pop("resource", UNSET)

        reason = cls(
            code=code,
            message=message,
            remediation=remediation,
            resource=resource,
        )

        reason.additional_properties = d
        return reason

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
