from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_table import DashboardTable


T = TypeVar("T", bound="DashboardTableTab")


@_attrs_define
class DashboardTableTab:
    """DashboardTableTab defines one table tab and its table component.

    Attributes:
        tab_key (None | str | Unset):  Default: ''.
        label_key (None | str | Unset):  Default: ''.
        table (DashboardTable | None | Unset): DashboardTable renders a table from dashboard chart data inputs.
    """

    tab_key: None | str | Unset = ""
    label_key: None | str | Unset = ""
    table: DashboardTable | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_table import DashboardTable  # noqa: PLC0415

        tab_key: None | str | Unset
        if isinstance(self.tab_key, Unset):
            tab_key = UNSET
        else:
            tab_key = self.tab_key

        label_key: None | str | Unset
        if isinstance(self.label_key, Unset):
            label_key = UNSET
        else:
            label_key = self.label_key

        table: dict[str, Any] | None | Unset
        if isinstance(self.table, Unset):
            table = UNSET
        elif isinstance(self.table, DashboardTable):
            table = self.table.to_dict()
        else:
            table = self.table

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if tab_key is not UNSET:
            field_dict["tabKey"] = tab_key
        if label_key is not UNSET:
            field_dict["labelKey"] = label_key
        if table is not UNSET:
            field_dict["table"] = table

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_table import DashboardTable  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_tab_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tab_key = _parse_tab_key(d.pop("tabKey", UNSET))

        def _parse_label_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label_key = _parse_label_key(d.pop("labelKey", UNSET))

        def _parse_table(data: object) -> DashboardTable | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                table_type_0 = DashboardTable.from_dict(data)

                return table_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardTable | None | Unset, data)

        table = _parse_table(d.pop("table", UNSET))

        dashboard_table_tab = cls(
            tab_key=tab_key,
            label_key=label_key,
            table=table,
        )

        return dashboard_table_tab
