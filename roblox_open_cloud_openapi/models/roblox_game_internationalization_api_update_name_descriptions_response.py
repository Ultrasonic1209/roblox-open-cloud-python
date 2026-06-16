from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_game_internationalization_api_failed_name_description import (
        RobloxGameInternationalizationApiFailedNameDescription,
    )
    from ..models.roblox_game_internationalization_api_name_description import (
        RobloxGameInternationalizationApiNameDescription,
    )


T = TypeVar("T", bound="RobloxGameInternationalizationApiUpdateNameDescriptionsResponse")


@_attrs_define
class RobloxGameInternationalizationApiUpdateNameDescriptionsResponse:
    """
    Attributes:
        success_operations (list[RobloxGameInternationalizationApiNameDescription] | Unset):
        failed_operations (list[RobloxGameInternationalizationApiFailedNameDescription] | Unset):
    """

    success_operations: list[RobloxGameInternationalizationApiNameDescription] | Unset = UNSET
    failed_operations: list[RobloxGameInternationalizationApiFailedNameDescription] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        success_operations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.success_operations, Unset):
            success_operations = []
            for success_operations_item_data in self.success_operations:
                success_operations_item = success_operations_item_data.to_dict()
                success_operations.append(success_operations_item)

        failed_operations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.failed_operations, Unset):
            failed_operations = []
            for failed_operations_item_data in self.failed_operations:
                failed_operations_item = failed_operations_item_data.to_dict()
                failed_operations.append(failed_operations_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if success_operations is not UNSET:
            field_dict["successOperations"] = success_operations
        if failed_operations is not UNSET:
            field_dict["failedOperations"] = failed_operations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_game_internationalization_api_failed_name_description import (
            RobloxGameInternationalizationApiFailedNameDescription,
        )
        from ..models.roblox_game_internationalization_api_name_description import (
            RobloxGameInternationalizationApiNameDescription,
        )

        d = dict(src_dict)
        _success_operations = d.pop("successOperations", UNSET)
        success_operations: list[RobloxGameInternationalizationApiNameDescription] | Unset = UNSET
        if _success_operations is not UNSET:
            success_operations = []
            for success_operations_item_data in _success_operations:
                success_operations_item = RobloxGameInternationalizationApiNameDescription.from_dict(
                    success_operations_item_data
                )

                success_operations.append(success_operations_item)

        _failed_operations = d.pop("failedOperations", UNSET)
        failed_operations: list[RobloxGameInternationalizationApiFailedNameDescription] | Unset = UNSET
        if _failed_operations is not UNSET:
            failed_operations = []
            for failed_operations_item_data in _failed_operations:
                failed_operations_item = RobloxGameInternationalizationApiFailedNameDescription.from_dict(
                    failed_operations_item_data
                )

                failed_operations.append(failed_operations_item)

        roblox_game_internationalization_api_update_name_descriptions_response = cls(
            success_operations=success_operations,
            failed_operations=failed_operations,
        )

        return roblox_game_internationalization_api_update_name_descriptions_response
