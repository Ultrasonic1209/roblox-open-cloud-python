from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemoryStoreFlushOperation")


@_attrs_define
class MemoryStoreFlushOperation:
    """This resource represents a long-running operation that is the result of a
    network API call.

        Attributes:
            path (None | str | Unset): The server-assigned path, which is only unique within the same service that
                originally returns it. If you use the default HTTP mapping, the
                `path` should be a resource path ending with `operations/{unique_id}`.
            done (bool | None | Unset): If the value is `false`, it means the operation is still in progress.
                If `true`, the operation is completed. Example: True.
    """

    path: None | str | Unset = UNSET
    done: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        done: bool | None | Unset
        if isinstance(self.done, Unset):
            done = UNSET
        else:
            done = self.done

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if done is not UNSET:
            field_dict["done"] = done

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_done(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        done = _parse_done(d.pop("done", UNSET))

        memory_store_flush_operation = cls(
            path=path,
            done=done,
        )

        return memory_store_flush_operation
