from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analytics_query_public_api_operation_metadata import AnalyticsQueryPublicApiOperationMetadata
    from ..models.analytics_query_public_api_query_error import AnalyticsQueryPublicApiQueryError


T = TypeVar("T", bound="AnalyticsQueryPublicApiOperationError")


@_attrs_define
class AnalyticsQueryPublicApiOperationError:
    """A completed long-running operation that failed with an error.

    Attributes:
        path (None | str | Unset): The server-assigned resource path.
        done (bool | Unset): If false, the operation is still in progress. If true, the operation is completed.
        error (AnalyticsQueryPublicApiQueryError | Unset): The error returned from a query request.
        metadata (AnalyticsQueryPublicApiOperationMetadata | Unset): The metadata associated with a long-running
            operation.
    """

    path: None | str | Unset = UNSET
    done: bool | Unset = UNSET
    error: AnalyticsQueryPublicApiQueryError | Unset = UNSET
    metadata: AnalyticsQueryPublicApiOperationMetadata | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        done = self.done

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if done is not UNSET:
            field_dict["done"] = done
        if error is not UNSET:
            field_dict["error"] = error
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_query_public_api_operation_metadata import AnalyticsQueryPublicApiOperationMetadata
        from ..models.analytics_query_public_api_query_error import AnalyticsQueryPublicApiQueryError

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        done = d.pop("done", UNSET)

        _error = d.pop("error", UNSET)
        error: AnalyticsQueryPublicApiQueryError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = AnalyticsQueryPublicApiQueryError.from_dict(_error)

        _metadata = d.pop("metadata", UNSET)
        metadata: AnalyticsQueryPublicApiOperationMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AnalyticsQueryPublicApiOperationMetadata.from_dict(_metadata)

        analytics_query_public_api_operation_error = cls(
            path=path,
            done=done,
            error=error,
            metadata=metadata,
        )

        return analytics_query_public_api_operation_error
