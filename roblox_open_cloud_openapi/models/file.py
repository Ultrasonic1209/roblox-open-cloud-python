from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="File")


@_attrs_define
class File:
    """A file to be uploaded

    Attributes:
        content_type (None | str | Unset): MIME type of the file content.
        filesize (int | Unset): Size of the file.
        md_5_checksum (None | str | Unset): MD5 checksum of the file.
        chunk_plan (list[int] | None | Unset): A list of chunk lengths.
    """

    content_type: None | str | Unset = UNSET
    filesize: int | Unset = UNSET
    md_5_checksum: None | str | Unset = UNSET
    chunk_plan: list[int] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        content_type: None | str | Unset
        if isinstance(self.content_type, Unset):
            content_type = UNSET
        else:
            content_type = self.content_type

        filesize = self.filesize

        md_5_checksum: None | str | Unset
        if isinstance(self.md_5_checksum, Unset):
            md_5_checksum = UNSET
        else:
            md_5_checksum = self.md_5_checksum

        chunk_plan: list[int] | None | Unset
        if isinstance(self.chunk_plan, Unset):
            chunk_plan = UNSET
        elif isinstance(self.chunk_plan, list):
            chunk_plan = self.chunk_plan

        else:
            chunk_plan = self.chunk_plan

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if filesize is not UNSET:
            field_dict["filesize"] = filesize
        if md_5_checksum is not UNSET:
            field_dict["md5Checksum"] = md_5_checksum
        if chunk_plan is not UNSET:
            field_dict["chunkPlan"] = chunk_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_content_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_type = _parse_content_type(d.pop("contentType", UNSET))

        filesize = d.pop("filesize", UNSET)

        def _parse_md_5_checksum(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        md_5_checksum = _parse_md_5_checksum(d.pop("md5Checksum", UNSET))

        def _parse_chunk_plan(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                chunk_plan_type_0 = cast(list[int], data)

                return chunk_plan_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        chunk_plan = _parse_chunk_plan(d.pop("chunkPlan", UNSET))

        file = cls(
            content_type=content_type,
            filesize=filesize,
            md_5_checksum=md_5_checksum,
            chunk_plan=chunk_plan,
        )

        return file
