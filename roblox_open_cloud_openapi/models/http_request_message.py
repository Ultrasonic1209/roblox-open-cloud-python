from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.http_version_policy import HttpVersionPolicy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_content import HttpContent
    from ..models.http_method import HttpMethod
    from ..models.http_request_message_options_type_0 import HttpRequestMessageOptionsType0
    from ..models.http_request_message_properties_type_0 import HttpRequestMessagePropertiesType0
    from ..models.string_string_i_enumerable_key_value_pair import StringStringIEnumerableKeyValuePair


T = TypeVar("T", bound="HttpRequestMessage")


@_attrs_define
class HttpRequestMessage:
    """
    Attributes:
        version (None | str | Unset):
        version_policy (HttpVersionPolicy | Unset):
        content (HttpContent | None | Unset):
        method (HttpMethod | None | Unset):
        request_uri (None | str | Unset):
        headers (list[StringStringIEnumerableKeyValuePair] | None | Unset):
        properties (HttpRequestMessagePropertiesType0 | None | Unset):
        options (HttpRequestMessageOptionsType0 | None | Unset):
    """

    version: None | str | Unset = UNSET
    version_policy: HttpVersionPolicy | Unset = UNSET
    content: HttpContent | None | Unset = UNSET
    method: HttpMethod | None | Unset = UNSET
    request_uri: None | str | Unset = UNSET
    headers: list[StringStringIEnumerableKeyValuePair] | None | Unset = UNSET
    properties: HttpRequestMessagePropertiesType0 | None | Unset = UNSET
    options: HttpRequestMessageOptionsType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.http_content import HttpContent
        from ..models.http_method import HttpMethod
        from ..models.http_request_message_options_type_0 import HttpRequestMessageOptionsType0
        from ..models.http_request_message_properties_type_0 import HttpRequestMessagePropertiesType0

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        version_policy: str | Unset = UNSET
        if not isinstance(self.version_policy, Unset):
            version_policy = self.version_policy.value

        content: dict[str, Any] | None | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        elif isinstance(self.content, HttpContent):
            content = self.content.to_dict()
        else:
            content = self.content

        method: dict[str, Any] | None | Unset
        if isinstance(self.method, Unset):
            method = UNSET
        elif isinstance(self.method, HttpMethod):
            method = self.method.to_dict()
        else:
            method = self.method

        request_uri: None | str | Unset
        if isinstance(self.request_uri, Unset):
            request_uri = UNSET
        else:
            request_uri = self.request_uri

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

        properties: dict[str, Any] | None | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif isinstance(self.properties, HttpRequestMessagePropertiesType0):
            properties = self.properties.to_dict()
        else:
            properties = self.properties

        options: dict[str, Any] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, HttpRequestMessageOptionsType0):
            options = self.options.to_dict()
        else:
            options = self.options

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if version_policy is not UNSET:
            field_dict["versionPolicy"] = version_policy
        if content is not UNSET:
            field_dict["content"] = content
        if method is not UNSET:
            field_dict["method"] = method
        if request_uri is not UNSET:
            field_dict["requestUri"] = request_uri
        if headers is not UNSET:
            field_dict["headers"] = headers
        if properties is not UNSET:
            field_dict["properties"] = properties
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.http_content import HttpContent
        from ..models.http_method import HttpMethod
        from ..models.http_request_message_options_type_0 import HttpRequestMessageOptionsType0
        from ..models.http_request_message_properties_type_0 import HttpRequestMessagePropertiesType0
        from ..models.string_string_i_enumerable_key_value_pair import StringStringIEnumerableKeyValuePair

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        _version_policy = d.pop("versionPolicy", UNSET)
        version_policy: HttpVersionPolicy | Unset
        if isinstance(_version_policy, Unset):
            version_policy = UNSET
        else:
            version_policy = HttpVersionPolicy(_version_policy)

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

        def _parse_method(data: object) -> HttpMethod | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                method_type_1 = HttpMethod.from_dict(data)

                return method_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HttpMethod | None | Unset, data)

        method = _parse_method(d.pop("method", UNSET))

        def _parse_request_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        request_uri = _parse_request_uri(d.pop("requestUri", UNSET))

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

        def _parse_properties(data: object) -> HttpRequestMessagePropertiesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = HttpRequestMessagePropertiesType0.from_dict(data)

                return properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HttpRequestMessagePropertiesType0 | None | Unset, data)

        properties = _parse_properties(d.pop("properties", UNSET))

        def _parse_options(data: object) -> HttpRequestMessageOptionsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                options_type_0 = HttpRequestMessageOptionsType0.from_dict(data)

                return options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HttpRequestMessageOptionsType0 | None | Unset, data)

        options = _parse_options(d.pop("options", UNSET))

        http_request_message = cls(
            version=version,
            version_policy=version_policy,
            content=content,
            method=method,
            request_uri=request_uri,
            headers=headers,
            properties=properties,
            options=options,
        )

        return http_request_message
