from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assets_upload_api_asset import AssetsUploadApiAsset
    from ..models.file import File
    from ..models.multipart_upload_start_request_additional_parameters_type_0 import (
        MultipartUploadStartRequestAdditionalParametersType0,
    )


T = TypeVar("T", bound="MultipartUploadStartRequest")


@_attrs_define
class MultipartUploadStartRequest:
    """Request of Roblox.AssetsManagement.AssetsUploadApi.MultipartUploadStartOperation

    Attributes:
        asset (AssetsUploadApiAsset | Unset): Represents an asset.
        file (File | Unset): A file to be uploaded
        additional_parameters (MultipartUploadStartRequestAdditionalParametersType0 | None | Unset): Optional:
            Additional parameters to be sent with the request can be included here.
    """

    asset: AssetsUploadApiAsset | Unset = UNSET
    file: File | Unset = UNSET
    additional_parameters: MultipartUploadStartRequestAdditionalParametersType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.multipart_upload_start_request_additional_parameters_type_0 import (
            MultipartUploadStartRequestAdditionalParametersType0,  # noqa: PLC0415
        )

        asset: dict[str, Any] | Unset = UNSET
        if not isinstance(self.asset, Unset):
            asset = self.asset.to_dict()

        file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        additional_parameters: dict[str, Any] | None | Unset
        if isinstance(self.additional_parameters, Unset):
            additional_parameters = UNSET
        elif isinstance(self.additional_parameters, MultipartUploadStartRequestAdditionalParametersType0):
            additional_parameters = self.additional_parameters.to_dict()
        else:
            additional_parameters = self.additional_parameters

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset is not UNSET:
            field_dict["asset"] = asset
        if file is not UNSET:
            field_dict["file"] = file
        if additional_parameters is not UNSET:
            field_dict["additionalParameters"] = additional_parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assets_upload_api_asset import AssetsUploadApiAsset  # noqa: PLC0415
        from ..models.file import File  # noqa: PLC0415
        from ..models.multipart_upload_start_request_additional_parameters_type_0 import (
            MultipartUploadStartRequestAdditionalParametersType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _asset = d.pop("asset", UNSET)
        asset: AssetsUploadApiAsset | Unset
        if isinstance(_asset, Unset):
            asset = UNSET
        else:
            asset = AssetsUploadApiAsset.from_dict(_asset)

        _file = d.pop("file", UNSET)
        file: File | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = File.from_dict(_file)

        def _parse_additional_parameters(
            data: object,
        ) -> MultipartUploadStartRequestAdditionalParametersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                additional_parameters_type_0 = MultipartUploadStartRequestAdditionalParametersType0.from_dict(data)

                return additional_parameters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MultipartUploadStartRequestAdditionalParametersType0 | None | Unset, data)

        additional_parameters = _parse_additional_parameters(d.pop("additionalParameters", UNSET))

        multipart_upload_start_request = cls(
            asset=asset,
            file=file,
            additional_parameters=additional_parameters,
        )

        return multipart_upload_start_request
