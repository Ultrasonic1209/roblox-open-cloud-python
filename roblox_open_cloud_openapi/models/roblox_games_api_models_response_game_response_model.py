from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_games_api_models_response_game_content_metadata_response_model import (
        RobloxGamesApiModelsResponseGameContentMetadataResponseModel,
    )


T = TypeVar("T", bound="RobloxGamesApiModelsResponseGameResponseModel")


@_attrs_define
class RobloxGamesApiModelsResponseGameResponseModel:
    """Response model for games.

    Attributes:
        creator_id (int | Unset): Creator Id
        creator_name (str | Unset): Creator name
        creator_type (str | Unset): Creator type
        creator_has_verified_badge (bool | Unset): Creator verified badge status
        total_up_votes (int | Unset): Total up votes
        total_down_votes (int | Unset): Total down votes
        universe_id (int | Unset): Universe id
        name (str | Unset): Game name
        place_id (int | Unset): Place Id
        player_count (int | Unset): Player count
        image_token (str | Unset): Place image token
        is_sponsored (bool | Unset): Is sponsored
        native_ad_data (str | Unset): Native ad data
        is_show_sponsored_label (bool | Unset): Show the sponsored label
        price (int | Unset): The game paid access price
        analytics_identifier (str | Unset): Provide all necessary information which helps analytics for improvement, for
            example, the algorithm, dataset version, position, etc..
        game_description (str | Unset): Provide all necessary information which helps analytics for improvement, for
            example, the algorithm, dataset version, position, etc..
        genre (str | Unset): The game genre display name
        minimum_age (int | Unset): Age Recommendation minimum age.
        age_recommendation_display_name (str | Unset): Age Recommendation display name.
        content_metadata (RobloxGamesApiModelsResponseGameContentMetadataResponseModel | Unset): Response model for
            game-level content metadata.
        canonical_url_path (str | Unset): Canonical URL path for the game page, e.g. /games/{placeId}/{canonical-slug}.
            It must be the same as the canonical URL (rel-canonical meta tag) on the game's EDP.
    """

    creator_id: int | Unset = UNSET
    creator_name: str | Unset = UNSET
    creator_type: str | Unset = UNSET
    creator_has_verified_badge: bool | Unset = UNSET
    total_up_votes: int | Unset = UNSET
    total_down_votes: int | Unset = UNSET
    universe_id: int | Unset = UNSET
    name: str | Unset = UNSET
    place_id: int | Unset = UNSET
    player_count: int | Unset = UNSET
    image_token: str | Unset = UNSET
    is_sponsored: bool | Unset = UNSET
    native_ad_data: str | Unset = UNSET
    is_show_sponsored_label: bool | Unset = UNSET
    price: int | Unset = UNSET
    analytics_identifier: str | Unset = UNSET
    game_description: str | Unset = UNSET
    genre: str | Unset = UNSET
    minimum_age: int | Unset = UNSET
    age_recommendation_display_name: str | Unset = UNSET
    content_metadata: RobloxGamesApiModelsResponseGameContentMetadataResponseModel | Unset = UNSET
    canonical_url_path: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        creator_id = self.creator_id

        creator_name = self.creator_name

        creator_type = self.creator_type

        creator_has_verified_badge = self.creator_has_verified_badge

        total_up_votes = self.total_up_votes

        total_down_votes = self.total_down_votes

        universe_id = self.universe_id

        name = self.name

        place_id = self.place_id

        player_count = self.player_count

        image_token = self.image_token

        is_sponsored = self.is_sponsored

        native_ad_data = self.native_ad_data

        is_show_sponsored_label = self.is_show_sponsored_label

        price = self.price

        analytics_identifier = self.analytics_identifier

        game_description = self.game_description

        genre = self.genre

        minimum_age = self.minimum_age

        age_recommendation_display_name = self.age_recommendation_display_name

        content_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content_metadata, Unset):
            content_metadata = self.content_metadata.to_dict()

        canonical_url_path = self.canonical_url_path

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if creator_id is not UNSET:
            field_dict["creatorId"] = creator_id
        if creator_name is not UNSET:
            field_dict["creatorName"] = creator_name
        if creator_type is not UNSET:
            field_dict["creatorType"] = creator_type
        if creator_has_verified_badge is not UNSET:
            field_dict["creatorHasVerifiedBadge"] = creator_has_verified_badge
        if total_up_votes is not UNSET:
            field_dict["totalUpVotes"] = total_up_votes
        if total_down_votes is not UNSET:
            field_dict["totalDownVotes"] = total_down_votes
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if name is not UNSET:
            field_dict["name"] = name
        if place_id is not UNSET:
            field_dict["placeId"] = place_id
        if player_count is not UNSET:
            field_dict["playerCount"] = player_count
        if image_token is not UNSET:
            field_dict["imageToken"] = image_token
        if is_sponsored is not UNSET:
            field_dict["isSponsored"] = is_sponsored
        if native_ad_data is not UNSET:
            field_dict["nativeAdData"] = native_ad_data
        if is_show_sponsored_label is not UNSET:
            field_dict["isShowSponsoredLabel"] = is_show_sponsored_label
        if price is not UNSET:
            field_dict["price"] = price
        if analytics_identifier is not UNSET:
            field_dict["analyticsIdentifier"] = analytics_identifier
        if game_description is not UNSET:
            field_dict["gameDescription"] = game_description
        if genre is not UNSET:
            field_dict["genre"] = genre
        if minimum_age is not UNSET:
            field_dict["minimumAge"] = minimum_age
        if age_recommendation_display_name is not UNSET:
            field_dict["ageRecommendationDisplayName"] = age_recommendation_display_name
        if content_metadata is not UNSET:
            field_dict["contentMetadata"] = content_metadata
        if canonical_url_path is not UNSET:
            field_dict["canonicalUrlPath"] = canonical_url_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_games_api_models_response_game_content_metadata_response_model import (
            RobloxGamesApiModelsResponseGameContentMetadataResponseModel,
        )

        d = dict(src_dict)
        creator_id = d.pop("creatorId", UNSET)

        creator_name = d.pop("creatorName", UNSET)

        creator_type = d.pop("creatorType", UNSET)

        creator_has_verified_badge = d.pop("creatorHasVerifiedBadge", UNSET)

        total_up_votes = d.pop("totalUpVotes", UNSET)

        total_down_votes = d.pop("totalDownVotes", UNSET)

        universe_id = d.pop("universeId", UNSET)

        name = d.pop("name", UNSET)

        place_id = d.pop("placeId", UNSET)

        player_count = d.pop("playerCount", UNSET)

        image_token = d.pop("imageToken", UNSET)

        is_sponsored = d.pop("isSponsored", UNSET)

        native_ad_data = d.pop("nativeAdData", UNSET)

        is_show_sponsored_label = d.pop("isShowSponsoredLabel", UNSET)

        price = d.pop("price", UNSET)

        analytics_identifier = d.pop("analyticsIdentifier", UNSET)

        game_description = d.pop("gameDescription", UNSET)

        genre = d.pop("genre", UNSET)

        minimum_age = d.pop("minimumAge", UNSET)

        age_recommendation_display_name = d.pop("ageRecommendationDisplayName", UNSET)

        _content_metadata = d.pop("contentMetadata", UNSET)
        content_metadata: RobloxGamesApiModelsResponseGameContentMetadataResponseModel | Unset
        if isinstance(_content_metadata, Unset):
            content_metadata = UNSET
        else:
            content_metadata = RobloxGamesApiModelsResponseGameContentMetadataResponseModel.from_dict(_content_metadata)

        canonical_url_path = d.pop("canonicalUrlPath", UNSET)

        roblox_games_api_models_response_game_response_model = cls(
            creator_id=creator_id,
            creator_name=creator_name,
            creator_type=creator_type,
            creator_has_verified_badge=creator_has_verified_badge,
            total_up_votes=total_up_votes,
            total_down_votes=total_down_votes,
            universe_id=universe_id,
            name=name,
            place_id=place_id,
            player_count=player_count,
            image_token=image_token,
            is_sponsored=is_sponsored,
            native_ad_data=native_ad_data,
            is_show_sponsored_label=is_show_sponsored_label,
            price=price,
            analytics_identifier=analytics_identifier,
            game_description=game_description,
            genre=genre,
            minimum_age=minimum_age,
            age_recommendation_display_name=age_recommendation_display_name,
            content_metadata=content_metadata,
            canonical_url_path=canonical_url_path,
        )

        return roblox_games_api_models_response_game_response_model
