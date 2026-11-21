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
        error_code (GamePassesErrorCode): Code representing various error conditions.
        error_message (str): The human readable error message.
        field (None | str | Unset): The relevant field that caused the error.
        hint (None | str | Unset): A hint as to what caused the error, if applicable.
    """

    error_code: GamePassesErrorCode
    error_message: str
    field: None | str | Unset = UNSET
    hint: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        error_code = self.error_code.value

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

        field_dict.update(
            {
                "errorCode": error_code,
                "errorMessage": error_message,
            }
        )
        if field is not UNSET:
            field_dict["field"] = field
        if hint is not UNSET:
            field_dict["hint"] = hint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error_code = GamePassesErrorCode(d.pop("errorCode"))

        error_message = d.pop("errorMessage")

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
