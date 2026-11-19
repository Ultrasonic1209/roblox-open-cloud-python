from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_agent_model import RobloxItemConfigurationApiAgentModel


T = TypeVar("T", bound="RobloxItemConfigurationApiAllowedAgentsAssetTypeActionResponse")


@_attrs_define
class RobloxItemConfigurationApiAllowedAgentsAssetTypeActionResponse:
    """
    Attributes:
        agents (list[RobloxItemConfigurationApiAgentModel] | Unset): The allowed agents for whom a user can perform
            specified action.
    """

    agents: list[RobloxItemConfigurationApiAgentModel] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        agents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.agents, Unset):
            agents = []
            for agents_item_data in self.agents:
                agents_item = agents_item_data.to_dict()
                agents.append(agents_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if agents is not UNSET:
            field_dict["agents"] = agents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_agent_model import RobloxItemConfigurationApiAgentModel  # noqa: PLC0415

        d = dict(src_dict)
        _agents = d.pop("agents", UNSET)
        agents: list[RobloxItemConfigurationApiAgentModel] | Unset = UNSET
        if _agents is not UNSET:
            agents = []
            for agents_item_data in _agents:
                agents_item = RobloxItemConfigurationApiAgentModel.from_dict(agents_item_data)

                agents.append(agents_item)

        roblox_item_configuration_api_allowed_agents_asset_type_action_response = cls(
            agents=agents,
        )

        return roblox_item_configuration_api_allowed_agents_asset_type_action_response
