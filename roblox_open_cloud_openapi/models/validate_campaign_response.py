from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_error import PublicError
    from ..models.reason import Reason


T = TypeVar("T", bound="ValidateCampaignResponse")


@_attrs_define
class ValidateCampaignResponse:
    """
    Attributes:
        errors (list[PublicError]): The errors CreateCampaign would return for this request, in the same order.
            Empty when valid.
        valid (bool): Whether CreateCampaign would accept this request.
        warnings (list[Reason]): Non-blocking notes about the request.
        resolved_billing_account_id (str | Unset): The billing account the campaign would be created in.
    """

    errors: list[PublicError]
    valid: bool
    warnings: list[Reason]
    resolved_billing_account_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()
            errors.append(errors_item)

        valid = self.valid

        warnings = []
        for warnings_item_data in self.warnings:
            warnings_item = warnings_item_data.to_dict()
            warnings.append(warnings_item)

        resolved_billing_account_id = self.resolved_billing_account_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errors": errors,
                "valid": valid,
                "warnings": warnings,
            }
        )
        if resolved_billing_account_id is not UNSET:
            field_dict["resolvedBillingAccountId"] = resolved_billing_account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_error import PublicError  # noqa: PLC0415
        from ..models.reason import Reason  # noqa: PLC0415

        d = dict(src_dict)
        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:
            errors_item = PublicError.from_dict(errors_item_data)

            errors.append(errors_item)

        valid = d.pop("valid")

        warnings = []
        _warnings = d.pop("warnings")
        for warnings_item_data in _warnings:
            warnings_item = Reason.from_dict(warnings_item_data)

            warnings.append(warnings_item)

        resolved_billing_account_id = d.pop("resolvedBillingAccountId", UNSET)

        validate_campaign_response = cls(
            errors=errors,
            valid=valid,
            warnings=warnings,
            resolved_billing_account_id=resolved_billing_account_id,
        )

        validate_campaign_response.additional_properties = d
        return validate_campaign_response

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
