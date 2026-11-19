from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicError")


@_attrs_define
class PublicError:
    """
    Attributes:
        code (str): A stable, machine-readable error code (for example, `INVALID_ARGUMENT`,
            `NOT_FOUND`, `PERMISSION_DENIED`, or `RATE_LIMITED`).
        message (str): A human-readable description of the error.
        action_url (str | Unset): Ads Manager page that a human opens to fix this error. Show this URL to the user and
            check again after they say they are done.
            Never collect payment details through the API or in chat.
        field (str | Unset): Request field path, when the error is tied to a specific field.
        reason (str | Unset): Specific machine-readable sub-reason, when applicable.
        remediation (str | Unset): Actionable guidance for resolving the error.
        retryable (bool | Unset): Whether the caller should retry the request.
    """

    code: str
    message: str
    action_url: str | Unset = UNSET
    field: str | Unset = UNSET
    reason: str | Unset = UNSET
    remediation: str | Unset = UNSET
    retryable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        action_url = self.action_url

        field = self.field

        reason = self.reason

        remediation = self.remediation

        retryable = self.retryable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if action_url is not UNSET:
            field_dict["actionUrl"] = action_url
        if field is not UNSET:
            field_dict["field"] = field
        if reason is not UNSET:
            field_dict["reason"] = reason
        if remediation is not UNSET:
            field_dict["remediation"] = remediation
        if retryable is not UNSET:
            field_dict["retryable"] = retryable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        action_url = d.pop("actionUrl", UNSET)

        field = d.pop("field", UNSET)

        reason = d.pop("reason", UNSET)

        remediation = d.pop("remediation", UNSET)

        retryable = d.pop("retryable", UNSET)

        public_error = cls(
            code=code,
            message=message,
            action_url=action_url,
            field=field,
            reason=reason,
            remediation=remediation,
            retryable=retryable,
        )

        public_error.additional_properties = d
        return public_error

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
