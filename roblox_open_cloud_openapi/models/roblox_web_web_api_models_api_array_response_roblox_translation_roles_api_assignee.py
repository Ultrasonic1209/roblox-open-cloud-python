from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_translation_roles_api_assignee import RobloxTranslationRolesApiAssignee


T = TypeVar("T", bound="RobloxWebWebAPIModelsApiArrayResponseRobloxTranslationRolesApiAssignee")


@_attrs_define
class RobloxWebWebAPIModelsApiArrayResponseRobloxTranslationRolesApiAssignee:
    """
    Attributes:
        data (list[RobloxTranslationRolesApiAssignee] | Unset):
    """

    data: list[RobloxTranslationRolesApiAssignee] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_translation_roles_api_assignee import RobloxTranslationRolesApiAssignee  # noqa: PLC0415

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[RobloxTranslationRolesApiAssignee] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = RobloxTranslationRolesApiAssignee.from_dict(data_item_data)

                data.append(data_item)

        roblox_web_web_api_models_api_array_response_roblox_translation_roles_api_assignee = cls(
            data=data,
        )

        return roblox_web_web_api_models_api_array_response_roblox_translation_roles_api_assignee
