from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_public_v1_billing_account import InternalPublicV1BillingAccount


T = TypeVar("T", bound="InternalPublicV1ListBillingAccountsResponse")


@_attrs_define
class InternalPublicV1ListBillingAccountsResponse:
    """
    Attributes:
        billing_accounts (list[InternalPublicV1BillingAccount] | Unset): The page of billing accounts.
        next_page_token (str | Unset): The cursor for the next page. Pass it as pageToken to fetch the next page.
            Absent on the last page.
    """

    billing_accounts: list[InternalPublicV1BillingAccount] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billing_accounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.billing_accounts, Unset):
            billing_accounts = []
            for billing_accounts_item_data in self.billing_accounts:
                billing_accounts_item = billing_accounts_item_data.to_dict()
                billing_accounts.append(billing_accounts_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_accounts is not UNSET:
            field_dict["billingAccounts"] = billing_accounts
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_public_v1_billing_account import InternalPublicV1BillingAccount

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _billing_accounts = d.pop("billingAccounts", UNSET)
        billing_accounts: list[InternalPublicV1BillingAccount] | Unset = UNSET
        if _billing_accounts is not UNSET:
            billing_accounts = []
            for billing_accounts_item_data in _billing_accounts:
                billing_accounts_item = InternalPublicV1BillingAccount.from_dict(billing_accounts_item_data)

                billing_accounts.append(billing_accounts_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        internal_public_v1_list_billing_accounts_response = cls(
            billing_accounts=billing_accounts,
            next_page_token=next_page_token,
        )

        internal_public_v1_list_billing_accounts_response.additional_properties = d
        return internal_public_v1_list_billing_accounts_response

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
