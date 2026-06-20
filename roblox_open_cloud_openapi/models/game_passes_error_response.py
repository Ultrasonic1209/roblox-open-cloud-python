from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.game_passes_error_code import GamePassesErrorCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="GamePassesErrorResponse")


@_attrs_define
class GamePassesErrorResponse:
    """This is the base class for all custom Exceptions that are thrown in this API.

    Attributes:
        error_code (GamePassesErrorCode | Unset): Code representing various error conditions.
        error_message (None | str | Unset): The human readable error message.
        field (None | str | Unset): The relevant field that caused the error.
        hint (None | str | Unset): A hint as to what caused the error, if applicable.
    """

    error_code: GamePassesErrorCode | Unset = UNSET
    error_message: None | str | Unset = UNSET
    field: None | str | Unset = UNSET
    hint: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        error_code: str | Unset = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code.value

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        field: None | str | Unset
        if isinstance(self.field, Unset):
            field = UNSET
        else:
            field = self.field

        hint: None | str | Unset
        if isinstance(self.hint, Unset):
            hint = UNSET
        else:
            hint = self.hint

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if field is not UNSET:
            field_dict["field"] = field
        if hint is not UNSET:
            field_dict["hint"] = hint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _error_code = d.pop("errorCode", UNSET)
        error_code: GamePassesErrorCode | Unset
        if isinstance(_error_code, Unset):
            error_code = UNSET
        else:
            error_code = GamePassesErrorCode(_error_code)

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))

        def _parse_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field = _parse_field(d.pop("field", UNSET))

        def _parse_hint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hint = _parse_hint(d.pop("hint", UNSET))

        game_passes_error_response = cls(
            error_code=error_code,
            error_message=error_message,
            field=field,
            hint=hint,
        )

        return game_passes_error_response
