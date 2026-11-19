from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.asset_privacy import AssetPrivacy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assets_upload_api_creator import AssetsUploadApiCreator


T = TypeVar("T", bound="CreationContext")


@_attrs_define
class CreationContext:
    """The context of creation that is not part of the asset content, such as metadata and creator information. Required
    for [Create Asset](#Assets_CreateAsset).

        Attributes:
            creator (AssetsUploadApiCreator | Unset): Represents a creator. Only one creator ID is set, according to the
                creator type.
            expected_price (int | Unset): Expected asset upload fee in Robux. When the actual price is more than expected,
                the operation fails with a 400 error.
            creating_universe_id (int | None | Unset):
            asset_privacy (AssetPrivacy | Unset): The privacy setting of the asset. Requested asset privacy is only
                applicable to asset types that allow privacy override. For more details see [Asset
                Privacy](/projects/assets/privacy.md).
    """

    creator: AssetsUploadApiCreator | Unset = UNSET
    expected_price: int | Unset = UNSET
    creating_universe_id: int | None | Unset = UNSET
    asset_privacy: AssetPrivacy | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        expected_price = self.expected_price

        creating_universe_id: int | None | Unset
        if isinstance(self.creating_universe_id, Unset):
            creating_universe_id = UNSET
        else:
            creating_universe_id = self.creating_universe_id

        asset_privacy: str | Unset = UNSET
        if not isinstance(self.asset_privacy, Unset):
            asset_privacy = self.asset_privacy.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if creator is not UNSET:
            field_dict["creator"] = creator
        if expected_price is not UNSET:
            field_dict["expectedPrice"] = expected_price
        if creating_universe_id is not UNSET:
            field_dict["creatingUniverseId"] = creating_universe_id
        if asset_privacy is not UNSET:
            field_dict["assetPrivacy"] = asset_privacy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assets_upload_api_creator import AssetsUploadApiCreator  # noqa: PLC0415

        d = dict(src_dict)
        _creator = d.pop("creator", UNSET)
        creator: AssetsUploadApiCreator | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = AssetsUploadApiCreator.from_dict(_creator)

        expected_price = d.pop("expectedPrice", UNSET)

        def _parse_creating_universe_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        creating_universe_id = _parse_creating_universe_id(d.pop("creatingUniverseId", UNSET))

        _asset_privacy = d.pop("assetPrivacy", UNSET)
        asset_privacy: AssetPrivacy | Unset
        if isinstance(_asset_privacy, Unset):
            asset_privacy = UNSET
        else:
            asset_privacy = AssetPrivacy(_asset_privacy)

        creation_context = cls(
            creator=creator,
            expected_price=expected_price,
            creating_universe_id=creating_universe_id,
            asset_privacy=asset_privacy,
        )

        return creation_context
