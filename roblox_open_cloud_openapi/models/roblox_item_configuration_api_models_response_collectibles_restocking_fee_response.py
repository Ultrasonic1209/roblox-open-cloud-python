from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsResponseCollectiblesRestockingFeeResponse")


@_attrs_define
class RobloxItemConfigurationApiModelsResponseCollectiblesRestockingFeeResponse:
    """Response model for getting the restocking fee.

    Attributes:
        restocking_fee_in_robux (int | Unset): The total restocking fee in Robux.
        unit_restocking_fee_in_robux (int | Unset): The per-unit restocking fee in Robux.
    """

    restocking_fee_in_robux: int | Unset = UNSET
    unit_restocking_fee_in_robux: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        restocking_fee_in_robux = self.restocking_fee_in_robux

        unit_restocking_fee_in_robux = self.unit_restocking_fee_in_robux

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if restocking_fee_in_robux is not UNSET:
            field_dict["restockingFeeInRobux"] = restocking_fee_in_robux
        if unit_restocking_fee_in_robux is not UNSET:
            field_dict["unitRestockingFeeInRobux"] = unit_restocking_fee_in_robux

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        restocking_fee_in_robux = d.pop("restockingFeeInRobux", UNSET)

        unit_restocking_fee_in_robux = d.pop("unitRestockingFeeInRobux", UNSET)

        roblox_item_configuration_api_models_response_collectibles_restocking_fee_response = cls(
            restocking_fee_in_robux=restocking_fee_in_robux,
            unit_restocking_fee_in_robux=unit_restocking_fee_in_robux,
        )

        return roblox_item_configuration_api_models_response_collectibles_restocking_fee_response
