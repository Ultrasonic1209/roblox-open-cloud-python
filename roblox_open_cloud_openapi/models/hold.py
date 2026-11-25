from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.hold_state import HoldState

if TYPE_CHECKING:
    from ..models.creator import Creator
    from ..models.resource import Resource


T = TypeVar("T", bound="Hold")


@_attrs_define
class Hold:
    """
    Attributes:
        hold_id (int):
        current_creator (Creator):
        target_creator (Creator):
        resource (Resource):
        hold_state (HoldState):
        expiration_acknowledged (bool):
        created_utc_time (datetime.datetime):
        updated_utc_time (datetime.datetime):
    """

    hold_id: int
    current_creator: Creator
    target_creator: Creator
    resource: Resource
    hold_state: HoldState
    expiration_acknowledged: bool
    created_utc_time: datetime.datetime
    updated_utc_time: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        hold_id = self.hold_id

        current_creator = self.current_creator.to_dict()

        target_creator = self.target_creator.to_dict()

        resource = self.resource.to_dict()

        hold_state = self.hold_state.value

        expiration_acknowledged = self.expiration_acknowledged

        created_utc_time = self.created_utc_time.isoformat()

        updated_utc_time = self.updated_utc_time.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "holdId": hold_id,
                "currentCreator": current_creator,
                "targetCreator": target_creator,
                "resource": resource,
                "holdState": hold_state,
                "expirationAcknowledged": expiration_acknowledged,
                "createdUtcTime": created_utc_time,
                "updatedUtcTime": updated_utc_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.creator import Creator  # noqa: PLC0415
        from ..models.resource import Resource  # noqa: PLC0415

        d = dict(src_dict)
        hold_id = d.pop("holdId")

        current_creator = Creator.from_dict(d.pop("currentCreator"))

        target_creator = Creator.from_dict(d.pop("targetCreator"))

        resource = Resource.from_dict(d.pop("resource"))

        hold_state = HoldState(d.pop("holdState"))

        expiration_acknowledged = d.pop("expirationAcknowledged")

        created_utc_time = datetime.datetime.fromisoformat(d.pop("createdUtcTime"))

        updated_utc_time = datetime.datetime.fromisoformat(d.pop("updatedUtcTime"))

        hold = cls(
            hold_id=hold_id,
            current_creator=current_creator,
            target_creator=target_creator,
            resource=resource,
            hold_state=hold_state,
            expiration_acknowledged=expiration_acknowledged,
            created_utc_time=created_utc_time,
            updated_utc_time=updated_utc_time,
        )

        return hold
