from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_models_request_bundle_create_bundle_context_request_bundle_type import (
    RobloxItemConfigurationApiModelsRequestBundleCreateBundleContextRequestBundleType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_models_bundle_body_color_set import (
        RobloxItemConfigurationApiModelsBundleBodyColorSet,
    )
    from ..models.roblox_item_configuration_api_models_bundle_body_scale import (
        RobloxItemConfigurationApiModelsBundleBodyScale,
    )
    from ..models.roblox_item_configuration_api_models_request_bundle_create_bundle_context_request_asset_quantities import (
        RobloxItemConfigurationApiModelsRequestBundleCreateBundleContextRequestAssetQuantities,
    )


T = TypeVar("T", bound="RobloxItemConfigurationApiModelsRequestBundleCreateBundleContextRequest")


@_attrs_define
class RobloxItemConfigurationApiModelsRequestBundleCreateBundleContextRequest:
    """DTO of incoming request from the client to create bundle context
    which is necessary for bundle creation.

        Attributes:
            asset_quantities (RobloxItemConfigurationApiModelsRequestBundleCreateBundleContextRequestAssetQuantities |
                Unset): The collection of AssetTypes and their corresponding quantities that are
                being requested to be uploaded by the client.
            bundle_description (str | Unset): Description for the particular bundle that is about to be created.
            bundle_name (str | Unset): Name for the particular bundle that is about to be created.
            bundle_type (RobloxItemConfigurationApiModelsRequestBundleCreateBundleContextRequestBundleType | Unset): The
                bundle type target of the specified action. ['Unknown' = 0, 'Body' = 1, 'DynamicHead' = 2, 'Shoes' = 3,
                'AvatarAnimations' = 4]
            body_scale (RobloxItemConfigurationApiModelsBundleBodyScale | Unset): The body scale of the bundle.
            body_color_set (RobloxItemConfigurationApiModelsBundleBodyColorSet | Unset): The body color set of the
                associated Outfit for the body.
            group_id (int | Unset): The group id that the bundle is meant to belong to.
            is_emissive (bool | Unset): Whether the bundle is expected to contain emissive content.
    """

    asset_quantities: RobloxItemConfigurationApiModelsRequestBundleCreateBundleContextRequestAssetQuantities | Unset = (
        UNSET
    )
    bundle_description: str | Unset = UNSET
    bundle_name: str | Unset = UNSET
    bundle_type: RobloxItemConfigurationApiModelsRequestBundleCreateBundleContextRequestBundleType | Unset = UNSET
    body_scale: RobloxItemConfigurationApiModelsBundleBodyScale | Unset = UNSET
    body_color_set: RobloxItemConfigurationApiModelsBundleBodyColorSet | Unset = UNSET
    group_id: int | Unset = UNSET
    is_emissive: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_quantities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.asset_quantities, Unset):
            asset_quantities = self.asset_quantities.to_dict()

        bundle_description = self.bundle_description

        bundle_name = self.bundle_name

        bundle_type: str | Unset = UNSET
        if not isinstance(self.bundle_type, Unset):
            bundle_type = self.bundle_type.value

        body_scale: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body_scale, Unset):
            body_scale = self.body_scale.to_dict()

        body_color_set: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body_color_set, Unset):
            body_color_set = self.body_color_set.to_dict()

        group_id = self.group_id

        is_emissive = self.is_emissive

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset_quantities is not UNSET:
            field_dict["assetQuantities"] = asset_quantities
        if bundle_description is not UNSET:
            field_dict["bundleDescription"] = bundle_description
        if bundle_name is not UNSET:
            field_dict["bundleName"] = bundle_name
        if bundle_type is not UNSET:
            field_dict["bundleType"] = bundle_type
        if body_scale is not UNSET:
            field_dict["bodyScale"] = body_scale
        if body_color_set is not UNSET:
            field_dict["bodyColorSet"] = body_color_set
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if is_emissive is not UNSET:
            field_dict["isEmissive"] = is_emissive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_models_bundle_body_color_set import (
            RobloxItemConfigurationApiModelsBundleBodyColorSet,  # noqa: PLC0415
        )
        from ..models.roblox_item_configuration_api_models_bundle_body_scale import (
            RobloxItemConfigurationApiModelsBundleBodyScale,  # noqa: PLC0415
        )
        from ..models.roblox_item_configuration_api_models_request_bundle_create_bundle_context_request_asset_quantities import (
            RobloxItemConfigurationApiModelsRequestBundleCreateBundleContextRequestAssetQuantities,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _asset_quantities = d.pop("assetQuantities", UNSET)
        asset_quantities: RobloxItemConfigurationApiModelsRequestBundleCreateBundleContextRequestAssetQuantities | Unset
        if isinstance(_asset_quantities, Unset):
            asset_quantities = UNSET
        else:
            asset_quantities = (
                RobloxItemConfigurationApiModelsRequestBundleCreateBundleContextRequestAssetQuantities.from_dict(
                    _asset_quantities
                )
            )

        bundle_description = d.pop("bundleDescription", UNSET)

        bundle_name = d.pop("bundleName", UNSET)

        _bundle_type = d.pop("bundleType", UNSET)
        bundle_type: RobloxItemConfigurationApiModelsRequestBundleCreateBundleContextRequestBundleType | Unset
        if isinstance(_bundle_type, Unset):
            bundle_type = UNSET
        else:
            bundle_type = RobloxItemConfigurationApiModelsRequestBundleCreateBundleContextRequestBundleType(
                _bundle_type
            )

        _body_scale = d.pop("bodyScale", UNSET)
        body_scale: RobloxItemConfigurationApiModelsBundleBodyScale | Unset
        if isinstance(_body_scale, Unset):
            body_scale = UNSET
        else:
            body_scale = RobloxItemConfigurationApiModelsBundleBodyScale.from_dict(_body_scale)

        _body_color_set = d.pop("bodyColorSet", UNSET)
        body_color_set: RobloxItemConfigurationApiModelsBundleBodyColorSet | Unset
        if isinstance(_body_color_set, Unset):
            body_color_set = UNSET
        else:
            body_color_set = RobloxItemConfigurationApiModelsBundleBodyColorSet.from_dict(_body_color_set)

        group_id = d.pop("groupId", UNSET)

        is_emissive = d.pop("isEmissive", UNSET)

        roblox_item_configuration_api_models_request_bundle_create_bundle_context_request = cls(
            asset_quantities=asset_quantities,
            bundle_description=bundle_description,
            bundle_name=bundle_name,
            bundle_type=bundle_type,
            body_scale=body_scale,
            body_color_set=body_color_set,
            group_id=group_id,
            is_emissive=is_emissive,
        )

        return roblox_item_configuration_api_models_request_bundle_create_bundle_context_request
