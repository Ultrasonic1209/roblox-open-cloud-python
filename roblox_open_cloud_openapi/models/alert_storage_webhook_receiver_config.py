from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_storage_webhook_receiver import AlertStorageWebhookReceiver


T = TypeVar("T", bound="AlertStorageWebhookReceiverConfig")


@_attrs_define
class AlertStorageWebhookReceiverConfig:
    """Webhook notification settings for an alert. When set, each webhook in the
    `receivers` list will be called whenever the alert fires or resolves.
    Set to `null` to disable webhook notifications for the alert.

        Attributes:
            receivers (list[AlertStorageWebhookReceiver] | None | Unset): List of webhook destinations to notify when the
                alert fires or resolves. Each entry
                references a webhook configuration you have created in the Webhook Delivery System.
                The list must contain unique entries with no duplicates.
    """

    receivers: list[AlertStorageWebhookReceiver] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        receivers: list[dict[str, Any]] | None | Unset
        if isinstance(self.receivers, Unset):
            receivers = UNSET
        elif isinstance(self.receivers, list):
            receivers = []
            for receivers_type_0_item_data in self.receivers:
                receivers_type_0_item = receivers_type_0_item_data.to_dict()
                receivers.append(receivers_type_0_item)

        else:
            receivers = self.receivers

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if receivers is not UNSET:
            field_dict["receivers"] = receivers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_storage_webhook_receiver import AlertStorageWebhookReceiver

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_receivers(data: object) -> list[AlertStorageWebhookReceiver] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                receivers_type_0 = []
                _receivers_type_0 = data
                for receivers_type_0_item_data in _receivers_type_0:
                    receivers_type_0_item = AlertStorageWebhookReceiver.from_dict(receivers_type_0_item_data)

                    receivers_type_0.append(receivers_type_0_item)

                return receivers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AlertStorageWebhookReceiver] | None | Unset, data)

        receivers = _parse_receivers(d.pop("receivers", UNSET))

        alert_storage_webhook_receiver_config = cls(
            receivers=receivers,
        )

        return alert_storage_webhook_receiver_config
