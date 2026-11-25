from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.creator_type import CreatorType

T = TypeVar("T", bound="Creator")


@_attrs_define
class Creator:
    """
    Attributes:
        creator_type (CreatorType):
        creator_id (int):
    """

    creator_type: CreatorType
    creator_id: int

    def to_dict(self) -> dict[str, Any]:
        creator_type = self.creator_type.value

        creator_id = self.creator_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "creatorType": creator_type,
                "creatorId": creator_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        creator_type = CreatorType(d.pop("creatorType"))

        creator_id = d.pop("creatorId")

        creator = cls(
            creator_type=creator_type,
            creator_id=creator_id,
        )

        return creator
