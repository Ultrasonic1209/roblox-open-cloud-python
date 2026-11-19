from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_breakdown_tab_page import DashboardBreakdownTabPage
    from ..models.dashboard_fixed_tab_page import DashboardFixedTabPage
    from ..models.dashboard_untabbed_page import DashboardUntabbedPage


T = TypeVar("T", bound="DashboardPage")


@_attrs_define
class DashboardPage:
    """DashboardPage models page shell behavior separately from surface layout.

    Attributes:
        untabbed (DashboardUntabbedPage | None | Unset): DashboardUntabbedPage renders a dashboard page without tabs.
        fixed_tab (DashboardFixedTabPage | None | Unset): A fixed-tab page; Creator Hub does not yet support authoring
            this page type.
        breakdown_tab (DashboardBreakdownTabPage | None | Unset): A breakdown-tab page; Creator Hub does not yet support
            authoring this page type.
    """

    untabbed: DashboardUntabbedPage | None | Unset = UNSET
    fixed_tab: DashboardFixedTabPage | None | Unset = UNSET
    breakdown_tab: DashboardBreakdownTabPage | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_breakdown_tab_page import DashboardBreakdownTabPage  # noqa: PLC0415
        from ..models.dashboard_fixed_tab_page import DashboardFixedTabPage  # noqa: PLC0415
        from ..models.dashboard_untabbed_page import DashboardUntabbedPage  # noqa: PLC0415

        untabbed: dict[str, Any] | None | Unset
        if isinstance(self.untabbed, Unset):
            untabbed = UNSET
        elif isinstance(self.untabbed, DashboardUntabbedPage):
            untabbed = self.untabbed.to_dict()
        else:
            untabbed = self.untabbed

        fixed_tab: dict[str, Any] | None | Unset
        if isinstance(self.fixed_tab, Unset):
            fixed_tab = UNSET
        elif isinstance(self.fixed_tab, DashboardFixedTabPage):
            fixed_tab = self.fixed_tab.to_dict()
        else:
            fixed_tab = self.fixed_tab

        breakdown_tab: dict[str, Any] | None | Unset
        if isinstance(self.breakdown_tab, Unset):
            breakdown_tab = UNSET
        elif isinstance(self.breakdown_tab, DashboardBreakdownTabPage):
            breakdown_tab = self.breakdown_tab.to_dict()
        else:
            breakdown_tab = self.breakdown_tab

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if untabbed is not UNSET:
            field_dict["untabbed"] = untabbed
        if fixed_tab is not UNSET:
            field_dict["fixedTab"] = fixed_tab
        if breakdown_tab is not UNSET:
            field_dict["breakdownTab"] = breakdown_tab

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_breakdown_tab_page import DashboardBreakdownTabPage  # noqa: PLC0415
        from ..models.dashboard_fixed_tab_page import DashboardFixedTabPage  # noqa: PLC0415
        from ..models.dashboard_untabbed_page import DashboardUntabbedPage  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_untabbed(data: object) -> DashboardUntabbedPage | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                untabbed_type_0 = DashboardUntabbedPage.from_dict(data)

                return untabbed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardUntabbedPage | None | Unset, data)

        untabbed = _parse_untabbed(d.pop("untabbed", UNSET))

        def _parse_fixed_tab(data: object) -> DashboardFixedTabPage | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fixed_tab_type_0 = DashboardFixedTabPage.from_dict(data)

                return fixed_tab_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardFixedTabPage | None | Unset, data)

        fixed_tab = _parse_fixed_tab(d.pop("fixedTab", UNSET))

        def _parse_breakdown_tab(data: object) -> DashboardBreakdownTabPage | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                breakdown_tab_type_0 = DashboardBreakdownTabPage.from_dict(data)

                return breakdown_tab_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardBreakdownTabPage | None | Unset, data)

        breakdown_tab = _parse_breakdown_tab(d.pop("breakdownTab", UNSET))

        dashboard_page = cls(
            untabbed=untabbed,
            fixed_tab=fixed_tab,
            breakdown_tab=breakdown_tab,
        )

        return dashboard_page
