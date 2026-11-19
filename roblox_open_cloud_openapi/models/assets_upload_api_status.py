from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_info import ErrorInfo


T = TypeVar("T", bound="AssetsUploadApiStatus")


@_attrs_define
class AssetsUploadApiStatus:
    """The logical error model explaining the error status.

    Attributes:
        code (None | str | Unset): The error code.
        message (None | str | Unset): The error message.
        details (list[ErrorInfo] | Unset):
    """

    code: None | str | Unset = UNSET
    message: None | str | Unset = UNSET
    details: list[ErrorInfo] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()
                details.append(details_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_info import ErrorInfo  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        _details = d.pop("details", UNSET)
        details: list[ErrorInfo] | Unset = UNSET
        if _details is not UNSET:
            details = []
            for details_item_data in _details:
                details_item = ErrorInfo.from_dict(details_item_data)

                details.append(details_item)

        assets_upload_api_status = cls(
            code=code,
            message=message,
            details=details,
        )

        return assets_upload_api_status
