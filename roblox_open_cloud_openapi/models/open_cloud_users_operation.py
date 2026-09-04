from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generate_user_thumbnail_metadata import GenerateUserThumbnailMetadata
    from ..models.generate_user_thumbnail_response import GenerateUserThumbnailResponse
    from ..models.open_cloud_users_status import OpenCloudUsersStatus


T = TypeVar("T", bound="OpenCloudUsersOperation")


@_attrs_define
class OpenCloudUsersOperation:
    """This resource represents a long-running operation that is the result of a
    network API call.

        Attributes:
            path (None | str | Unset): The server-assigned path, which is only unique within the same service that
                originally returns it. If you use the default HTTP mapping, the
                `path` should be a resource path ending with `operations/{unique_id}`.
            metadata (GenerateUserThumbnailMetadata | None | Unset): Service-specific metadata associated with the
                operation.  It typically
                contains progress information and common metadata such as create time.
                Some services might not provide such metadata.  Any method that returns a
                long-running operation should document the metadata type, if any.
            done (bool | Unset): If the value is `false`, it means the operation is still in progress.
                If `true`, the operation is completed, and either `error` or `response` is
                available.
            error (None | OpenCloudUsersStatus | Unset): The error result of the operation in case of failure or
                cancellation.
            response (GenerateUserThumbnailResponse | None | Unset): The normal response of the operation in case of
                success.  If the original
                method returns no data on success, such as `Delete`, the response is
                `google.protobuf.Empty`.  If the original method is standard
                `Get`/`Create`/`Update`, the response should be the resource.  For other
                methods, the response should have the type `XxxResponse`, where `Xxx`
                is the original method name.  For example, if the original method name
                is `TakeSnapshot()`, the inferred response type is
                `TakeSnapshotResponse`.
    """

    path: None | str | Unset = UNSET
    metadata: GenerateUserThumbnailMetadata | None | Unset = UNSET
    done: bool | Unset = UNSET
    error: None | OpenCloudUsersStatus | Unset = UNSET
    response: GenerateUserThumbnailResponse | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.generate_user_thumbnail_metadata import GenerateUserThumbnailMetadata
        from ..models.generate_user_thumbnail_response import GenerateUserThumbnailResponse
        from ..models.open_cloud_users_status import OpenCloudUsersStatus

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, GenerateUserThumbnailMetadata):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        done = self.done

        error: dict[str, Any] | None | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        elif isinstance(self.error, OpenCloudUsersStatus):
            error = self.error.to_dict()
        else:
            error = self.error

        response: dict[str, Any] | None | Unset
        if isinstance(self.response, Unset):
            response = UNSET
        elif isinstance(self.response, GenerateUserThumbnailResponse):
            response = self.response.to_dict()
        else:
            response = self.response

        field_dict: dict[str, Any] = {}

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
        from ..models.generate_user_thumbnail_metadata import GenerateUserThumbnailMetadata
        from ..models.generate_user_thumbnail_response import GenerateUserThumbnailResponse
        from ..models.open_cloud_users_status import OpenCloudUsersStatus

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_metadata(data: object) -> GenerateUserThumbnailMetadata | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_1 = GenerateUserThumbnailMetadata.from_dict(data)

                return metadata_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GenerateUserThumbnailMetadata | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        done = d.pop("done", UNSET)

        def _parse_error(data: object) -> None | OpenCloudUsersStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_1 = OpenCloudUsersStatus.from_dict(data)

                return error_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OpenCloudUsersStatus | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_response(data: object) -> GenerateUserThumbnailResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_type_1 = GenerateUserThumbnailResponse.from_dict(data)

                return response_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GenerateUserThumbnailResponse | None | Unset, data)

        response = _parse_response(d.pop("response", UNSET))

        open_cloud_users_operation = cls(
            path=path,
            metadata=metadata,
            done=done,
            error=error,
            response=response,
        )

        return open_cloud_users_operation
