from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payment_activity import PaymentActivity


T = TypeVar("T", bound="ListPaymentActivitiesResponse")


@_attrs_define
class ListPaymentActivitiesResponse:
    """
    Attributes:
        activities (list[PaymentActivity]): Payment activities for the selected scope; REFUND returns the complete time
            range.
        next_page_token (str | Unset): Opaque cursor for the next page of CHARGE or AD_CREDIT. Absent on the last page
            and for REFUND.
    """

    activities: list[PaymentActivity]
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activities = []
        for activities_item_data in self.activities:
            activities_item = activities_item_data.to_dict()
            activities.append(activities_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activities": activities,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_activity import PaymentActivity  # noqa: PLC0415

        d = dict(src_dict)
        activities = []
        _activities = d.pop("activities")
        for activities_item_data in _activities:
            activities_item = PaymentActivity.from_dict(activities_item_data)

            activities.append(activities_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_payment_activities_response = cls(
            activities=activities,
            next_page_token=next_page_token,
        )

        list_payment_activities_response.additional_properties = d
        return list_payment_activities_response

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
