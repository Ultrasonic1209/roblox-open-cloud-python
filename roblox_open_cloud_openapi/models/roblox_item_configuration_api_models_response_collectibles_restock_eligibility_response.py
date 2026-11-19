from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_models_response_collectibles_restock_eligibility_response_ineligibility_reason import (
    RobloxItemConfigurationApiModelsResponseCollectiblesRestockEligibilityResponseIneligibilityReason,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsResponseCollectiblesRestockEligibilityResponse")


@_attrs_define
class RobloxItemConfigurationApiModelsResponseCollectiblesRestockEligibilityResponse:
    """Structured eligibility response so the frontend does not need to re-derive restocking eligibility.

    Attributes:
        is_restocking_enabled (bool | Unset): Whether the restocking feature is globally enabled.
        is_eligible (bool | Unset): Whether the item is eligible for restocking right now.
        ineligibility_reason
            (RobloxItemConfigurationApiModelsResponseCollectiblesRestockEligibilityResponseIneligibilityReason | Unset): Why
            the item is ineligible for restocking. Serialized as PascalCase enum name
            (e.g. "NotLimited", "NotFree"). Null/omitted when the item is eligible.
        has_been_restocked (bool | Unset): Whether the item has been restocked before (derived from
            TotalRestockedQuantity > 0).
        total_restocked_quantity (int | Unset): Cumulative restocked quantity so far.
        max_restock_quantity_per_operation (int | Unset): Maximum additional quantity allowed in a single restock
            operation.
    """

    is_restocking_enabled: bool | Unset = UNSET
    is_eligible: bool | Unset = UNSET
    ineligibility_reason: (
        RobloxItemConfigurationApiModelsResponseCollectiblesRestockEligibilityResponseIneligibilityReason | Unset
    ) = UNSET
    has_been_restocked: bool | Unset = UNSET
    total_restocked_quantity: int | Unset = UNSET
    max_restock_quantity_per_operation: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_restocking_enabled = self.is_restocking_enabled

        is_eligible = self.is_eligible

        ineligibility_reason: int | Unset = UNSET
        if not isinstance(self.ineligibility_reason, Unset):
            ineligibility_reason = self.ineligibility_reason.value

        has_been_restocked = self.has_been_restocked

        total_restocked_quantity = self.total_restocked_quantity

        max_restock_quantity_per_operation = self.max_restock_quantity_per_operation

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_restocking_enabled is not UNSET:
            field_dict["isRestockingEnabled"] = is_restocking_enabled
        if is_eligible is not UNSET:
            field_dict["isEligible"] = is_eligible
        if ineligibility_reason is not UNSET:
            field_dict["ineligibilityReason"] = ineligibility_reason
        if has_been_restocked is not UNSET:
            field_dict["hasBeenRestocked"] = has_been_restocked
        if total_restocked_quantity is not UNSET:
            field_dict["totalRestockedQuantity"] = total_restocked_quantity
        if max_restock_quantity_per_operation is not UNSET:
            field_dict["maxRestockQuantityPerOperation"] = max_restock_quantity_per_operation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_restocking_enabled = d.pop("isRestockingEnabled", UNSET)

        is_eligible = d.pop("isEligible", UNSET)

        _ineligibility_reason = d.pop("ineligibilityReason", UNSET)
        ineligibility_reason: (
            RobloxItemConfigurationApiModelsResponseCollectiblesRestockEligibilityResponseIneligibilityReason | Unset
        )
        if isinstance(_ineligibility_reason, Unset):
            ineligibility_reason = UNSET
        else:
            ineligibility_reason = (
                RobloxItemConfigurationApiModelsResponseCollectiblesRestockEligibilityResponseIneligibilityReason(
                    _ineligibility_reason
                )
            )

        has_been_restocked = d.pop("hasBeenRestocked", UNSET)

        total_restocked_quantity = d.pop("totalRestockedQuantity", UNSET)

        max_restock_quantity_per_operation = d.pop("maxRestockQuantityPerOperation", UNSET)

        roblox_item_configuration_api_models_response_collectibles_restock_eligibility_response = cls(
            is_restocking_enabled=is_restocking_enabled,
            is_eligible=is_eligible,
            ineligibility_reason=ineligibility_reason,
            has_been_restocked=has_been_restocked,
            total_restocked_quantity=total_restocked_quantity,
            max_restock_quantity_per_operation=max_restock_quantity_per_operation,
        )

        return roblox_item_configuration_api_models_response_collectibles_restock_eligibility_response
