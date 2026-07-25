from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.internal_public_v1_billing_account_status import InternalPublicV1BillingAccountStatus
from ..models.internal_public_v1_billing_account_type import InternalPublicV1BillingAccountType
from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalPublicV1BillingAccount")


@_attrs_define
class InternalPublicV1BillingAccount:
    """
    Attributes:
        create_time (str | Unset): The time the account was created, as an RFC 3339 UTC timestamp.
        display_name (str | Unset): The human-readable name of the account.
        id (str | Unset): The unique identifier of the billing account. Use it as the {id} path parameter.
        organization_id (str | Unset): The identifier of the organization that owns the account.
        status (InternalPublicV1BillingAccountStatus | Unset): The current state of the account. Can be `ACTIVE`,
            `DISABLED`, or `ARCHIVED`.
        time_zone (str | Unset): The IANA time zone the account's reporting dates and budget schedules are
            interpreted in. Example: `America/Los_Angeles`.
        type_ (InternalPublicV1BillingAccountType | Unset): The account category. External advertisers are always
            SELF_SERVICE; MANAGED and
            INTERNAL are Roblox-operated accounts. Can be `SELF_SERVICE`, `MANAGED`, or `INTERNAL`.
        update_time (str | Unset): The time the account was last updated, as an RFC 3339 UTC timestamp.
    """

    create_time: str | Unset = UNSET
    display_name: str | Unset = UNSET
    id: str | Unset = UNSET
    organization_id: str | Unset = UNSET
    status: InternalPublicV1BillingAccountStatus | Unset = UNSET
    time_zone: str | Unset = UNSET
    type_: InternalPublicV1BillingAccountType | Unset = UNSET
    update_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_time = self.create_time

        display_name = self.display_name

        id = self.id

        organization_id = self.organization_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        time_zone = self.time_zone

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        update_time = self.update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if id is not UNSET:
            field_dict["id"] = id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if status is not UNSET:
            field_dict["status"] = status
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if type_ is not UNSET:
            field_dict["type"] = type_
        if update_time is not UNSET:
            field_dict["updateTime"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        create_time = d.pop("createTime", UNSET)

        display_name = d.pop("displayName", UNSET)

        id = d.pop("id", UNSET)

        organization_id = d.pop("organizationId", UNSET)

        _status = d.pop("status", UNSET)
        status: InternalPublicV1BillingAccountStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = InternalPublicV1BillingAccountStatus(_status)

        time_zone = d.pop("timeZone", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: InternalPublicV1BillingAccountType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = InternalPublicV1BillingAccountType(_type_)

        update_time = d.pop("updateTime", UNSET)

        internal_public_v1_billing_account = cls(
            create_time=create_time,
            display_name=display_name,
            id=id,
            organization_id=organization_id,
            status=status,
            time_zone=time_zone,
            type_=type_,
            update_time=update_time,
        )

        internal_public_v1_billing_account.additional_properties = d
        return internal_public_v1_billing_account

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
