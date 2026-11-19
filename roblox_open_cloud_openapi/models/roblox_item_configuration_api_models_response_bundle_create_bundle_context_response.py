from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsResponseBundleCreateBundleContextResponse")


@_attrs_define
class RobloxItemConfigurationApiModelsResponseBundleCreateBundleContextResponse:
    """Response DTO for create bundle context endpoint.

    Attributes:
        operation_id (str | Unset): ID that was generated for the given bundle create request.
    """

    operation_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        operation_id = self.operation_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if operation_id is not UNSET:
            field_dict["operationId"] = operation_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation_id = d.pop("operationId", UNSET)

        roblox_item_configuration_api_models_response_bundle_create_bundle_context_response = cls(
            operation_id=operation_id,
        )

        return roblox_item_configuration_api_models_response_bundle_create_bundle_context_response
