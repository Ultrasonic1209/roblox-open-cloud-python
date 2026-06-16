from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.private_server_subscription_metadata import PrivateServerSubscriptionMetadata


T = TypeVar("T", bound="PrivateServerSubscriptionResponse")


@_attrs_define
class PrivateServerSubscriptionResponse:
    """
    Attributes:
        active (bool | Unset):
        expired (bool | Unset):
        expiration_date (datetime.datetime | Unset):
        price (int | None | Unset):
        can_renew (bool | Unset):
        has_insufficient_funds (bool | Unset):
        has_recurring_profile (bool | Unset):
        has_price_changed (bool | Unset):
        purchase_schedule_id (int | None | Unset):
        total_discount_amount_in_robux (int | None | Unset):
        metadata (None | PrivateServerSubscriptionMetadata | Unset):
    """

    active: bool | Unset = UNSET
    expired: bool | Unset = UNSET
    expiration_date: datetime.datetime | Unset = UNSET
    price: int | None | Unset = UNSET
    can_renew: bool | Unset = UNSET
    has_insufficient_funds: bool | Unset = UNSET
    has_recurring_profile: bool | Unset = UNSET
    has_price_changed: bool | Unset = UNSET
    purchase_schedule_id: int | None | Unset = UNSET
    total_discount_amount_in_robux: int | None | Unset = UNSET
    metadata: None | PrivateServerSubscriptionMetadata | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.private_server_subscription_metadata import PrivateServerSubscriptionMetadata

        active = self.active

        expired = self.expired

        expiration_date: str | Unset = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        price: int | None | Unset
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        can_renew = self.can_renew

        has_insufficient_funds = self.has_insufficient_funds

        has_recurring_profile = self.has_recurring_profile

        has_price_changed = self.has_price_changed

        purchase_schedule_id: int | None | Unset
        if isinstance(self.purchase_schedule_id, Unset):
            purchase_schedule_id = UNSET
        else:
            purchase_schedule_id = self.purchase_schedule_id

        total_discount_amount_in_robux: int | None | Unset
        if isinstance(self.total_discount_amount_in_robux, Unset):
            total_discount_amount_in_robux = UNSET
        else:
            total_discount_amount_in_robux = self.total_discount_amount_in_robux

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, PrivateServerSubscriptionMetadata):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if expired is not UNSET:
            field_dict["expired"] = expired
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if price is not UNSET:
            field_dict["price"] = price
        if can_renew is not UNSET:
            field_dict["canRenew"] = can_renew
        if has_insufficient_funds is not UNSET:
            field_dict["hasInsufficientFunds"] = has_insufficient_funds
        if has_recurring_profile is not UNSET:
            field_dict["hasRecurringProfile"] = has_recurring_profile
        if has_price_changed is not UNSET:
            field_dict["hasPriceChanged"] = has_price_changed
        if purchase_schedule_id is not UNSET:
            field_dict["purchaseScheduleId"] = purchase_schedule_id
        if total_discount_amount_in_robux is not UNSET:
            field_dict["totalDiscountAmountInRobux"] = total_discount_amount_in_robux
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.private_server_subscription_metadata import PrivateServerSubscriptionMetadata

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        expired = d.pop("expired", UNSET)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: datetime.datetime | Unset
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = datetime.datetime.fromisoformat(_expiration_date)

        def _parse_price(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        price = _parse_price(d.pop("price", UNSET))

        can_renew = d.pop("canRenew", UNSET)

        has_insufficient_funds = d.pop("hasInsufficientFunds", UNSET)

        has_recurring_profile = d.pop("hasRecurringProfile", UNSET)

        has_price_changed = d.pop("hasPriceChanged", UNSET)

        def _parse_purchase_schedule_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        purchase_schedule_id = _parse_purchase_schedule_id(d.pop("purchaseScheduleId", UNSET))

        def _parse_total_discount_amount_in_robux(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_discount_amount_in_robux = _parse_total_discount_amount_in_robux(
            d.pop("totalDiscountAmountInRobux", UNSET)
        )

        def _parse_metadata(data: object) -> None | PrivateServerSubscriptionMetadata | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_1 = PrivateServerSubscriptionMetadata.from_dict(data)

                return metadata_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PrivateServerSubscriptionMetadata | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        private_server_subscription_response = cls(
            active=active,
            expired=expired,
            expiration_date=expiration_date,
            price=price,
            can_renew=can_renew,
            has_insufficient_funds=has_insufficient_funds,
            has_recurring_profile=has_recurring_profile,
            has_price_changed=has_price_changed,
            purchase_schedule_id=purchase_schedule_id,
            total_discount_amount_in_robux=total_discount_amount_in_robux,
            metadata=metadata,
        )

        return private_server_subscription_response
