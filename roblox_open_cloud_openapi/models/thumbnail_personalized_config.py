from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.personalized_config_status import PersonalizedConfigStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.personalized_thumbnail import PersonalizedThumbnail


T = TypeVar("T", bound="ThumbnailPersonalizedConfig")


@_attrs_define
class ThumbnailPersonalizedConfig:
    """A thumbnail personalization configuration.

    Attributes:
        id (str): The unique identifier of the personalization configuration.
        personalized_config_status (PersonalizedConfigStatus): The lifecycle status of a thumbnail personalization
            configuration.
        created_utc (datetime.datetime): The UTC date and time when the configuration was created.
        thumbnails (list[PersonalizedThumbnail]): The homepage thumbnails included in the configuration.
        last_served_utc (datetime.datetime | None | Unset): The UTC date and time when the configuration last served a
            thumbnail, when available.
    """

    id: str
    personalized_config_status: PersonalizedConfigStatus
    created_utc: datetime.datetime
    thumbnails: list[PersonalizedThumbnail]
    last_served_utc: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        personalized_config_status = self.personalized_config_status.value

        created_utc = self.created_utc.isoformat()

        thumbnails = []
        for thumbnails_item_data in self.thumbnails:
            thumbnails_item = thumbnails_item_data.to_dict()
            thumbnails.append(thumbnails_item)

        last_served_utc: None | str | Unset
        if isinstance(self.last_served_utc, Unset):
            last_served_utc = UNSET
        elif isinstance(self.last_served_utc, datetime.datetime):
            last_served_utc = self.last_served_utc.isoformat()
        else:
            last_served_utc = self.last_served_utc

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "personalizedConfigStatus": personalized_config_status,
                "createdUtc": created_utc,
                "thumbnails": thumbnails,
            }
        )
        if last_served_utc is not UNSET:
            field_dict["lastServedUtc"] = last_served_utc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.personalized_thumbnail import PersonalizedThumbnail

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id")

        personalized_config_status = PersonalizedConfigStatus(d.pop("personalizedConfigStatus"))

        created_utc = datetime.datetime.fromisoformat(d.pop("createdUtc"))

        thumbnails = []
        _thumbnails = d.pop("thumbnails")
        for thumbnails_item_data in _thumbnails:
            thumbnails_item = PersonalizedThumbnail.from_dict(thumbnails_item_data)

            thumbnails.append(thumbnails_item)

        def _parse_last_served_utc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_served_utc_type_0 = datetime.datetime.fromisoformat(data)

                return last_served_utc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_served_utc = _parse_last_served_utc(d.pop("lastServedUtc", UNSET))

        thumbnail_personalized_config = cls(
            id=id,
            personalized_config_status=personalized_config_status,
            created_utc=created_utc,
            thumbnails=thumbnails,
            last_served_utc=last_served_utc,
        )

        return thumbnail_personalized_config
