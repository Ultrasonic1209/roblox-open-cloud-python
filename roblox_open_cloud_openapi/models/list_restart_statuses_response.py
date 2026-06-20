from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_restart_statuses_response_restart_statuses_type_0 import (
        ListRestartStatusesResponseRestartStatusesType0,
    )


T = TypeVar("T", bound="ListRestartStatusesResponse")


@_attrs_define
class ListRestartStatusesResponse:
    """Response model for listing restart statuses.

    Attributes:
        restart_statuses (ListRestartStatusesResponseRestartStatusesType0 | None | Unset): Restart statuses keyed by
            restart ID.
    """

    restart_statuses: ListRestartStatusesResponseRestartStatusesType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_restart_statuses_response_restart_statuses_type_0 import (
            ListRestartStatusesResponseRestartStatusesType0,
        )

        restart_statuses: dict[str, Any] | None | Unset
        if isinstance(self.restart_statuses, Unset):
            restart_statuses = UNSET
        elif isinstance(self.restart_statuses, ListRestartStatusesResponseRestartStatusesType0):
            restart_statuses = self.restart_statuses.to_dict()
        else:
            restart_statuses = self.restart_statuses

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if restart_statuses is not UNSET:
            field_dict["restartStatuses"] = restart_statuses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_restart_statuses_response_restart_statuses_type_0 import (
            ListRestartStatusesResponseRestartStatusesType0,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_restart_statuses(data: object) -> ListRestartStatusesResponseRestartStatusesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                restart_statuses_type_0 = ListRestartStatusesResponseRestartStatusesType0.from_dict(data)

                return restart_statuses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListRestartStatusesResponseRestartStatusesType0 | None | Unset, data)

        restart_statuses = _parse_restart_statuses(d.pop("restartStatuses", UNSET))

        list_restart_statuses_response = cls(
            restart_statuses=restart_statuses,
        )

        return list_restart_statuses_response
