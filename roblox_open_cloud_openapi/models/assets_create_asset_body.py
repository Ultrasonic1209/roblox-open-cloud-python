from __future__ import annotations

import json
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

if TYPE_CHECKING:
    from ..models.assets_create_asset_body_additional_parameters_type_0 import (
        AssetsCreateAssetBodyAdditionalParametersType0,
    )
    from ..models.assets_upload_api_asset import AssetsUploadApiAsset


T = TypeVar("T", bound="AssetsCreateAssetBody")


@_attrs_define
class AssetsCreateAssetBody:
    """
    Attributes:
        file_content (File): The binary asset file path and the content type. See [Asset types and
            limits](/cloud/guides/usage-assets.md#supported-asset-types-and-limits).
        request (AssetsUploadApiAsset): Represents an asset.
        additional_parameters (AssetsCreateAssetBodyAdditionalParametersType0 | None | Unset): Optional: Additional
            parameters to be sent with the request can be included here.
    """

    file_content: File
    request: AssetsUploadApiAsset
    additional_parameters: AssetsCreateAssetBodyAdditionalParametersType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.assets_create_asset_body_additional_parameters_type_0 import (
            AssetsCreateAssetBodyAdditionalParametersType0,  # noqa: PLC0415
        )

        file_content = self.file_content.to_tuple()

        request = self.request.to_dict()

        additional_parameters: dict[str, Any] | None | Unset
        if isinstance(self.additional_parameters, Unset):
            additional_parameters = UNSET
        elif isinstance(self.additional_parameters, AssetsCreateAssetBodyAdditionalParametersType0):
            additional_parameters = self.additional_parameters.to_dict()
        else:
            additional_parameters = self.additional_parameters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fileContent": file_content,
                "request": request,
            }
        )
        if additional_parameters is not UNSET:
            field_dict["additionalParameters"] = additional_parameters

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        from ..models.assets_create_asset_body_additional_parameters_type_0 import (
            AssetsCreateAssetBodyAdditionalParametersType0,  # noqa: PLC0415
        )

        files: types.RequestFiles = []

        files.append(("fileContent", self.file_content.to_tuple()))

        files.append(("request", (None, json.dumps(self.request.to_dict()).encode(), "application/json")))

        if not isinstance(self.additional_parameters, Unset):
            if isinstance(self.additional_parameters, AssetsCreateAssetBodyAdditionalParametersType0):
                files.append(
                    (
                        "additionalParameters",
                        (None, json.dumps(self.additional_parameters.to_dict()).encode(), "application/json"),
                    )
                )
            else:
                files.append(("additionalParameters", (None, str(self.additional_parameters).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assets_create_asset_body_additional_parameters_type_0 import (
            AssetsCreateAssetBodyAdditionalParametersType0,  # noqa: PLC0415
        )
        from ..models.assets_upload_api_asset import AssetsUploadApiAsset  # noqa: PLC0415

        d = dict(src_dict)
        file_content = File(payload=BytesIO(d.pop("fileContent")))

        request = AssetsUploadApiAsset.from_dict(d.pop("request"))

        def _parse_additional_parameters(data: object) -> AssetsCreateAssetBodyAdditionalParametersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                additional_parameters_type_0 = AssetsCreateAssetBodyAdditionalParametersType0.from_dict(data)

                return additional_parameters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AssetsCreateAssetBodyAdditionalParametersType0 | None | Unset, data)

        additional_parameters = _parse_additional_parameters(d.pop("additionalParameters", UNSET))

        assets_create_asset_body = cls(
            file_content=file_content,
            request=request,
            additional_parameters=additional_parameters,
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
