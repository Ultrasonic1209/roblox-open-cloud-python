from __future__ import annotations

import json
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import File

if TYPE_CHECKING:
    from ..models.asset import Asset


T = TypeVar("T", bound="AssetsCreateAssetBody")


@_attrs_define
class AssetsCreateAssetBody:
    """
    Attributes:
        request (Asset): Represents an asset.
        file_content (File): The binary asset file path and the content type. See [Asset types and
            limits](/cloud/guides/usage-assets.md#supported-asset-types-and-limits).
    """

    request: Asset
    file_content: File
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request = self.request.to_dict()

        file_content = self.file_content.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "request": request,
                "fileContent": file_content,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("request", (None, json.dumps(self.request.to_dict()).encode(), "application/json")))

        files.append(("fileContent", self.file_content.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset import Asset

        d = dict(src_dict)
        request = Asset.from_dict(d.pop("request"))

        file_content = File(payload=BytesIO(d.pop("fileContent")))

        assets_create_asset_body = cls(
            request=request,
            file_content=file_content,
        )

        assets_create_asset_body.additional_properties = d
        return assets_create_asset_body

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
