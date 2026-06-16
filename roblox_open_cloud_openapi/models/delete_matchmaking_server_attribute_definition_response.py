from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DeleteMatchmakingServerAttributeDefinitionResponse")


@_attrs_define
class DeleteMatchmakingServerAttributeDefinitionResponse:
    """The response for deleting a matchmaking server attribute definition."""

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        delete_matchmaking_server_attribute_definition_response = cls()

        return delete_matchmaking_server_attribute_definition_response
