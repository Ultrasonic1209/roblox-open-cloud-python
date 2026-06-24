from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_api_develop_models_universe_settings_response_audiences_item import (
    RobloxApiDevelopModelsUniverseSettingsResponseAudiencesItem,
)
from ..models.roblox_api_develop_models_universe_settings_response_fiat_moderation_status import (
    RobloxApiDevelopModelsUniverseSettingsResponseFiatModerationStatus,
)
from ..models.roblox_api_develop_models_universe_settings_response_genre import (
    RobloxApiDevelopModelsUniverseSettingsResponseGenre,
)
from ..models.roblox_api_develop_models_universe_settings_response_playable_devices_item import (
    RobloxApiDevelopModelsUniverseSettingsResponsePlayableDevicesItem,
)
from ..models.roblox_api_develop_models_universe_settings_response_universe_animation_type import (
    RobloxApiDevelopModelsUniverseSettingsResponseUniverseAnimationType,
)
from ..models.roblox_api_develop_models_universe_settings_response_universe_avatar_type import (
    RobloxApiDevelopModelsUniverseSettingsResponseUniverseAvatarType,
)
from ..models.roblox_api_develop_models_universe_settings_response_universe_body_type import (
    RobloxApiDevelopModelsUniverseSettingsResponseUniverseBodyType,
)
from ..models.roblox_api_develop_models_universe_settings_response_universe_collision_type import (
    RobloxApiDevelopModelsUniverseSettingsResponseUniverseCollisionType,
)
from ..models.roblox_api_develop_models_universe_settings_response_universe_joint_positioning_type import (
    RobloxApiDevelopModelsUniverseSettingsResponseUniverseJointPositioningType,
)
from ..models.roblox_api_develop_models_universe_settings_response_universe_scale_type import (
    RobloxApiDevelopModelsUniverseSettingsResponseUniverseScaleType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiDevelopModelsUniverseSettingsResponse")


@_attrs_define
class RobloxApiDevelopModelsUniverseSettingsResponse:
    """Model for UniverseSettings controller responses

    Attributes:
        allow_private_servers (bool | Unset): If the universe allows the use of private servers.
        private_server_price (int | Unset): The price to purchase a private server in robux.
        is_mesh_texture_api_access_allowed (bool | Unset): Whether access to APIs for mesh and texture is enabled for
            this universe.
        is_rewarded_on_demand_ads_allowed (bool | Unset): Whether rewarded on-demand ads are allowed for this universe.
        id (int | Unset): The universe Id.
        name (str | Unset): The universe name.
        universe_avatar_type (RobloxApiDevelopModelsUniverseSettingsResponseUniverseAvatarType | Unset): Which avatar
            types are allowed in the universe. ['MorphToR6' = 1, 'PlayerChoice' = 2, 'MorphToR15' = 3]
        universe_scale_type (RobloxApiDevelopModelsUniverseSettingsResponseUniverseScaleType | Unset): Whether custom
            scales allowed in the universe. ['NoScales' = 1, 'AllScales' = 2]
        universe_animation_type (RobloxApiDevelopModelsUniverseSettingsResponseUniverseAnimationType | Unset): Whether
            custom animations are allowed in the universe. ['Standard' = 1, 'PlayerChoice' = 2]
        universe_collision_type (RobloxApiDevelopModelsUniverseSettingsResponseUniverseCollisionType | Unset): What type
            of collisions are used by the universe. ['InnerBox' = 1, 'OuterBox' = 2]
        universe_body_type (RobloxApiDevelopModelsUniverseSettingsResponseUniverseBodyType | Unset): What avatar body
            types are allowed by the universe. ['Standard' = 1, 'PlayerChoice' = 2]
        universe_joint_positioning_type (RobloxApiDevelopModelsUniverseSettingsResponseUniverseJointPositioningType |
            Unset): What avatar joint positioning is allowed by the universe. ['Standard' = 1, 'ArtistIntent' = 2]
        is_archived (bool | Unset): Archive status of the universe
        is_friends_only (bool | Unset): Whether game access is limited to friends for user-owned games or group members
            for group-owned games.
        genre (RobloxApiDevelopModelsUniverseSettingsResponseGenre | Unset): Game genre. ['All' = 0, 'Tutorial' = 1,
            'Scary' = 2, 'TownAndCity' = 3, 'War' = 4, 'Funny' = 5, 'Fantasy' = 6, 'Adventure' = 7, 'SciFi' = 8, 'Pirate' =
            9, 'FPS' = 10, 'RPG' = 11, 'Sports' = 12, 'Ninja' = 13, 'WildWest' = 14]
        playable_devices (list[RobloxApiDevelopModelsUniverseSettingsResponsePlayableDevicesItem] | Unset): List of
            device types this game can be played on.
        is_for_sale (bool | Unset): Whether the game is offered for sale.
        price (int | Unset): Price of the game, in Robux.
        is_studio_access_to_apis_allowed (bool | Unset): Whether studio access to APIs is allowed or not.
        privacy_type (str | Unset): Privacy type of the universe.
        is_for_sale_in_fiat (bool | Unset): Whether the game is offered for sale in fiat.
        fiat_base_price_id (str | Unset): The basePriceId for the Fiat product.
        fiat_moderation_status (RobloxApiDevelopModelsUniverseSettingsResponseFiatModerationStatus | Unset): The current
            moderation status of the game if it is for sale in fiat. ['Invalid' = 0, 'NotModerated' = 1, 'Pending' = 2,
            'Approved' = 3, 'Rejected' = 4]
        audiences (list[RobloxApiDevelopModelsUniverseSettingsResponseAudiencesItem] | Unset): The audiences this
            universe is visible to (e.g. Editors, PlayTesters, Friends, Public).
            Always non-null; may be empty when audience visibility has not been configured.
        demo_mode_enabled (bool | Unset): Whether demo mode is enabled.
        demo_mode_last_changed_time (datetime.datetime | Unset): When demo mode was last toggled. For client-side
            throttle UX.
    """

    allow_private_servers: bool | Unset = UNSET
    private_server_price: int | Unset = UNSET
    is_mesh_texture_api_access_allowed: bool | Unset = UNSET
    is_rewarded_on_demand_ads_allowed: bool | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    universe_avatar_type: RobloxApiDevelopModelsUniverseSettingsResponseUniverseAvatarType | Unset = UNSET
    universe_scale_type: RobloxApiDevelopModelsUniverseSettingsResponseUniverseScaleType | Unset = UNSET
    universe_animation_type: RobloxApiDevelopModelsUniverseSettingsResponseUniverseAnimationType | Unset = UNSET
    universe_collision_type: RobloxApiDevelopModelsUniverseSettingsResponseUniverseCollisionType | Unset = UNSET
    universe_body_type: RobloxApiDevelopModelsUniverseSettingsResponseUniverseBodyType | Unset = UNSET
    universe_joint_positioning_type: (
        RobloxApiDevelopModelsUniverseSettingsResponseUniverseJointPositioningType | Unset
    ) = UNSET
    is_archived: bool | Unset = UNSET
    is_friends_only: bool | Unset = UNSET
    genre: RobloxApiDevelopModelsUniverseSettingsResponseGenre | Unset = UNSET
    playable_devices: list[RobloxApiDevelopModelsUniverseSettingsResponsePlayableDevicesItem] | Unset = UNSET
    is_for_sale: bool | Unset = UNSET
    price: int | Unset = UNSET
    is_studio_access_to_apis_allowed: bool | Unset = UNSET
    privacy_type: str | Unset = UNSET
    is_for_sale_in_fiat: bool | Unset = UNSET
    fiat_base_price_id: str | Unset = UNSET
    fiat_moderation_status: RobloxApiDevelopModelsUniverseSettingsResponseFiatModerationStatus | Unset = UNSET
    audiences: list[RobloxApiDevelopModelsUniverseSettingsResponseAudiencesItem] | Unset = UNSET
    demo_mode_enabled: bool | Unset = UNSET
    demo_mode_last_changed_time: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        allow_private_servers = self.allow_private_servers

        private_server_price = self.private_server_price

        is_mesh_texture_api_access_allowed = self.is_mesh_texture_api_access_allowed

        is_rewarded_on_demand_ads_allowed = self.is_rewarded_on_demand_ads_allowed

        id = self.id

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

        is_studio_access_to_apis_allowed = self.is_studio_access_to_apis_allowed

        privacy_type = self.privacy_type

        is_for_sale_in_fiat = self.is_for_sale_in_fiat

        fiat_base_price_id = self.fiat_base_price_id

        fiat_moderation_status: int | Unset = UNSET
        if not isinstance(self.fiat_moderation_status, Unset):
            fiat_moderation_status = self.fiat_moderation_status.value

        audiences: list[int] | Unset = UNSET
        if not isinstance(self.audiences, Unset):
            audiences = []
            for audiences_item_data in self.audiences:
                audiences_item = audiences_item_data.value
                audiences.append(audiences_item)

        demo_mode_enabled = self.demo_mode_enabled

        demo_mode_last_changed_time: str | Unset = UNSET
        if not isinstance(self.demo_mode_last_changed_time, Unset):
            demo_mode_last_changed_time = self.demo_mode_last_changed_time.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if allow_private_servers is not UNSET:
            field_dict["allowPrivateServers"] = allow_private_servers
        if private_server_price is not UNSET:
            field_dict["privateServerPrice"] = private_server_price
        if is_mesh_texture_api_access_allowed is not UNSET:
            field_dict["isMeshTextureApiAccessAllowed"] = is_mesh_texture_api_access_allowed
        if is_rewarded_on_demand_ads_allowed is not UNSET:
            field_dict["isRewardedOnDemandAdsAllowed"] = is_rewarded_on_demand_ads_allowed
        if id is not UNSET:
            field_dict["id"] = id
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
        if is_studio_access_to_apis_allowed is not UNSET:
            field_dict["isStudioAccessToApisAllowed"] = is_studio_access_to_apis_allowed
        if privacy_type is not UNSET:
            field_dict["privacyType"] = privacy_type
        if is_for_sale_in_fiat is not UNSET:
            field_dict["isForSaleInFiat"] = is_for_sale_in_fiat
        if fiat_base_price_id is not UNSET:
            field_dict["fiatBasePriceId"] = fiat_base_price_id
        if fiat_moderation_status is not UNSET:
            field_dict["fiatModerationStatus"] = fiat_moderation_status
        if audiences is not UNSET:
            field_dict["audiences"] = audiences
        if demo_mode_enabled is not UNSET:
            field_dict["demoModeEnabled"] = demo_mode_enabled
        if demo_mode_last_changed_time is not UNSET:
            field_dict["demoModeLastChangedTime"] = demo_mode_last_changed_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        allow_private_servers = d.pop("allowPrivateServers", UNSET)

        private_server_price = d.pop("privateServerPrice", UNSET)

        is_mesh_texture_api_access_allowed = d.pop("isMeshTextureApiAccessAllowed", UNSET)

        is_rewarded_on_demand_ads_allowed = d.pop("isRewardedOnDemandAdsAllowed", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _universe_avatar_type = d.pop("universeAvatarType", UNSET)
        universe_avatar_type: RobloxApiDevelopModelsUniverseSettingsResponseUniverseAvatarType | Unset
        if isinstance(_universe_avatar_type, Unset):
            universe_avatar_type = UNSET
        else:
            universe_avatar_type = RobloxApiDevelopModelsUniverseSettingsResponseUniverseAvatarType(
                _universe_avatar_type
            )

        _universe_scale_type = d.pop("universeScaleType", UNSET)
        universe_scale_type: RobloxApiDevelopModelsUniverseSettingsResponseUniverseScaleType | Unset
        if isinstance(_universe_scale_type, Unset):
            universe_scale_type = UNSET
        else:
            universe_scale_type = RobloxApiDevelopModelsUniverseSettingsResponseUniverseScaleType(_universe_scale_type)

        _universe_animation_type = d.pop("universeAnimationType", UNSET)
        universe_animation_type: RobloxApiDevelopModelsUniverseSettingsResponseUniverseAnimationType | Unset
        if isinstance(_universe_animation_type, Unset):
            universe_animation_type = UNSET
        else:
            universe_animation_type = RobloxApiDevelopModelsUniverseSettingsResponseUniverseAnimationType(
                _universe_animation_type
            )

        _universe_collision_type = d.pop("universeCollisionType", UNSET)
        universe_collision_type: RobloxApiDevelopModelsUniverseSettingsResponseUniverseCollisionType | Unset
        if isinstance(_universe_collision_type, Unset):
            universe_collision_type = UNSET
        else:
            universe_collision_type = RobloxApiDevelopModelsUniverseSettingsResponseUniverseCollisionType(
                _universe_collision_type
            )

        _universe_body_type = d.pop("universeBodyType", UNSET)
        universe_body_type: RobloxApiDevelopModelsUniverseSettingsResponseUniverseBodyType | Unset
        if isinstance(_universe_body_type, Unset):
            universe_body_type = UNSET
        else:
            universe_body_type = RobloxApiDevelopModelsUniverseSettingsResponseUniverseBodyType(_universe_body_type)

        _universe_joint_positioning_type = d.pop("universeJointPositioningType", UNSET)
        universe_joint_positioning_type: (
            RobloxApiDevelopModelsUniverseSettingsResponseUniverseJointPositioningType | Unset
        )
        if isinstance(_universe_joint_positioning_type, Unset):
            universe_joint_positioning_type = UNSET
        else:
            universe_joint_positioning_type = (
                RobloxApiDevelopModelsUniverseSettingsResponseUniverseJointPositioningType(
                    _universe_joint_positioning_type
                )
            )

        is_archived = d.pop("isArchived", UNSET)

        is_friends_only = d.pop("isFriendsOnly", UNSET)

        _genre = d.pop("genre", UNSET)
        genre: RobloxApiDevelopModelsUniverseSettingsResponseGenre | Unset
        if isinstance(_genre, Unset):
            genre = UNSET
        else:
            genre = RobloxApiDevelopModelsUniverseSettingsResponseGenre(_genre)

        _playable_devices = d.pop("playableDevices", UNSET)
        playable_devices: list[RobloxApiDevelopModelsUniverseSettingsResponsePlayableDevicesItem] | Unset = UNSET
        if _playable_devices is not UNSET:
            playable_devices = []
            for playable_devices_item_data in _playable_devices:
                playable_devices_item = RobloxApiDevelopModelsUniverseSettingsResponsePlayableDevicesItem(
                    playable_devices_item_data
                )

                playable_devices.append(playable_devices_item)

        is_for_sale = d.pop("isForSale", UNSET)

        price = d.pop("price", UNSET)

        is_studio_access_to_apis_allowed = d.pop("isStudioAccessToApisAllowed", UNSET)

        privacy_type = d.pop("privacyType", UNSET)

        is_for_sale_in_fiat = d.pop("isForSaleInFiat", UNSET)

        fiat_base_price_id = d.pop("fiatBasePriceId", UNSET)

        _fiat_moderation_status = d.pop("fiatModerationStatus", UNSET)
        fiat_moderation_status: RobloxApiDevelopModelsUniverseSettingsResponseFiatModerationStatus | Unset
        if isinstance(_fiat_moderation_status, Unset):
            fiat_moderation_status = UNSET
        else:
            fiat_moderation_status = RobloxApiDevelopModelsUniverseSettingsResponseFiatModerationStatus(
                _fiat_moderation_status
            )

        _audiences = d.pop("audiences", UNSET)
        audiences: list[RobloxApiDevelopModelsUniverseSettingsResponseAudiencesItem] | Unset = UNSET
        if _audiences is not UNSET:
            audiences = []
            for audiences_item_data in _audiences:
                audiences_item = RobloxApiDevelopModelsUniverseSettingsResponseAudiencesItem(audiences_item_data)

                audiences.append(audiences_item)

        demo_mode_enabled = d.pop("demoModeEnabled", UNSET)

        _demo_mode_last_changed_time = d.pop("demoModeLastChangedTime", UNSET)
        demo_mode_last_changed_time: datetime.datetime | Unset
        if isinstance(_demo_mode_last_changed_time, Unset):
            demo_mode_last_changed_time = UNSET
        else:
            demo_mode_last_changed_time = datetime.datetime.fromisoformat(_demo_mode_last_changed_time)

        roblox_api_develop_models_universe_settings_response = cls(
            allow_private_servers=allow_private_servers,
            private_server_price=private_server_price,
            is_mesh_texture_api_access_allowed=is_mesh_texture_api_access_allowed,
            is_rewarded_on_demand_ads_allowed=is_rewarded_on_demand_ads_allowed,
            id=id,
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
            is_studio_access_to_apis_allowed=is_studio_access_to_apis_allowed,
            privacy_type=privacy_type,
            is_for_sale_in_fiat=is_for_sale_in_fiat,
            fiat_base_price_id=fiat_base_price_id,
            fiat_moderation_status=fiat_moderation_status,
            audiences=audiences,
            demo_mode_enabled=demo_mode_enabled,
            demo_mode_last_changed_time=demo_mode_last_changed_time,
        )

        return roblox_api_develop_models_universe_settings_response
