from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultipartUploadChunkCompleteRequest")


@_attrs_define
class MultipartUploadChunkCompleteRequest:
    """Request of Roblox.AssetsManagement.AssetsUploadApi.MultipartUploadChunkCompleteOperation

    Attributes:
        chunk_num (int | Unset): The number of this Chunk.
        e_tag (None | str | Unset): ETag of this chunk.
    """

    chunk_num: int | Unset = UNSET
    e_tag: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        chunk_num = self.chunk_num

        e_tag: None | str | Unset
        if isinstance(self.e_tag, Unset):
            e_tag = UNSET
        else:
            e_tag = self.e_tag

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if chunk_num is not UNSET:
            field_dict["chunkNum"] = chunk_num
        if e_tag is not UNSET:
            field_dict["eTag"] = e_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chunk_num = d.pop("chunkNum", UNSET)

        def _parse_e_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        e_tag = _parse_e_tag(d.pop("eTag", UNSET))

        multipart_upload_chunk_complete_request = cls(
            chunk_num=chunk_num,
            e_tag=e_tag,
        )

        return multipart_upload_chunk_complete_request
