from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.event_visibility import EventVisibility
from ..models.featuring_status import FeaturingStatus
from ..models.rsvp_status import RsvpStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_response import CategoryResponse
    from ..models.config_response import ConfigResponse
    from ..models.host_response import HostResponse
    from ..models.thumbnail_response import ThumbnailResponse


T = TypeVar("T", bound="GameEventResponse")


@_attrs_define
class GameEventResponse:
    """v3 game event response. All fields except VirtualEventsApi.Models.V3.Response.GameEventResponse.Id are gated by the
    `?fields=` mask.

        Attributes:
            id (None | str | Unset): The unique id of the game event. Always populated. Serialized as a string to
                preserve precision for clients (event IDs exceed 2^53).
            title (None | str | Unset):
            display_title (None | str | Unset): Localized title (caller's locale). Populated only when `displayTitle` is in
                the mask.
            subtitle (None | str | Unset):
            display_subtitle (None | str | Unset): Localized subtitle. Populated only when `displaySubtitle` is in the mask.
            description (None | str | Unset):
            display_description (None | str | Unset): Localized description. Populated only when `displayDescription` is in
                the mask.
            start_time (datetime.datetime | None | Unset):
            end_time (datetime.datetime | None | Unset):
            universe_id (int | None | Unset):
            place_id (int | None | Unset):
            host (HostResponse | None | Unset): Host block. VirtualEventsApi.Models.V3.Response.HostResponse.HostName and
                VirtualEventsApi.Models.V3.Response.HostResponse.HasVerifiedBadge are omitted when host-details resolution
                failed.
            visibility (EventVisibility | None | Unset):
            featuring_status (FeaturingStatus | None | Unset):
            tagline (None | str | Unset): Tagline for featuring review; visible to curators only when featuring is opted
                into.
            categories (list[CategoryResponse] | None | Unset):
            thumbnails (list[ThumbnailResponse] | None | Unset):
            all_thumbnails_created (bool | None | Unset): Whether all requested thumbnails were successfully persisted.
                Returned on Create/Update.
            config (ConfigResponse | None | Unset):
            user_rsvp_status (None | RsvpStatus | Unset): Authenticated caller's RSVP status. Omitted for unauthenticated
                callers.
            create_time (datetime.datetime | None | Unset):
            update_time (datetime.datetime | None | Unset):
    """

    id: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    display_title: None | str | Unset = UNSET
    subtitle: None | str | Unset = UNSET
    display_subtitle: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    display_description: None | str | Unset = UNSET
    start_time: datetime.datetime | None | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    universe_id: int | None | Unset = UNSET
    place_id: int | None | Unset = UNSET
    host: HostResponse | None | Unset = UNSET
    visibility: EventVisibility | None | Unset = UNSET
    featuring_status: FeaturingStatus | None | Unset = UNSET
    tagline: None | str | Unset = UNSET
    categories: list[CategoryResponse] | None | Unset = UNSET
    thumbnails: list[ThumbnailResponse] | None | Unset = UNSET
    all_thumbnails_created: bool | None | Unset = UNSET
    config: ConfigResponse | None | Unset = UNSET
    user_rsvp_status: None | RsvpStatus | Unset = UNSET
    create_time: datetime.datetime | None | Unset = UNSET
    update_time: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.config_response import ConfigResponse
        from ..models.host_response import HostResponse

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        display_title: None | str | Unset
        if isinstance(self.display_title, Unset):
            display_title = UNSET
        else:
            display_title = self.display_title

        subtitle: None | str | Unset
        if isinstance(self.subtitle, Unset):
            subtitle = UNSET
        else:
            subtitle = self.subtitle

        display_subtitle: None | str | Unset
        if isinstance(self.display_subtitle, Unset):
            display_subtitle = UNSET
        else:
            display_subtitle = self.display_subtitle

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        display_description: None | str | Unset
        if isinstance(self.display_description, Unset):
            display_description = UNSET
        else:
            display_description = self.display_description

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

        universe_id: int | None | Unset
        if isinstance(self.universe_id, Unset):
            universe_id = UNSET
        else:
            universe_id = self.universe_id

        place_id: int | None | Unset
        if isinstance(self.place_id, Unset):
            place_id = UNSET
        else:
            place_id = self.place_id

        host: dict[str, Any] | None | Unset
        if isinstance(self.host, Unset):
            host = UNSET
        elif isinstance(self.host, HostResponse):
            host = self.host.to_dict()
        else:
            host = self.host

        visibility: None | str | Unset
        if isinstance(self.visibility, Unset):
            visibility = UNSET
        elif isinstance(self.visibility, EventVisibility):
            visibility = self.visibility.value
        else:
            visibility = self.visibility

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

        all_thumbnails_created: bool | None | Unset
        if isinstance(self.all_thumbnails_created, Unset):
            all_thumbnails_created = UNSET
        else:
            all_thumbnails_created = self.all_thumbnails_created

        config: dict[str, Any] | None | Unset
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, ConfigResponse):
            config = self.config.to_dict()
        else:
            config = self.config

        user_rsvp_status: None | str | Unset
        if isinstance(self.user_rsvp_status, Unset):
            user_rsvp_status = UNSET
        elif isinstance(self.user_rsvp_status, RsvpStatus):
            user_rsvp_status = self.user_rsvp_status.value
        else:
            user_rsvp_status = self.user_rsvp_status

        create_time: None | str | Unset
        if isinstance(self.create_time, Unset):
            create_time = UNSET
        elif isinstance(self.create_time, datetime.datetime):
            create_time = self.create_time.isoformat()
        else:
            create_time = self.create_time

        update_time: None | str | Unset
        if isinstance(self.update_time, Unset):
            update_time = UNSET
        elif isinstance(self.update_time, datetime.datetime):
            update_time = self.update_time.isoformat()
        else:
            update_time = self.update_time

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if display_title is not UNSET:
            field_dict["displayTitle"] = display_title
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if display_subtitle is not UNSET:
            field_dict["displaySubtitle"] = display_subtitle
        if description is not UNSET:
            field_dict["description"] = description
        if display_description is not UNSET:
            field_dict["displayDescription"] = display_description
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if place_id is not UNSET:
            field_dict["placeId"] = place_id
        if host is not UNSET:
            field_dict["host"] = host
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if featuring_status is not UNSET:
            field_dict["featuringStatus"] = featuring_status
        if tagline is not UNSET:
            field_dict["tagline"] = tagline
        if categories is not UNSET:
            field_dict["categories"] = categories
        if thumbnails is not UNSET:
            field_dict["thumbnails"] = thumbnails
        if all_thumbnails_created is not UNSET:
            field_dict["allThumbnailsCreated"] = all_thumbnails_created
        if config is not UNSET:
            field_dict["config"] = config
        if user_rsvp_status is not UNSET:
            field_dict["userRsvpStatus"] = user_rsvp_status
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if update_time is not UNSET:
            field_dict["updateTime"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category_response import CategoryResponse
        from ..models.config_response import ConfigResponse
        from ..models.host_response import HostResponse
        from ..models.thumbnail_response import ThumbnailResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_display_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_title = _parse_display_title(d.pop("displayTitle", UNSET))

        def _parse_subtitle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subtitle = _parse_subtitle(d.pop("subtitle", UNSET))

        def _parse_display_subtitle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_subtitle = _parse_display_subtitle(d.pop("displaySubtitle", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_display_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_description = _parse_display_description(d.pop("displayDescription", UNSET))

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

        def _parse_universe_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        universe_id = _parse_universe_id(d.pop("universeId", UNSET))

        def _parse_place_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        place_id = _parse_place_id(d.pop("placeId", UNSET))

        def _parse_host(data: object) -> HostResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                host_type_1 = HostResponse.from_dict(data)

                return host_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HostResponse | None | Unset, data)

        host = _parse_host(d.pop("host", UNSET))

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

        def _parse_categories(data: object) -> list[CategoryResponse] | None | Unset:
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
                    categories_type_0_item = CategoryResponse.from_dict(categories_type_0_item_data)

                    categories_type_0.append(categories_type_0_item)

                return categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CategoryResponse] | None | Unset, data)

        categories = _parse_categories(d.pop("categories", UNSET))

        def _parse_thumbnails(data: object) -> list[ThumbnailResponse] | None | Unset:
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
                    thumbnails_type_0_item = ThumbnailResponse.from_dict(thumbnails_type_0_item_data)

                    thumbnails_type_0.append(thumbnails_type_0_item)

                return thumbnails_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ThumbnailResponse] | None | Unset, data)

        thumbnails = _parse_thumbnails(d.pop("thumbnails", UNSET))

        def _parse_all_thumbnails_created(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        all_thumbnails_created = _parse_all_thumbnails_created(d.pop("allThumbnailsCreated", UNSET))

        def _parse_config(data: object) -> ConfigResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_1 = ConfigResponse.from_dict(data)

                return config_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConfigResponse | None | Unset, data)

        config = _parse_config(d.pop("config", UNSET))

        def _parse_user_rsvp_status(data: object) -> None | RsvpStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_rsvp_status_type_1 = RsvpStatus(data)

                return user_rsvp_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RsvpStatus | Unset, data)

        user_rsvp_status = _parse_user_rsvp_status(d.pop("userRsvpStatus", UNSET))

        def _parse_create_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                create_time_type_0 = datetime.datetime.fromisoformat(data)

                return create_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        create_time = _parse_create_time(d.pop("createTime", UNSET))

        def _parse_update_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                update_time_type_0 = datetime.datetime.fromisoformat(data)

                return update_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        update_time = _parse_update_time(d.pop("updateTime", UNSET))

        game_event_response = cls(
            id=id,
            title=title,
            display_title=display_title,
            subtitle=subtitle,
            display_subtitle=display_subtitle,
            description=description,
            display_description=display_description,
            start_time=start_time,
            end_time=end_time,
            universe_id=universe_id,
            place_id=place_id,
            host=host,
            visibility=visibility,
            featuring_status=featuring_status,
            tagline=tagline,
            categories=categories,
            thumbnails=thumbnails,
            all_thumbnails_created=all_thumbnails_created,
            config=config,
            user_rsvp_status=user_rsvp_status,
            create_time=create_time,
            update_time=update_time,
        )

        return game_event_response
