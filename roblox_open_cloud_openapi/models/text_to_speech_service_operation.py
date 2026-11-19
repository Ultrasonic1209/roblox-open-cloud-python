from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_to_speech_service_operation_metadata import TextToSpeechServiceOperationMetadata
    from ..models.text_to_speech_service_operation_response import TextToSpeechServiceOperationResponse
    from ..models.text_to_speech_service_status import TextToSpeechServiceStatus


T = TypeVar("T", bound="TextToSpeechServiceOperation")


@_attrs_define
class TextToSpeechServiceOperation:
    """This resource represents a long-running operation that is the result of a
    network API call.

        Attributes:
            path (str | Unset): The server-assigned path, which is only unique within the same service that
                originally returns it. If you use the default HTTP mapping, the
                `path` should be a resource path ending with `operations/{unique_id}`.
            metadata (TextToSpeechServiceOperationMetadata | Unset): Service-specific metadata associated with the
                operation.  It typically
                contains progress information and common metadata such as create time.
                Some services might not provide such metadata.  Any method that returns a
                long-running operation should document the metadata type, if any.
            done (bool | Unset): If the value is `false`, it means the operation is still in progress.
                If `true`, the operation is completed, and either `error` or `response` is
                available. Example: True.
            error (TextToSpeechServiceStatus | Unset): The `Status` type defines a logical error model that is suitable for
                different programming environments, including REST APIs and RPC APIs. It is
                used by [gRPC](https://github.com/grpc). Each `Status` message contains
                three pieces of data: error code, error message, and error details.

                You can find out more about this error model and how to work with it in the
                [API Design Guide](https://cloud.google.com/apis/design/errors).
            response (TextToSpeechServiceOperationResponse | Unset): The normal response of the operation in case of
                success.  If the original
                method returns no data on success, such as `Delete`, the response is
                `google.protobuf.Empty`.  If the original method is standard
                `Get`/`Create`/`Update`, the response should be the resource.  For other
                methods, the response should have the type `XxxResponse`, where `Xxx`
                is the original method name.  For example, if the original method name
                is `TakeSnapshot()`, the inferred response type is
                `TakeSnapshotResponse`.
    """

    path: str | Unset = UNSET
    metadata: TextToSpeechServiceOperationMetadata | Unset = UNSET
    done: bool | Unset = UNSET
    error: TextToSpeechServiceStatus | Unset = UNSET
    response: TextToSpeechServiceOperationResponse | Unset = UNSET
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
        from ..models.text_to_speech_service_operation_metadata import TextToSpeechServiceOperationMetadata  # noqa: PLC0415
        from ..models.text_to_speech_service_operation_response import TextToSpeechServiceOperationResponse  # noqa: PLC0415
        from ..models.text_to_speech_service_status import TextToSpeechServiceStatus  # noqa: PLC0415

        d = dict(src_dict)
        path = d.pop("path", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: TextToSpeechServiceOperationMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = TextToSpeechServiceOperationMetadata.from_dict(_metadata)

        done = d.pop("done", UNSET)

        _error = d.pop("error", UNSET)
        error: TextToSpeechServiceStatus | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = TextToSpeechServiceStatus.from_dict(_error)

        _response = d.pop("response", UNSET)
        response: TextToSpeechServiceOperationResponse | Unset
        if isinstance(_response, Unset):
            response = UNSET
        else:
            response = TextToSpeechServiceOperationResponse.from_dict(_response)

        text_to_speech_service_operation = cls(
            path=path,
            metadata=metadata,
            done=done,
            error=error,
            response=response,
        )

        text_to_speech_service_operation.additional_properties = d
        return text_to_speech_service_operation

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
