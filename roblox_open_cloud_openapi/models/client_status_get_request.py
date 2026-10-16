from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientStatusGetRequest")


@_attrs_define
class ClientStatusGetRequest:
    """Get Client Status request.

    Attributes:
        browser_tracker_id (int | None | Unset): The client's browser tracker id.
    """

    browser_tracker_id: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        browser_tracker_id: int | None | Unset
        if isinstance(self.browser_tracker_id, Unset):
            browser_tracker_id = UNSET
        else:
            browser_tracker_id = self.browser_tracker_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if browser_tracker_id is not UNSET:
            field_dict["browserTrackerId"] = browser_tracker_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_browser_tracker_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        browser_tracker_id = _parse_browser_tracker_id(d.pop("browserTrackerId", UNSET))

        client_status_get_request = cls(
            browser_tracker_id=browser_tracker_id,
        )

        return client_status_get_request
