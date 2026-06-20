from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matchmaking_server_attribute_definition import MatchmakingServerAttributeDefinition


T = TypeVar("T", bound="ListMatchmakingServerAttributeDefinitionsResponse")


@_attrs_define
class ListMatchmakingServerAttributeDefinitionsResponse:
    """The response for listing matchmaking server attribute definitions.

    Attributes:
        server_attribute_schema (list[MatchmakingServerAttributeDefinition] | None | Unset): All
            ServerAttributeDefinitions for a universe.
    """

    server_attribute_schema: list[MatchmakingServerAttributeDefinition] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        server_attribute_schema: list[dict[str, Any]] | None | Unset
        if isinstance(self.server_attribute_schema, Unset):
            server_attribute_schema = UNSET
        elif isinstance(self.server_attribute_schema, list):
            server_attribute_schema = []
            for server_attribute_schema_type_0_item_data in self.server_attribute_schema:
                server_attribute_schema_type_0_item = server_attribute_schema_type_0_item_data.to_dict()
                server_attribute_schema.append(server_attribute_schema_type_0_item)

        else:
            server_attribute_schema = self.server_attribute_schema

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if server_attribute_schema is not UNSET:
            field_dict["serverAttributeSchema"] = server_attribute_schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matchmaking_server_attribute_definition import MatchmakingServerAttributeDefinition

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_server_attribute_schema(data: object) -> list[MatchmakingServerAttributeDefinition] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                server_attribute_schema_type_0 = []
                _server_attribute_schema_type_0 = data
                for server_attribute_schema_type_0_item_data in _server_attribute_schema_type_0:
                    server_attribute_schema_type_0_item = MatchmakingServerAttributeDefinition.from_dict(
                        server_attribute_schema_type_0_item_data
                    )

                    server_attribute_schema_type_0.append(server_attribute_schema_type_0_item)

                return server_attribute_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MatchmakingServerAttributeDefinition] | None | Unset, data)

        server_attribute_schema = _parse_server_attribute_schema(d.pop("serverAttributeSchema", UNSET))

        list_matchmaking_server_attribute_definitions_response = cls(
            server_attribute_schema=server_attribute_schema,
        )

        return list_matchmaking_server_attribute_definitions_response
