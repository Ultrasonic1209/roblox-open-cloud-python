from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_models_request_bundle_create_bundle_request_bundle_type import (
    RobloxItemConfigurationApiModelsRequestBundleCreateBundleRequestBundleType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsRequestBundleCreateBundleRequest")


@_attrs_define
class RobloxItemConfigurationApiModelsRequestBundleCreateBundleRequest:
    """DTO of incoming request from the client to create a bundle.

    Attributes:
        bundle_type (RobloxItemConfigurationApiModelsRequestBundleCreateBundleRequestBundleType | Unset): The bundle
            type target for the bundle creation. ['Unknown' = 0, 'Body' = 1, 'DynamicHead' = 2, 'Shoes' = 3,
            'AvatarAnimations' = 4]
        name (str | Unset): Name of the bundle to be created.
        description (str | Unset): Description of the bundle.
        asset_ids (list[int] | Unset): List of asset ids which are to be part of this bundle.
            These asset ids must include only the allowed asset types for the particular
            bundle type that is being created.
        operation_id (str | Unset): Operation ID of the original intent that was created to start bundle creation.
        agreed_creation_fee (int | Unset): Fee in Robux to create bundle.
            It needs to be the same as the actual price on the upload fee product entity.
            Otherwise, the bundle will fail to be created.
    """

    bundle_type: RobloxItemConfigurationApiModelsRequestBundleCreateBundleRequestBundleType | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    asset_ids: list[int] | Unset = UNSET
    operation_id: str | Unset = UNSET
    agreed_creation_fee: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        bundle_type: str | Unset = UNSET
        if not isinstance(self.bundle_type, Unset):
            bundle_type = self.bundle_type.value

        name = self.name

        description = self.description

        asset_ids: list[int] | Unset = UNSET
        if not isinstance(self.asset_ids, Unset):
            asset_ids = self.asset_ids

        operation_id = self.operation_id

        agreed_creation_fee = self.agreed_creation_fee

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if bundle_type is not UNSET:
            field_dict["bundleType"] = bundle_type
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if asset_ids is not UNSET:
            field_dict["assetIds"] = asset_ids
        if operation_id is not UNSET:
            field_dict["operationId"] = operation_id
        if agreed_creation_fee is not UNSET:
            field_dict["agreedCreationFee"] = agreed_creation_fee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _bundle_type = d.pop("bundleType", UNSET)
        bundle_type: RobloxItemConfigurationApiModelsRequestBundleCreateBundleRequestBundleType | Unset
        if isinstance(_bundle_type, Unset):
            bundle_type = UNSET
        else:
            bundle_type = RobloxItemConfigurationApiModelsRequestBundleCreateBundleRequestBundleType(_bundle_type)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        asset_ids = cast(list[int], d.pop("assetIds", UNSET))

        operation_id = d.pop("operationId", UNSET)

        agreed_creation_fee = d.pop("agreedCreationFee", UNSET)

        roblox_item_configuration_api_models_request_bundle_create_bundle_request = cls(
            bundle_type=bundle_type,
            name=name,
            description=description,
            asset_ids=asset_ids,
            operation_id=operation_id,
            agreed_creation_fee=agreed_creation_fee,
        )

        return roblox_item_configuration_api_models_request_bundle_create_bundle_request
