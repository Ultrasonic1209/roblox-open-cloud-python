from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.roblox_subscriptions_open_cloud_v2_subscription_expiration_details_reason import (
    RobloxSubscriptionsOpenCloudV2SubscriptionExpirationDetailsReason,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxSubscriptionsOpenCloudV2SubscriptionExpirationDetails")


@_attrs_define
class RobloxSubscriptionsOpenCloudV2SubscriptionExpirationDetails:
    """Information about the expiration of a subscription.

    Attributes:
        reason (RobloxSubscriptionsOpenCloudV2SubscriptionExpirationDetailsReason | Unset): The reason the subscription
            expired.

            Possible values:

              | Value | Description |
              | --- | --- |
              | EXPIRATION_REASON_UNSPECIFIED | The expiration reason is unspecified. |
              | PRODUCT_INACTIVE | The subscription product is inactive. |
              | PRODUCT_DELETED | The subscription product is deleted. |
              | SUBSCRIBER_CANCELLED | The subscriber cancelled the subscription. |
              | SUBSCRIBER_REFUNDED | The subscriber requested a refund. |
              | LAPSED | The subscriber’s payment was not received. | Example: EXPIRATION_REASON_UNSPECIFIED.
    """

    reason: RobloxSubscriptionsOpenCloudV2SubscriptionExpirationDetailsReason | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason: str | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _reason = d.pop("reason", UNSET)
        reason: RobloxSubscriptionsOpenCloudV2SubscriptionExpirationDetailsReason | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = RobloxSubscriptionsOpenCloudV2SubscriptionExpirationDetailsReason(_reason)

        roblox_subscriptions_open_cloud_v2_subscription_expiration_details = cls(
            reason=reason,
        )

        roblox_subscriptions_open_cloud_v2_subscription_expiration_details.additional_properties = d
        return roblox_subscriptions_open_cloud_v2_subscription_expiration_details

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
