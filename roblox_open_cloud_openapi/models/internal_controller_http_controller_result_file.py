from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalControllerHttpControllerResultFile")


@_attrs_define
class InternalControllerHttpControllerResultFile:
    """
    Attributes:
        download_url (str | Unset): DownloadURL is the time-limited presigned link to this file. Example: https://rbx-
            vlop-dsa-research-results-test.s3.amazonaws.com/research/query/3f6b1c2e/part-0.csv.gz?X-Amz-Signature=....
        name (str | Unset): Name is the object's file name under the job's result prefix. Example: part-0.csv.gz.
    """

    download_url: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        download_url = self.download_url

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if download_url is not UNSET:
            field_dict["download_url"] = download_url
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        download_url = d.pop("download_url", UNSET)

        name = d.pop("name", UNSET)

        internal_controller_http_controller_result_file = cls(
            download_url=download_url,
            name=name,
        )

        internal_controller_http_controller_result_file.additional_properties = d
        return internal_controller_http_controller_result_file

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
