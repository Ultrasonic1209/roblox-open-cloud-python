from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.string_string_i_enumerable_key_value_pair import StringStringIEnumerableKeyValuePair


T = TypeVar("T", bound="HttpContent")


@_attrs_define
class HttpContent:
    """
    Attributes:
        headers (list[StringStringIEnumerableKeyValuePair] | None | Unset):
    """

    headers: list[StringStringIEnumerableKeyValuePair] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        headers: list[dict[str, Any]] | None | Unset
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, list):
            headers = []
            for headers_type_0_item_data in self.headers:
                headers_type_0_item = headers_type_0_item_data.to_dict()
                headers.append(headers_type_0_item)

        else:
            headers = self.headers

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.string_string_i_enumerable_key_value_pair import StringStringIEnumerableKeyValuePair

        d = dict(src_dict)

        def _parse_headers(data: object) -> list[StringStringIEnumerableKeyValuePair] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                headers_type_0 = []
                _headers_type_0 = data
                for headers_type_0_item_data in _headers_type_0:
                    headers_type_0_item = StringStringIEnumerableKeyValuePair.from_dict(headers_type_0_item_data)

                    headers_type_0.append(headers_type_0_item)

                return headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[StringStringIEnumerableKeyValuePair] | None | Unset, data)

        headers = _parse_headers(d.pop("headers", UNSET))

        http_content = cls(
            headers=headers,
        )

        return http_content
