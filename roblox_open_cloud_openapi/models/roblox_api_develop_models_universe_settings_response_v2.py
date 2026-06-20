from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_api_develop_models_universe_settings_response_v2_audiences_item import (
    RobloxApiDevelopModelsUniverseSettingsResponseV2AudiencesItem,
)
from ..models.roblox_api_develop_models_universe_settings_response_v2_fiat_moderation_status import (
    RobloxApiDevelopModelsUniverseSettingsResponseV2FiatModerationStatus,
)
from ..models.roblox_api_develop_models_universe_settings_response_v2_genre import (
    RobloxApiDevelopModelsUniverseSettingsResponseV2Genre,
)
from ..models.roblox_api_develop_models_universe_settings_response_v2_playable_devices_item import (
    RobloxApiDevelopModelsUniverseSettingsResponseV2PlayableDevicesItem,
)
from ..models.roblox_api_develop_models_universe_settings_response_v2_universe_animation_type import (
    RobloxApiDevelopModelsUniverseSettingsResponseV2UniverseAnimationType,
)
from ..models.roblox_api_develop_models_universe_settings_response_v2_universe_avatar_type import (
    RobloxApiDevelopModelsUniverseSettingsResponseV2UniverseAvatarType,
)
from ..models.roblox_api_develop_models_universe_settings_response_v2_universe_collision_type import (
    RobloxApiDevelopModelsUniverseSettingsResponseV2UniverseCollisionType,
)
from ..models.roblox_api_develop_models_universe_settings_response_v2_universe_joint_positioning_type import (
    RobloxApiDevelopModelsUniverseSettingsResponseV2UniverseJointPositioningType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_develop_models_universe_moderation_policy_status import (
        RobloxApiDevelopModelsUniverseModerationPolicyStatus,
    )
    from ..models.roblox_platform_universe_settings_universe_avatar_asset_override_response_model import (
        RobloxPlatformUniverseSettingsUniverseAvatarAssetOverrideResponseModel,
    )
    from ..models.roblox_universe_plugin_permission_authority_models_universe_plugin_permissions import (
        RobloxUniversePluginPermissionAuthorityModelsUniversePluginPermissions,
    )
    from ..models.roblox_web_responses_avatar_scale_model import RobloxWebResponsesAvatarScaleModel


T = TypeVar("T", bound="RobloxApiDevelopModelsUniverseSettingsResponseV2")


@_attrs_define
class RobloxApiDevelopModelsUniverseSettingsResponseV2:
    """Model for UniverseSettings controller responses

    Attributes:
        allow_private_servers (bool | Unset): If the universe allows the use of private servers.
        private_server_price (int | Unset): The price to purchase a private server in robux.
        opt_in_regions (list[RobloxApiDevelopModelsUniverseModerationPolicyStatus] | Unset): The regions the universe
            has opted in for
        is_mesh_texture_api_access_allowed (bool | Unset): Whether access to APIs for mesh and texture is enabled for
            this universe.
        is_rewarded_on_demand_ads_allowed (bool | Unset): Whether rewarded on-demand ads are allowed for this universe.
        id (int | Unset): The universe Id.
        name (str | Unset): The universe name.
        description (str | Unset): The universe description.
        universe_avatar_type (RobloxApiDevelopModelsUniverseSettingsResponseV2UniverseAvatarType | Unset): Which avatar
            types are allowed in the universe. ['MorphToR6' = 1, 'PlayerChoice' = 2, 'MorphToR15' = 3]
        universe_animation_type (RobloxApiDevelopModelsUniverseSettingsResponseV2UniverseAnimationType | Unset): Whether
            custom animations are allowed in the universe. ['Standard' = 1, 'PlayerChoice' = 2]
        universe_collision_type (RobloxApiDevelopModelsUniverseSettingsResponseV2UniverseCollisionType | Unset): What
            type of collisions are used by the universe. ['InnerBox' = 1, 'OuterBox' = 2]
        universe_joint_positioning_type (RobloxApiDevelopModelsUniverseSettingsResponseV2UniverseJointPositioningType |
            Unset): What avatar joint positioning is allowed by the universe. ['Standard' = 1, 'ArtistIntent' = 2]
        engine_avatar_settings (str | Unset): Optional JSON string used to store avatar settings used by the game
            engine.
            Note: This is an experimental field which may be changed or removed in future.
        is_archived (bool | Unset): Archive status of the universe
        is_friends_only (bool | Unset): Whether game access is limited to friends for user-owned games or group members
            for group-owned games.
        genre (RobloxApiDevelopModelsUniverseSettingsResponseV2Genre | Unset): Game genre. ['All' = 0, 'Tutorial' = 1,
            'Scary' = 2, 'TownAndCity' = 3, 'War' = 4, 'Funny' = 5, 'Fantasy' = 6, 'Adventure' = 7, 'SciFi' = 8, 'Pirate' =
            9, 'FPS' = 10, 'RPG' = 11, 'Sports' = 12, 'Ninja' = 13, 'WildWest' = 14]
        playable_devices (list[RobloxApiDevelopModelsUniverseSettingsResponseV2PlayableDevicesItem] | Unset): List of
            device types this game can be played on.
        is_for_sale (bool | Unset): Whether the game is offered for sale.
        price (int | Unset): Price of the game, in Robux.
        universe_avatar_asset_overrides (list[RobloxPlatformUniverseSettingsUniverseAvatarAssetOverrideResponseModel] |
            Unset): A collection of avatar asset settings allowed by the universe.
        universe_avatar_min_scales (RobloxWebResponsesAvatarScaleModel | Unset):
        universe_avatar_max_scales (RobloxWebResponsesAvatarScaleModel | Unset):
        studio_access_to_apis_allowed (bool | Unset): Whether Studio can access data stores of this universe.
        permissions (RobloxUniversePluginPermissionAuthorityModelsUniversePluginPermissions | Unset):
        is_for_sale_in_fiat (bool | Unset): Whether the game is offered for sale in fiat.
        fiat_base_price_id (str | Unset): The basePriceId for the Fiat product.
        fiat_moderation_status (RobloxApiDevelopModelsUniverseSettingsResponseV2FiatModerationStatus | Unset): The
            current moderation status of the game if it is for sale in fiat. ['Invalid' = 0, 'NotModerated' = 1, 'Pending' =
            2, 'Approved' = 3, 'Rejected' = 4]
        audiences (list[RobloxApiDevelopModelsUniverseSettingsResponseV2AudiencesItem] | Unset): The audiences this
            universe is visible to (e.g. Editors, PlayTesters, Friends, Public).
            Always non-null; may be empty when audience visibility has not been configured.
    """

    allow_private_servers: bool | Unset = UNSET
    private_server_price: int | Unset = UNSET
    opt_in_regions: list[RobloxApiDevelopModelsUniverseModerationPolicyStatus] | Unset = UNSET
    is_mesh_texture_api_access_allowed: bool | Unset = UNSET
    is_rewarded_on_demand_ads_allowed: bool | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    universe_avatar_type: RobloxApiDevelopModelsUniverseSettingsResponseV2UniverseAvatarType | Unset = UNSET
    universe_animation_type: RobloxApiDevelopModelsUniverseSettingsResponseV2UniverseAnimationType | Unset = UNSET
    universe_collision_type: RobloxApiDevelopModelsUniverseSettingsResponseV2UniverseCollisionType | Unset = UNSET
    universe_joint_positioning_type: (
        RobloxApiDevelopModelsUniverseSettingsResponseV2UniverseJointPositioningType | Unset
    ) = UNSET
    engine_avatar_settings: str | Unset = UNSET
    is_archived: bool | Unset = UNSET
    is_friends_only: bool | Unset = UNSET
    genre: RobloxApiDevelopModelsUniverseSettingsResponseV2Genre | Unset = UNSET
    playable_devices: list[RobloxApiDevelopModelsUniverseSettingsResponseV2PlayableDevicesItem] | Unset = UNSET
    is_for_sale: bool | Unset = UNSET
    price: int | Unset = UNSET
    universe_avatar_asset_overrides: (
        list[RobloxPlatformUniverseSettingsUniverseAvatarAssetOverrideResponseModel] | Unset
    ) = UNSET
    universe_avatar_min_scales: RobloxWebResponsesAvatarScaleModel | Unset = UNSET
    universe_avatar_max_scales: RobloxWebResponsesAvatarScaleModel | Unset = UNSET
    studio_access_to_apis_allowed: bool | Unset = UNSET
    permissions: RobloxUniversePluginPermissionAuthorityModelsUniversePluginPermissions | Unset = UNSET
    is_for_sale_in_fiat: bool | Unset = UNSET
    fiat_base_price_id: str | Unset = UNSET
    fiat_moderation_status: RobloxApiDevelopModelsUniverseSettingsResponseV2FiatModerationStatus | Unset = UNSET
    audiences: list[RobloxApiDevelopModelsUniverseSettingsResponseV2AudiencesItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        allow_private_servers = self.allow_private_servers

        private_server_price = self.private_server_price

        opt_in_regions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.opt_in_regions, Unset):
            opt_in_regions = []
            for opt_in_regions_item_data in self.opt_in_regions:
                opt_in_regions_item = opt_in_regions_item_data.to_dict()
                opt_in_regions.append(opt_in_regions_item)

        is_mesh_texture_api_access_allowed = self.is_mesh_texture_api_access_allowed

        is_rewarded_on_demand_ads_allowed = self.is_rewarded_on_demand_ads_allowed

        id = self.id

        name = self.name

        description = self.description

        universe_avatar_type: int | Unset = UNSET
        if not isinstance(self.universe_avatar_type, Unset):
            universe_avatar_type = self.universe_avatar_type.value

        universe_animation_type: int | Unset = UNSET
        if not isinstance(self.universe_animation_type, Unset):
            universe_animation_type = self.universe_animation_type.value

        universe_collision_type: int | Unset = UNSET
        if not isinstance(self.universe_collision_type, Unset):
            universe_collision_type = self.universe_collision_type.value

        universe_joint_positioning_type: int | Unset = UNSET
        if not isinstance(self.universe_joint_positioning_type, Unset):
            universe_joint_positioning_type = self.universe_joint_positioning_type.value

        engine_avatar_settings = self.engine_avatar_settings

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

        universe_avatar_asset_overrides: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.universe_avatar_asset_overrides, Unset):
            universe_avatar_asset_overrides = []
            for universe_avatar_asset_overrides_item_data in self.universe_avatar_asset_overrides:
                universe_avatar_asset_overrides_item = universe_avatar_asset_overrides_item_data.to_dict()
                universe_avatar_asset_overrides.append(universe_avatar_asset_overrides_item)

        universe_avatar_min_scales: dict[str, Any] | Unset = UNSET
        if not isinstance(self.universe_avatar_min_scales, Unset):
            universe_avatar_min_scales = self.universe_avatar_min_scales.to_dict()

        universe_avatar_max_scales: dict[str, Any] | Unset = UNSET
        if not isinstance(self.universe_avatar_max_scales, Unset):
            universe_avatar_max_scales = self.universe_avatar_max_scales.to_dict()

        studio_access_to_apis_allowed = self.studio_access_to_apis_allowed

        permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if allow_private_servers is not UNSET:
            field_dict["allowPrivateServers"] = allow_private_servers
        if private_server_price is not UNSET:
            field_dict["privateServerPrice"] = private_server_price
        if opt_in_regions is not UNSET:
            field_dict["optInRegions"] = opt_in_regions
        if is_mesh_texture_api_access_allowed is not UNSET:
            field_dict["isMeshTextureApiAccessAllowed"] = is_mesh_texture_api_access_allowed
        if is_rewarded_on_demand_ads_allowed is not UNSET:
            field_dict["isRewardedOnDemandAdsAllowed"] = is_rewarded_on_demand_ads_allowed
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if universe_avatar_type is not UNSET:
            field_dict["universeAvatarType"] = universe_avatar_type
        if universe_animation_type is not UNSET:
            field_dict["universeAnimationType"] = universe_animation_type
        if universe_collision_type is not UNSET:
            field_dict["universeCollisionType"] = universe_collision_type
        if universe_joint_positioning_type is not UNSET:
            field_dict["universeJointPositioningType"] = universe_joint_positioning_type
        if engine_avatar_settings is not UNSET:
            field_dict["engineAvatarSettings"] = engine_avatar_settings
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
        if universe_avatar_asset_overrides is not UNSET:
            field_dict["universeAvatarAssetOverrides"] = universe_avatar_asset_overrides
        if universe_avatar_min_scales is not UNSET:
            field_dict["universeAvatarMinScales"] = universe_avatar_min_scales
        if universe_avatar_max_scales is not UNSET:
            field_dict["universeAvatarMaxScales"] = universe_avatar_max_scales
        if studio_access_to_apis_allowed is not UNSET:
            field_dict["studioAccessToApisAllowed"] = studio_access_to_apis_allowed
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if is_for_sale_in_fiat is not UNSET:
            field_dict["isForSaleInFiat"] = is_for_sale_in_fiat
        if fiat_base_price_id is not UNSET:
            field_dict["fiatBasePriceId"] = fiat_base_price_id
        if fiat_moderation_status is not UNSET:
            field_dict["fiatModerationStatus"] = fiat_moderation_status
        if audiences is not UNSET:
            field_dict["audiences"] = audiences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_develop_models_universe_moderation_policy_status import (
            RobloxApiDevelopModelsUniverseModerationPolicyStatus,
        )
        from ..models.roblox_platform_universe_settings_universe_avatar_asset_override_response_model import (
            RobloxPlatformUniverseSettingsUniverseAvatarAssetOverrideResponseModel,
        )
        from ..models.roblox_universe_plugin_permission_authority_models_universe_plugin_permissions import (
            RobloxUniversePluginPermissionAuthorityModelsUniversePluginPermissions,
        )
        from ..models.roblox_web_responses_avatar_scale_model import RobloxWebResponsesAvatarScaleModel

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        allow_private_servers = d.pop("allowPrivateServers", UNSET)

        private_server_price = d.pop("privateServerPrice", UNSET)

        _opt_in_regions = d.pop("optInRegions", UNSET)
        opt_in_regions: list[RobloxApiDevelopModelsUniverseModerationPolicyStatus] | Unset = UNSET
        if _opt_in_regions is not UNSET:
            opt_in_regions = []
            for opt_in_regions_item_data in _opt_in_regions:
                opt_in_regions_item = RobloxApiDevelopModelsUniverseModerationPolicyStatus.from_dict(
                    opt_in_regions_item_data
                )

                opt_in_regions.append(opt_in_regions_item)

        is_mesh_texture_api_access_allowed = d.pop("isMeshTextureApiAccessAllowed", UNSET)

        is_rewarded_on_demand_ads_allowed = d.pop("isRewardedOnDemandAdsAllowed", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _universe_avatar_type = d.pop("universeAvatarType", UNSET)
        universe_avatar_type: RobloxApiDevelopModelsUniverseSettingsResponseV2UniverseAvatarType | Unset
        if isinstance(_universe_avatar_type, Unset):
            universe_avatar_type = UNSET
        else:
            universe_avatar_type = RobloxApiDevelopModelsUniverseSettingsResponseV2UniverseAvatarType(
                _universe_avatar_type
            )

        _universe_animation_type = d.pop("universeAnimationType", UNSET)
        universe_animation_type: RobloxApiDevelopModelsUniverseSettingsResponseV2UniverseAnimationType | Unset
        if isinstance(_universe_animation_type, Unset):
            universe_animation_type = UNSET
        else:
            universe_animation_type = RobloxApiDevelopModelsUniverseSettingsResponseV2UniverseAnimationType(
                _universe_animation_type
            )

        _universe_collision_type = d.pop("universeCollisionType", UNSET)
        universe_collision_type: RobloxApiDevelopModelsUniverseSettingsResponseV2UniverseCollisionType | Unset
        if isinstance(_universe_collision_type, Unset):
            universe_collision_type = UNSET
        else:
            universe_collision_type = RobloxApiDevelopModelsUniverseSettingsResponseV2UniverseCollisionType(
                _universe_collision_type
            )

        _universe_joint_positioning_type = d.pop("universeJointPositioningType", UNSET)
        universe_joint_positioning_type: (
            RobloxApiDevelopModelsUniverseSettingsResponseV2UniverseJointPositioningType | Unset
        )
        if isinstance(_universe_joint_positioning_type, Unset):
            universe_joint_positioning_type = UNSET
        else:
            universe_joint_positioning_type = (
                RobloxApiDevelopModelsUniverseSettingsResponseV2UniverseJointPositioningType(
                    _universe_joint_positioning_type
                )
            )

        engine_avatar_settings = d.pop("engineAvatarSettings", UNSET)

        is_archived = d.pop("isArchived", UNSET)

        is_friends_only = d.pop("isFriendsOnly", UNSET)

        _genre = d.pop("genre", UNSET)
        genre: RobloxApiDevelopModelsUniverseSettingsResponseV2Genre | Unset
        if isinstance(_genre, Unset):
            genre = UNSET
        else:
            genre = RobloxApiDevelopModelsUniverseSettingsResponseV2Genre(_genre)

        _playable_devices = d.pop("playableDevices", UNSET)
        playable_devices: list[RobloxApiDevelopModelsUniverseSettingsResponseV2PlayableDevicesItem] | Unset = UNSET
        if _playable_devices is not UNSET:
            playable_devices = []
            for playable_devices_item_data in _playable_devices:
                playable_devices_item = RobloxApiDevelopModelsUniverseSettingsResponseV2PlayableDevicesItem(
                    playable_devices_item_data
                )

                playable_devices.append(playable_devices_item)

        is_for_sale = d.pop("isForSale", UNSET)

        price = d.pop("price", UNSET)

        _universe_avatar_asset_overrides = d.pop("universeAvatarAssetOverrides", UNSET)
        universe_avatar_asset_overrides: (
            list[RobloxPlatformUniverseSettingsUniverseAvatarAssetOverrideResponseModel] | Unset
        ) = UNSET
        if _universe_avatar_asset_overrides is not UNSET:
            universe_avatar_asset_overrides = []
            for universe_avatar_asset_overrides_item_data in _universe_avatar_asset_overrides:
                universe_avatar_asset_overrides_item = (
                    RobloxPlatformUniverseSettingsUniverseAvatarAssetOverrideResponseModel.from_dict(
                        universe_avatar_asset_overrides_item_data
                    )
                )

                universe_avatar_asset_overrides.append(universe_avatar_asset_overrides_item)

        _universe_avatar_min_scales = d.pop("universeAvatarMinScales", UNSET)
        universe_avatar_min_scales: RobloxWebResponsesAvatarScaleModel | Unset
        if isinstance(_universe_avatar_min_scales, Unset):
            universe_avatar_min_scales = UNSET
        else:
            universe_avatar_min_scales = RobloxWebResponsesAvatarScaleModel.from_dict(_universe_avatar_min_scales)

        _universe_avatar_max_scales = d.pop("universeAvatarMaxScales", UNSET)
        universe_avatar_max_scales: RobloxWebResponsesAvatarScaleModel | Unset
        if isinstance(_universe_avatar_max_scales, Unset):
            universe_avatar_max_scales = UNSET
        else:
            universe_avatar_max_scales = RobloxWebResponsesAvatarScaleModel.from_dict(_universe_avatar_max_scales)

        studio_access_to_apis_allowed = d.pop("studioAccessToApisAllowed", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: RobloxUniversePluginPermissionAuthorityModelsUniversePluginPermissions | Unset
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = RobloxUniversePluginPermissionAuthorityModelsUniversePluginPermissions.from_dict(_permissions)

        is_for_sale_in_fiat = d.pop("isForSaleInFiat", UNSET)

        fiat_base_price_id = d.pop("fiatBasePriceId", UNSET)

        _fiat_moderation_status = d.pop("fiatModerationStatus", UNSET)
        fiat_moderation_status: RobloxApiDevelopModelsUniverseSettingsResponseV2FiatModerationStatus | Unset
        if isinstance(_fiat_moderation_status, Unset):
            fiat_moderation_status = UNSET
        else:
            fiat_moderation_status = RobloxApiDevelopModelsUniverseSettingsResponseV2FiatModerationStatus(
                _fiat_moderation_status
            )

        _audiences = d.pop("audiences", UNSET)
        audiences: list[RobloxApiDevelopModelsUniverseSettingsResponseV2AudiencesItem] | Unset = UNSET
        if _audiences is not UNSET:
            audiences = []
            for audiences_item_data in _audiences:
                audiences_item = RobloxApiDevelopModelsUniverseSettingsResponseV2AudiencesItem(audiences_item_data)

                audiences.append(audiences_item)

        roblox_api_develop_models_universe_settings_response_v2 = cls(
            allow_private_servers=allow_private_servers,
            private_server_price=private_server_price,
            opt_in_regions=opt_in_regions,
            is_mesh_texture_api_access_allowed=is_mesh_texture_api_access_allowed,
            is_rewarded_on_demand_ads_allowed=is_rewarded_on_demand_ads_allowed,
            id=id,
            name=name,
            description=description,
            universe_avatar_type=universe_avatar_type,
            universe_animation_type=universe_animation_type,
            universe_collision_type=universe_collision_type,
            universe_joint_positioning_type=universe_joint_positioning_type,
            engine_avatar_settings=engine_avatar_settings,
            is_archived=is_archived,
            is_friends_only=is_friends_only,
            genre=genre,
            playable_devices=playable_devices,
            is_for_sale=is_for_sale,
            price=price,
            universe_avatar_asset_overrides=universe_avatar_asset_overrides,
            universe_avatar_min_scales=universe_avatar_min_scales,
            universe_avatar_max_scales=universe_avatar_max_scales,
            studio_access_to_apis_allowed=studio_access_to_apis_allowed,
            permissions=permissions,
            is_for_sale_in_fiat=is_for_sale_in_fiat,
            fiat_base_price_id=fiat_base_price_id,
            fiat_moderation_status=fiat_moderation_status,
            audiences=audiences,
        )

        return roblox_api_develop_models_universe_settings_response_v2
