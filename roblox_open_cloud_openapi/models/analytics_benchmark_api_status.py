from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analytics_benchmark_api_any import AnalyticsBenchmarkApiAny


T = TypeVar("T", bound="AnalyticsBenchmarkApiStatus")


@_attrs_define
class AnalyticsBenchmarkApiStatus:
    """
    Attributes:
        code (int | Unset):
        message (str | Unset):
        details (list[AnalyticsBenchmarkApiAny] | Unset):
    """

    code: int | Unset = UNSET
    message: str | Unset = UNSET
    details: list[AnalyticsBenchmarkApiAny] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()
                details.append(details_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_benchmark_api_any import AnalyticsBenchmarkApiAny  # noqa: PLC0415

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        _details = d.pop("details", UNSET)
        details: list[AnalyticsBenchmarkApiAny] | Unset = UNSET
        if _details is not UNSET:
            details = []
            for details_item_data in _details:
                details_item = AnalyticsBenchmarkApiAny.from_dict(details_item_data)

                details.append(details_item)

        analytics_benchmark_api_status = cls(
            code=code,
            message=message,
            details=details,
        )

        return analytics_benchmark_api_status
