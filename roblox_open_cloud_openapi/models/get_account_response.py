from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.account import Account


T = TypeVar("T", bound="GetAccountResponse")


@_attrs_define
class GetAccountResponse:
    """Response structure for GetAccount endpoints.

    Attributes:
        account (Account): Representation of an Account and its settings.
    """

    account: Account

    def to_dict(self) -> dict[str, Any]:
        account = self.account.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "account": account,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account  # noqa: PLC0415

        d = dict(src_dict)
        account = Account.from_dict(d.pop("account"))

        get_account_response = cls(
            account=account,
        )

        return get_account_response
