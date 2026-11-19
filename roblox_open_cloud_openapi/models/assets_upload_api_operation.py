from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assets_upload_api_asset import AssetsUploadApiAsset
    from ..models.assets_upload_api_status import AssetsUploadApiStatus


T = TypeVar("T", bound="AssetsUploadApiOperation")


@_attrs_define
class AssetsUploadApiOperation:
    """This resource represents a long-running operation that is the result of a network API call.

    Attributes:
        operation_id (str):
        path (None | str | Unset): The server-assigned resource path. The default format is `operations/{operation_id}`.
            Example: operations/some-operation.
        done (bool | Unset): If `false`, the operation is still in progress. If `true`, the operation is completed.
        error (AssetsUploadApiStatus | Unset): The logical error model explaining the error status.
        response (AssetsUploadApiAsset | Unset): Represents an asset.
    """

    operation_id: str
    path: None | str | Unset = UNSET
    done: bool | Unset = UNSET
    error: AssetsUploadApiStatus | Unset = UNSET
    response: AssetsUploadApiAsset | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        operation_id = self.operation_id

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        done = self.done

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response, Unset):
            response = self.response.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "operationId": operation_id,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path
        if done is not UNSET:
            field_dict["done"] = done
        if error is not UNSET:
            field_dict["error"] = error
        if response is not UNSET:
            field_dict["response"] = response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assets_upload_api_asset import AssetsUploadApiAsset  # noqa: PLC0415
        from ..models.assets_upload_api_status import AssetsUploadApiStatus  # noqa: PLC0415

        d = dict(src_dict)
        operation_id = d.pop("operationId")

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        done = d.pop("done", UNSET)

        _error = d.pop("error", UNSET)
        error: AssetsUploadApiStatus | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = AssetsUploadApiStatus.from_dict(_error)

        _response = d.pop("response", UNSET)
        response: AssetsUploadApiAsset | Unset
        if isinstance(_response, Unset):
            response = UNSET
        else:
            response = AssetsUploadApiAsset.from_dict(_response)

        assets_upload_api_operation = cls(
            operation_id=operation_id,
            path=path,
            done=done,
            error=error,
            response=response,
        )

        return assets_upload_api_operation
