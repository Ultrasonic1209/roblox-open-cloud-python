from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_catalog_api_collectible_license_license_type import RobloxCatalogApiCollectibleLicenseLicenseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxCatalogApiCollectibleLicense")


@_attrs_define
class RobloxCatalogApiCollectibleLicense:
    """A model representing the license attached to a collectible, linked via the collectibleItemId.

    Attributes:
        id (str | Unset):
        license_type (RobloxCatalogApiCollectibleLicenseLicenseType | Unset): The type of license attached to a
            collectible. ['Invalid' = 0, 'ThirdParty' = 1, 'FirstParty' = 2]
    """

    id: str | Unset = UNSET
    license_type: RobloxCatalogApiCollectibleLicenseLicenseType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        license_type: int | Unset = UNSET
        if not isinstance(self.license_type, Unset):
            license_type = self.license_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if license_type is not UNSET:
            field_dict["licenseType"] = license_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        _license_type = d.pop("licenseType", UNSET)
        license_type: RobloxCatalogApiCollectibleLicenseLicenseType | Unset
        if isinstance(_license_type, Unset):
            license_type = UNSET
        else:
            license_type = RobloxCatalogApiCollectibleLicenseLicenseType(_license_type)

        roblox_catalog_api_collectible_license = cls(
            id=id,
            license_type=license_type,
        )

        return roblox_catalog_api_collectible_license
