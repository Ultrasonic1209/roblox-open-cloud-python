from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LuauExecutionSessionTaskOutput")


@_attrs_define
class LuauExecutionSessionTaskOutput:
    """Contains the output of a task's execution.

    Attributes:
        results (list[Any] | Unset): Return values from the script that was run. Return values that are not
            JSON serializable (such as Data Model Instances) will be returned as
            nulls.
    """

    results: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results: list[Any] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = self.results

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        results = cast(list[Any], d.pop("results", UNSET))

        luau_execution_session_task_output = cls(
            results=results,
        )

        luau_execution_session_task_output.additional_properties = d
        return luau_execution_session_task_output

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
