from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="StructuredStackFrame")


@_attrs_define
class StructuredStackFrame:
    """Part of the ServerManagementService.V2.Models.GameServerLog and ServerManagementService.V2.Models.ClientLog response
    objects.
    Representing the metadata for a single frame in a structured stack trace.

        Attributes:
            line (int | Unset): The line number where the error occurred.
            function (None | str | Unset): The name of the function in which the error occurred.
            script_path (None | str | Unset): The data model path to the script where the error occurred.
            script_unique_id (None | str | Unset): The unique id for the script where the error occurred.
                Will be null for frames where the code was from ```loadScript``` or ```require(assetId)```.
                If ServerManagementService.V2.Models.StructuredStackFrame.IsDynamic is true, this will be a dynamic id that does
                not refer to a script in the studio Data Model.
            is_dynamic (bool | None | Unset): Identifies whether the
                ServerManagementService.V2.Models.StructuredStackFrame.ScriptUniqueId refers to a script that exists in the
                Studio Data Model.
                If this is true, then the script that generated the error was copied at runtime.
                This includes Starter scripts (e.g. StarterGui, StarterPack, StarterPlayerScripts, StarterCharacterScripts).
    """

    line: int | Unset = UNSET
    function: None | str | Unset = UNSET
    script_path: None | str | Unset = UNSET
    script_unique_id: None | str | Unset = UNSET
    is_dynamic: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        line = self.line

        function: None | str | Unset
        if isinstance(self.function, Unset):
            function = UNSET
        else:
            function = self.function

        script_path: None | str | Unset
        if isinstance(self.script_path, Unset):
            script_path = UNSET
        else:
            script_path = self.script_path

        script_unique_id: None | str | Unset
        if isinstance(self.script_unique_id, Unset):
            script_unique_id = UNSET
        else:
            script_unique_id = self.script_unique_id

        is_dynamic: bool | None | Unset
        if isinstance(self.is_dynamic, Unset):
            is_dynamic = UNSET
        else:
            is_dynamic = self.is_dynamic

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if line is not UNSET:
            field_dict["line"] = line
        if function is not UNSET:
            field_dict["function"] = function
        if script_path is not UNSET:
            field_dict["scriptPath"] = script_path
        if script_unique_id is not UNSET:
            field_dict["scriptUniqueId"] = script_unique_id
        if is_dynamic is not UNSET:
            field_dict["isDynamic"] = is_dynamic

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        line = d.pop("line", UNSET)

        def _parse_function(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        function = _parse_function(d.pop("function", UNSET))

        def _parse_script_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        script_path = _parse_script_path(d.pop("scriptPath", UNSET))

        def _parse_script_unique_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        script_unique_id = _parse_script_unique_id(d.pop("scriptUniqueId", UNSET))

        def _parse_is_dynamic(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_dynamic = _parse_is_dynamic(d.pop("isDynamic", UNSET))

        structured_stack_frame = cls(
            line=line,
            function=function,
            script_path=script_path,
            script_unique_id=script_unique_id,
            is_dynamic=is_dynamic,
        )

        return structured_stack_frame
