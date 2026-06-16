from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_api_develop_models_universe_settings_request_fiat_product_change_type import (
    RobloxApiDevelopModelsUniverseSettingsRequestFiatProductChangeType,
)
from ..models.roblox_api_develop_models_universe_settings_request_genre import (
    RobloxApiDevelopModelsUniverseSettingsRequestGenre,
)
from ..models.roblox_api_develop_models_universe_settings_request_playable_devices_item import (
    RobloxApiDevelopModelsUniverseSettingsRequestPlayableDevicesItem,
)
from ..models.roblox_api_develop_models_universe_settings_request_universe_animation_type import (
    RobloxApiDevelopModelsUniverseSettingsRequestUniverseAnimationType,
)
from ..models.roblox_api_develop_models_universe_settings_request_universe_avatar_type import (
    RobloxApiDevelopModelsUniverseSettingsRequestUniverseAvatarType,
)
from ..models.roblox_api_develop_models_universe_settings_request_universe_body_type import (
    RobloxApiDevelopModelsUniverseSettingsRequestUniverseBodyType,
)
from ..models.roblox_api_develop_models_universe_settings_request_universe_collision_type import (
    RobloxApiDevelopModelsUniverseSettingsRequestUniverseCollisionType,
)
from ..models.roblox_api_develop_models_universe_settings_request_universe_joint_positioning_type import (
    RobloxApiDevelopModelsUniverseSettingsRequestUniverseJointPositioningType,
)
from ..models.roblox_api_develop_models_universe_settings_request_universe_scale_type import (
    RobloxApiDevelopModelsUniverseSettingsRequestUniverseScaleType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiDevelopModelsUniverseSettingsRequest")


@_attrs_define
class RobloxApiDevelopModelsUniverseSettingsRequest:
    """Model for UniverseSettings patch requests

    Attributes:
        name (str | Unset): The name of the universe.
        universe_avatar_type (RobloxApiDevelopModelsUniverseSettingsRequestUniverseAvatarType | Unset): Which avatar
            types are allowed in the universe.
        universe_scale_type (RobloxApiDevelopModelsUniverseSettingsRequestUniverseScaleType | Unset): Whether custom
            scales allowed in the universe.
        universe_animation_type (RobloxApiDevelopModelsUniverseSettingsRequestUniverseAnimationType | Unset): Whether
            custom animations are allowed in the universe.
        universe_collision_type (RobloxApiDevelopModelsUniverseSettingsRequestUniverseCollisionType | Unset): What type
            of collisions are used by the universe.
        universe_body_type (RobloxApiDevelopModelsUniverseSettingsRequestUniverseBodyType | Unset): What avatar body
            types are allowed by the universe.
        universe_joint_positioning_type (RobloxApiDevelopModelsUniverseSettingsRequestUniverseJointPositioningType |
            Unset): What avatar joint positioning type is allowed by the universe.
        is_archived (bool | Unset): Archive status of the universe.
        is_friends_only (bool | Unset): Whether game access is limited to friends for user-owned games or group members
            for group-owned games.
        genre (RobloxApiDevelopModelsUniverseSettingsRequestGenre | Unset): Game genre.
        playable_devices (list[RobloxApiDevelopModelsUniverseSettingsRequestPlayableDevicesItem] | Unset): List of
            device types this game can be played on.
        is_for_sale (bool | Unset): Whether the game is offered for sale.
        price (int | Unset): Price of the game, in Robux.
        is_mesh_texture_api_access_allowed (bool | Unset): Sets whether access to APIs for mesh and texture is enabled
            for this universe.
        is_rewarded_on_demand_ads_allowed (bool | Unset): Set is rewarded on-demand ads are allowed for this universe.
        fiat_base_price_id (str | Unset): Sets the base price of the experience for Fiat purchases.
        fiat_product_change_type (RobloxApiDevelopModelsUniverseSettingsRequestFiatProductChangeType | Unset):
            Determines the change type of the Fiat Product Change request.
            Can either Activate the product, Update the price, or Deactivate the product.
    """

    name: str | Unset = UNSET
    universe_avatar_type: RobloxApiDevelopModelsUniverseSettingsRequestUniverseAvatarType | Unset = UNSET
    universe_scale_type: RobloxApiDevelopModelsUniverseSettingsRequestUniverseScaleType | Unset = UNSET
    universe_animation_type: RobloxApiDevelopModelsUniverseSettingsRequestUniverseAnimationType | Unset = UNSET
    universe_collision_type: RobloxApiDevelopModelsUniverseSettingsRequestUniverseCollisionType | Unset = UNSET
    universe_body_type: RobloxApiDevelopModelsUniverseSettingsRequestUniverseBodyType | Unset = UNSET
    universe_joint_positioning_type: (
        RobloxApiDevelopModelsUniverseSettingsRequestUniverseJointPositioningType | Unset
    ) = UNSET
    is_archived: bool | Unset = UNSET
    is_friends_only: bool | Unset = UNSET
    genre: RobloxApiDevelopModelsUniverseSettingsRequestGenre | Unset = UNSET
    playable_devices: list[RobloxApiDevelopModelsUniverseSettingsRequestPlayableDevicesItem] | Unset = UNSET
    is_for_sale: bool | Unset = UNSET
    price: int | Unset = UNSET
    is_mesh_texture_api_access_allowed: bool | Unset = UNSET
    is_rewarded_on_demand_ads_allowed: bool | Unset = UNSET
    fiat_base_price_id: str | Unset = UNSET
    fiat_product_change_type: RobloxApiDevelopModelsUniverseSettingsRequestFiatProductChangeType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        universe_avatar_type: int | Unset = UNSET
        if not isinstance(self.universe_avatar_type, Unset):
            universe_avatar_type = self.universe_avatar_type.value

        universe_scale_type: int | Unset = UNSET
        if not isinstance(self.universe_scale_type, Unset):
            universe_scale_type = self.universe_scale_type.value

        universe_animation_type: int | Unset = UNSET
        if not isinstance(self.universe_animation_type, Unset):
            universe_animation_type = self.universe_animation_type.value

        universe_collision_type: int | Unset = UNSET
        if not isinstance(self.universe_collision_type, Unset):
            universe_collision_type = self.universe_collision_type.value

        universe_body_type: int | Unset = UNSET
        if not isinstance(self.universe_body_type, Unset):
            universe_body_type = self.universe_body_type.value

        universe_joint_positioning_type: int | Unset = UNSET
        if not isinstance(self.universe_joint_positioning_type, Unset):
            universe_joint_positioning_type = self.universe_joint_positioning_type.value

        is_archived = self.is_archived

        is_friends_only = self.is_friends_only

        genre: int | Unset = UNSET
        if not isinstance(self.genre, Unset):
            genre = self.genre.value

        playable_devices: list[int] | Unset = UNSET
        if not isinstance(self.playable_devices, Unset):
            playable_devices = []
            for playable_devices_item_data in self.playable_devices:
                playable_devices_item = playable_devices_item_data.value
                playable_devices.append(playable_devices_item)

        is_for_sale = self.is_for_sale

        price = self.price

        is_mesh_texture_api_access_allowed = self.is_mesh_texture_api_access_allowed

        is_rewarded_on_demand_ads_allowed = self.is_rewarded_on_demand_ads_allowed

        fiat_base_price_id = self.fiat_base_price_id

        fiat_product_change_type: int | Unset = UNSET
        if not isinstance(self.fiat_product_change_type, Unset):
            fiat_product_change_type = self.fiat_product_change_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if universe_avatar_type is not UNSET:
            field_dict["universeAvatarType"] = universe_avatar_type
        if universe_scale_type is not UNSET:
            field_dict["universeScaleType"] = universe_scale_type
        if universe_animation_type is not UNSET:
            field_dict["universeAnimationType"] = universe_animation_type
        if universe_collision_type is not UNSET:
            field_dict["universeCollisionType"] = universe_collision_type
        if universe_body_type is not UNSET:
            field_dict["universeBodyType"] = universe_body_type
        if universe_joint_positioning_type is not UNSET:
            field_dict["universeJointPositioningType"] = universe_joint_positioning_type
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if is_friends_only is not UNSET:
            field_dict["isFriendsOnly"] = is_friends_only
        if genre is not UNSET:
            field_dict["genre"] = genre
        if playable_devices is not UNSET:
            field_dict["playableDevices"] = playable_devices
        if is_for_sale is not UNSET:
            field_dict["isForSale"] = is_for_sale
        if price is not UNSET:
            field_dict["price"] = price
        if is_mesh_texture_api_access_allowed is not UNSET:
            field_dict["isMeshTextureApiAccessAllowed"] = is_mesh_texture_api_access_allowed
        if is_rewarded_on_demand_ads_allowed is not UNSET:
            field_dict["isRewardedOnDemandAdsAllowed"] = is_rewarded_on_demand_ads_allowed
        if fiat_base_price_id is not UNSET:
            field_dict["fiatBasePriceId"] = fiat_base_price_id
        if fiat_product_change_type is not UNSET:
            field_dict["fiatProductChangeType"] = fiat_product_change_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _universe_avatar_type = d.pop("universeAvatarType", UNSET)
        universe_avatar_type: RobloxApiDevelopModelsUniverseSettingsRequestUniverseAvatarType | Unset
        if isinstance(_universe_avatar_type, Unset):
            universe_avatar_type = UNSET
        else:
            universe_avatar_type = RobloxApiDevelopModelsUniverseSettingsRequestUniverseAvatarType(
                _universe_avatar_type
            )

        _universe_scale_type = d.pop("universeScaleType", UNSET)
        universe_scale_type: RobloxApiDevelopModelsUniverseSettingsRequestUniverseScaleType | Unset
        if isinstance(_universe_scale_type, Unset):
            universe_scale_type = UNSET
        else:
            universe_scale_type = RobloxApiDevelopModelsUniverseSettingsRequestUniverseScaleType(_universe_scale_type)

        _universe_animation_type = d.pop("universeAnimationType", UNSET)
        universe_animation_type: RobloxApiDevelopModelsUniverseSettingsRequestUniverseAnimationType | Unset
        if isinstance(_universe_animation_type, Unset):
            universe_animation_type = UNSET
        else:
            universe_animation_type = RobloxApiDevelopModelsUniverseSettingsRequestUniverseAnimationType(
                _universe_animation_type
            )

        _universe_collision_type = d.pop("universeCollisionType", UNSET)
        universe_collision_type: RobloxApiDevelopModelsUniverseSettingsRequestUniverseCollisionType | Unset
        if isinstance(_universe_collision_type, Unset):
            universe_collision_type = UNSET
        else:
            universe_collision_type = RobloxApiDevelopModelsUniverseSettingsRequestUniverseCollisionType(
                _universe_collision_type
            )

        _universe_body_type = d.pop("universeBodyType", UNSET)
        universe_body_type: RobloxApiDevelopModelsUniverseSettingsRequestUniverseBodyType | Unset
        if isinstance(_universe_body_type, Unset):
            universe_body_type = UNSET
        else:
            universe_body_type = RobloxApiDevelopModelsUniverseSettingsRequestUniverseBodyType(_universe_body_type)

        _universe_joint_positioning_type = d.pop("universeJointPositioningType", UNSET)
        universe_joint_positioning_type: (
            RobloxApiDevelopModelsUniverseSettingsRequestUniverseJointPositioningType | Unset
        )
        if isinstance(_universe_joint_positioning_type, Unset):
            universe_joint_positioning_type = UNSET
        else:
            universe_joint_positioning_type = RobloxApiDevelopModelsUniverseSettingsRequestUniverseJointPositioningType(
                _universe_joint_positioning_type
            )

        is_archived = d.pop("isArchived", UNSET)

        is_friends_only = d.pop("isFriendsOnly", UNSET)

        _genre = d.pop("genre", UNSET)
        genre: RobloxApiDevelopModelsUniverseSettingsRequestGenre | Unset
        if isinstance(_genre, Unset):
            genre = UNSET
        else:
            genre = RobloxApiDevelopModelsUniverseSettingsRequestGenre(_genre)

        _playable_devices = d.pop("playableDevices", UNSET)
        playable_devices: list[RobloxApiDevelopModelsUniverseSettingsRequestPlayableDevicesItem] | Unset = UNSET
        if _playable_devices is not UNSET:
            playable_devices = []
            for playable_devices_item_data in _playable_devices:
                playable_devices_item = RobloxApiDevelopModelsUniverseSettingsRequestPlayableDevicesItem(
                    playable_devices_item_data
                )

                playable_devices.append(playable_devices_item)

        is_for_sale = d.pop("isForSale", UNSET)

        price = d.pop("price", UNSET)

        is_mesh_texture_api_access_allowed = d.pop("isMeshTextureApiAccessAllowed", UNSET)

        is_rewarded_on_demand_ads_allowed = d.pop("isRewardedOnDemandAdsAllowed", UNSET)

        fiat_base_price_id = d.pop("fiatBasePriceId", UNSET)

        _fiat_product_change_type = d.pop("fiatProductChangeType", UNSET)
        fiat_product_change_type: RobloxApiDevelopModelsUniverseSettingsRequestFiatProductChangeType | Unset
        if isinstance(_fiat_product_change_type, Unset):
            fiat_product_change_type = UNSET
        else:
            fiat_product_change_type = RobloxApiDevelopModelsUniverseSettingsRequestFiatProductChangeType(
                _fiat_product_change_type
            )

        roblox_api_develop_models_universe_settings_request = cls(
            name=name,
            universe_avatar_type=universe_avatar_type,
            universe_scale_type=universe_scale_type,
            universe_animation_type=universe_animation_type,
            universe_collision_type=universe_collision_type,
            universe_body_type=universe_body_type,
            universe_joint_positioning_type=universe_joint_positioning_type,
            is_archived=is_archived,
            is_friends_only=is_friends_only,
            genre=genre,
            playable_devices=playable_devices,
            is_for_sale=is_for_sale,
            price=price,
            is_mesh_texture_api_access_allowed=is_mesh_texture_api_access_allowed,
            is_rewarded_on_demand_ads_allowed=is_rewarded_on_demand_ads_allowed,
            fiat_base_price_id=fiat_base_price_id,
            fiat_product_change_type=fiat_product_change_type,
        )

        return roblox_api_develop_models_universe_settings_request
