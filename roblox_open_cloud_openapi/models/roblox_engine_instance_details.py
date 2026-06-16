from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_engine_folder import RobloxEngineFolder
    from ..models.roblox_engine_local_script import RobloxEngineLocalScript
    from ..models.roblox_engine_module_script import RobloxEngineModuleScript
    from ..models.roblox_engine_script import RobloxEngineScript


T = TypeVar("T", bound="RobloxEngineInstanceDetails")


@_attrs_define
class RobloxEngineInstanceDetails:
    """Contains instance type-specific details about a data model instance.

    Attributes:
        folder (RobloxEngineFolder | Unset): A simple container used to hold and organize Roblox instances.
        local_script (RobloxEngineLocalScript | Unset): A LocalScript is a Lua code container that runs its contents on
            the client (player's device) instead of the server.
        module_script (RobloxEngineModuleScript | Unset): A ModuleScript is a type of Lua source container that runs
            once and must return exactly one value.
        script (RobloxEngineScript | Unset): A Script is a Lua code container that can access server-side objects,
            properties, and events, such as to award badges to players using BadgeService, while LocalScripts on the client
            cannot.
    """

    folder: RobloxEngineFolder | Unset = UNSET
    local_script: RobloxEngineLocalScript | Unset = UNSET
    module_script: RobloxEngineModuleScript | Unset = UNSET
    script: RobloxEngineScript | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        folder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.folder, Unset):
            folder = self.folder.to_dict()

        local_script: dict[str, Any] | Unset = UNSET
        if not isinstance(self.local_script, Unset):
            local_script = self.local_script.to_dict()

        module_script: dict[str, Any] | Unset = UNSET
        if not isinstance(self.module_script, Unset):
            module_script = self.module_script.to_dict()

        script: dict[str, Any] | Unset = UNSET
        if not isinstance(self.script, Unset):
            script = self.script.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if folder is not UNSET:
            field_dict["Folder"] = folder
        if local_script is not UNSET:
            field_dict["LocalScript"] = local_script
        if module_script is not UNSET:
            field_dict["ModuleScript"] = module_script
        if script is not UNSET:
            field_dict["Script"] = script

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_engine_folder import RobloxEngineFolder
        from ..models.roblox_engine_local_script import RobloxEngineLocalScript
        from ..models.roblox_engine_module_script import RobloxEngineModuleScript
        from ..models.roblox_engine_script import RobloxEngineScript

        d = dict(src_dict)
        _folder = d.pop("Folder", UNSET)
        folder: RobloxEngineFolder | Unset
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = RobloxEngineFolder.from_dict(_folder)

        _local_script = d.pop("LocalScript", UNSET)
        local_script: RobloxEngineLocalScript | Unset
        if isinstance(_local_script, Unset):
            local_script = UNSET
        else:
            local_script = RobloxEngineLocalScript.from_dict(_local_script)

        _module_script = d.pop("ModuleScript", UNSET)
        module_script: RobloxEngineModuleScript | Unset
        if isinstance(_module_script, Unset):
            module_script = UNSET
        else:
            module_script = RobloxEngineModuleScript.from_dict(_module_script)

        _script = d.pop("Script", UNSET)
        script: RobloxEngineScript | Unset
        if isinstance(_script, Unset):
            script = UNSET
        else:
            script = RobloxEngineScript.from_dict(_script)

        roblox_engine_instance_details = cls(
            folder=folder,
            local_script=local_script,
            module_script=module_script,
            script=script,
        )

        roblox_engine_instance_details.additional_properties = d
        return roblox_engine_instance_details

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
