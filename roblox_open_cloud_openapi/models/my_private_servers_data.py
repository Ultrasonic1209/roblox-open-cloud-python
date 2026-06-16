from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.private_server_subscription_metadata import PrivateServerSubscriptionMetadata


T = TypeVar("T", bound="MyPrivateServersData")


@_attrs_define
class MyPrivateServersData:
    """
    Attributes:
        active (bool | Unset):
        universe_id (int | Unset):
        place_id (int | None | Unset):
        name (None | str | Unset):
        owner_id (int | Unset):
        owner_name (None | str | Unset):
        price_in_robux (int | None | Unset):
        private_server_id (int | Unset):
        expiration_date (datetime.datetime | Unset):
        will_renew (bool | Unset):
        universe_name (None | str | Unset):
        purchase_schedule_id (int | None | Unset):
        total_discount_amount_in_robux (int | None | Unset):
        metadata (None | PrivateServerSubscriptionMetadata | Unset):
    """

    active: bool | Unset = UNSET
    universe_id: int | Unset = UNSET
    place_id: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    owner_id: int | Unset = UNSET
    owner_name: None | str | Unset = UNSET
    price_in_robux: int | None | Unset = UNSET
    private_server_id: int | Unset = UNSET
    expiration_date: datetime.datetime | Unset = UNSET
    will_renew: bool | Unset = UNSET
    universe_name: None | str | Unset = UNSET
    purchase_schedule_id: int | None | Unset = UNSET
    total_discount_amount_in_robux: int | None | Unset = UNSET
    metadata: None | PrivateServerSubscriptionMetadata | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.private_server_subscription_metadata import PrivateServerSubscriptionMetadata

        active = self.active

        universe_id = self.universe_id

        place_id: int | None | Unset
        if isinstance(self.place_id, Unset):
            place_id = UNSET
        else:
            place_id = self.place_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        owner_id = self.owner_id

        owner_name: None | str | Unset
        if isinstance(self.owner_name, Unset):
            owner_name = UNSET
        else:
            owner_name = self.owner_name

        price_in_robux: int | None | Unset
        if isinstance(self.price_in_robux, Unset):
            price_in_robux = UNSET
        else:
            price_in_robux = self.price_in_robux

        private_server_id = self.private_server_id

        expiration_date: str | Unset = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        will_renew = self.will_renew

        universe_name: None | str | Unset
        if isinstance(self.universe_name, Unset):
            universe_name = UNSET
        else:
            universe_name = self.universe_name

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
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if place_id is not UNSET:
            field_dict["placeId"] = place_id
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if owner_name is not UNSET:
            field_dict["ownerName"] = owner_name
        if price_in_robux is not UNSET:
            field_dict["priceInRobux"] = price_in_robux
        if private_server_id is not UNSET:
            field_dict["privateServerId"] = private_server_id
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if will_renew is not UNSET:
            field_dict["willRenew"] = will_renew
        if universe_name is not UNSET:
            field_dict["universeName"] = universe_name
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

        universe_id = d.pop("universeId", UNSET)

        def _parse_place_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        place_id = _parse_place_id(d.pop("placeId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        owner_id = d.pop("ownerId", UNSET)

        def _parse_owner_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_name = _parse_owner_name(d.pop("ownerName", UNSET))

        def _parse_price_in_robux(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        price_in_robux = _parse_price_in_robux(d.pop("priceInRobux", UNSET))

        private_server_id = d.pop("privateServerId", UNSET)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: datetime.datetime | Unset
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = datetime.datetime.fromisoformat(_expiration_date)

        will_renew = d.pop("willRenew", UNSET)

        def _parse_universe_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        universe_name = _parse_universe_name(d.pop("universeName", UNSET))

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

        my_private_servers_data = cls(
            active=active,
            universe_id=universe_id,
            place_id=place_id,
            name=name,
            owner_id=owner_id,
            owner_name=owner_name,
            price_in_robux=price_in_robux,
            private_server_id=private_server_id,
            expiration_date=expiration_date,
            will_renew=will_renew,
            universe_name=universe_name,
            purchase_schedule_id=purchase_schedule_id,
            total_discount_amount_in_robux=total_discount_amount_in_robux,
            metadata=metadata,
        )

        return my_private_servers_data
