from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.internal_public_v1_campaign_id_failure_reason import InternalPublicV1CampaignIDFailureReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalPublicV1CampaignIDFailure")


@_attrs_define
class InternalPublicV1CampaignIDFailure:
    """
    Attributes:
        id (str | Unset): The campaign ID that could not be resolved.
        reason (InternalPublicV1CampaignIDFailureReason | Unset): Why the ID could not be resolved. `NOT_FOUND` means
            the campaign does not exist
            or is not owned by the caller.
    """

    id: str | Unset = UNSET
    reason: InternalPublicV1CampaignIDFailureReason | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        reason: str | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: InternalPublicV1CampaignIDFailureReason | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = InternalPublicV1CampaignIDFailureReason(_reason)

        internal_public_v1_campaign_id_failure = cls(
            id=id,
            reason=reason,
        )

        internal_public_v1_campaign_id_failure.additional_properties = d
        return internal_public_v1_campaign_id_failure

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
