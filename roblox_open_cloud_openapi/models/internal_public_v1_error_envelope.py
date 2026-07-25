from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_public_v1_public_error import InternalPublicV1PublicError


T = TypeVar("T", bound="InternalPublicV1ErrorEnvelope")


@_attrs_define
class InternalPublicV1ErrorEnvelope:
    """
    Attributes:
        detail (str | Unset): A human-readable explanation of this specific failure.
        errors (list[InternalPublicV1PublicError] | Unset): The individual errors. There is at least one entry; each has
            a code and message.
        status (int | Unset): The HTTP status code, repeated here for convenience.
        title (str | Unset): A short summary of the error class.
    """

    detail: str | Unset = UNSET
    errors: list[InternalPublicV1PublicError] | Unset = UNSET
    status: int | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detail = self.detail

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        status = self.status

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if detail is not UNSET:
            field_dict["detail"] = detail
        if errors is not UNSET:
            field_dict["errors"] = errors
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_public_v1_public_error import InternalPublicV1PublicError

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        detail = d.pop("detail", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[InternalPublicV1PublicError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = InternalPublicV1PublicError.from_dict(errors_item_data)

                errors.append(errors_item)

        status = d.pop("status", UNSET)

        title = d.pop("title", UNSET)

        internal_public_v1_error_envelope = cls(
            detail=detail,
            errors=errors,
            status=status,
            title=title,
        )

        internal_public_v1_error_envelope.additional_properties = d
        return internal_public_v1_error_envelope

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
