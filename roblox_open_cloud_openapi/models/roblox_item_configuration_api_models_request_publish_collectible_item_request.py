from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_models_request_publish_collectible_item_request_publishing_type import (
    RobloxItemConfigurationApiModelsRequestPublishCollectibleItemRequestPublishingType,
)
from ..models.roblox_item_configuration_api_models_request_publish_collectible_item_request_resale_restriction import (
    RobloxItemConfigurationApiModelsRequestPublishCollectibleItemRequestResaleRestriction,
)
from ..models.roblox_item_configuration_api_models_request_publish_collectible_item_request_target_type import (
    RobloxItemConfigurationApiModelsRequestPublishCollectibleItemRequestTargetType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_models_request_collectibles_sale_location_configuration_model import (
        RobloxItemConfigurationApiModelsRequestCollectiblesSaleLocationConfigurationModel,
    )


T = TypeVar("T", bound="RobloxItemConfigurationApiModelsRequestPublishCollectibleItemRequest")


@_attrs_define
class RobloxItemConfigurationApiModelsRequestPublishCollectibleItemRequest:
    """Request model to publish a new CollectibleItem.

    Attributes:
        is_rental_opt_in (bool | Unset): Whether the item is opted into rental.
        idempotency_token (str | Unset): Idempotency token for publishing purposes.
        target_id (int | Unset): Target item's Id.
        target_type (RobloxItemConfigurationApiModelsRequestPublishCollectibleItemRequestTargetType | Unset): Target
            item's type. ['Asset' = 0, 'Bundle' = 1, 'IecToken' = 2, 'Look' = 3]
        publishing_type (RobloxItemConfigurationApiModelsRequestPublishCollectibleItemRequestPublishingType | Unset):
            Publishing type of the CollectibleItem. ['Invalid' = 0, 'Limited' = 1, 'NonLimited' = 2]
        agreed_publishing_fee (int | Unset): The publishing fee seen by the end-user.
        creator_user_id (int | Unset): The UserId of the creator if the creator is a user.
        creator_group_id (int | Unset): The GroupId of the creator if the creator is a group.
        publisher_user_id (int | Unset): The UserId of the publisher who pays the publishing fee.
            This should only be set if the creator is a group.
        quantity (int | Unset): The total number of instances for the CollectibleItem.
        quantity_limit_per_user (int | Unset): The max number of instances for the CollectibleItem a user can own.
        resale_restriction (RobloxItemConfigurationApiModelsRequestPublishCollectibleItemRequestResaleRestriction |
            Unset): The resale restriction of the CollectibleItem. ['INVALID' = 0, 'NONE' = 1, 'DISABLED' = 2]
        price_in_robux (int | Unset): The sale price of the CollectibleItem and it will be used as minimum price for
            DPF.
        price_offset (int | Unset): Gets or sets the price offset of the item in Robux above the price floor.
        opt_out_from_regional_pricing (bool | Unset): Whether to opt out of the regional pricing.
        is_free (bool | Unset): Gets or sets if the item is free.
        sale_location_configuration (RobloxItemConfigurationApiModelsRequestCollectiblesSaleLocationConfigurationModel |
            Unset): Model for Sale Location of Collectible Items.
        name (str | Unset): The desired name of the CollectibleItem. If not set, will use the underlying itemname.
        description (str | Unset): The desired description of the CollectibleItem. If not set, will use the underlying
            itemname.
        on_sale_time (datetime.datetime | Unset): Scheduled on sale time for publishing the item.
        off_sale_time (datetime.datetime | Unset): Scheduled off sale time for publishing the item.
        agreement_id (str | Unset): Optional. Content-licensing agreement id for a licensed publish.
            If unset, publishing behavior is unchanged. Not persisted on the collectible.
    """

    is_rental_opt_in: bool | Unset = UNSET
    idempotency_token: str | Unset = UNSET
    target_id: int | Unset = UNSET
    target_type: RobloxItemConfigurationApiModelsRequestPublishCollectibleItemRequestTargetType | Unset = UNSET
    publishing_type: RobloxItemConfigurationApiModelsRequestPublishCollectibleItemRequestPublishingType | Unset = UNSET
    agreed_publishing_fee: int | Unset = UNSET
    creator_user_id: int | Unset = UNSET
    creator_group_id: int | Unset = UNSET
    publisher_user_id: int | Unset = UNSET
    quantity: int | Unset = UNSET
    quantity_limit_per_user: int | Unset = UNSET
    resale_restriction: (
        RobloxItemConfigurationApiModelsRequestPublishCollectibleItemRequestResaleRestriction | Unset
    ) = UNSET
    price_in_robux: int | Unset = UNSET
    price_offset: int | Unset = UNSET
    opt_out_from_regional_pricing: bool | Unset = UNSET
    is_free: bool | Unset = UNSET
    sale_location_configuration: (
        RobloxItemConfigurationApiModelsRequestCollectiblesSaleLocationConfigurationModel | Unset
    ) = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    on_sale_time: datetime.datetime | Unset = UNSET
    off_sale_time: datetime.datetime | Unset = UNSET
    agreement_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_rental_opt_in = self.is_rental_opt_in

        idempotency_token = self.idempotency_token

        target_id = self.target_id

        target_type: int | Unset = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type.value

        publishing_type: int | Unset = UNSET
        if not isinstance(self.publishing_type, Unset):
            publishing_type = self.publishing_type.value

        agreed_publishing_fee = self.agreed_publishing_fee

        creator_user_id = self.creator_user_id

        creator_group_id = self.creator_group_id

        publisher_user_id = self.publisher_user_id

        quantity = self.quantity

        quantity_limit_per_user = self.quantity_limit_per_user

        resale_restriction: int | Unset = UNSET
        if not isinstance(self.resale_restriction, Unset):
            resale_restriction = self.resale_restriction.value

        price_in_robux = self.price_in_robux

        price_offset = self.price_offset

        opt_out_from_regional_pricing = self.opt_out_from_regional_pricing

        is_free = self.is_free

        sale_location_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sale_location_configuration, Unset):
            sale_location_configuration = self.sale_location_configuration.to_dict()

        name = self.name

        description = self.description

        on_sale_time: str | Unset = UNSET
        if not isinstance(self.on_sale_time, Unset):
            on_sale_time = self.on_sale_time.isoformat()

        off_sale_time: str | Unset = UNSET
        if not isinstance(self.off_sale_time, Unset):
            off_sale_time = self.off_sale_time.isoformat()

        agreement_id = self.agreement_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_rental_opt_in is not UNSET:
            field_dict["isRentalOptIn"] = is_rental_opt_in
        if idempotency_token is not UNSET:
            field_dict["idempotencyToken"] = idempotency_token
        if target_id is not UNSET:
            field_dict["targetId"] = target_id
        if target_type is not UNSET:
            field_dict["targetType"] = target_type
        if publishing_type is not UNSET:
            field_dict["publishingType"] = publishing_type
        if agreed_publishing_fee is not UNSET:
            field_dict["agreedPublishingFee"] = agreed_publishing_fee
        if creator_user_id is not UNSET:
            field_dict["creatorUserId"] = creator_user_id
        if creator_group_id is not UNSET:
            field_dict["creatorGroupId"] = creator_group_id
        if publisher_user_id is not UNSET:
            field_dict["publisherUserId"] = publisher_user_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if quantity_limit_per_user is not UNSET:
            field_dict["quantityLimitPerUser"] = quantity_limit_per_user
        if resale_restriction is not UNSET:
            field_dict["resaleRestriction"] = resale_restriction
        if price_in_robux is not UNSET:
            field_dict["priceInRobux"] = price_in_robux
        if price_offset is not UNSET:
            field_dict["priceOffset"] = price_offset
        if opt_out_from_regional_pricing is not UNSET:
            field_dict["optOutFromRegionalPricing"] = opt_out_from_regional_pricing
        if is_free is not UNSET:
            field_dict["isFree"] = is_free
        if sale_location_configuration is not UNSET:
            field_dict["saleLocationConfiguration"] = sale_location_configuration
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if on_sale_time is not UNSET:
            field_dict["onSaleTime"] = on_sale_time
        if off_sale_time is not UNSET:
            field_dict["offSaleTime"] = off_sale_time
        if agreement_id is not UNSET:
            field_dict["agreementId"] = agreement_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_models_request_collectibles_sale_location_configuration_model import (
            RobloxItemConfigurationApiModelsRequestCollectiblesSaleLocationConfigurationModel,  # noqa: PLC0415
        )

        d = dict(src_dict)
        is_rental_opt_in = d.pop("isRentalOptIn", UNSET)

        idempotency_token = d.pop("idempotencyToken", UNSET)

        target_id = d.pop("targetId", UNSET)

        _target_type = d.pop("targetType", UNSET)
        target_type: RobloxItemConfigurationApiModelsRequestPublishCollectibleItemRequestTargetType | Unset
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = RobloxItemConfigurationApiModelsRequestPublishCollectibleItemRequestTargetType(_target_type)

        _publishing_type = d.pop("publishingType", UNSET)
        publishing_type: RobloxItemConfigurationApiModelsRequestPublishCollectibleItemRequestPublishingType | Unset
        if isinstance(_publishing_type, Unset):
            publishing_type = UNSET
        else:
            publishing_type = RobloxItemConfigurationApiModelsRequestPublishCollectibleItemRequestPublishingType(
                _publishing_type
            )

        agreed_publishing_fee = d.pop("agreedPublishingFee", UNSET)

        creator_user_id = d.pop("creatorUserId", UNSET)

        creator_group_id = d.pop("creatorGroupId", UNSET)

        publisher_user_id = d.pop("publisherUserId", UNSET)

        quantity = d.pop("quantity", UNSET)

        quantity_limit_per_user = d.pop("quantityLimitPerUser", UNSET)

        _resale_restriction = d.pop("resaleRestriction", UNSET)
        resale_restriction: (
            RobloxItemConfigurationApiModelsRequestPublishCollectibleItemRequestResaleRestriction | Unset
        )
        if isinstance(_resale_restriction, Unset):
            resale_restriction = UNSET
        else:
            resale_restriction = RobloxItemConfigurationApiModelsRequestPublishCollectibleItemRequestResaleRestriction(
                _resale_restriction
            )

        price_in_robux = d.pop("priceInRobux", UNSET)

        price_offset = d.pop("priceOffset", UNSET)

        opt_out_from_regional_pricing = d.pop("optOutFromRegionalPricing", UNSET)

        is_free = d.pop("isFree", UNSET)

        _sale_location_configuration = d.pop("saleLocationConfiguration", UNSET)
        sale_location_configuration: (
            RobloxItemConfigurationApiModelsRequestCollectiblesSaleLocationConfigurationModel | Unset
        )
        if isinstance(_sale_location_configuration, Unset):
            sale_location_configuration = UNSET
        else:
            sale_location_configuration = (
                RobloxItemConfigurationApiModelsRequestCollectiblesSaleLocationConfigurationModel.from_dict(
                    _sale_location_configuration
                )
            )

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _on_sale_time = d.pop("onSaleTime", UNSET)
        on_sale_time: datetime.datetime | Unset
        if isinstance(_on_sale_time, Unset):
            on_sale_time = UNSET
        else:
            on_sale_time = datetime.datetime.fromisoformat(_on_sale_time)

        _off_sale_time = d.pop("offSaleTime", UNSET)
        off_sale_time: datetime.datetime | Unset
        if isinstance(_off_sale_time, Unset):
            off_sale_time = UNSET
        else:
            off_sale_time = datetime.datetime.fromisoformat(_off_sale_time)

        agreement_id = d.pop("agreementId", UNSET)

        roblox_item_configuration_api_models_request_publish_collectible_item_request = cls(
            is_rental_opt_in=is_rental_opt_in,
            idempotency_token=idempotency_token,
            target_id=target_id,
            target_type=target_type,
            publishing_type=publishing_type,
            agreed_publishing_fee=agreed_publishing_fee,
            creator_user_id=creator_user_id,
            creator_group_id=creator_group_id,
            publisher_user_id=publisher_user_id,
            quantity=quantity,
            quantity_limit_per_user=quantity_limit_per_user,
            resale_restriction=resale_restriction,
            price_in_robux=price_in_robux,
            price_offset=price_offset,
            opt_out_from_regional_pricing=opt_out_from_regional_pricing,
            is_free=is_free,
            sale_location_configuration=sale_location_configuration,
            name=name,
            description=description,
            on_sale_time=on_sale_time,
            off_sale_time=off_sale_time,
            agreement_id=agreement_id,
        )

        return roblox_item_configuration_api_models_request_publish_collectible_item_request
