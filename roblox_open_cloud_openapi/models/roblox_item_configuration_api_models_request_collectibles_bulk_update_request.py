from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_models_request_collectibles_bulk_update_payload import (
        RobloxItemConfigurationApiModelsRequestCollectiblesBulkUpdatePayload,
    )
    from ..models.roblox_item_configuration_api_models_request_collectibles_bulk_update_targets import (
        RobloxItemConfigurationApiModelsRequestCollectiblesBulkUpdateTargets,
    )


T = TypeVar("T", bound="RobloxItemConfigurationApiModelsRequestCollectiblesBulkUpdateRequest")


@_attrs_define
class RobloxItemConfigurationApiModelsRequestCollectiblesBulkUpdateRequest:
    """Request model for bulk updating items.

    Attributes:
        idempotency_key (str | Unset): Idempotency key for the bulk update request.
        group_id (int | Unset): The group id, if the update is for a group.
        update_targets (RobloxItemConfigurationApiModelsRequestCollectiblesBulkUpdateTargets | Unset): Targets model for
            bulk update.
        update_payload (RobloxItemConfigurationApiModelsRequestCollectiblesBulkUpdatePayload | Unset): Payload model for
            bulk updating items.
    """

    idempotency_key: str | Unset = UNSET
    group_id: int | Unset = UNSET
    update_targets: RobloxItemConfigurationApiModelsRequestCollectiblesBulkUpdateTargets | Unset = UNSET
    update_payload: RobloxItemConfigurationApiModelsRequestCollectiblesBulkUpdatePayload | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        idempotency_key = self.idempotency_key

        group_id = self.group_id

        update_targets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_targets, Unset):
            update_targets = self.update_targets.to_dict()

        update_payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_payload, Unset):
            update_payload = self.update_payload.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if idempotency_key is not UNSET:
            field_dict["idempotencyKey"] = idempotency_key
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if update_targets is not UNSET:
            field_dict["updateTargets"] = update_targets
        if update_payload is not UNSET:
            field_dict["updatePayload"] = update_payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_models_request_collectibles_bulk_update_payload import (
            RobloxItemConfigurationApiModelsRequestCollectiblesBulkUpdatePayload,  # noqa: PLC0415
        )
        from ..models.roblox_item_configuration_api_models_request_collectibles_bulk_update_targets import (
            RobloxItemConfigurationApiModelsRequestCollectiblesBulkUpdateTargets,  # noqa: PLC0415
        )

        d = dict(src_dict)
        idempotency_key = d.pop("idempotencyKey", UNSET)

        group_id = d.pop("groupId", UNSET)

        _update_targets = d.pop("updateTargets", UNSET)
        update_targets: RobloxItemConfigurationApiModelsRequestCollectiblesBulkUpdateTargets | Unset
        if isinstance(_update_targets, Unset):
            update_targets = UNSET
        else:
            update_targets = RobloxItemConfigurationApiModelsRequestCollectiblesBulkUpdateTargets.from_dict(
                _update_targets
            )

        _update_payload = d.pop("updatePayload", UNSET)
        update_payload: RobloxItemConfigurationApiModelsRequestCollectiblesBulkUpdatePayload | Unset
        if isinstance(_update_payload, Unset):
            update_payload = UNSET
        else:
            update_payload = RobloxItemConfigurationApiModelsRequestCollectiblesBulkUpdatePayload.from_dict(
                _update_payload
            )

        roblox_item_configuration_api_models_request_collectibles_bulk_update_request = cls(
            idempotency_key=idempotency_key,
            group_id=group_id,
            update_targets=update_targets,
            update_payload=update_payload,
        )

        return roblox_item_configuration_api_models_request_collectibles_bulk_update_request
