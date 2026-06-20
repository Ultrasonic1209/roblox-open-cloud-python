from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.currency_holder_type import CurrencyHolderType
from ..models.transaction_type import TransactionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SalesReportDownloadRequest")


@_attrs_define
class SalesReportDownloadRequest:
    """
    Attributes:
        target_id (int | Unset):
        target_type (CurrencyHolderType | Unset):
        start_date (None | str | Unset):
        end_date (None | str | Unset):
        transaction_type (TransactionType | Unset):
    """

    target_id: int | Unset = UNSET
    target_type: CurrencyHolderType | Unset = UNSET
    start_date: None | str | Unset = UNSET
    end_date: None | str | Unset = UNSET
    transaction_type: TransactionType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        target_id = self.target_id

        target_type: str | Unset = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type.value

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        else:
            start_date = self.start_date

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        else:
            end_date = self.end_date

        transaction_type: str | Unset = UNSET
        if not isinstance(self.transaction_type, Unset):
            transaction_type = self.transaction_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if target_id is not UNSET:
            field_dict["targetId"] = target_id
        if target_type is not UNSET:
            field_dict["targetType"] = target_type
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if transaction_type is not UNSET:
            field_dict["transactionType"] = transaction_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        target_id = d.pop("targetId", UNSET)

        _target_type = d.pop("targetType", UNSET)
        target_type: CurrencyHolderType | Unset
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = CurrencyHolderType(_target_type)

        def _parse_start_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_date = _parse_start_date(d.pop("startDate", UNSET))

        def _parse_end_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_date = _parse_end_date(d.pop("endDate", UNSET))

        _transaction_type = d.pop("transactionType", UNSET)
        transaction_type: TransactionType | Unset
        if isinstance(_transaction_type, Unset):
            transaction_type = UNSET
        else:
            transaction_type = TransactionType(_transaction_type)

        sales_report_download_request = cls(
            target_id=target_id,
            target_type=target_type,
            start_date=start_date,
            end_date=end_date,
            transaction_type=transaction_type,
        )

        return sales_report_download_request
