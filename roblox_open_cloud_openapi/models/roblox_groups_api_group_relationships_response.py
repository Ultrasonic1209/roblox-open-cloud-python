from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_groups_api_group_relationships_response_relationship_type import (
    RobloxGroupsApiGroupRelationshipsResponseRelationshipType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_group_detail_response import RobloxGroupsApiGroupDetailResponse


T = TypeVar("T", bound="RobloxGroupsApiGroupRelationshipsResponse")


@_attrs_define
class RobloxGroupsApiGroupRelationshipsResponse:
    """A group relationships response model

    Attributes:
        group_id (int | Unset): The group id
        relationship_type (RobloxGroupsApiGroupRelationshipsResponseRelationshipType | Unset): The group relationship
            type ['Allies' = 1, 'Enemies' = 2]
        total_group_count (int | Unset): The total number of groups for this relationship type
        related_groups (list[RobloxGroupsApiGroupDetailResponse] | Unset): The related or requested groups
        next_row_index (int | Unset): The index for the next page of related groups
    """

    group_id: int | Unset = UNSET
    relationship_type: RobloxGroupsApiGroupRelationshipsResponseRelationshipType | Unset = UNSET
    total_group_count: int | Unset = UNSET
    related_groups: list[RobloxGroupsApiGroupDetailResponse] | Unset = UNSET
    next_row_index: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_id = self.group_id

        relationship_type: int | Unset = UNSET
        if not isinstance(self.relationship_type, Unset):
            relationship_type = self.relationship_type.value

        total_group_count = self.total_group_count

        related_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.related_groups, Unset):
            related_groups = []
            for related_groups_item_data in self.related_groups:
                related_groups_item = related_groups_item_data.to_dict()
                related_groups.append(related_groups_item)

        next_row_index = self.next_row_index

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if relationship_type is not UNSET:
            field_dict["relationshipType"] = relationship_type
        if total_group_count is not UNSET:
            field_dict["totalGroupCount"] = total_group_count
        if related_groups is not UNSET:
            field_dict["relatedGroups"] = related_groups
        if next_row_index is not UNSET:
            field_dict["nextRowIndex"] = next_row_index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_group_detail_response import RobloxGroupsApiGroupDetailResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        group_id = d.pop("groupId", UNSET)

        _relationship_type = d.pop("relationshipType", UNSET)
        relationship_type: RobloxGroupsApiGroupRelationshipsResponseRelationshipType | Unset
        if isinstance(_relationship_type, Unset):
            relationship_type = UNSET
        else:
            relationship_type = RobloxGroupsApiGroupRelationshipsResponseRelationshipType(_relationship_type)

        total_group_count = d.pop("totalGroupCount", UNSET)

        _related_groups = d.pop("relatedGroups", UNSET)
        related_groups: list[RobloxGroupsApiGroupDetailResponse] | Unset = UNSET
        if _related_groups is not UNSET:
            related_groups = []
            for related_groups_item_data in _related_groups:
                related_groups_item = RobloxGroupsApiGroupDetailResponse.from_dict(related_groups_item_data)

                related_groups.append(related_groups_item)

        next_row_index = d.pop("nextRowIndex", UNSET)

        roblox_groups_api_group_relationships_response = cls(
            group_id=group_id,
            relationship_type=relationship_type,
            total_group_count=total_group_count,
            related_groups=related_groups,
            next_row_index=next_row_index,
        )

        return roblox_groups_api_group_relationships_response
