from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.transaction_records_api_http_status_code import TransactionRecordsApiHttpStatusCode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_content import HttpContent
    from ..models.http_request_message import HttpRequestMessage
    from ..models.string_string_i_enumerable_key_value_pair import StringStringIEnumerableKeyValuePair


T = TypeVar("T", bound="HttpResponseMessage")


@_attrs_define
class HttpResponseMessage:
    """
    Attributes:
        version (None | str | Unset):
        content (HttpContent | None | Unset):
        status_code (TransactionRecordsApiHttpStatusCode | Unset):
        reason_phrase (None | str | Unset):
        headers (list[StringStringIEnumerableKeyValuePair] | None | Unset):
        trailing_headers (list[StringStringIEnumerableKeyValuePair] | None | Unset):
        request_message (HttpRequestMessage | None | Unset):
        is_success_status_code (bool | Unset):
    """

    version: None | str | Unset = UNSET
    content: HttpContent | None | Unset = UNSET
    status_code: TransactionRecordsApiHttpStatusCode | Unset = UNSET
    reason_phrase: None | str | Unset = UNSET
    headers: list[StringStringIEnumerableKeyValuePair] | None | Unset = UNSET
    trailing_headers: list[StringStringIEnumerableKeyValuePair] | None | Unset = UNSET
    request_message: HttpRequestMessage | None | Unset = UNSET
    is_success_status_code: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.http_content import HttpContent
        from ..models.http_request_message import HttpRequestMessage

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        content: dict[str, Any] | None | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        elif isinstance(self.content, HttpContent):
            content = self.content.to_dict()
        else:
            content = self.content

        status_code: str | Unset = UNSET
        if not isinstance(self.status_code, Unset):
            status_code = self.status_code.value

        reason_phrase: None | str | Unset
        if isinstance(self.reason_phrase, Unset):
            reason_phrase = UNSET
        else:
            reason_phrase = self.reason_phrase

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

        trailing_headers: list[dict[str, Any]] | None | Unset
        if isinstance(self.trailing_headers, Unset):
            trailing_headers = UNSET
        elif isinstance(self.trailing_headers, list):
            trailing_headers = []
            for trailing_headers_type_0_item_data in self.trailing_headers:
                trailing_headers_type_0_item = trailing_headers_type_0_item_data.to_dict()
                trailing_headers.append(trailing_headers_type_0_item)

        else:
            trailing_headers = self.trailing_headers

        request_message: dict[str, Any] | None | Unset
        if isinstance(self.request_message, Unset):
            request_message = UNSET
        elif isinstance(self.request_message, HttpRequestMessage):
            request_message = self.request_message.to_dict()
        else:
            request_message = self.request_message

        is_success_status_code = self.is_success_status_code

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if content is not UNSET:
            field_dict["content"] = content
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if reason_phrase is not UNSET:
            field_dict["reasonPhrase"] = reason_phrase
        if headers is not UNSET:
            field_dict["headers"] = headers
        if trailing_headers is not UNSET:
            field_dict["trailingHeaders"] = trailing_headers
        if request_message is not UNSET:
            field_dict["requestMessage"] = request_message
        if is_success_status_code is not UNSET:
            field_dict["isSuccessStatusCode"] = is_success_status_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.http_content import HttpContent
        from ..models.http_request_message import HttpRequestMessage
        from ..models.string_string_i_enumerable_key_value_pair import StringStringIEnumerableKeyValuePair

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_content(data: object) -> HttpContent | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_1 = HttpContent.from_dict(data)

                return content_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HttpContent | None | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        _status_code = d.pop("statusCode", UNSET)
        status_code: TransactionRecordsApiHttpStatusCode | Unset
        if isinstance(_status_code, Unset):
            status_code = UNSET
        else:
            status_code = TransactionRecordsApiHttpStatusCode(_status_code)

        def _parse_reason_phrase(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason_phrase = _parse_reason_phrase(d.pop("reasonPhrase", UNSET))

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

        def _parse_trailing_headers(data: object) -> list[StringStringIEnumerableKeyValuePair] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                trailing_headers_type_0 = []
                _trailing_headers_type_0 = data
                for trailing_headers_type_0_item_data in _trailing_headers_type_0:
                    trailing_headers_type_0_item = StringStringIEnumerableKeyValuePair.from_dict(
                        trailing_headers_type_0_item_data
                    )

                    trailing_headers_type_0.append(trailing_headers_type_0_item)

                return trailing_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[StringStringIEnumerableKeyValuePair] | None | Unset, data)

        trailing_headers = _parse_trailing_headers(d.pop("trailingHeaders", UNSET))

        def _parse_request_message(data: object) -> HttpRequestMessage | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                request_message_type_1 = HttpRequestMessage.from_dict(data)

                return request_message_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HttpRequestMessage | None | Unset, data)

        request_message = _parse_request_message(d.pop("requestMessage", UNSET))

        is_success_status_code = d.pop("isSuccessStatusCode", UNSET)

        http_response_message = cls(
            version=version,
            content=content,
            status_code=status_code,
            reason_phrase=reason_phrase,
            headers=headers,
            trailing_headers=trailing_headers,
            request_message=request_message,
            is_success_status_code=is_success_status_code,
        )

        return http_response_message
