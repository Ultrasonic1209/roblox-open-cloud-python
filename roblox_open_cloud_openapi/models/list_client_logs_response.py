from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_log import ClientLog


T = TypeVar("T", bound="ListClientLogsResponse")


@_attrs_define
class ListClientLogsResponse:
    """A page of client log entries from one play session.

    Attributes:
        client_logs (list[ClientLog] | None | Unset): The client log entries in this page.
        next_page_token (None | str | Unset): An opaque token for the next page. Omitted when there are no more entries.
    """

    client_logs: list[ClientLog] | None | Unset = UNSET
    next_page_token: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        client_logs: list[dict[str, Any]] | None | Unset
        if isinstance(self.client_logs, Unset):
            client_logs = UNSET
        elif isinstance(self.client_logs, list):
            client_logs = []
            for client_logs_type_0_item_data in self.client_logs:
                client_logs_type_0_item = client_logs_type_0_item_data.to_dict()
                client_logs.append(client_logs_type_0_item)

        else:
            client_logs = self.client_logs

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if client_logs is not UNSET:
            field_dict["clientLogs"] = client_logs
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.client_log import ClientLog  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_client_logs(data: object) -> list[ClientLog] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                client_logs_type_0 = []
                _client_logs_type_0 = data
                for client_logs_type_0_item_data in _client_logs_type_0:
                    client_logs_type_0_item = ClientLog.from_dict(client_logs_type_0_item_data)

                    client_logs_type_0.append(client_logs_type_0_item)

                return client_logs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClientLog] | None | Unset, data)

        client_logs = _parse_client_logs(d.pop("clientLogs", UNSET))

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        list_client_logs_response = cls(
            client_logs=client_logs,
            next_page_token=next_page_token,
        )

        return list_client_logs_response
