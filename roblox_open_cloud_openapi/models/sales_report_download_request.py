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
        target_id (int):
        target_type (CurrencyHolderType):
        start_date (None | str):
        end_date (None | str):
        transaction_type (TransactionType | Unset):
    """

    target_id: int
    target_type: CurrencyHolderType
    start_date: None | str
    end_date: None | str
    transaction_type: TransactionType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        target_id = self.target_id

        target_type = self.target_type.value

        start_date: None | str
        start_date = self.start_date

        end_date: None | str
        end_date = self.end_date

        transaction_type: str | Unset = UNSET
        if not isinstance(self.transaction_type, Unset):
            transaction_type = self.transaction_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "targetId": target_id,
                "targetType": target_type,
                "startDate": start_date,
                "endDate": end_date,
            }
        )
        if transaction_type is not UNSET:
            field_dict["transactionType"] = transaction_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        target_id = d.pop("targetId")

        target_type = CurrencyHolderType(d.pop("targetType"))

        def _parse_start_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        start_date = _parse_start_date(d.pop("startDate"))

        def _parse_end_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        end_date = _parse_end_date(d.pop("endDate"))

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
