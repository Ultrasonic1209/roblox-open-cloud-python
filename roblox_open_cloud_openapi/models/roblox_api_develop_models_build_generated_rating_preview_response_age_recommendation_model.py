from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationModel")


@_attrs_define
class RobloxApiDevelopModelsBuildGeneratedRatingPreviewResponseAgeRecommendationModel:
    """Age recommendation.

    Attributes:
        display_name (str | Unset): Localized display name.
        minimum_age (int | Unset): Minimum recommended age.
        display_name_with_header_short (str | Unset): Localized short display name including the maturity header.
        minimum_age_display (str | Unset): Localized minimum-age display value.
        content_maturity (str | Unset): Explicit content maturity value.
        igrs_rating (str | Unset): IGRS rating enum name, when present.
        igrs_rating_display_message (str | Unset): Localized IGRS rating display message, when present.
    """

    display_name: str | Unset = UNSET
    minimum_age: int | Unset = UNSET
    display_name_with_header_short: str | Unset = UNSET
    minimum_age_display: str | Unset = UNSET
    content_maturity: str | Unset = UNSET
    igrs_rating: str | Unset = UNSET
    igrs_rating_display_message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        minimum_age = self.minimum_age

        display_name_with_header_short = self.display_name_with_header_short

        minimum_age_display = self.minimum_age_display

        content_maturity = self.content_maturity

        igrs_rating = self.igrs_rating

        igrs_rating_display_message = self.igrs_rating_display_message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if minimum_age is not UNSET:
            field_dict["minimumAge"] = minimum_age
        if display_name_with_header_short is not UNSET:
            field_dict["displayNameWithHeaderShort"] = display_name_with_header_short
        if minimum_age_display is not UNSET:
            field_dict["minimumAgeDisplay"] = minimum_age_display
        if content_maturity is not UNSET:
            field_dict["contentMaturity"] = content_maturity
        if igrs_rating is not UNSET:
            field_dict["igrsRating"] = igrs_rating
        if igrs_rating_display_message is not UNSET:
            field_dict["igrsRatingDisplayMessage"] = igrs_rating_display_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        display_name = d.pop("displayName", UNSET)

        minimum_age = d.pop("minimumAge", UNSET)

        display_name_with_header_short = d.pop("displayNameWithHeaderShort", UNSET)

        minimum_age_display = d.pop("minimumAgeDisplay", UNSET)

        content_maturity = d.pop("contentMaturity", UNSET)

        igrs_rating = d.pop("igrsRating", UNSET)

        igrs_rating_display_message = d.pop("igrsRatingDisplayMessage", UNSET)

        roblox_api_develop_models_build_generated_rating_preview_response_age_recommendation_model = cls(
            display_name=display_name,
            minimum_age=minimum_age,
            display_name_with_header_short=display_name_with_header_short,
            minimum_age_display=minimum_age_display,
            content_maturity=content_maturity,
            igrs_rating=igrs_rating,
            igrs_rating_display_message=igrs_rating_display_message,
        )

        return roblox_api_develop_models_build_generated_rating_preview_response_age_recommendation_model
