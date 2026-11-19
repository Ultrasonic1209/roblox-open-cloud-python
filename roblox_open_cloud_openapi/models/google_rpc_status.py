from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_protobuf_well_known_types_any import GoogleProtobufWellKnownTypesAny


T = TypeVar("T", bound="GoogleRpcStatus")


@_attrs_define
class GoogleRpcStatus:
    """
    Attributes:
        code (int | Unset):
        message (None | str | Unset):
        details (list[GoogleProtobufWellKnownTypesAny] | None | Unset):
    """

    code: int | Unset = UNSET
    message: None | str | Unset = UNSET
    details: list[GoogleProtobufWellKnownTypesAny] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        details: list[dict[str, Any]] | None | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, list):
            details = []
            for details_type_0_item_data in self.details:
                details_type_0_item = details_type_0_item_data.to_dict()
                details.append(details_type_0_item)

        else:
            details = self.details

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
        from ..models.google_protobuf_well_known_types_any import GoogleProtobufWellKnownTypesAny  # noqa: PLC0415

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_details(data: object) -> list[GoogleProtobufWellKnownTypesAny] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                details_type_0 = []
                _details_type_0 = data
                for details_type_0_item_data in _details_type_0:
                    details_type_0_item = GoogleProtobufWellKnownTypesAny.from_dict(details_type_0_item_data)

                    details_type_0.append(details_type_0_item)

                return details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GoogleProtobufWellKnownTypesAny] | None | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        google_rpc_status = cls(
            code=code,
            message=message,
            details=details,
        )

        return google_rpc_status
