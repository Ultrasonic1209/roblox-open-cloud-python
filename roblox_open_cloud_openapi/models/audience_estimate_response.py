from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AudienceEstimateResponse")


@_attrs_define
class AudienceEstimateResponse:
    """
    Attributes:
        lower_bound (int): Estimated lower bound of reachable users.
        upper_bound (int): Estimated upper bound of reachable users.
    """

    lower_bound: int
    upper_bound: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lower_bound = self.lower_bound

        upper_bound = self.upper_bound

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lowerBound": lower_bound,
                "upperBound": upper_bound,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lower_bound = d.pop("lowerBound")

        upper_bound = d.pop("upperBound")

        audience_estimate_response = cls(
            lower_bound=lower_bound,
            upper_bound=upper_bound,
        )

        audience_estimate_response.additional_properties = d
        return audience_estimate_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
