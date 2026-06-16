from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset import Asset
    from ..models.ocv1_assets_status import OCV1AssetsStatus


T = TypeVar("T", bound="OCV1AssetsOperation")


@_attrs_define
class OCV1AssetsOperation:
    """This resource represents a long-running operation that is the result of a network API call.

    Attributes:
        path (str | Unset): The server-assigned resource path. The default format is `operations/{operation_id}`.
        done (bool | Unset): If `false`, the operation is still in progress. If `true`, the operation is completed.
        error (OCV1AssetsStatus | Unset): The logical error model explaining the error status.
        response (Asset | Unset): Represents an asset.
    """

    path: str | Unset = UNSET
    done: bool | Unset = UNSET
    error: OCV1AssetsStatus | Unset = UNSET
    response: Asset | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        done = self.done

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response, Unset):
            response = self.response.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        from ..models.asset import Asset
        from ..models.ocv1_assets_status import OCV1AssetsStatus

        d = dict(src_dict)
        path = d.pop("path", UNSET)

        done = d.pop("done", UNSET)

        _error = d.pop("error", UNSET)
        error: OCV1AssetsStatus | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = OCV1AssetsStatus.from_dict(_error)

        _response = d.pop("response", UNSET)
        response: Asset | Unset
        if isinstance(_response, Unset):
            response = UNSET
        else:
            response = Asset.from_dict(_response)

        ocv1_assets_operation = cls(
            path=path,
            done=done,
            error=error,
            response=response,
        )

        ocv1_assets_operation.additional_properties = d
        return ocv1_assets_operation

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
