from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_localizationtables_localizationtables_v1_change_agent_change_agent_type import (
    RobloxLocalizationtablesLocalizationtablesV1ChangeAgentChangeAgentType,
)
from ..models.roblox_localizationtables_localizationtables_v1_change_agent_optional_id_case import (
    RobloxLocalizationtablesLocalizationtablesV1ChangeAgentOptionalIdCase,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxLocalizationtablesLocalizationtablesV1ChangeAgent")


@_attrs_define
class RobloxLocalizationtablesLocalizationtablesV1ChangeAgent:
    """
    Attributes:
        change_agent_type (RobloxLocalizationtablesLocalizationtablesV1ChangeAgentChangeAgentType | Unset):  ['Invalid'
            = 0, 'User' = 1, 'Automation' = 2, 'Default' = 3]
        id (str | Unset):
        optional_id_case (RobloxLocalizationtablesLocalizationtablesV1ChangeAgentOptionalIdCase | Unset):  ['None' = 0,
            'Id' = 2]
    """

    change_agent_type: RobloxLocalizationtablesLocalizationtablesV1ChangeAgentChangeAgentType | Unset = UNSET
    id: str | Unset = UNSET
    optional_id_case: RobloxLocalizationtablesLocalizationtablesV1ChangeAgentOptionalIdCase | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        change_agent_type: str | Unset = UNSET
        if not isinstance(self.change_agent_type, Unset):
            change_agent_type = self.change_agent_type.value

        id = self.id

        optional_id_case: str | Unset = UNSET
        if not isinstance(self.optional_id_case, Unset):
            optional_id_case = self.optional_id_case.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if change_agent_type is not UNSET:
            field_dict["ChangeAgentType"] = change_agent_type
        if id is not UNSET:
            field_dict["Id"] = id
        if optional_id_case is not UNSET:
            field_dict["OptionalIdCase"] = optional_id_case

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _change_agent_type = d.pop("ChangeAgentType", UNSET)
        change_agent_type: RobloxLocalizationtablesLocalizationtablesV1ChangeAgentChangeAgentType | Unset
        if isinstance(_change_agent_type, Unset):
            change_agent_type = UNSET
        else:
            change_agent_type = RobloxLocalizationtablesLocalizationtablesV1ChangeAgentChangeAgentType(
                _change_agent_type
            )

        id = d.pop("Id", UNSET)

        _optional_id_case = d.pop("OptionalIdCase", UNSET)
        optional_id_case: RobloxLocalizationtablesLocalizationtablesV1ChangeAgentOptionalIdCase | Unset
        if isinstance(_optional_id_case, Unset):
            optional_id_case = UNSET
        else:
            optional_id_case = RobloxLocalizationtablesLocalizationtablesV1ChangeAgentOptionalIdCase(_optional_id_case)

        roblox_localizationtables_localizationtables_v1_change_agent = cls(
            change_agent_type=change_agent_type,
            id=id,
            optional_id_case=optional_id_case,
        )

        return roblox_localizationtables_localizationtables_v1_change_agent
