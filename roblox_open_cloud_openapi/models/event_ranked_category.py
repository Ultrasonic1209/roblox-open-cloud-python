from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.event_category import EventCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventRankedCategory")


@_attrs_define
class EventRankedCategory:
    """Representation of the category associated with an event.

    Attributes:
        category (EventCategory | Unset): The event category type of an event.

            Mirror of:
            https://github.rbx.com/Roblox/virtual-events/blob/master/services/virtual-
            events/src/Implementations/Types/EventCategory.cs
        rank (int | Unset): The rank of the category.
    """

    category: EventCategory | Unset = UNSET
    rank: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        rank = self.rank

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if rank is not UNSET:
            field_dict["rank"] = rank

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _category = d.pop("category", UNSET)
        category: EventCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = EventCategory(_category)

        rank = d.pop("rank", UNSET)

        event_ranked_category = cls(
            category=category,
            rank=rank,
        )

        return event_ranked_category
