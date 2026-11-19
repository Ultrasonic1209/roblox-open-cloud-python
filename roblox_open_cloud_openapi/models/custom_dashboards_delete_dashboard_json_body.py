from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomDashboardsDeleteDashboardJsonBody")


@_attrs_define
class CustomDashboardsDeleteDashboardJsonBody:
    """
    Attributes:
        expected_head_etag (None | str | Unset):  Default: ''.
    """

    expected_head_etag: None | str | Unset = ""

    def to_dict(self) -> dict[str, Any]:
        expected_head_etag: None | str | Unset
        if isinstance(self.expected_head_etag, Unset):
            expected_head_etag = UNSET
        else:
            expected_head_etag = self.expected_head_etag

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if expected_head_etag is not UNSET:
            field_dict["expectedHeadEtag"] = expected_head_etag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_expected_head_etag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expected_head_etag = _parse_expected_head_etag(d.pop("expectedHeadEtag", UNSET))

        custom_dashboards_delete_dashboard_json_body = cls(
            expected_head_etag=expected_head_etag,
        )

        return custom_dashboards_delete_dashboard_json_body
