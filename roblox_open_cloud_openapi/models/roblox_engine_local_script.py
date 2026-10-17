from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.roblox_engine_local_script_run_context import RobloxEngineLocalScriptRunContext
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxEngineLocalScript")


@_attrs_define
class RobloxEngineLocalScript:
    """A LocalScript is a Lua code container that runs its contents on the client (player's device) instead of the server.

    Attributes:
        enabled (bool | Unset): Determines whether a BaseScript will run or not. Example: True.
        run_context (RobloxEngineLocalScriptRunContext | Unset): Determines the context under which the script will run.

            Possible values:

              | Value | Description |
              | --- | --- |
              | Legacy | Runs in legacy script containers dependent on the type of script used, such as LocalScript or
            Script. |
              | Server | Runs on the server. |
              | Client | Runs on the client. |
              | Plugin | Runs as a descendant of Plugin instances. | Example: Legacy.
        source (str | Unset): The code to be executed.
    """

    enabled: bool | Unset = UNSET
    run_context: RobloxEngineLocalScriptRunContext | Unset = UNSET
    source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        run_context: str | Unset = UNSET
        if not isinstance(self.run_context, Unset):
            run_context = self.run_context.value

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["Enabled"] = enabled
        if run_context is not UNSET:
            field_dict["RunContext"] = run_context
        if source is not UNSET:
            field_dict["Source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("Enabled", UNSET)

        _run_context = d.pop("RunContext", UNSET)
        run_context: RobloxEngineLocalScriptRunContext | Unset
        if isinstance(_run_context, Unset):
            run_context = UNSET
        else:
            run_context = RobloxEngineLocalScriptRunContext(_run_context)

        source = d.pop("Source", UNSET)

        roblox_engine_local_script = cls(
            enabled=enabled,
            run_context=run_context,
            source=source,
        )

        roblox_engine_local_script.additional_properties = d
        return roblox_engine_local_script

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
