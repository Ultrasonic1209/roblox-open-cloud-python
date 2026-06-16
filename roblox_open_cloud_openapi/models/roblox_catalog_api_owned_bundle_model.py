from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_catalog_api_bundle_creator_model import RobloxCatalogApiBundleCreatorModel


T = TypeVar("T", bound="RobloxCatalogApiOwnedBundleModel")


@_attrs_define
class RobloxCatalogApiOwnedBundleModel:
    """A model to represent owned bundles.

    Attributes:
        id (int | Unset):
        name (str | Unset):
        bundle_type (str | Unset):
        creator (RobloxCatalogApiBundleCreatorModel | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    bundle_type: str | Unset = UNSET
    creator: RobloxCatalogApiBundleCreatorModel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        bundle_type = self.bundle_type

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if bundle_type is not UNSET:
            field_dict["bundleType"] = bundle_type
        if creator is not UNSET:
            field_dict["creator"] = creator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_catalog_api_bundle_creator_model import RobloxCatalogApiBundleCreatorModel

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        bundle_type = d.pop("bundleType", UNSET)

        _creator = d.pop("creator", UNSET)
        creator: RobloxCatalogApiBundleCreatorModel | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = RobloxCatalogApiBundleCreatorModel.from_dict(_creator)

        roblox_catalog_api_owned_bundle_model = cls(
            id=id,
            name=name,
            bundle_type=bundle_type,
            creator=creator,
        )

        return roblox_catalog_api_owned_bundle_model
