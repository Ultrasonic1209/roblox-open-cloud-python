from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.dashboard_metadata_lifecycle_state_type_0_type_0 import DashboardMetadataLifecycleStateType0Type0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_actor import DashboardActor


T = TypeVar("T", bound="DashboardMetadata")


@_attrs_define
class DashboardMetadata:
    """DashboardMetadata is the metadata-only shape returned by list calls.
    It intentionally omits the document body so list views do not load dashboard payloads.

        Attributes:
            dashboard_id (None | str | Unset):  Default: ''.
            universe_id (None | str | Unset): Signed 64-bit integer encoded as a decimal string. Default: '0'.
            name (None | str | Unset):  Default: ''.
            description (None | str | Unset):  Default: ''.
            lifecycle_state (DashboardMetadataLifecycleStateType0Type0 | int | None | Unset): DashboardLifecycleState
                describes whether a dashboard is visible to normal reads. Default:
                DashboardMetadataLifecycleStateType0Type0.DASHBOARD_LIFECYCLE_STATE_INVALID.
            is_pinned (bool | None | Unset):  Default: False.
            pinned_time (datetime.datetime | None | Unset):
            created_time (datetime.datetime | None | Unset):
            created_by (DashboardActor | None | Unset): DashboardActor identifies a user responsible for creating or
                mutating dashboard state.
            updated_time (datetime.datetime | None | Unset):
            updated_by (DashboardActor | None | Unset): DashboardActor identifies a user responsible for creating or
                mutating dashboard state.
            published_time (datetime.datetime | None | Unset):
            published_by (DashboardActor | None | Unset): DashboardActor identifies a user responsible for creating or
                mutating dashboard state.
            deleted_time (datetime.datetime | None | Unset):
            deleted_by (DashboardActor | None | Unset): DashboardActor identifies a user responsible for creating or
                mutating dashboard state.
            head_etag (None | str | Unset): Optimistic concurrency token for metadata, publish, and delete mutations.
                Default: ''.
            latest_published_document_id (None | str | Unset): Identifier for the latest persisted dashboard document.
                Latest-only content
                wins; older document payloads are not exposed for backend restore. Default: ''.
            latest_published_version (None | str | Unset): Monotonically increasing version for latest persisted content.
                Default: '0'.
    """

    dashboard_id: None | str | Unset = ""
    universe_id: None | str | Unset = "0"
    name: None | str | Unset = ""
    description: None | str | Unset = ""
    lifecycle_state: DashboardMetadataLifecycleStateType0Type0 | int | None | Unset = (
        DashboardMetadataLifecycleStateType0Type0.DASHBOARD_LIFECYCLE_STATE_INVALID
    )
    is_pinned: bool | None | Unset = False
    pinned_time: datetime.datetime | None | Unset = UNSET
    created_time: datetime.datetime | None | Unset = UNSET
    created_by: DashboardActor | None | Unset = UNSET
    updated_time: datetime.datetime | None | Unset = UNSET
    updated_by: DashboardActor | None | Unset = UNSET
    published_time: datetime.datetime | None | Unset = UNSET
    published_by: DashboardActor | None | Unset = UNSET
    deleted_time: datetime.datetime | None | Unset = UNSET
    deleted_by: DashboardActor | None | Unset = UNSET
    head_etag: None | str | Unset = ""
    latest_published_document_id: None | str | Unset = ""
    latest_published_version: None | str | Unset = "0"

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_actor import DashboardActor  # noqa: PLC0415

        dashboard_id: None | str | Unset
        if isinstance(self.dashboard_id, Unset):
            dashboard_id = UNSET
        else:
            dashboard_id = self.dashboard_id

        universe_id: None | str | Unset
        if isinstance(self.universe_id, Unset):
            universe_id = UNSET
        else:
            universe_id = self.universe_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        lifecycle_state: int | None | str | Unset
        if isinstance(self.lifecycle_state, Unset):
            lifecycle_state = UNSET
        elif isinstance(self.lifecycle_state, DashboardMetadataLifecycleStateType0Type0):
            lifecycle_state = self.lifecycle_state.value
        else:
            lifecycle_state = self.lifecycle_state

        is_pinned: bool | None | Unset
        if isinstance(self.is_pinned, Unset):
            is_pinned = UNSET
        else:
            is_pinned = self.is_pinned

        pinned_time: None | str | Unset
        if isinstance(self.pinned_time, Unset):
            pinned_time = UNSET
        elif isinstance(self.pinned_time, datetime.datetime):
            pinned_time = self.pinned_time.isoformat()
        else:
            pinned_time = self.pinned_time

        created_time: None | str | Unset
        if isinstance(self.created_time, Unset):
            created_time = UNSET
        elif isinstance(self.created_time, datetime.datetime):
            created_time = self.created_time.isoformat()
        else:
            created_time = self.created_time

        created_by: dict[str, Any] | None | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        elif isinstance(self.created_by, DashboardActor):
            created_by = self.created_by.to_dict()
        else:
            created_by = self.created_by

        updated_time: None | str | Unset
        if isinstance(self.updated_time, Unset):
            updated_time = UNSET
        elif isinstance(self.updated_time, datetime.datetime):
            updated_time = self.updated_time.isoformat()
        else:
            updated_time = self.updated_time

        updated_by: dict[str, Any] | None | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        elif isinstance(self.updated_by, DashboardActor):
            updated_by = self.updated_by.to_dict()
        else:
            updated_by = self.updated_by

        published_time: None | str | Unset
        if isinstance(self.published_time, Unset):
            published_time = UNSET
        elif isinstance(self.published_time, datetime.datetime):
            published_time = self.published_time.isoformat()
        else:
            published_time = self.published_time

        published_by: dict[str, Any] | None | Unset
        if isinstance(self.published_by, Unset):
            published_by = UNSET
        elif isinstance(self.published_by, DashboardActor):
            published_by = self.published_by.to_dict()
        else:
            published_by = self.published_by

        deleted_time: None | str | Unset
        if isinstance(self.deleted_time, Unset):
            deleted_time = UNSET
        elif isinstance(self.deleted_time, datetime.datetime):
            deleted_time = self.deleted_time.isoformat()
        else:
            deleted_time = self.deleted_time

        deleted_by: dict[str, Any] | None | Unset
        if isinstance(self.deleted_by, Unset):
            deleted_by = UNSET
        elif isinstance(self.deleted_by, DashboardActor):
            deleted_by = self.deleted_by.to_dict()
        else:
            deleted_by = self.deleted_by

        head_etag: None | str | Unset
        if isinstance(self.head_etag, Unset):
            head_etag = UNSET
        else:
            head_etag = self.head_etag

        latest_published_document_id: None | str | Unset
        if isinstance(self.latest_published_document_id, Unset):
            latest_published_document_id = UNSET
        else:
            latest_published_document_id = self.latest_published_document_id

        latest_published_version: None | str | Unset
        if isinstance(self.latest_published_version, Unset):
            latest_published_version = UNSET
        else:
            latest_published_version = self.latest_published_version

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if dashboard_id is not UNSET:
            field_dict["dashboardId"] = dashboard_id
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if lifecycle_state is not UNSET:
            field_dict["lifecycleState"] = lifecycle_state
        if is_pinned is not UNSET:
            field_dict["isPinned"] = is_pinned
        if pinned_time is not UNSET:
            field_dict["pinnedTime"] = pinned_time
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if updated_time is not UNSET:
            field_dict["updatedTime"] = updated_time
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by
        if published_time is not UNSET:
            field_dict["publishedTime"] = published_time
        if published_by is not UNSET:
            field_dict["publishedBy"] = published_by
        if deleted_time is not UNSET:
            field_dict["deletedTime"] = deleted_time
        if deleted_by is not UNSET:
            field_dict["deletedBy"] = deleted_by
        if head_etag is not UNSET:
            field_dict["headEtag"] = head_etag
        if latest_published_document_id is not UNSET:
            field_dict["latestPublishedDocumentId"] = latest_published_document_id
        if latest_published_version is not UNSET:
            field_dict["latestPublishedVersion"] = latest_published_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_actor import DashboardActor  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_dashboard_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dashboard_id = _parse_dashboard_id(d.pop("dashboardId", UNSET))

        def _parse_universe_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        universe_id = _parse_universe_id(d.pop("universeId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_lifecycle_state(data: object) -> DashboardMetadataLifecycleStateType0Type0 | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lifecycle_state_type_0_type_0 = DashboardMetadataLifecycleStateType0Type0(data)

                return lifecycle_state_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardMetadataLifecycleStateType0Type0 | int | None | Unset, data)

        lifecycle_state = _parse_lifecycle_state(d.pop("lifecycleState", UNSET))

        def _parse_is_pinned(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_pinned = _parse_is_pinned(d.pop("isPinned", UNSET))

        def _parse_pinned_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pinned_time_type_0 = datetime.datetime.fromisoformat(data)

                return pinned_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        pinned_time = _parse_pinned_time(d.pop("pinnedTime", UNSET))

        def _parse_created_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_time_type_0 = datetime.datetime.fromisoformat(data)

                return created_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_time = _parse_created_time(d.pop("createdTime", UNSET))

        def _parse_created_by(data: object) -> DashboardActor | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                created_by_type_0 = DashboardActor.from_dict(data)

                return created_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardActor | None | Unset, data)

        created_by = _parse_created_by(d.pop("createdBy", UNSET))

        def _parse_updated_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_time_type_0 = datetime.datetime.fromisoformat(data)

                return updated_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_time = _parse_updated_time(d.pop("updatedTime", UNSET))

        def _parse_updated_by(data: object) -> DashboardActor | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                updated_by_type_0 = DashboardActor.from_dict(data)

                return updated_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardActor | None | Unset, data)

        updated_by = _parse_updated_by(d.pop("updatedBy", UNSET))

        def _parse_published_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_time_type_0 = datetime.datetime.fromisoformat(data)

                return published_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        published_time = _parse_published_time(d.pop("publishedTime", UNSET))

        def _parse_published_by(data: object) -> DashboardActor | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                published_by_type_0 = DashboardActor.from_dict(data)

                return published_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardActor | None | Unset, data)

        published_by = _parse_published_by(d.pop("publishedBy", UNSET))

        def _parse_deleted_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_time_type_0 = datetime.datetime.fromisoformat(data)

                return deleted_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        deleted_time = _parse_deleted_time(d.pop("deletedTime", UNSET))

        def _parse_deleted_by(data: object) -> DashboardActor | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_by_type_0 = DashboardActor.from_dict(data)

                return deleted_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardActor | None | Unset, data)

        deleted_by = _parse_deleted_by(d.pop("deletedBy", UNSET))

        def _parse_head_etag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        head_etag = _parse_head_etag(d.pop("headEtag", UNSET))

        def _parse_latest_published_document_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_published_document_id = _parse_latest_published_document_id(d.pop("latestPublishedDocumentId", UNSET))

        def _parse_latest_published_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_published_version = _parse_latest_published_version(d.pop("latestPublishedVersion", UNSET))

        dashboard_metadata = cls(
            dashboard_id=dashboard_id,
            universe_id=universe_id,
            name=name,
            description=description,
            lifecycle_state=lifecycle_state,
            is_pinned=is_pinned,
            pinned_time=pinned_time,
            created_time=created_time,
            created_by=created_by,
            updated_time=updated_time,
            updated_by=updated_by,
            published_time=published_time,
            published_by=published_by,
            deleted_time=deleted_time,
            deleted_by=deleted_by,
            head_etag=head_etag,
            latest_published_document_id=latest_published_document_id,
            latest_published_version=latest_published_version,
        )

        return dashboard_metadata
