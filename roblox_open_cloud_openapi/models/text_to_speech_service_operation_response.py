from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TextToSpeechServiceOperationResponse")


@_attrs_define
class TextToSpeechServiceOperationResponse:
    """The normal response of the operation in case of success.  If the original
    method returns no data on success, such as `Delete`, the response is
    `google.protobuf.Empty`.  If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource.  For other
    methods, the response should have the type `XxxResponse`, where `Xxx`
    is the original method name.  For example, if the original method name
    is `TakeSnapshot()`, the inferred response type is
    `TakeSnapshotResponse`.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text_to_speech_service_operation_response = cls()

        text_to_speech_service_operation_response.additional_properties = d
        return text_to_speech_service_operation_response

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
