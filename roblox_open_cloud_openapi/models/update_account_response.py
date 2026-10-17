from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.account import Account


T = TypeVar("T", bound="UpdateAccountResponse")


@_attrs_define
class UpdateAccountResponse:
    """Response structure for UpdateAccount endpoints.

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
        from ..models.account import Account

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        account = Account.from_dict(d.pop("account"))

        update_account_response = cls(
            account=account,
        )

        return update_account_response
