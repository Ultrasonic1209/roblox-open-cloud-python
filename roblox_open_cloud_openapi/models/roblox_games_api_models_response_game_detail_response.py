from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.roblox_games_api_models_response_game_detail_response_universe_avatar_type import (
    RobloxGamesApiModelsResponseGameDetailResponseUniverseAvatarType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_games_api_models_response_game_creator import RobloxGamesApiModelsResponseGameCreator
    from ..models.roblox_games_api_models_response_refund_policy import RobloxGamesApiModelsResponseRefundPolicy


T = TypeVar("T", bound="RobloxGamesApiModelsResponseGameDetailResponse")


@_attrs_define
class RobloxGamesApiModelsResponseGameDetailResponse:
    """Response model for getting the game detail

    Attributes:
        id (int | Unset): The game universe id
        root_place_id (int | Unset): The game root place id
        name (str | Unset): The game name
        description (str | Unset): The game description
        source_name (str | Unset): The game name in the source language, if different from the returned name.
        source_description (str | Unset): The game description in the source language, if different from the returned
            description.
        creator (RobloxGamesApiModelsResponseGameCreator | Unset): Response model for getting the game creator
        price (int | Unset): The game paid access price
        allowed_gear_genres (list[str] | Unset): The game allowed gear genres
        allowed_gear_categories (list[str] | Unset): The game allowed gear categoris
        is_genre_enforced (bool | Unset): The game must specify a genre
        copying_allowed (bool | Unset): The game allows place to be copied
        playing (int | Unset): Current player count of the game
        visits (int | Unset): The total visits to the game
        max_players (int | Unset): The game max players
        created (datetime.datetime | Unset): The game created time
        updated (datetime.datetime | Unset): The game updated time
        studio_access_to_apis_allowed (bool | Unset): The setting of IsStudioAccessToApisAllowed of the universe
        create_vip_servers_allowed (bool | Unset): Gets or sets the flag to indicate whether the create vip servers
            button should be allowed in game details page
        universe_avatar_type (RobloxGamesApiModelsResponseGameDetailResponseUniverseAvatarType | Unset): Avatar type.
            Possible values are MorphToR6, MorphToR15, and PlayerChoice
        genre (str | Unset): The game genre display name
        genre_l1 (str | Unset): The game genre from experience-genres-service
        genre_l2 (str | Unset): The game subgenre from experience-genres-service
        untranslated_genre_l1 (str | Unset): The game genre from experience-genres-service untranslated
        is_all_genre (bool | Unset): Is this game all genre.
        is_favorited_by_user (bool | Unset): Is this game favorited by user.
        favorited_count (int | Unset): Game number of favorites.
        license_description (str | Unset):
        refund_link (str | Unset):
        localized_fiat_price (str | Unset):
        refund_policy (RobloxGamesApiModelsResponseRefundPolicy | Unset):
        canonical_url_path (str | Unset): Canonical URL path for the game page, e.g. /games/{placeId}/{canonical-slug}.
            It must be the same as the canonical URL (rel-canonical meta tag) on the game's EDP.
        is_content_restricted (bool | Unset): Indicates whether this experience is content-restricted and has had its
            details wiped.
            When true, the content fields (name, description, creator, etc.) contain placeholder or
            empty values rather than the real data. Consumers should branch on this flag instead of
            inferring restriction from placeholder text.
    """

    id: int | Unset = UNSET
    root_place_id: int | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    source_name: str | Unset = UNSET
    source_description: str | Unset = UNSET
    creator: RobloxGamesApiModelsResponseGameCreator | Unset = UNSET
    price: int | Unset = UNSET
    allowed_gear_genres: list[str] | Unset = UNSET
    allowed_gear_categories: list[str] | Unset = UNSET
    is_genre_enforced: bool | Unset = UNSET
    copying_allowed: bool | Unset = UNSET
    playing: int | Unset = UNSET
    visits: int | Unset = UNSET
    max_players: int | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    updated: datetime.datetime | Unset = UNSET
    studio_access_to_apis_allowed: bool | Unset = UNSET
    create_vip_servers_allowed: bool | Unset = UNSET
    universe_avatar_type: RobloxGamesApiModelsResponseGameDetailResponseUniverseAvatarType | Unset = UNSET
    genre: str | Unset = UNSET
    genre_l1: str | Unset = UNSET
    genre_l2: str | Unset = UNSET
    untranslated_genre_l1: str | Unset = UNSET
    is_all_genre: bool | Unset = UNSET
    is_favorited_by_user: bool | Unset = UNSET
    favorited_count: int | Unset = UNSET
    license_description: str | Unset = UNSET
    refund_link: str | Unset = UNSET
    localized_fiat_price: str | Unset = UNSET
    refund_policy: RobloxGamesApiModelsResponseRefundPolicy | Unset = UNSET
    canonical_url_path: str | Unset = UNSET
    is_content_restricted: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        root_place_id = self.root_place_id

        name = self.name

        description = self.description

        source_name = self.source_name

        source_description = self.source_description

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        price = self.price

        allowed_gear_genres: list[str] | Unset = UNSET
        if not isinstance(self.allowed_gear_genres, Unset):
            allowed_gear_genres = self.allowed_gear_genres

        allowed_gear_categories: list[str] | Unset = UNSET
        if not isinstance(self.allowed_gear_categories, Unset):
            allowed_gear_categories = self.allowed_gear_categories

        is_genre_enforced = self.is_genre_enforced

        copying_allowed = self.copying_allowed

        playing = self.playing

        visits = self.visits

        max_players = self.max_players

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        studio_access_to_apis_allowed = self.studio_access_to_apis_allowed

        create_vip_servers_allowed = self.create_vip_servers_allowed

        universe_avatar_type: int | Unset = UNSET
        if not isinstance(self.universe_avatar_type, Unset):
            universe_avatar_type = self.universe_avatar_type.value

        genre = self.genre

        genre_l1 = self.genre_l1

        genre_l2 = self.genre_l2

        untranslated_genre_l1 = self.untranslated_genre_l1

        is_all_genre = self.is_all_genre

        is_favorited_by_user = self.is_favorited_by_user

        favorited_count = self.favorited_count

        license_description = self.license_description

        refund_link = self.refund_link

        localized_fiat_price = self.localized_fiat_price

        refund_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.refund_policy, Unset):
            refund_policy = self.refund_policy.to_dict()

        canonical_url_path = self.canonical_url_path

        is_content_restricted = self.is_content_restricted

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if root_place_id is not UNSET:
            field_dict["rootPlaceId"] = root_place_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if source_name is not UNSET:
            field_dict["sourceName"] = source_name
        if source_description is not UNSET:
            field_dict["sourceDescription"] = source_description
        if creator is not UNSET:
            field_dict["creator"] = creator
        if price is not UNSET:
            field_dict["price"] = price
        if allowed_gear_genres is not UNSET:
            field_dict["allowedGearGenres"] = allowed_gear_genres
        if allowed_gear_categories is not UNSET:
            field_dict["allowedGearCategories"] = allowed_gear_categories
        if is_genre_enforced is not UNSET:
            field_dict["isGenreEnforced"] = is_genre_enforced
        if copying_allowed is not UNSET:
            field_dict["copyingAllowed"] = copying_allowed
        if playing is not UNSET:
            field_dict["playing"] = playing
        if visits is not UNSET:
            field_dict["visits"] = visits
        if max_players is not UNSET:
            field_dict["maxPlayers"] = max_players
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if studio_access_to_apis_allowed is not UNSET:
            field_dict["studioAccessToApisAllowed"] = studio_access_to_apis_allowed
        if create_vip_servers_allowed is not UNSET:
            field_dict["createVipServersAllowed"] = create_vip_servers_allowed
        if universe_avatar_type is not UNSET:
            field_dict["universeAvatarType"] = universe_avatar_type
        if genre is not UNSET:
            field_dict["genre"] = genre
        if genre_l1 is not UNSET:
            field_dict["genre_l1"] = genre_l1
        if genre_l2 is not UNSET:
            field_dict["genre_l2"] = genre_l2
        if untranslated_genre_l1 is not UNSET:
            field_dict["untranslated_genre_l1"] = untranslated_genre_l1
        if is_all_genre is not UNSET:
            field_dict["isAllGenre"] = is_all_genre
        if is_favorited_by_user is not UNSET:
            field_dict["isFavoritedByUser"] = is_favorited_by_user
        if favorited_count is not UNSET:
            field_dict["favoritedCount"] = favorited_count
        if license_description is not UNSET:
            field_dict["licenseDescription"] = license_description
        if refund_link is not UNSET:
            field_dict["refundLink"] = refund_link
        if localized_fiat_price is not UNSET:
            field_dict["localizedFiatPrice"] = localized_fiat_price
        if refund_policy is not UNSET:
            field_dict["refundPolicy"] = refund_policy
        if canonical_url_path is not UNSET:
            field_dict["canonicalUrlPath"] = canonical_url_path
        if is_content_restricted is not UNSET:
            field_dict["isContentRestricted"] = is_content_restricted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_games_api_models_response_game_creator import RobloxGamesApiModelsResponseGameCreator
        from ..models.roblox_games_api_models_response_refund_policy import RobloxGamesApiModelsResponseRefundPolicy

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        root_place_id = d.pop("rootPlaceId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        source_name = d.pop("sourceName", UNSET)

        source_description = d.pop("sourceDescription", UNSET)

        _creator = d.pop("creator", UNSET)
        creator: RobloxGamesApiModelsResponseGameCreator | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = RobloxGamesApiModelsResponseGameCreator.from_dict(_creator)

        price = d.pop("price", UNSET)

        allowed_gear_genres = cast(list[str], d.pop("allowedGearGenres", UNSET))

        allowed_gear_categories = cast(list[str], d.pop("allowedGearCategories", UNSET))

        is_genre_enforced = d.pop("isGenreEnforced", UNSET)

        copying_allowed = d.pop("copyingAllowed", UNSET)

        playing = d.pop("playing", UNSET)

        visits = d.pop("visits", UNSET)

        max_players = d.pop("maxPlayers", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        _updated = d.pop("updated", UNSET)
        updated: datetime.datetime | Unset
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = datetime.datetime.fromisoformat(_updated)

        studio_access_to_apis_allowed = d.pop("studioAccessToApisAllowed", UNSET)

        create_vip_servers_allowed = d.pop("createVipServersAllowed", UNSET)

        _universe_avatar_type = d.pop("universeAvatarType", UNSET)
        universe_avatar_type: RobloxGamesApiModelsResponseGameDetailResponseUniverseAvatarType | Unset
        if isinstance(_universe_avatar_type, Unset):
            universe_avatar_type = UNSET
        else:
            universe_avatar_type = RobloxGamesApiModelsResponseGameDetailResponseUniverseAvatarType(
                _universe_avatar_type
            )

        genre = d.pop("genre", UNSET)

        genre_l1 = d.pop("genre_l1", UNSET)

        genre_l2 = d.pop("genre_l2", UNSET)

        untranslated_genre_l1 = d.pop("untranslated_genre_l1", UNSET)

        is_all_genre = d.pop("isAllGenre", UNSET)

        is_favorited_by_user = d.pop("isFavoritedByUser", UNSET)

        favorited_count = d.pop("favoritedCount", UNSET)

        license_description = d.pop("licenseDescription", UNSET)

        refund_link = d.pop("refundLink", UNSET)

        localized_fiat_price = d.pop("localizedFiatPrice", UNSET)

        _refund_policy = d.pop("refundPolicy", UNSET)
        refund_policy: RobloxGamesApiModelsResponseRefundPolicy | Unset
        if isinstance(_refund_policy, Unset):
            refund_policy = UNSET
        else:
            refund_policy = RobloxGamesApiModelsResponseRefundPolicy.from_dict(_refund_policy)

        canonical_url_path = d.pop("canonicalUrlPath", UNSET)

        is_content_restricted = d.pop("isContentRestricted", UNSET)

        roblox_games_api_models_response_game_detail_response = cls(
            id=id,
            root_place_id=root_place_id,
            name=name,
            description=description,
            source_name=source_name,
            source_description=source_description,
            creator=creator,
            price=price,
            allowed_gear_genres=allowed_gear_genres,
            allowed_gear_categories=allowed_gear_categories,
            is_genre_enforced=is_genre_enforced,
            copying_allowed=copying_allowed,
            playing=playing,
            visits=visits,
            max_players=max_players,
            created=created,
            updated=updated,
            studio_access_to_apis_allowed=studio_access_to_apis_allowed,
            create_vip_servers_allowed=create_vip_servers_allowed,
            universe_avatar_type=universe_avatar_type,
            genre=genre,
            genre_l1=genre_l1,
            genre_l2=genre_l2,
            untranslated_genre_l1=untranslated_genre_l1,
            is_all_genre=is_all_genre,
            is_favorited_by_user=is_favorited_by_user,
            favorited_count=favorited_count,
            license_description=license_description,
            refund_link=refund_link,
            localized_fiat_price=localized_fiat_price,
            refund_policy=refund_policy,
            canonical_url_path=canonical_url_path,
            is_content_restricted=is_content_restricted,
        )

        return roblox_games_api_models_response_game_detail_response
