from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenCloudUsersStatus")


@_attrs_define
class OpenCloudUsersStatus:
    """The `Status` type defines a logical error model that is suitable for different programming environments, including
    REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces
    of data: error code, error message, and error details. You can find out more about this error model and how to work
    with it in the [API Design Guide](https://cloud.google.com/apis/design/errors).

        Attributes:
            code (int | Unset): The status code, which should be an enum value of [google.rpc.Code][google.rpc.Code].
            message (None | str | Unset): A developer-facing error message, which should be in English. Any user-facing
                error message should be localized and sent in the [google.rpc.Status.details][google.rpc.Status.details] field,
                or localized by the client.
            details (list[Any] | None | Unset): A list of messages that carry the error details.  There is a common set of
                message types for APIs to use.
    """

    code: int | Unset = UNSET
    message: None | str | Unset = UNSET
    details: list[Any] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        details: list[Any] | None | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, list):
            details = self.details

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
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        code = d.pop("code", UNSET)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_details(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                details_type_0 = cast(list[Any], data)

                return details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        open_cloud_users_status = cls(
            code=code,
            message=message,
            details=details,
        )

        return open_cloud_users_status
