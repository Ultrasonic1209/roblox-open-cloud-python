from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.search_category_type import SearchCategoryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSaveRequestType0")


@_attrs_define
class CreateSaveRequestType0:
    """Request model for creating a save

    Attributes:
        target_type (SearchCategoryType): This represents a "subset" of Toolbox.Service.CategoryType options and
            represent the full set
            of "categories" (or asset types) that can be searched upon from the toolbox search API.
        target_id (int): The ID of the asset being saved
        collection_name (None | str | Unset): Custom collections are not currently supported.
            This field should be omitted.
    """

    target_type: SearchCategoryType
    target_id: int
    collection_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        target_type = self.target_type.value

        target_id = self.target_id

        collection_name: None | str | Unset
        if isinstance(self.collection_name, Unset):
            collection_name = UNSET
        else:
            collection_name = self.collection_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "targetType": target_type,
                "targetId": target_id,
            }
        )
        if collection_name is not UNSET:
            field_dict["collectionName"] = collection_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        target_type = SearchCategoryType(d.pop("targetType"))

        target_id = d.pop("targetId")

        def _parse_collection_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_name = _parse_collection_name(d.pop("collectionName", UNSET))

        create_save_request_type_0 = cls(
            target_type=target_type,
            target_id=target_id,
            collection_name=collection_name,
        )

        return create_save_request_type_0
