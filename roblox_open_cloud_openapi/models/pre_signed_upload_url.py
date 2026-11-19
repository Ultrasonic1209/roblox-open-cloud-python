from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PreSignedUploadUrl")


@_attrs_define
class PreSignedUploadUrl:
    """A pre-signed upload URL which allows anyone with this URL to upload a file with limited HTTP method and file size.

    Example curl command to upload with a pre-signed PUT url:
    curl -v {pre-signed url} -T {filepath}

        Attributes:
            http_verb (None | str | Unset): HTTP Verb to use with the given url.
            url (None | str | Unset): Pre signed url used to upload.
            expiration_time_ms (str | Unset): Expiration of pre signed url.
            chunk_num (str | Unset): Num of file chunk to upload corresponding to the ChunkPlan in the start request.
            content_start (str | Unset): Start position of this chunk.
            content_length (str | Unset): Length of this chunk.
    """

    http_verb: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    expiration_time_ms: str | Unset = UNSET
    chunk_num: str | Unset = UNSET
    content_start: str | Unset = UNSET
    content_length: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        http_verb: None | str | Unset
        if isinstance(self.http_verb, Unset):
            http_verb = UNSET
        else:
            http_verb = self.http_verb

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        expiration_time_ms = self.expiration_time_ms

        chunk_num = self.chunk_num

        content_start = self.content_start

        content_length = self.content_length

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if http_verb is not UNSET:
            field_dict["httpVerb"] = http_verb
        if url is not UNSET:
            field_dict["url"] = url
        if expiration_time_ms is not UNSET:
            field_dict["expirationTimeMs"] = expiration_time_ms
        if chunk_num is not UNSET:
            field_dict["chunkNum"] = chunk_num
        if content_start is not UNSET:
            field_dict["contentStart"] = content_start
        if content_length is not UNSET:
            field_dict["contentLength"] = content_length

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_http_verb(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        http_verb = _parse_http_verb(d.pop("httpVerb", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        expiration_time_ms = d.pop("expirationTimeMs", UNSET)

        chunk_num = d.pop("chunkNum", UNSET)

        content_start = d.pop("contentStart", UNSET)

        content_length = d.pop("contentLength", UNSET)

        pre_signed_upload_url = cls(
            http_verb=http_verb,
            url=url,
            expiration_time_ms=expiration_time_ms,
            chunk_num=chunk_num,
            content_start=content_start,
            content_length=content_length,
        )

        return pre_signed_upload_url
