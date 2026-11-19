from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.public_error import PublicError


T = TypeVar("T", bound="ErrorEnvelope")


@_attrs_define
class ErrorEnvelope:
    """
    Attributes:
        detail (str): A human-readable explanation of this specific failure.
        errors (list[PublicError]): The individual errors. There is at least one entry; each has a code and message.
        status (int): The HTTP status code, repeated here for convenience.
        title (str): A short summary of the error class.
    """

    detail: str
    errors: list[PublicError]
    status: int
    title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detail = self.detail

        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()
            errors.append(errors_item)

        status = self.status

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "detail": detail,
                "errors": errors,
                "status": status,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_error import PublicError  # noqa: PLC0415

        d = dict(src_dict)
        detail = d.pop("detail")

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:
            errors_item = PublicError.from_dict(errors_item_data)

            errors.append(errors_item)

        status = d.pop("status")

        title = d.pop("title")

        error_envelope = cls(
            detail=detail,
            errors=errors,
            status=status,
            title=title,
        )

        error_envelope.additional_properties = d
        return error_envelope

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
