from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_type_0 import AssetType0
    from ..models.creator_model_v2_type_0 import CreatorModelV2Type0
    from ..models.creator_store_product_type_0 import CreatorStoreProductType0
    from ..models.voting_model_type_0 import VotingModelType0


T = TypeVar("T", bound="CreatorStoreAssetType0")


@_attrs_define
class CreatorStoreAssetType0:
    """Representation of a creator store asset.

    Attributes:
        asset (AssetType0 | None): The asset information.
        voting (None | Unset | VotingModelType0): The asset's voting details.
        creator (CreatorModelV2Type0 | None | Unset): The asset creator's details.
        creator_store_product (CreatorStoreProductType0 | None | Unset): The asset's product details.
    """

    asset: AssetType0 | None
    voting: None | Unset | VotingModelType0 = UNSET
    creator: CreatorModelV2Type0 | None | Unset = UNSET
    creator_store_product: CreatorStoreProductType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.asset_type_0 import AssetType0  # noqa: PLC0415
        from ..models.creator_model_v2_type_0 import CreatorModelV2Type0  # noqa: PLC0415
        from ..models.creator_store_product_type_0 import CreatorStoreProductType0  # noqa: PLC0415
        from ..models.voting_model_type_0 import VotingModelType0  # noqa: PLC0415

        asset: dict[str, Any] | None
        if isinstance(self.asset, AssetType0):
            asset = self.asset.to_dict()
        else:
            asset = self.asset

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
        elif isinstance(self.creator_store_product, CreatorStoreProductType0):
            creator_store_product = self.creator_store_product.to_dict()
        else:
            creator_store_product = self.creator_store_product

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "asset": asset,
            }
        )
        if voting is not UNSET:
            field_dict["voting"] = voting
        if creator is not UNSET:
            field_dict["creator"] = creator
        if creator_store_product is not UNSET:
            field_dict["creatorStoreProduct"] = creator_store_product

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_type_0 import AssetType0  # noqa: PLC0415
        from ..models.creator_model_v2_type_0 import CreatorModelV2Type0  # noqa: PLC0415
        from ..models.creator_store_product_type_0 import CreatorStoreProductType0  # noqa: PLC0415
        from ..models.voting_model_type_0 import VotingModelType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_asset(data: object) -> AssetType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_asset_type_0 = AssetType0.from_dict(data)

                return componentsschemas_asset_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AssetType0 | None, data)

        asset = _parse_asset(d.pop("asset"))

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

        def _parse_creator_store_product(data: object) -> CreatorStoreProductType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_creator_store_product_type_0 = CreatorStoreProductType0.from_dict(data)

                return componentsschemas_creator_store_product_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreatorStoreProductType0 | None | Unset, data)

        creator_store_product = _parse_creator_store_product(d.pop("creatorStoreProduct", UNSET))

        creator_store_asset_type_0 = cls(
            asset=asset,
            voting=voting,
            creator=creator,
            creator_store_product=creator_store_product,
        )

        return creator_store_asset_type_0
