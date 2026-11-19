from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateNotificationStringRequest")


@_attrs_define
class CreateNotificationStringRequest:
    """
    Attributes:
        name (None | str):
        content (None | str):
        universe_id (int):
    """

    name: None | str
    content: None | str
    universe_id: int

    def to_dict(self) -> dict[str, Any]:
        name: None | str
        name = self.name

        content: None | str
        content = self.content

        universe_id = self.universe_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "content": content,
                "universeId": universe_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_content(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        content = _parse_content(d.pop("content"))

        universe_id = d.pop("universeId")

        create_notification_string_request = cls(
            name=name,
            content=content,
            universe_id=universe_id,
        )

        return create_notification_string_request
