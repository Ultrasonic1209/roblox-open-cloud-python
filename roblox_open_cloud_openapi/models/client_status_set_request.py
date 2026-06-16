from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientStatusSetRequest")


@_attrs_define
class ClientStatusSetRequest:
    """Set Client Status request.

    Attributes:
        status (None | str | Unset): The client's status to send.
        browser_tracker_id (int | None | Unset): The client's browser tracker id.
    """

    status: None | str | Unset = UNSET
    browser_tracker_id: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        browser_tracker_id: int | None | Unset
        if isinstance(self.browser_tracker_id, Unset):
            browser_tracker_id = UNSET
        else:
            browser_tracker_id = self.browser_tracker_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if browser_tracker_id is not UNSET:
            field_dict["browserTrackerId"] = browser_tracker_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_browser_tracker_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        browser_tracker_id = _parse_browser_tracker_id(d.pop("browserTrackerId", UNSET))

        client_status_set_request = cls(
            status=status,
            browser_tracker_id=browser_tracker_id,
        )

        return client_status_set_request
