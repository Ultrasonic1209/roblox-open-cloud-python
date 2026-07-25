from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.internal_public_v1_campaign_status_delivery_status import InternalPublicV1CampaignStatusDeliveryStatus
from ..models.internal_public_v1_campaign_status_delivery_status_reasons_item import (
    InternalPublicV1CampaignStatusDeliveryStatusReasonsItem,
)
from ..models.internal_public_v1_campaign_status_status import InternalPublicV1CampaignStatusStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalPublicV1CampaignStatus")


@_attrs_define
class InternalPublicV1CampaignStatus:
    """
    Attributes:
        delivery_status (InternalPublicV1CampaignStatusDeliveryStatus | Unset): The current serving state. Can be
            `SERVING`, `IN_REVIEW`, `NOT_SERVING`, or `REJECTED`.
        delivery_status_reasons (list[InternalPublicV1CampaignStatusDeliveryStatusReasonsItem] | Unset): The reasons
            behind the current deliveryStatus. Omitted when there are none.
        id (str | Unset): The campaign identifier.
        status (InternalPublicV1CampaignStatusStatus | Unset): The lifecycle state. Can be `ACTIVE`, `PAUSED`, or
            `CANCELLED`.
    """

    delivery_status: InternalPublicV1CampaignStatusDeliveryStatus | Unset = UNSET
    delivery_status_reasons: list[InternalPublicV1CampaignStatusDeliveryStatusReasonsItem] | Unset = UNSET
    id: str | Unset = UNSET
    status: InternalPublicV1CampaignStatusStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delivery_status: str | Unset = UNSET
        if not isinstance(self.delivery_status, Unset):
            delivery_status = self.delivery_status.value

        delivery_status_reasons: list[str] | Unset = UNSET
        if not isinstance(self.delivery_status_reasons, Unset):
            delivery_status_reasons = []
            for delivery_status_reasons_item_data in self.delivery_status_reasons:
                delivery_status_reasons_item = delivery_status_reasons_item_data.value
                delivery_status_reasons.append(delivery_status_reasons_item)

        id = self.id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delivery_status is not UNSET:
            field_dict["deliveryStatus"] = delivery_status
        if delivery_status_reasons is not UNSET:
            field_dict["deliveryStatusReasons"] = delivery_status_reasons
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _delivery_status = d.pop("deliveryStatus", UNSET)
        delivery_status: InternalPublicV1CampaignStatusDeliveryStatus | Unset
        if isinstance(_delivery_status, Unset):
            delivery_status = UNSET
        else:
            delivery_status = InternalPublicV1CampaignStatusDeliveryStatus(_delivery_status)

        _delivery_status_reasons = d.pop("deliveryStatusReasons", UNSET)
        delivery_status_reasons: list[InternalPublicV1CampaignStatusDeliveryStatusReasonsItem] | Unset = UNSET
        if _delivery_status_reasons is not UNSET:
            delivery_status_reasons = []
            for delivery_status_reasons_item_data in _delivery_status_reasons:
                delivery_status_reasons_item = InternalPublicV1CampaignStatusDeliveryStatusReasonsItem(
                    delivery_status_reasons_item_data
                )

                delivery_status_reasons.append(delivery_status_reasons_item)

        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: InternalPublicV1CampaignStatusStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = InternalPublicV1CampaignStatusStatus(_status)

        internal_public_v1_campaign_status = cls(
            delivery_status=delivery_status,
            delivery_status_reasons=delivery_status_reasons,
            id=id,
            status=status,
        )

        internal_public_v1_campaign_status.additional_properties = d
        return internal_public_v1_campaign_status

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
