from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomDashboardConflictDetails")


@_attrs_define
class CustomDashboardConflictDetails:
    """CustomDashboardConflictDetails describes an optimistic concurrency failure.

    Attributes:
        expected_head_etag (None | str | Unset):  Default: ''.
        actual_head_etag (None | str | Unset):  Default: ''.
    """

    expected_head_etag: None | str | Unset = ""
    actual_head_etag: None | str | Unset = ""

    def to_dict(self) -> dict[str, Any]:
        expected_head_etag: None | str | Unset
        if isinstance(self.expected_head_etag, Unset):
            expected_head_etag = UNSET
        else:
            expected_head_etag = self.expected_head_etag

        actual_head_etag: None | str | Unset
        if isinstance(self.actual_head_etag, Unset):
            actual_head_etag = UNSET
        else:
            actual_head_etag = self.actual_head_etag

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if expected_head_etag is not UNSET:
            field_dict["expectedHeadEtag"] = expected_head_etag
        if actual_head_etag is not UNSET:
            field_dict["actualHeadEtag"] = actual_head_etag

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

        def _parse_actual_head_etag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        actual_head_etag = _parse_actual_head_etag(d.pop("actualHeadEtag", UNSET))

        custom_dashboard_conflict_details = cls(
            expected_head_etag=expected_head_etag,
            actual_head_etag=actual_head_etag,
        )

        return custom_dashboard_conflict_details
