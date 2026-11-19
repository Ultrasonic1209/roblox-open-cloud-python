from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.campaign_options_response_objectives_item import CampaignOptionsResponseObjectivesItem
from ..models.campaign_options_response_payment_types_item import CampaignOptionsResponsePaymentTypesItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ad_format import AdFormat
    from ..models.billing_account_option import BillingAccountOption
    from ..models.budget_constraint import BudgetConstraint
    from ..models.creative_requirements import CreativeRequirements
    from ..models.objective_option import ObjectiveOption
    from ..models.public_universe_eligibility import PublicUniverseEligibility
    from ..models.targeting_dimensions import TargetingDimensions
    from ..models.video_options import VideoOptions


T = TypeVar("T", bound="CampaignOptionsResponse")


@_attrs_define
class CampaignOptionsResponse:
    """
    Attributes:
        ad_formats (list[AdFormat] | Unset): The recommended creative image sizes, in pixels. Images in other sizes are
            accepted, but these sizes fit the tile best.
        billing_accounts (list[BillingAccountOption] | Unset): The billing accounts you can create a campaign for this
            experience in: your
            own, then the owning group's for a group-owned experience. Pass one as
            billingAccountId when creating the campaign.
        budget_constraints (list[BudgetConstraint] | Unset): The minimum budget per budget type. Without universeId,
            also includes the
            personal account's maximum daily budget for CREDIT_CARD.
            With universeId, read maximumDailyBudgetMicros on the selected billing account.
        creative_requirements (CreativeRequirements | Unset):
        eligibility (PublicUniverseEligibility | Unset):
        mutable_fields (list[str] | Unset): The campaign fields accepted by UpdateCampaign. Lists `video` only when the
            video
            of a campaign can be changed.
        objective_options (list[ObjectiveOption] | Unset): Per-objective availability and targeting support. Filtered to
            the objective
            query parameter when supplied.
        objectives (list[CampaignOptionsResponseObjectivesItem] | Unset): The campaign objectives you can create. Values
            can be `PLAYS`, `ENGAGEMENT`, or
            `ROBUX_SPEND`. objectiveOptions tells you whether each one is available for the
            experience.
        payment_types (list[CampaignOptionsResponsePaymentTypesItem] | Unset): The payment types a campaign may choose.
            Values can be `CREDIT_CARD`,
            `ADS_CREDIT`, or `INVOICE`. With universeId, the payment types at least one of
            billingAccounts can use now; empty when there are none. Without universeId, this
            is a static menu based on the caller's account type. It does not check card
            setup, ad credit activation, or balance; supply universeId for that.
        targeting_dimensions (TargetingDimensions | Unset):
        video (VideoOptions | Unset):
    """

    ad_formats: list[AdFormat] | Unset = UNSET
    billing_accounts: list[BillingAccountOption] | Unset = UNSET
    budget_constraints: list[BudgetConstraint] | Unset = UNSET
    creative_requirements: CreativeRequirements | Unset = UNSET
    eligibility: PublicUniverseEligibility | Unset = UNSET
    mutable_fields: list[str] | Unset = UNSET
    objective_options: list[ObjectiveOption] | Unset = UNSET
    objectives: list[CampaignOptionsResponseObjectivesItem] | Unset = UNSET
    payment_types: list[CampaignOptionsResponsePaymentTypesItem] | Unset = UNSET
    targeting_dimensions: TargetingDimensions | Unset = UNSET
    video: VideoOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ad_formats: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ad_formats, Unset):
            ad_formats = []
            for ad_formats_item_data in self.ad_formats:
                ad_formats_item = ad_formats_item_data.to_dict()
                ad_formats.append(ad_formats_item)

        billing_accounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.billing_accounts, Unset):
            billing_accounts = []
            for billing_accounts_item_data in self.billing_accounts:
                billing_accounts_item = billing_accounts_item_data.to_dict()
                billing_accounts.append(billing_accounts_item)

        budget_constraints: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.budget_constraints, Unset):
            budget_constraints = []
            for budget_constraints_item_data in self.budget_constraints:
                budget_constraints_item = budget_constraints_item_data.to_dict()
                budget_constraints.append(budget_constraints_item)

        creative_requirements: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creative_requirements, Unset):
            creative_requirements = self.creative_requirements.to_dict()

        eligibility: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eligibility, Unset):
            eligibility = self.eligibility.to_dict()

        mutable_fields: list[str] | Unset = UNSET
        if not isinstance(self.mutable_fields, Unset):
            mutable_fields = self.mutable_fields

        objective_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.objective_options, Unset):
            objective_options = []
            for objective_options_item_data in self.objective_options:
                objective_options_item = objective_options_item_data.to_dict()
                objective_options.append(objective_options_item)

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

        video: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video, Unset):
            video = self.video.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ad_formats is not UNSET:
            field_dict["adFormats"] = ad_formats
        if billing_accounts is not UNSET:
            field_dict["billingAccounts"] = billing_accounts
        if budget_constraints is not UNSET:
            field_dict["budgetConstraints"] = budget_constraints
        if creative_requirements is not UNSET:
            field_dict["creativeRequirements"] = creative_requirements
        if eligibility is not UNSET:
            field_dict["eligibility"] = eligibility
        if mutable_fields is not UNSET:
            field_dict["mutableFields"] = mutable_fields
        if objective_options is not UNSET:
            field_dict["objectiveOptions"] = objective_options
        if objectives is not UNSET:
            field_dict["objectives"] = objectives
        if payment_types is not UNSET:
            field_dict["paymentTypes"] = payment_types
        if targeting_dimensions is not UNSET:
            field_dict["targetingDimensions"] = targeting_dimensions
        if video is not UNSET:
            field_dict["video"] = video

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ad_format import AdFormat  # noqa: PLC0415
        from ..models.billing_account_option import BillingAccountOption  # noqa: PLC0415
        from ..models.budget_constraint import BudgetConstraint  # noqa: PLC0415
        from ..models.creative_requirements import CreativeRequirements  # noqa: PLC0415
        from ..models.objective_option import ObjectiveOption  # noqa: PLC0415
        from ..models.public_universe_eligibility import PublicUniverseEligibility  # noqa: PLC0415
        from ..models.targeting_dimensions import TargetingDimensions  # noqa: PLC0415
        from ..models.video_options import VideoOptions  # noqa: PLC0415

        d = dict(src_dict)
        _ad_formats = d.pop("adFormats", UNSET)
        ad_formats: list[AdFormat] | Unset = UNSET
        if _ad_formats is not UNSET:
            ad_formats = []
            for ad_formats_item_data in _ad_formats:
                ad_formats_item = AdFormat.from_dict(ad_formats_item_data)

                ad_formats.append(ad_formats_item)

        _billing_accounts = d.pop("billingAccounts", UNSET)
        billing_accounts: list[BillingAccountOption] | Unset = UNSET
        if _billing_accounts is not UNSET:
            billing_accounts = []
            for billing_accounts_item_data in _billing_accounts:
                billing_accounts_item = BillingAccountOption.from_dict(billing_accounts_item_data)

                billing_accounts.append(billing_accounts_item)

        _budget_constraints = d.pop("budgetConstraints", UNSET)
        budget_constraints: list[BudgetConstraint] | Unset = UNSET
        if _budget_constraints is not UNSET:
            budget_constraints = []
            for budget_constraints_item_data in _budget_constraints:
                budget_constraints_item = BudgetConstraint.from_dict(budget_constraints_item_data)

                budget_constraints.append(budget_constraints_item)

        _creative_requirements = d.pop("creativeRequirements", UNSET)
        creative_requirements: CreativeRequirements | Unset
        if isinstance(_creative_requirements, Unset):
            creative_requirements = UNSET
        else:
            creative_requirements = CreativeRequirements.from_dict(_creative_requirements)

        _eligibility = d.pop("eligibility", UNSET)
        eligibility: PublicUniverseEligibility | Unset
        if isinstance(_eligibility, Unset):
            eligibility = UNSET
        else:
            eligibility = PublicUniverseEligibility.from_dict(_eligibility)

        mutable_fields = cast(list[str], d.pop("mutableFields", UNSET))

        _objective_options = d.pop("objectiveOptions", UNSET)
        objective_options: list[ObjectiveOption] | Unset = UNSET
        if _objective_options is not UNSET:
            objective_options = []
            for objective_options_item_data in _objective_options:
                objective_options_item = ObjectiveOption.from_dict(objective_options_item_data)

                objective_options.append(objective_options_item)

        _objectives = d.pop("objectives", UNSET)
        objectives: list[CampaignOptionsResponseObjectivesItem] | Unset = UNSET
        if _objectives is not UNSET:
            objectives = []
            for objectives_item_data in _objectives:
                objectives_item = CampaignOptionsResponseObjectivesItem(objectives_item_data)

                objectives.append(objectives_item)

        _payment_types = d.pop("paymentTypes", UNSET)
        payment_types: list[CampaignOptionsResponsePaymentTypesItem] | Unset = UNSET
        if _payment_types is not UNSET:
            payment_types = []
            for payment_types_item_data in _payment_types:
                payment_types_item = CampaignOptionsResponsePaymentTypesItem(payment_types_item_data)

                payment_types.append(payment_types_item)

        _targeting_dimensions = d.pop("targetingDimensions", UNSET)
        targeting_dimensions: TargetingDimensions | Unset
        if isinstance(_targeting_dimensions, Unset):
            targeting_dimensions = UNSET
        else:
            targeting_dimensions = TargetingDimensions.from_dict(_targeting_dimensions)

        _video = d.pop("video", UNSET)
        video: VideoOptions | Unset
        if isinstance(_video, Unset):
            video = UNSET
        else:
            video = VideoOptions.from_dict(_video)

        campaign_options_response = cls(
            ad_formats=ad_formats,
            billing_accounts=billing_accounts,
            budget_constraints=budget_constraints,
            creative_requirements=creative_requirements,
            eligibility=eligibility,
            mutable_fields=mutable_fields,
            objective_options=objective_options,
            objectives=objectives,
            payment_types=payment_types,
            targeting_dimensions=targeting_dimensions,
            video=video,
        )

        campaign_options_response.additional_properties = d
        return campaign_options_response

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
