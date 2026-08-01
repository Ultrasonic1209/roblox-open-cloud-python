from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.event_visibility import EventVisibility
from ..models.featuring_status import FeaturingStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_game_event_config_request import CreateGameEventConfigRequest
    from ..models.event_media import EventMedia
    from ..models.event_ranked_category import EventRankedCategory


T = TypeVar("T", bound="CreateGameEventRequest")


@_attrs_define
class CreateGameEventRequest:
    """Request body for `POST /v3/universes/{universeId}/game-events`.
    `universeId` comes from the URL path, not the body.
    VirtualEventsApi.Models.V3.Request.CreateGameEventRequest.Visibility is restricted to Public/Private — Moderated is
    server-side only.
    Nullable CLR properties allow JSON binding to materialize incomplete requests; required
    fields are enforced by the virtual-events gRPC service when `CreateVirtualEvent` runs.

        Attributes:
            title (None | str | Unset): Event title. Clients must provide a non-empty value.
            subtitle (None | str | Unset): Event subtitle. Clients must provide a non-empty value.
            description (None | str | Unset): Optional event description.
            start_time (datetime.datetime | None | Unset): Event start time. Clients must provide a timestamp such as
                `yyyy-MM-ddTHH:mm:ss.fffzzz` or `yyyy-MM-ddTHH:mm:ss.fffZ`.
            end_time (datetime.datetime | None | Unset): Event end time. Clients must provide a timestamp such as
                `yyyy-MM-ddTHH:mm:ss.fffzzz` or `yyyy-MM-ddTHH:mm:ss.fffZ`, and it must be after
                VirtualEventsApi.Models.V3.Request.CreateGameEventRequest.StartTime.
            visibility (EventVisibility | None | Unset): Must be `Public` or `Private`; `Moderated` is server-managed and
                rejected.
            group_id (int | None | Unset): Group host. When omitted, the authenticated user is the host.
            place_id (int | None | Unset): Optional venue place ID. When omitted, the event is created in the universe root
                place.
            categories (list[EventRankedCategory] | None | Unset):
            thumbnails (list[EventMedia] | None | Unset):
            config (CreateGameEventConfigRequest | None | Unset): Optional event configuration block (recurrence +
                notification audience) on the v3 Create body.
            featuring_status (FeaturingStatus | None | Unset): Optional featuring status flag. When omitted, defaults to
                "not featured".
            tagline (None | str | Unset): Optional tagline. Length and content are validated server-side.
    """

    title: None | str | Unset = UNSET
    subtitle: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    start_time: datetime.datetime | None | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    visibility: EventVisibility | None | Unset = UNSET
    group_id: int | None | Unset = UNSET
    place_id: int | None | Unset = UNSET
    categories: list[EventRankedCategory] | None | Unset = UNSET
    thumbnails: list[EventMedia] | None | Unset = UNSET
    config: CreateGameEventConfigRequest | None | Unset = UNSET
    featuring_status: FeaturingStatus | None | Unset = UNSET
    tagline: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_game_event_config_request import CreateGameEventConfigRequest

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

        group_id: int | None | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        else:
            group_id = self.group_id

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
        elif isinstance(self.config, CreateGameEventConfigRequest):
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
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
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
        from ..models.create_game_event_config_request import CreateGameEventConfigRequest
        from ..models.event_media import EventMedia
        from ..models.event_ranked_category import EventRankedCategory

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

        def _parse_group_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        group_id = _parse_group_id(d.pop("groupId", UNSET))

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

        def _parse_config(data: object) -> CreateGameEventConfigRequest | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_1 = CreateGameEventConfigRequest.from_dict(data)

                return config_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateGameEventConfigRequest | None | Unset, data)

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

        create_game_event_request = cls(
            title=title,
            subtitle=subtitle,
            description=description,
            start_time=start_time,
            end_time=end_time,
            visibility=visibility,
            group_id=group_id,
            place_id=place_id,
            categories=categories,
            thumbnails=thumbnails,
            config=config,
            featuring_status=featuring_status,
            tagline=tagline,
        )

        return create_game_event_request
