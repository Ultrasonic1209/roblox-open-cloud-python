from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.thumbnail_personalized_config import ThumbnailPersonalizedConfig


T = TypeVar("T", bound="FindPersonalizedConfigsResponse")


@_attrs_define
class FindPersonalizedConfigsResponse:
    """A page of thumbnail personalization configurations.

    Attributes:
        personalized_configs (list[ThumbnailPersonalizedConfig]): The personalization configurations matching the
            requested universe and status.
        next_cursor (None | str | Unset): The cursor to use for the next page of results.
    """

    personalized_configs: list[ThumbnailPersonalizedConfig]
    next_cursor: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        personalized_configs = []
        for personalized_configs_item_data in self.personalized_configs:
            personalized_configs_item = personalized_configs_item_data.to_dict()
            personalized_configs.append(personalized_configs_item)

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "personalizedConfigs": personalized_configs,
            }
        )
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.thumbnail_personalized_config import ThumbnailPersonalizedConfig

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        personalized_configs = []
        _personalized_configs = d.pop("personalizedConfigs")
        for personalized_configs_item_data in _personalized_configs:
            personalized_configs_item = ThumbnailPersonalizedConfig.from_dict(personalized_configs_item_data)

            personalized_configs.append(personalized_configs_item)

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))

        find_personalized_configs_response = cls(
            personalized_configs=personalized_configs,
            next_cursor=next_cursor,
        )

        return find_personalized_configs_response
