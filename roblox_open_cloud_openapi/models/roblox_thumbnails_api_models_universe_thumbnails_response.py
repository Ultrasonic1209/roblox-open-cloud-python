from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_web_web_api_models_api_error_model import RobloxWebWebAPIModelsApiErrorModel
    from ..models.thumbnails_api_roblox_web_responses_thumbnails_thumbnail_response import (
        ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse,
    )


T = TypeVar("T", bound="RobloxThumbnailsApiModelsUniverseThumbnailsResponse")


@_attrs_define
class RobloxThumbnailsApiModelsUniverseThumbnailsResponse:
    """A response model for thumbnails which belong to a specific universe ID

    Attributes:
        universe_id (int | Unset): Integer universe ID
        error (RobloxWebWebAPIModelsApiErrorModel | Unset):
        thumbnails (list[ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse] | Unset): An array of
            ThumbnailResponse objects
    """

    universe_id: int | Unset = UNSET
    error: RobloxWebWebAPIModelsApiErrorModel | Unset = UNSET
    thumbnails: list[ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        universe_id = self.universe_id

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        thumbnails: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.thumbnails, Unset):
            thumbnails = []
            for thumbnails_item_data in self.thumbnails:
                thumbnails_item = thumbnails_item_data.to_dict()
                thumbnails.append(thumbnails_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if error is not UNSET:
            field_dict["error"] = error
        if thumbnails is not UNSET:
            field_dict["thumbnails"] = thumbnails

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_web_web_api_models_api_error_model import RobloxWebWebAPIModelsApiErrorModel
        from ..models.thumbnails_api_roblox_web_responses_thumbnails_thumbnail_response import (
            ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse,
        )

        d = dict(src_dict)
        universe_id = d.pop("universeId", UNSET)

        _error = d.pop("error", UNSET)
        error: RobloxWebWebAPIModelsApiErrorModel | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = RobloxWebWebAPIModelsApiErrorModel.from_dict(_error)

        _thumbnails = d.pop("thumbnails", UNSET)
        thumbnails: list[ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse] | Unset = UNSET
        if _thumbnails is not UNSET:
            thumbnails = []
            for thumbnails_item_data in _thumbnails:
                thumbnails_item = ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse.from_dict(
                    thumbnails_item_data
                )

                thumbnails.append(thumbnails_item)

        roblox_thumbnails_api_models_universe_thumbnails_response = cls(
            universe_id=universe_id,
            error=error,
            thumbnails=thumbnails,
        )

        return roblox_thumbnails_api_models_universe_thumbnails_response
