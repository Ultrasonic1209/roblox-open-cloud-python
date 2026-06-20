from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LuauExecutionSessionTaskBinaryInput")


@_attrs_define
class LuauExecutionSessionTaskBinaryInput:
    """Represents a large binary input that can be given to a
    `LuauExecutionSessionTask`.

    Each `LuauExecutionSessionTaskBinaryInput` is associated with a presigned URL
    which can be used to upload an arbitrary object. After uploading the object,
    the path of the `LuauExecutionSessionTaskBinaryInput` can be passed when
    creating a `LuauExecutionSessionTask` to make the object available to the
    task.

    Within the task, the contents of the object are made available within a table
    passed as the first argument to the script, with the key `BinaryInput`. The
    following example demonstrates how to retrieve the data:

    ```
    local taskInput: LuauExecutionTaskInput = ({...})[1]
    local buf: buffer = taskInput.BinaryInput
    ```

    Each `LuauExecutionSessionTaskBinaryInput` is valid for 15 minutes from the
    time of creation. Within that time, in desired, you can use it to create
    multiple tasks for the same universe.

    The uploaded binary object must be no larger than 100 MiB.

        Attributes:
            path (str | Unset): The resource path of the luau execution session task binary input.

                Format:
                `universes/{universe_id}/luau-execution-session-task-binary-
                inputs/{luau_execution_session_task_binary_input_id}` Example: universes/123/luau-execution-session-task-binary-
                inputs/123e4567-e89b-12d3-a456-426655440000.
            size (int | Unset): The size of the binary input object to be uploaded.

                The maximum allowed size is 100 MiB.
            upload_uri (str | Unset): Upload the binary input object using this URI.
    """

    path: str | Unset = UNSET
    size: int | Unset = UNSET
    upload_uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        size = self.size

        upload_uri = self.upload_uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if size is not UNSET:
            field_dict["size"] = size
        if upload_uri is not UNSET:
            field_dict["uploadUri"] = upload_uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        path = d.pop("path", UNSET)

        size = d.pop("size", UNSET)

        upload_uri = d.pop("uploadUri", UNSET)

        luau_execution_session_task_binary_input = cls(
            path=path,
            size=size,
            upload_uri=upload_uri,
        )

        luau_execution_session_task_binary_input.additional_properties = d
        return luau_execution_session_task_binary_input

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
