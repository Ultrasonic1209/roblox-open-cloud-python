from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_capabilities import DashboardCapabilities
    from ..models.dashboard_metadata import DashboardMetadata


T = TypeVar("T", bound="ListDashboardsResponse")


@_attrs_define
class ListDashboardsResponse:
    """
    Attributes:
        dashboards (list[DashboardMetadata] | None | Unset):
        next_page_token (None | str | Unset):  Default: ''.
        capabilities (DashboardCapabilities | None | Unset): Capabilities and limits for the calling user in
            `ListDashboardsRequest.universe_id`.
            Identical to what `GetDashboardCapabilities` returns for the same caller and
            universe; both are populated by one shared implementation. Present on every
            page so a manage page does not need a second round trip.
    """

    dashboards: list[DashboardMetadata] | None | Unset = UNSET
    next_page_token: None | str | Unset = ""
    capabilities: DashboardCapabilities | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_capabilities import DashboardCapabilities  # noqa: PLC0415

        dashboards: list[dict[str, Any]] | None | Unset
        if isinstance(self.dashboards, Unset):
            dashboards = UNSET
        elif isinstance(self.dashboards, list):
            dashboards = []
            for dashboards_type_0_item_data in self.dashboards:
                dashboards_type_0_item = dashboards_type_0_item_data.to_dict()
                dashboards.append(dashboards_type_0_item)

        else:
            dashboards = self.dashboards

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        capabilities: dict[str, Any] | None | Unset
        if isinstance(self.capabilities, Unset):
            capabilities = UNSET
        elif isinstance(self.capabilities, DashboardCapabilities):
            capabilities = self.capabilities.to_dict()
        else:
            capabilities = self.capabilities

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if dashboards is not UNSET:
            field_dict["dashboards"] = dashboards
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_capabilities import DashboardCapabilities  # noqa: PLC0415
        from ..models.dashboard_metadata import DashboardMetadata  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_dashboards(data: object) -> list[DashboardMetadata] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dashboards_type_0 = []
                _dashboards_type_0 = data
                for dashboards_type_0_item_data in _dashboards_type_0:
                    dashboards_type_0_item = DashboardMetadata.from_dict(dashboards_type_0_item_data)

                    dashboards_type_0.append(dashboards_type_0_item)

                return dashboards_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DashboardMetadata] | None | Unset, data)

        dashboards = _parse_dashboards(d.pop("dashboards", UNSET))

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        def _parse_capabilities(data: object) -> DashboardCapabilities | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                capabilities_type_0 = DashboardCapabilities.from_dict(data)

                return capabilities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardCapabilities | None | Unset, data)

        capabilities = _parse_capabilities(d.pop("capabilities", UNSET))

        list_dashboards_response = cls(
            dashboards=dashboards,
            next_page_token=next_page_token,
            capabilities=capabilities,
        )

        return list_dashboards_response
