from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardPageMetadata")


@_attrs_define
class DashboardPageMetadata:
    """DashboardPageMetadata carries localized metadata for a dashboard page.

    Attributes:
        title_key (None | str | Unset):  Default: ''.
    """

    title_key: None | str | Unset = ""

    def to_dict(self) -> dict[str, Any]:
        title_key: None | str | Unset
        if isinstance(self.title_key, Unset):
            title_key = UNSET
        else:
            title_key = self.title_key

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if title_key is not UNSET:
            field_dict["titleKey"] = title_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_title_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title_key = _parse_title_key(d.pop("titleKey", UNSET))

        dashboard_page_metadata = cls(
            title_key=title_key,
        )

        return dashboard_page_metadata
