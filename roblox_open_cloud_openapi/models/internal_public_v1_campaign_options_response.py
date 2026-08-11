from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.internal_public_v1_campaign_options_response_objectives_item import (
    InternalPublicV1CampaignOptionsResponseObjectivesItem,
)
from ..models.internal_public_v1_campaign_options_response_payment_types_item import (
    InternalPublicV1CampaignOptionsResponsePaymentTypesItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_public_v1_ad_format import InternalPublicV1AdFormat
    from ..models.internal_public_v1_targeting_dimensions import InternalPublicV1TargetingDimensions
    from ..models.universe_eligibility import UniverseEligibility


T = TypeVar("T", bound="InternalPublicV1CampaignOptionsResponse")


@_attrs_define
class InternalPublicV1CampaignOptionsResponse:
    """
    Attributes:
        ad_formats (list[InternalPublicV1AdFormat] | Unset): The supported creative formats and their pixel dimensions.
        eligibility (UniverseEligibility | Unset):
        objectives (list[InternalPublicV1CampaignOptionsResponseObjectivesItem] | Unset): The campaign objectives you
            can create. Only `ENGAGEMENT` is supported in v1.
        payment_types (list[InternalPublicV1CampaignOptionsResponsePaymentTypesItem] | Unset): The payment types
            available for the caller's account. Values can be
            `CREDIT_CARD`, `ADS_CREDIT`, or `INVOICE`.
        targeting_dimensions (InternalPublicV1TargetingDimensions | Unset):
    """

    ad_formats: list[InternalPublicV1AdFormat] | Unset = UNSET
    eligibility: UniverseEligibility | Unset = UNSET
    objectives: list[InternalPublicV1CampaignOptionsResponseObjectivesItem] | Unset = UNSET
    payment_types: list[InternalPublicV1CampaignOptionsResponsePaymentTypesItem] | Unset = UNSET
    targeting_dimensions: InternalPublicV1TargetingDimensions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ad_formats: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ad_formats, Unset):
            ad_formats = []
            for ad_formats_item_data in self.ad_formats:
                ad_formats_item = ad_formats_item_data.to_dict()
                ad_formats.append(ad_formats_item)

        eligibility: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eligibility, Unset):
            eligibility = self.eligibility.to_dict()

        objectives: list[str] | Unset = UNSET
        if not isinstance(self.objectives, Unset):
            objectives = []
            for objectives_item_data in self.objectives:
                objectives_item = objectives_item_data.value
                objectives.append(objectives_item)

        payment_types: list[str] | Unset = UNSET
        if not isinstance(self.payment_types, Unset):
            payment_types = []
            for payment_types_item_data in self.payment_types:
                payment_types_item = payment_types_item_data.value
                payment_types.append(payment_types_item)

        targeting_dimensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.targeting_dimensions, Unset):
            targeting_dimensions = self.targeting_dimensions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ad_formats is not UNSET:
            field_dict["adFormats"] = ad_formats
        if eligibility is not UNSET:
            field_dict["eligibility"] = eligibility
        if objectives is not UNSET:
            field_dict["objectives"] = objectives
        if payment_types is not UNSET:
            field_dict["paymentTypes"] = payment_types
        if targeting_dimensions is not UNSET:
            field_dict["targetingDimensions"] = targeting_dimensions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_public_v1_ad_format import InternalPublicV1AdFormat
        from ..models.internal_public_v1_targeting_dimensions import InternalPublicV1TargetingDimensions
        from ..models.universe_eligibility import UniverseEligibility

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _ad_formats = d.pop("adFormats", UNSET)
        ad_formats: list[InternalPublicV1AdFormat] | Unset = UNSET
        if _ad_formats is not UNSET:
            ad_formats = []
            for ad_formats_item_data in _ad_formats:
                ad_formats_item = InternalPublicV1AdFormat.from_dict(ad_formats_item_data)

                ad_formats.append(ad_formats_item)

        _eligibility = d.pop("eligibility", UNSET)
        eligibility: UniverseEligibility | Unset
        if isinstance(_eligibility, Unset):
            eligibility = UNSET
        else:
            eligibility = UniverseEligibility.from_dict(_eligibility)

        _objectives = d.pop("objectives", UNSET)
        objectives: list[InternalPublicV1CampaignOptionsResponseObjectivesItem] | Unset = UNSET
        if _objectives is not UNSET:
            objectives = []
            for objectives_item_data in _objectives:
                objectives_item = InternalPublicV1CampaignOptionsResponseObjectivesItem(objectives_item_data)

                objectives.append(objectives_item)

        _payment_types = d.pop("paymentTypes", UNSET)
        payment_types: list[InternalPublicV1CampaignOptionsResponsePaymentTypesItem] | Unset = UNSET
        if _payment_types is not UNSET:
            payment_types = []
            for payment_types_item_data in _payment_types:
                payment_types_item = InternalPublicV1CampaignOptionsResponsePaymentTypesItem(payment_types_item_data)

                payment_types.append(payment_types_item)

        _targeting_dimensions = d.pop("targetingDimensions", UNSET)
        targeting_dimensions: InternalPublicV1TargetingDimensions | Unset
        if isinstance(_targeting_dimensions, Unset):
            targeting_dimensions = UNSET
        else:
            targeting_dimensions = InternalPublicV1TargetingDimensions.from_dict(_targeting_dimensions)

        internal_public_v1_campaign_options_response = cls(
            ad_formats=ad_formats,
            eligibility=eligibility,
            objectives=objectives,
            payment_types=payment_types,
            targeting_dimensions=targeting_dimensions,
        )

        internal_public_v1_campaign_options_response.additional_properties = d
        return internal_public_v1_campaign_options_response

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
