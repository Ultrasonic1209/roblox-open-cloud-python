from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AlertStorageWebhookReceiver")


@_attrs_define
class AlertStorageWebhookReceiver:
    """A single webhook notification destination linked to an alert configuration.

    Attributes:
        webhook_configuration_id (str): The ID of the webhook configuration in the Webhook Delivery System. Must be a
            valid
            UUID and unique within the list on this alert configuration.
    """

    webhook_configuration_id: str

    def to_dict(self) -> dict[str, Any]:
        webhook_configuration_id = self.webhook_configuration_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "webhookConfigurationId": webhook_configuration_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        webhook_configuration_id = d.pop("webhookConfigurationId")

        alert_storage_webhook_receiver = cls(
            webhook_configuration_id=webhook_configuration_id,
        )

        return alert_storage_webhook_receiver
