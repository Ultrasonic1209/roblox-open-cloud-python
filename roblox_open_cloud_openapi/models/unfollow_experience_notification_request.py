from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnfollowExperienceNotificationRequest")


@_attrs_define
class UnfollowExperienceNotificationRequest:
    """
    Attributes:
        universe_id (int | Unset):
    """

    universe_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        universe_id = self.universe_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        universe_id = d.pop("universeId", UNSET)

        unfollow_experience_notification_request = cls(
            universe_id=universe_id,
        )

        return unfollow_experience_notification_request
