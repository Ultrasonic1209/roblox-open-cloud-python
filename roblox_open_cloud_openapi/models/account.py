from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.account_tax_type import AccountTaxType
from ..models.tax_id_type import TaxIdType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Account")


@_attrs_define
class Account:
    """Representation of an Account and its settings.

    Attributes:
        account_tax_type (AccountTaxType): Account setting for tax treatment type.
        account_name (None | str | Unset): Gets or sets the name for this account.
        tax_id (None | str | Unset): Gets or sets the tax id for this account.
        tax_id_type (None | TaxIdType | Unset): Gets or sets the type of the tax id for this account.
    """

    account_tax_type: AccountTaxType
    account_name: None | str | Unset = UNSET
    tax_id: None | str | Unset = UNSET
    tax_id_type: None | TaxIdType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        account_tax_type = self.account_tax_type.value

        account_name: None | str | Unset
        if isinstance(self.account_name, Unset):
            account_name = UNSET
        else:
            account_name = self.account_name

        tax_id: None | str | Unset
        if isinstance(self.tax_id, Unset):
            tax_id = UNSET
        else:
            tax_id = self.tax_id

        tax_id_type: None | str | Unset
        if isinstance(self.tax_id_type, Unset):
            tax_id_type = UNSET
        elif isinstance(self.tax_id_type, TaxIdType):
            tax_id_type = self.tax_id_type.value
        else:
            tax_id_type = self.tax_id_type

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "accountTaxType": account_tax_type,
            }
        )
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if tax_id is not UNSET:
            field_dict["taxId"] = tax_id
        if tax_id_type is not UNSET:
            field_dict["taxIdType"] = tax_id_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_tax_type = AccountTaxType(d.pop("accountTaxType"))

        def _parse_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_name = _parse_account_name(d.pop("accountName", UNSET))

        def _parse_tax_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tax_id = _parse_tax_id(d.pop("taxId", UNSET))

        def _parse_tax_id_type(data: object) -> None | TaxIdType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tax_id_type_type_1 = TaxIdType(data)

                return tax_id_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaxIdType | Unset, data)

        tax_id_type = _parse_tax_id_type(d.pop("taxIdType", UNSET))

        account = cls(
            account_tax_type=account_tax_type,
            account_name=account_name,
            tax_id=tax_id,
            tax_id_type=tax_id_type,
        )

        return account
