from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_localization_tables_api_translator_agent_type import RobloxLocalizationTablesApiTranslatorAgentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxLocalizationTablesApiTranslator")


@_attrs_define
class RobloxLocalizationTablesApiTranslator:
    """
    Attributes:
        id (int | Unset):
        agent_type (RobloxLocalizationTablesApiTranslatorAgentType | Unset):  ['User' = 0, 'Automation' = 1]
    """

    id: int | Unset = UNSET
    agent_type: RobloxLocalizationTablesApiTranslatorAgentType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        agent_type: str | Unset = UNSET
        if not isinstance(self.agent_type, Unset):
            agent_type = self.agent_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if agent_type is not UNSET:
            field_dict["agentType"] = agent_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        _agent_type = d.pop("agentType", UNSET)
        agent_type: RobloxLocalizationTablesApiTranslatorAgentType | Unset
        if isinstance(_agent_type, Unset):
            agent_type = UNSET
        else:
            agent_type = RobloxLocalizationTablesApiTranslatorAgentType(_agent_type)

        roblox_localization_tables_api_translator = cls(
            id=id,
            agent_type=agent_type,
        )

        return roblox_localization_tables_api_translator
