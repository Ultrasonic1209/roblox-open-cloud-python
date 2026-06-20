from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.creator_model_v2_type_0 import CreatorModelV2Type0
    from ..models.toolbox_service_asset_type_0 import ToolboxServiceAssetType0
    from ..models.toolbox_service_creator_store_product_type_0 import ToolboxServiceCreatorStoreProductType0
    from ..models.voting_model_type_0 import VotingModelType0


T = TypeVar("T", bound="CreatorStoreAssetType0")


@_attrs_define
class CreatorStoreAssetType0:
    """Representation of a creator store asset.

    Attributes:
        voting (None | Unset | VotingModelType0): The asset's voting details.
        creator (CreatorModelV2Type0 | None | Unset): The asset creator's details.
        creator_store_product (None | ToolboxServiceCreatorStoreProductType0 | Unset): The asset's product details.
        asset (None | ToolboxServiceAssetType0 | Unset): The asset information.
    """

    voting: None | Unset | VotingModelType0 = UNSET
    creator: CreatorModelV2Type0 | None | Unset = UNSET
    creator_store_product: None | ToolboxServiceCreatorStoreProductType0 | Unset = UNSET
    asset: None | ToolboxServiceAssetType0 | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.creator_model_v2_type_0 import CreatorModelV2Type0
        from ..models.toolbox_service_asset_type_0 import ToolboxServiceAssetType0
        from ..models.toolbox_service_creator_store_product_type_0 import ToolboxServiceCreatorStoreProductType0
        from ..models.voting_model_type_0 import VotingModelType0

        voting: dict[str, Any] | None | Unset
        if isinstance(self.voting, Unset):
            voting = UNSET
        elif isinstance(self.voting, VotingModelType0):
            voting = self.voting.to_dict()
        else:
            voting = self.voting

        creator: dict[str, Any] | None | Unset
        if isinstance(self.creator, Unset):
            creator = UNSET
        elif isinstance(self.creator, CreatorModelV2Type0):
            creator = self.creator.to_dict()
        else:
            creator = self.creator

        creator_store_product: dict[str, Any] | None | Unset
        if isinstance(self.creator_store_product, Unset):
            creator_store_product = UNSET
        elif isinstance(self.creator_store_product, ToolboxServiceCreatorStoreProductType0):
            creator_store_product = self.creator_store_product.to_dict()
        else:
            creator_store_product = self.creator_store_product

        asset: dict[str, Any] | None | Unset
        if isinstance(self.asset, Unset):
            asset = UNSET
        elif isinstance(self.asset, ToolboxServiceAssetType0):
            asset = self.asset.to_dict()
        else:
            asset = self.asset

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if voting is not UNSET:
            field_dict["voting"] = voting
        if creator is not UNSET:
            field_dict["creator"] = creator
        if creator_store_product is not UNSET:
            field_dict["creatorStoreProduct"] = creator_store_product
        if asset is not UNSET:
            field_dict["asset"] = asset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.creator_model_v2_type_0 import CreatorModelV2Type0
        from ..models.toolbox_service_asset_type_0 import ToolboxServiceAssetType0
        from ..models.toolbox_service_creator_store_product_type_0 import ToolboxServiceCreatorStoreProductType0
        from ..models.voting_model_type_0 import VotingModelType0

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_voting(data: object) -> None | Unset | VotingModelType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_voting_model_type_0 = VotingModelType0.from_dict(data)

                return componentsschemas_voting_model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VotingModelType0, data)

        voting = _parse_voting(d.pop("voting", UNSET))

        def _parse_creator(data: object) -> CreatorModelV2Type0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_creator_model_v2_type_0 = CreatorModelV2Type0.from_dict(data)

                return componentsschemas_creator_model_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreatorModelV2Type0 | None | Unset, data)

        creator = _parse_creator(d.pop("creator", UNSET))

        def _parse_creator_store_product(data: object) -> None | ToolboxServiceCreatorStoreProductType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_toolbox_service_creator_store_product_type_0 = (
                    ToolboxServiceCreatorStoreProductType0.from_dict(data)
                )

                return componentsschemas_toolbox_service_creator_store_product_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ToolboxServiceCreatorStoreProductType0 | Unset, data)

        creator_store_product = _parse_creator_store_product(d.pop("creatorStoreProduct", UNSET))

        def _parse_asset(data: object) -> None | ToolboxServiceAssetType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_toolbox_service_asset_type_0 = ToolboxServiceAssetType0.from_dict(data)

                return componentsschemas_toolbox_service_asset_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ToolboxServiceAssetType0 | Unset, data)

        asset = _parse_asset(d.pop("asset", UNSET))

        creator_store_asset_type_0 = cls(
            voting=voting,
            creator=creator,
            creator_store_product=creator_store_product,
            asset=asset,
        )

        return creator_store_asset_type_0
