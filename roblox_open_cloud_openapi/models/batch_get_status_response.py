from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.campaign_id_failure import CampaignIDFailure
    from ..models.campaign_status import CampaignStatus


T = TypeVar("T", bound="BatchGetStatusResponse")


@_attrs_define
class BatchGetStatusResponse:
    """
    Attributes:
        failures (list[CampaignIDFailure] | Unset): The IDs that could not be resolved. Omitted when every ID resolved.
        statuses (list[CampaignStatus] | Unset): One entry per successfully resolved campaign.
    """

    failures: list[CampaignIDFailure] | Unset = UNSET
    statuses: list[CampaignStatus] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        failures: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.failures, Unset):
            failures = []
            for failures_item_data in self.failures:
                failures_item = failures_item_data.to_dict()
                failures.append(failures_item)

        statuses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.statuses, Unset):
            statuses = []
            for statuses_item_data in self.statuses:
                statuses_item = statuses_item_data.to_dict()
                statuses.append(statuses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if failures is not UNSET:
            field_dict["failures"] = failures
        if statuses is not UNSET:
            field_dict["statuses"] = statuses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.campaign_id_failure import CampaignIDFailure  # noqa: PLC0415
        from ..models.campaign_status import CampaignStatus  # noqa: PLC0415

        d = dict(src_dict)
        _failures = d.pop("failures", UNSET)
        failures: list[CampaignIDFailure] | Unset = UNSET
        if _failures is not UNSET:
            failures = []
            for failures_item_data in _failures:
                failures_item = CampaignIDFailure.from_dict(failures_item_data)

                failures.append(failures_item)

        _statuses = d.pop("statuses", UNSET)
        statuses: list[CampaignStatus] | Unset = UNSET
        if _statuses is not UNSET:
            statuses = []
            for statuses_item_data in _statuses:
                statuses_item = CampaignStatus.from_dict(statuses_item_data)

                statuses.append(statuses_item)

        batch_get_status_response = cls(
            failures=failures,
            statuses=statuses,
        )

        batch_get_status_response.additional_properties = d
        return batch_get_status_response

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
