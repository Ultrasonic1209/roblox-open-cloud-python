from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_agent_model_type import RobloxItemConfigurationApiAgentModelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiAgentModel")


@_attrs_define
class RobloxItemConfigurationApiAgentModel:
    """The agent model.

    Attributes:
        type_ (RobloxItemConfigurationApiAgentModelType | Unset):  ['User' = 1, 'Group' = 2]
        id (int | Unset):
        name (str | Unset):
    """

    type_: RobloxItemConfigurationApiAgentModelType | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: int | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: RobloxItemConfigurationApiAgentModelType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RobloxItemConfigurationApiAgentModelType(_type_)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        roblox_item_configuration_api_agent_model = cls(
            type_=type_,
            id=id,
            name=name,
        )

        return roblox_item_configuration_api_agent_model
