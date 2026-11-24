from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalControllerHttpControllerSubmitQueryData")


@_attrs_define
class InternalControllerHttpControllerSubmitQueryData:
    """
    Attributes:
        id (str | Unset): ID is the public job id used to poll status and fetch results. Example:
            3f6b1c2e-9d4a-4c1b-9f2e-2a1b3c4d5e6f.
        state (str | Unset): State is the job's lifecycle state; a freshly submitted job is SUBMITTED. Example:
            SUBMITTED.
    """

    id: str | Unset = UNSET
    state: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        state = d.pop("state", UNSET)

        internal_controller_http_controller_submit_query_data = cls(
            id=id,
            state=state,
        )

        internal_controller_http_controller_submit_query_data.additional_properties = d
        return internal_controller_http_controller_submit_query_data

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
