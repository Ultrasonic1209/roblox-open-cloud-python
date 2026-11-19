from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsRequestCollectiblesBulkUpdatePayload")


@_attrs_define
class RobloxItemConfigurationApiModelsRequestCollectiblesBulkUpdatePayload:
    """Payload model for bulk updating items.

    Attributes:
        rental_opt_in (bool | Unset): The Rental Opt in status to be applied to the items.
    """

    rental_opt_in: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        rental_opt_in = self.rental_opt_in

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if rental_opt_in is not UNSET:
            field_dict["rentalOptIn"] = rental_opt_in

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rental_opt_in = d.pop("rentalOptIn", UNSET)

        roblox_item_configuration_api_models_request_collectibles_bulk_update_payload = cls(
            rental_opt_in=rental_opt_in,
        )

        return roblox_item_configuration_api_models_request_collectibles_bulk_update_payload
