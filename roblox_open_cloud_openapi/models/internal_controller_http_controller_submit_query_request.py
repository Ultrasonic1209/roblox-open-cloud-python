from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_controller_http_controller_submit_query_request_query import (
        InternalControllerHttpControllerSubmitQueryRequestQuery,
    )


T = TypeVar("T", bound="InternalControllerHttpControllerSubmitQueryRequest")


@_attrs_define
class InternalControllerHttpControllerSubmitQueryRequest:
    """
    Attributes:
        dataset (str):  Example: communities.
        fields (list[str] | Unset): Fields is the projection; omitted means the dataset's default fields.
        query (InternalControllerHttpControllerSubmitQueryRequestQuery | Unset): Query is the filter DSL
            ({and|or|not:[{operation,field_name,field_values}]}).
    """

    dataset: str
    fields: list[str] | Unset = UNSET
    query: InternalControllerHttpControllerSubmitQueryRequestQuery | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset = self.dataset

        fields: list[str] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields

        query: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataset": dataset,
            }
        )
        if fields is not UNSET:
            field_dict["fields"] = fields
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_controller_http_controller_submit_query_request_query import (
            InternalControllerHttpControllerSubmitQueryRequestQuery,  # noqa: PLC0415
        )

        d = dict(src_dict)
        dataset = d.pop("dataset")

        fields = cast(list[str], d.pop("fields", UNSET))

        _query = d.pop("query", UNSET)
        query: InternalControllerHttpControllerSubmitQueryRequestQuery | Unset
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = InternalControllerHttpControllerSubmitQueryRequestQuery.from_dict(_query)

        internal_controller_http_controller_submit_query_request = cls(
            dataset=dataset,
            fields=fields,
            query=query,
        )

        internal_controller_http_controller_submit_query_request.additional_properties = d
        return internal_controller_http_controller_submit_query_request

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
