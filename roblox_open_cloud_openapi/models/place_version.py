from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.publish_status import PublishStatus
from ..models.save_type import SaveType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlaceVersion")


@_attrs_define
class PlaceVersion:
    """
    Attributes:
        version (None | str | Unset):
        title (None | str | Unset):
        description (None | str | Unset):
        contributors (list[int] | None | Unset):
        save_type (SaveType | Unset):
        is_published (bool | Unset):
        publish_status (PublishStatus | Unset):
        has_notes (bool | Unset):
        created_time (datetime.datetime | Unset):
        created_by (int | None | Unset):
    """

    version: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    contributors: list[int] | None | Unset = UNSET
    save_type: SaveType | Unset = UNSET
    is_published: bool | Unset = UNSET
    publish_status: PublishStatus | Unset = UNSET
    has_notes: bool | Unset = UNSET
    created_time: datetime.datetime | Unset = UNSET
    created_by: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        contributors: list[int] | None | Unset
        if isinstance(self.contributors, Unset):
            contributors = UNSET
        elif isinstance(self.contributors, list):
            contributors = self.contributors

        else:
            contributors = self.contributors

        save_type: int | Unset = UNSET
        if not isinstance(self.save_type, Unset):
            save_type = self.save_type.value

        is_published = self.is_published

        publish_status: int | Unset = UNSET
        if not isinstance(self.publish_status, Unset):
            publish_status = self.publish_status.value

        has_notes = self.has_notes

        created_time: str | Unset = UNSET
        if not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        created_by: int | None | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if contributors is not UNSET:
            field_dict["contributors"] = contributors
        if save_type is not UNSET:
            field_dict["saveType"] = save_type
        if is_published is not UNSET:
            field_dict["isPublished"] = is_published
        if publish_status is not UNSET:
            field_dict["publishStatus"] = publish_status
        if has_notes is not UNSET:
            field_dict["hasNotes"] = has_notes
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_contributors(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                contributors_type_0 = cast(list[int], data)

                return contributors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        contributors = _parse_contributors(d.pop("contributors", UNSET))

        _save_type = d.pop("saveType", UNSET)
        save_type: SaveType | Unset
        if isinstance(_save_type, Unset):
            save_type = UNSET
        else:
            save_type = SaveType(_save_type)

        is_published = d.pop("isPublished", UNSET)

        _publish_status = d.pop("publishStatus", UNSET)
        publish_status: PublishStatus | Unset
        if isinstance(_publish_status, Unset):
            publish_status = UNSET
        else:
            publish_status = PublishStatus(_publish_status)

        has_notes = d.pop("hasNotes", UNSET)

        _created_time = d.pop("createdTime", UNSET)
        created_time: datetime.datetime | Unset
        if isinstance(_created_time, Unset):
            created_time = UNSET
        else:
            created_time = datetime.datetime.fromisoformat(_created_time)

        def _parse_created_by(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        created_by = _parse_created_by(d.pop("createdBy", UNSET))

        place_version = cls(
            version=version,
            title=title,
            description=description,
            contributors=contributors,
            save_type=save_type,
            is_published=is_published,
            publish_status=publish_status,
            has_notes=has_notes,
            created_time=created_time,
            created_by=created_by,
        )

        return place_version
