from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transaction_record_response import TransactionRecordResponse


T = TypeVar("T", bound="TransactionRecordResponseApiPageResponse")


@_attrs_define
class TransactionRecordResponseApiPageResponse:
    """
    Attributes:
        previous_page_cursor (None | str | Unset):
        next_page_cursor (None | str | Unset):
        data (list[TransactionRecordResponse] | None | Unset):
    """

    previous_page_cursor: None | str | Unset = UNSET
    next_page_cursor: None | str | Unset = UNSET
    data: list[TransactionRecordResponse] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        previous_page_cursor: None | str | Unset
        if isinstance(self.previous_page_cursor, Unset):
            previous_page_cursor = UNSET
        else:
            previous_page_cursor = self.previous_page_cursor

        next_page_cursor: None | str | Unset
        if isinstance(self.next_page_cursor, Unset):
            next_page_cursor = UNSET
        else:
            next_page_cursor = self.next_page_cursor

        data: list[dict[str, Any]] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, list):
            data = []
            for data_type_0_item_data in self.data:
                data_type_0_item = data_type_0_item_data.to_dict()
                data.append(data_type_0_item)

        else:
            data = self.data

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if previous_page_cursor is not UNSET:
            field_dict["previousPageCursor"] = previous_page_cursor
        if next_page_cursor is not UNSET:
            field_dict["nextPageCursor"] = next_page_cursor
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transaction_record_response import TransactionRecordResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_previous_page_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_page_cursor = _parse_previous_page_cursor(d.pop("previousPageCursor", UNSET))

        def _parse_next_page_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_cursor = _parse_next_page_cursor(d.pop("nextPageCursor", UNSET))

        def _parse_data(data: object) -> list[TransactionRecordResponse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = []
                _data_type_0 = data
                for data_type_0_item_data in _data_type_0:
                    data_type_0_item = TransactionRecordResponse.from_dict(data_type_0_item_data)

                    data_type_0.append(data_type_0_item)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TransactionRecordResponse] | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        transaction_record_response_api_page_response = cls(
            previous_page_cursor=previous_page_cursor,
            next_page_cursor=next_page_cursor,
            data=data,
        )

        return transaction_record_response_api_page_response
