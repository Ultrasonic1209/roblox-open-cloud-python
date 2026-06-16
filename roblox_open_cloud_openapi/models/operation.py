from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_protobuf_any import GoogleProtobufAny
    from ..models.status import Status


T = TypeVar("T", bound="Operation")


@_attrs_define
class Operation:
    """This resource represents a long-running operation that is the result of a
    network API call.

        Attributes:
            path (str | Unset): The server-assigned path, which is only unique within the same service that
                originally returns it. If you use the default HTTP mapping, the
                `path` should be a resource path ending with `operations/{unique_id}`.
            metadata (GoogleProtobufAny | Unset): Contains an arbitrary serialized message along with a @type that describes
                the type of the serialized message.
            done (bool | Unset): If the value is `false`, it means the operation is still in progress.
                If `true`, the operation is completed, and either `error` or `response` is
                available. Example: True.
            error (Status | Unset): The `Status` type defines a logical error model that is suitable for different
                programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each
                `Status` message contains three pieces of data: error code, error message, and error details. You can find out
                more about this error model and how to work with it in the [API Design
                Guide](https://cloud.google.com/apis/design/errors).
            response (GoogleProtobufAny | Unset): Contains an arbitrary serialized message along with a @type that describes
                the type of the serialized message.
    """

    path: str | Unset = UNSET
    metadata: GoogleProtobufAny | Unset = UNSET
    done: bool | Unset = UNSET
    error: Status | Unset = UNSET
    response: GoogleProtobufAny | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        done = self.done

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response, Unset):
            response = self.response.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if done is not UNSET:
            field_dict["done"] = done
        if error is not UNSET:
            field_dict["error"] = error
        if response is not UNSET:
            field_dict["response"] = response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.google_protobuf_any import GoogleProtobufAny
        from ..models.status import Status

        d = dict(src_dict)
        path = d.pop("path", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: GoogleProtobufAny | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = GoogleProtobufAny.from_dict(_metadata)

        done = d.pop("done", UNSET)

        _error = d.pop("error", UNSET)
        error: Status | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = Status.from_dict(_error)

        _response = d.pop("response", UNSET)
        response: GoogleProtobufAny | Unset
        if isinstance(_response, Unset):
            response = UNSET
        else:
            response = GoogleProtobufAny.from_dict(_response)

        operation = cls(
            path=path,
            metadata=metadata,
            done=done,
            error=error,
            response=response,
        )

        operation.additional_properties = d
        return operation

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
