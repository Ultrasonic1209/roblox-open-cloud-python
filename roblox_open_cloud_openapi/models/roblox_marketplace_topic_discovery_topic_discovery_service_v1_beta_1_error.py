from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxMarketplaceTopicDiscoveryTopicDiscoveryServiceV1Beta1Error")


@_attrs_define
class RobloxMarketplaceTopicDiscoveryTopicDiscoveryServiceV1Beta1Error:
    """
    Attributes:
        message (str | Unset):
        code (int | Unset):
    """

    message: str | Unset = UNSET
    code: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        code = self.code

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if message is not UNSET:
            field_dict["Message"] = message
        if code is not UNSET:
            field_dict["Code"] = code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("Message", UNSET)

        code = d.pop("Code", UNSET)

        roblox_marketplace_topic_discovery_topic_discovery_service_v1_beta_1_error = cls(
            message=message,
            code=code,
        )

        return roblox_marketplace_topic_discovery_topic_discovery_service_v1_beta_1_error
