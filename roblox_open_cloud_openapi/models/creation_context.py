from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.asset_privacy import AssetPrivacy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.creator import Creator


T = TypeVar("T", bound="CreationContext")


@_attrs_define
class CreationContext:
    """The context of creation that is not part of the asset content, such as metadata and creator information. Required
    for [Create Asset](#POST-v1-assets).

        Attributes:
            asset_privacy (AssetPrivacy | Unset): The privacy setting of the asset. Requested asset privacy is only
                applicable to asset types that allow privacy override. For more details see [Asset
                Privacy](/projects/assets/privacy.md).
            creator (Creator | Unset): Represents a creator.
            expected_price (int | Unset): Expected asset upload fee in Robux. When the actual price is more than expected,
                the operation fails with a 400 error.
    """

    asset_privacy: AssetPrivacy | Unset = UNSET
    creator: Creator | Unset = UNSET
    expected_price: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_privacy: str | Unset = UNSET
        if not isinstance(self.asset_privacy, Unset):
            asset_privacy = self.asset_privacy.value

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        expected_price = self.expected_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_privacy is not UNSET:
            field_dict["assetPrivacy"] = asset_privacy
        if creator is not UNSET:
            field_dict["creator"] = creator
        if expected_price is not UNSET:
            field_dict["expectedPrice"] = expected_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.creator import Creator

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _asset_privacy = d.pop("assetPrivacy", UNSET)
        asset_privacy: AssetPrivacy | Unset
        if isinstance(_asset_privacy, Unset):
            asset_privacy = UNSET
        else:
            asset_privacy = AssetPrivacy(_asset_privacy)

        _creator = d.pop("creator", UNSET)
        creator: Creator | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = Creator.from_dict(_creator)

        expected_price = d.pop("expectedPrice", UNSET)

        creation_context = cls(
            asset_privacy=asset_privacy,
            creator=creator,
            expected_price=expected_price,
        )

        creation_context.additional_properties = d
        return creation_context

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
