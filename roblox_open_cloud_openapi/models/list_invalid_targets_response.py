from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.creator import Creator


T = TypeVar("T", bound="ListInvalidTargetsResponse")


@_attrs_define
class ListInvalidTargetsResponse:
    """
    Attributes:
        invalid_targets (list[Creator]):
    """

    invalid_targets: list[Creator]

    def to_dict(self) -> dict[str, Any]:
        invalid_targets = []
        for invalid_targets_item_data in self.invalid_targets:
            invalid_targets_item = invalid_targets_item_data.to_dict()
            invalid_targets.append(invalid_targets_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "invalidTargets": invalid_targets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.creator import Creator  # noqa: PLC0415

        d = dict(src_dict)
        invalid_targets = []
        _invalid_targets = d.pop("invalidTargets")
        for invalid_targets_item_data in _invalid_targets:
            invalid_targets_item = Creator.from_dict(invalid_targets_item_data)

            invalid_targets.append(invalid_targets_item)

        list_invalid_targets_response = cls(
            invalid_targets=invalid_targets,
        )

        return list_invalid_targets_response
