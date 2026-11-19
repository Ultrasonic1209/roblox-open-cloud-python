from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_page import DashboardPage


T = TypeVar("T", bound="CustomDashboardConfig")


@_attrs_define
class CustomDashboardConfig:
    """CustomDashboardConfig is the renderer-owned dashboard authoring model. It is
    intentionally a normalized dashboard document rather than a direct mirror of
    Creator Hub RAQI TypeScript config types. Creator Hub adapters may generate
    TS from this proto and map it into the current RAQI renderer.

        Attributes:
            page (DashboardPage | None | Unset): DashboardPage models page shell behavior separately from surface layout.
    """

    page: DashboardPage | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_page import DashboardPage  # noqa: PLC0415

        page: dict[str, Any] | None | Unset
        if isinstance(self.page, Unset):
            page = UNSET
        elif isinstance(self.page, DashboardPage):
            page = self.page.to_dict()
        else:
            page = self.page

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if page is not UNSET:
            field_dict["page"] = page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_page import DashboardPage  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_page(data: object) -> DashboardPage | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                page_type_0 = DashboardPage.from_dict(data)

                return page_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardPage | None | Unset, data)

        page = _parse_page(d.pop("page", UNSET))

        custom_dashboard_config = cls(
            page=page,
        )

        return custom_dashboard_config
