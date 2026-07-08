from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.operation_metadata import OperationMetadata


T = TypeVar("T", bound="OperationPending")


@_attrs_define
class OperationPending:
    """A long-running operation that is still in progress.

    Attributes:
        path (None | str | Unset): The server-assigned resource path.
        done (bool | Unset): If false, the operation is still in progress. If true, the operation is completed.
        metadata (OperationMetadata | Unset): The metadata associated with a long-running operation.
    """

    path: None | str | Unset = UNSET
    done: bool | Unset = UNSET
    metadata: OperationMetadata | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        done = self.done

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if done is not UNSET:
            field_dict["done"] = done
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.operation_metadata import OperationMetadata

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        done = d.pop("done", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: OperationMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OperationMetadata.from_dict(_metadata)

        operation_pending = cls(
            path=path,
            done=done,
            metadata=metadata,
        )

        return operation_pending
