from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsResponseBundleCreateBundleResponse")


@_attrs_define
class RobloxItemConfigurationApiModelsResponseBundleCreateBundleResponse:
    """DTO response for the create bundle request.

    Attributes:
        creation_status_id (str | Unset): ID associated with the corresponding create bundle request.
            This ID is used to query for bundle creation status endpoint.
    """

    creation_status_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        creation_status_id = self.creation_status_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if creation_status_id is not UNSET:
            field_dict["creationStatusId"] = creation_status_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        creation_status_id = d.pop("creationStatusId", UNSET)

        roblox_item_configuration_api_models_response_bundle_create_bundle_response = cls(
            creation_status_id=creation_status_id,
        )

        return roblox_item_configuration_api_models_response_bundle_create_bundle_response
