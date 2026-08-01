from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.event_visibility import EventVisibility
from ..models.featuring_status import FeaturingStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_media import EventMedia
    from ..models.event_ranked_category import EventRankedCategory
    from ..models.update_game_event_config_request import UpdateGameEventConfigRequest


T = TypeVar("T", bound="UpdateGameEventRequest")


@_attrs_define
class UpdateGameEventRequest:
    """Request body for `PATCH /v3/game-events/{eventId}`.
    Every field is optional; null = "no change". An empty body is a no-op and returns the current resource.

        Attributes:
            title (None | str | Unset):
            subtitle (None | str | Unset):
            description (None | str | Unset):
            start_time (datetime.datetime | None | Unset):
            end_time (datetime.datetime | None | Unset):
            visibility (EventVisibility | None | Unset): Must be `Public` or `Private`; other values are rejected. Null = no
                change.
            place_id (int | None | Unset):
            categories (list[EventRankedCategory] | None | Unset):
            thumbnails (list[EventMedia] | None | Unset):
            config (None | Unset | UpdateGameEventConfigRequest): Optional config block on the v3 PATCH body. Null sub-
                fields = no change.
            featuring_status (FeaturingStatus | None | Unset):
            tagline (None | str | Unset):
    """

    title: None | str | Unset = UNSET
    subtitle: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    start_time: datetime.datetime | None | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    visibility: EventVisibility | None | Unset = UNSET
    place_id: int | None | Unset = UNSET
    categories: list[EventRankedCategory] | None | Unset = UNSET
    thumbnails: list[EventMedia] | None | Unset = UNSET
    config: None | Unset | UpdateGameEventConfigRequest = UNSET
    featuring_status: FeaturingStatus | None | Unset = UNSET
    tagline: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_game_event_config_request import UpdateGameEventConfigRequest

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        subtitle: None | str | Unset
        if isinstance(self.subtitle, Unset):
            subtitle = UNSET
        else:
            subtitle = self.subtitle

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        start_time: None | str | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        elif isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        visibility: None | str | Unset
        if isinstance(self.visibility, Unset):
            visibility = UNSET
        elif isinstance(self.visibility, EventVisibility):
            visibility = self.visibility.value
        else:
            visibility = self.visibility

        place_id: int | None | Unset
        if isinstance(self.place_id, Unset):
            place_id = UNSET
        else:
            place_id = self.place_id

        categories: list[dict[str, Any]] | None | Unset
        if isinstance(self.categories, Unset):
            categories = UNSET
        elif isinstance(self.categories, list):
            categories = []
            for categories_type_0_item_data in self.categories:
                categories_type_0_item = categories_type_0_item_data.to_dict()
                categories.append(categories_type_0_item)

        else:
            categories = self.categories

        thumbnails: list[dict[str, Any]] | None | Unset
        if isinstance(self.thumbnails, Unset):
            thumbnails = UNSET
        elif isinstance(self.thumbnails, list):
            thumbnails = []
            for thumbnails_type_0_item_data in self.thumbnails:
                thumbnails_type_0_item = thumbnails_type_0_item_data.to_dict()
                thumbnails.append(thumbnails_type_0_item)

        else:
            thumbnails = self.thumbnails

        config: dict[str, Any] | None | Unset
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, UpdateGameEventConfigRequest):
            config = self.config.to_dict()
        else:
            config = self.config

        featuring_status: None | str | Unset
        if isinstance(self.featuring_status, Unset):
            featuring_status = UNSET
        elif isinstance(self.featuring_status, FeaturingStatus):
            featuring_status = self.featuring_status.value
        else:
            featuring_status = self.featuring_status

        tagline: None | str | Unset
        if isinstance(self.tagline, Unset):
            tagline = UNSET
        else:
            tagline = self.tagline

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if description is not UNSET:
            field_dict["description"] = description
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if place_id is not UNSET:
            field_dict["placeId"] = place_id
        if categories is not UNSET:
            field_dict["categories"] = categories
        if thumbnails is not UNSET:
            field_dict["thumbnails"] = thumbnails
        if config is not UNSET:
            field_dict["config"] = config
        if featuring_status is not UNSET:
            field_dict["featuringStatus"] = featuring_status
        if tagline is not UNSET:
            field_dict["tagline"] = tagline

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_media import EventMedia
        from ..models.event_ranked_category import EventRankedCategory
        from ..models.update_game_event_config_request import UpdateGameEventConfigRequest

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_subtitle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subtitle = _parse_subtitle(d.pop("subtitle", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_start_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_0 = datetime.datetime.fromisoformat(data)

                return start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_time = _parse_start_time(d.pop("startTime", UNSET))

        def _parse_end_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = datetime.datetime.fromisoformat(data)

                return end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_time = _parse_end_time(d.pop("endTime", UNSET))

        def _parse_visibility(data: object) -> EventVisibility | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                visibility_type_1 = EventVisibility(data)

                return visibility_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EventVisibility | None | Unset, data)

        visibility = _parse_visibility(d.pop("visibility", UNSET))

        def _parse_place_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        place_id = _parse_place_id(d.pop("placeId", UNSET))

        def _parse_categories(data: object) -> list[EventRankedCategory] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                categories_type_0 = []
                _categories_type_0 = data
                for categories_type_0_item_data in _categories_type_0:
                    categories_type_0_item = EventRankedCategory.from_dict(categories_type_0_item_data)

                    categories_type_0.append(categories_type_0_item)

                return categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EventRankedCategory] | None | Unset, data)

        categories = _parse_categories(d.pop("categories", UNSET))

        def _parse_thumbnails(data: object) -> list[EventMedia] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                thumbnails_type_0 = []
                _thumbnails_type_0 = data
                for thumbnails_type_0_item_data in _thumbnails_type_0:
                    thumbnails_type_0_item = EventMedia.from_dict(thumbnails_type_0_item_data)

                    thumbnails_type_0.append(thumbnails_type_0_item)

                return thumbnails_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EventMedia] | None | Unset, data)

        thumbnails = _parse_thumbnails(d.pop("thumbnails", UNSET))

        def _parse_config(data: object) -> None | Unset | UpdateGameEventConfigRequest:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_1 = UpdateGameEventConfigRequest.from_dict(data)

                return config_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateGameEventConfigRequest, data)

        config = _parse_config(d.pop("config", UNSET))

        def _parse_featuring_status(data: object) -> FeaturingStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                featuring_status_type_1 = FeaturingStatus(data)

                return featuring_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FeaturingStatus | None | Unset, data)

        featuring_status = _parse_featuring_status(d.pop("featuringStatus", UNSET))

        def _parse_tagline(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tagline = _parse_tagline(d.pop("tagline", UNSET))

        update_game_event_request = cls(
            title=title,
            subtitle=subtitle,
            description=description,
            start_time=start_time,
            end_time=end_time,
            visibility=visibility,
            place_id=place_id,
            categories=categories,
            thumbnails=thumbnails,
            config=config,
            featuring_status=featuring_status,
            tagline=tagline,
        )

        return update_game_event_request
