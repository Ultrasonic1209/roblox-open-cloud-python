from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subscription_payment_provider import SubscriptionPaymentProvider
from ..models.subscription_purchase_platform import SubscriptionPurchasePlatform
from ..models.subscription_state import SubscriptionState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscription_expiration_details import SubscriptionExpirationDetails


T = TypeVar("T", bound="Subscription")


@_attrs_define
class Subscription:
    """Represents a user's subscription to a subscription product. The
    subscription ID is the same as the user ID of the user who subscribed.

        Attributes:
            path (str | Unset): The resource path of the subscription.

                Format:
                `universes/{universe_id}/subscription-products/{subscription_product_id}/subscriptions/{subscription_id}`
                Example: universes/123/subscription-products/some-subscription-product-id/subscriptions/some-subscription-id.
            create_time (datetime.datetime | Unset): The timestamp when the subscription was created. Example:
                2023-07-05T12:34:56Z.
            update_time (datetime.datetime | Unset): The timestamp when the subscription was last updated. Example:
                2023-07-05T12:34:56Z.
            active (bool | Unset): Whether the subscription is active.

                This is equivalent  to whether `state` is equal to SUBSCRIBED_WILL_RENEW,
                SUBSCRIBED_WILL_NOT_RENEW, or SUBSCRIBED_RENEWAL_PAYMENT_PENDING. Example: True.
            will_renew (bool | Unset): Whether the subscription will renew.

                This is equivalent to whether `state` is equal to SUBSCRIBED_WILL_RENEW or
                SUBSCRIBED_RENEWAL_PAYMENT_PENDING. Example: True.
            last_billing_time (datetime.datetime | Unset): The timestamp when the subscription was last billed. Example:
                2023-07-05T12:34:56Z.
            next_renew_time (datetime.datetime | Unset): The timestamp when the subscription will next be automatically
                renewed. Example: 2023-07-05T12:34:56Z.
            expire_time (datetime.datetime | Unset): The timestamp when the subscription will, or did, expire. Example:
                2023-07-05T12:34:56Z.
            state (SubscriptionState | Unset): The state of the subscription.

                Possible values:

                  | Value | Description |
                  | --- | --- |
                  | STATE_UNSPECIFIED | The subscription state is unspecified. |
                  | SUBSCRIBED_WILL_RENEW | The subscription is active and will be automatically renewed at `next_renew_time`. |
                  | SUBSCRIBED_WILL_NOT_RENEW | The subscription is active but will not be automatically renewed. |
                  | SUBSCRIBED_RENEWAL_PAYMENT_PENDING | The subscription is active and within the renewal grace period pending
                payment confirmation. |
                  | EXPIRED | The subscription has expired.  See `expiration_details` for more information. | Example:
                STATE_UNSPECIFIED.
            expiration_details (SubscriptionExpirationDetails | Unset): Information about the expiration of a subscription.
            purchase_platform (SubscriptionPurchasePlatform | Unset): The platform on which the subscription was purchased.

                Possible values:

                  | Value | Description |
                  | --- | --- |
                  | PURCHASE_PLATFORM_UNSPECIFIED | The purchase platform is unspecified. |
                  | DESKTOP | The subscription was purchased on the Roblox website. |
                  | MOBILE | The subscription was purchased on the Roblox mobile app. | Example: PURCHASE_PLATFORM_UNSPECIFIED.
            payment_provider (SubscriptionPaymentProvider | Unset): The payment provider used to purchase the subscription.

                Possible values:

                  | Value | Description |
                  | --- | --- |
                  | PAYMENT_PROVIDER_UNSPECIFIED | The payment provider is unspecified. |
                  | STRIPE | The subscription was purchased using Stripe. |
                  | APPLE | The subscription was purchased using Apple. |
                  | GOOGLE | The subscription was purchased using Google. |
                  | ROBLOX_CREDIT | The subscription was purchased using Roblox Credit. |
                  | ROBUX | The subscription was purchased using Robux. | Example: PAYMENT_PROVIDER_UNSPECIFIED.
            user (str | Unset): The user who subscribed to the subscription. Example: users/123.
    """

    path: str | Unset = UNSET
    create_time: datetime.datetime | Unset = UNSET
    update_time: datetime.datetime | Unset = UNSET
    active: bool | Unset = UNSET
    will_renew: bool | Unset = UNSET
    last_billing_time: datetime.datetime | Unset = UNSET
    next_renew_time: datetime.datetime | Unset = UNSET
    expire_time: datetime.datetime | Unset = UNSET
    state: SubscriptionState | Unset = UNSET
    expiration_details: SubscriptionExpirationDetails | Unset = UNSET
    purchase_platform: SubscriptionPurchasePlatform | Unset = UNSET
    payment_provider: SubscriptionPaymentProvider | Unset = UNSET
    user: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        update_time: str | Unset = UNSET
        if not isinstance(self.update_time, Unset):
            update_time = self.update_time.isoformat()

        active = self.active

        will_renew = self.will_renew

        last_billing_time: str | Unset = UNSET
        if not isinstance(self.last_billing_time, Unset):
            last_billing_time = self.last_billing_time.isoformat()

        next_renew_time: str | Unset = UNSET
        if not isinstance(self.next_renew_time, Unset):
            next_renew_time = self.next_renew_time.isoformat()

        expire_time: str | Unset = UNSET
        if not isinstance(self.expire_time, Unset):
            expire_time = self.expire_time.isoformat()

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        expiration_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expiration_details, Unset):
            expiration_details = self.expiration_details.to_dict()

        purchase_platform: str | Unset = UNSET
        if not isinstance(self.purchase_platform, Unset):
            purchase_platform = self.purchase_platform.value

        payment_provider: str | Unset = UNSET
        if not isinstance(self.payment_provider, Unset):
            payment_provider = self.payment_provider.value

        user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if update_time is not UNSET:
            field_dict["updateTime"] = update_time
        if active is not UNSET:
            field_dict["active"] = active
        if will_renew is not UNSET:
            field_dict["willRenew"] = will_renew
        if last_billing_time is not UNSET:
            field_dict["lastBillingTime"] = last_billing_time
        if next_renew_time is not UNSET:
            field_dict["nextRenewTime"] = next_renew_time
        if expire_time is not UNSET:
            field_dict["expireTime"] = expire_time
        if state is not UNSET:
            field_dict["state"] = state
        if expiration_details is not UNSET:
            field_dict["expirationDetails"] = expiration_details
        if purchase_platform is not UNSET:
            field_dict["purchasePlatform"] = purchase_platform
        if payment_provider is not UNSET:
            field_dict["paymentProvider"] = payment_provider
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscription_expiration_details import SubscriptionExpirationDetails

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        path = d.pop("path", UNSET)

        _create_time = d.pop("createTime", UNSET)
        create_time: datetime.datetime | Unset
        if isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = datetime.datetime.fromisoformat(_create_time)

        _update_time = d.pop("updateTime", UNSET)
        update_time: datetime.datetime | Unset
        if isinstance(_update_time, Unset):
            update_time = UNSET
        else:
            update_time = datetime.datetime.fromisoformat(_update_time)

        active = d.pop("active", UNSET)

        will_renew = d.pop("willRenew", UNSET)

        _last_billing_time = d.pop("lastBillingTime", UNSET)
        last_billing_time: datetime.datetime | Unset
        if isinstance(_last_billing_time, Unset):
            last_billing_time = UNSET
        else:
            last_billing_time = datetime.datetime.fromisoformat(_last_billing_time)

        _next_renew_time = d.pop("nextRenewTime", UNSET)
        next_renew_time: datetime.datetime | Unset
        if isinstance(_next_renew_time, Unset):
            next_renew_time = UNSET
        else:
            next_renew_time = datetime.datetime.fromisoformat(_next_renew_time)

        _expire_time = d.pop("expireTime", UNSET)
        expire_time: datetime.datetime | Unset
        if isinstance(_expire_time, Unset):
            expire_time = UNSET
        else:
            expire_time = datetime.datetime.fromisoformat(_expire_time)

        _state = d.pop("state", UNSET)
        state: SubscriptionState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = SubscriptionState(_state)

        _expiration_details = d.pop("expirationDetails", UNSET)
        expiration_details: SubscriptionExpirationDetails | Unset
        if isinstance(_expiration_details, Unset):
            expiration_details = UNSET
        else:
            expiration_details = SubscriptionExpirationDetails.from_dict(_expiration_details)

        _purchase_platform = d.pop("purchasePlatform", UNSET)
        purchase_platform: SubscriptionPurchasePlatform | Unset
        if isinstance(_purchase_platform, Unset):
            purchase_platform = UNSET
        else:
            purchase_platform = SubscriptionPurchasePlatform(_purchase_platform)

        _payment_provider = d.pop("paymentProvider", UNSET)
        payment_provider: SubscriptionPaymentProvider | Unset
        if isinstance(_payment_provider, Unset):
            payment_provider = UNSET
        else:
            payment_provider = SubscriptionPaymentProvider(_payment_provider)

        user = d.pop("user", UNSET)

        subscription = cls(
            path=path,
            create_time=create_time,
            update_time=update_time,
            active=active,
            will_renew=will_renew,
            last_billing_time=last_billing_time,
            next_renew_time=next_renew_time,
            expire_time=expire_time,
            state=state,
            expiration_details=expiration_details,
            purchase_platform=purchase_platform,
            payment_provider=payment_provider,
            user=user,
        )

        subscription.additional_properties = d
        return subscription

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
