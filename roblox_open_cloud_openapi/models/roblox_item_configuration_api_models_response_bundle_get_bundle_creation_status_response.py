from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_models_response_bundle_get_bundle_creation_status_response_status import (
    RobloxItemConfigurationApiModelsResponseBundleGetBundleCreationStatusResponseStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsResponseBundleGetBundleCreationStatusResponse")


@_attrs_define
class RobloxItemConfigurationApiModelsResponseBundleGetBundleCreationStatusResponse:
    """DTO response containing create bundle status.

    Attributes:
        bundle_id (int | Unset): Bundle ID associated with the creation request if it had a successful status.
        status (RobloxItemConfigurationApiModelsResponseBundleGetBundleCreationStatusResponseStatus | Unset): Current
            status for the given creationStatusId. ['Unknown' = 0, 'InProgress' = 1, 'Success' = 2, 'ValidationFailed' = 3,
            'InsufficientFunds' = 4, 'Failed' = 5, 'CreationFeeMismatch' = 6, 'MetadataMismatch' = 7]
    """

    bundle_id: int | Unset = UNSET
    status: RobloxItemConfigurationApiModelsResponseBundleGetBundleCreationStatusResponseStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        bundle_id = self.bundle_id

        status: int | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if bundle_id is not UNSET:
            field_dict["bundleId"] = bundle_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bundle_id = d.pop("bundleId", UNSET)

        _status = d.pop("status", UNSET)
        status: RobloxItemConfigurationApiModelsResponseBundleGetBundleCreationStatusResponseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RobloxItemConfigurationApiModelsResponseBundleGetBundleCreationStatusResponseStatus(_status)

        roblox_item_configuration_api_models_response_bundle_get_bundle_creation_status_response = cls(
            bundle_id=bundle_id,
            status=status,
        )

        return roblox_item_configuration_api_models_response_bundle_get_bundle_creation_status_response
