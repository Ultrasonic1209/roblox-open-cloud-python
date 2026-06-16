from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_groups_api_payout_request_payout_type import RobloxGroupsApiPayoutRequestPayoutType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_payout_recipient_request import RobloxGroupsApiPayoutRecipientRequest
    from ..models.roblox_groups_api_watermark_contribution_request import RobloxGroupsApiWatermarkContributionRequest


T = TypeVar("T", bound="RobloxGroupsApiPayoutRequest")


@_attrs_define
class RobloxGroupsApiPayoutRequest:
    """Multi-payout request information.

    Attributes:
        payout_type (RobloxGroupsApiPayoutRequestPayoutType | Unset): The Roblox.Groups.Api.PayoutType. ['FixedAmount' =
            1, 'Percentage' = 2]
        recipients (list[RobloxGroupsApiPayoutRecipientRequest] | Unset): The recipients of the payouts.
        idempotency_key (str | Unset): The idempotency key of the payout request.
        watermark_contributions (list[RobloxGroupsApiWatermarkContributionRequest] | Unset): Optional watermark
            contributions for DevEx attribution tracking.
    """

    payout_type: RobloxGroupsApiPayoutRequestPayoutType | Unset = UNSET
    recipients: list[RobloxGroupsApiPayoutRecipientRequest] | Unset = UNSET
    idempotency_key: str | Unset = UNSET
    watermark_contributions: list[RobloxGroupsApiWatermarkContributionRequest] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        payout_type: int | Unset = UNSET
        if not isinstance(self.payout_type, Unset):
            payout_type = self.payout_type.value

        recipients: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = []
            for recipients_item_data in self.recipients:
                recipients_item = recipients_item_data.to_dict()
                recipients.append(recipients_item)

        idempotency_key = self.idempotency_key

        watermark_contributions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.watermark_contributions, Unset):
            watermark_contributions = []
            for watermark_contributions_item_data in self.watermark_contributions:
                watermark_contributions_item = watermark_contributions_item_data.to_dict()
                watermark_contributions.append(watermark_contributions_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if payout_type is not UNSET:
            field_dict["PayoutType"] = payout_type
        if recipients is not UNSET:
            field_dict["Recipients"] = recipients
        if idempotency_key is not UNSET:
            field_dict["IdempotencyKey"] = idempotency_key
        if watermark_contributions is not UNSET:
            field_dict["WatermarkContributions"] = watermark_contributions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_payout_recipient_request import RobloxGroupsApiPayoutRecipientRequest
        from ..models.roblox_groups_api_watermark_contribution_request import (
            RobloxGroupsApiWatermarkContributionRequest,
        )

        d = dict(src_dict)
        _payout_type = d.pop("PayoutType", UNSET)
        payout_type: RobloxGroupsApiPayoutRequestPayoutType | Unset
        if isinstance(_payout_type, Unset):
            payout_type = UNSET
        else:
            payout_type = RobloxGroupsApiPayoutRequestPayoutType(_payout_type)

        _recipients = d.pop("Recipients", UNSET)
        recipients: list[RobloxGroupsApiPayoutRecipientRequest] | Unset = UNSET
        if _recipients is not UNSET:
            recipients = []
            for recipients_item_data in _recipients:
                recipients_item = RobloxGroupsApiPayoutRecipientRequest.from_dict(recipients_item_data)

                recipients.append(recipients_item)

        idempotency_key = d.pop("IdempotencyKey", UNSET)

        _watermark_contributions = d.pop("WatermarkContributions", UNSET)
        watermark_contributions: list[RobloxGroupsApiWatermarkContributionRequest] | Unset = UNSET
        if _watermark_contributions is not UNSET:
            watermark_contributions = []
            for watermark_contributions_item_data in _watermark_contributions:
                watermark_contributions_item = RobloxGroupsApiWatermarkContributionRequest.from_dict(
                    watermark_contributions_item_data
                )

                watermark_contributions.append(watermark_contributions_item)

        roblox_groups_api_payout_request = cls(
            payout_type=payout_type,
            recipients=recipients,
            idempotency_key=idempotency_key,
            watermark_contributions=watermark_contributions,
        )

        return roblox_groups_api_payout_request
