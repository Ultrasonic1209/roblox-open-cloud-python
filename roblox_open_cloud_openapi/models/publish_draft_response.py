from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublishDraftResponse")


@_attrs_define
class PublishDraftResponse:
    """Response model for publishing a draft.

    Attributes:
        config_version (int | Unset): The configuration version after publishing.
    """

    config_version: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        config_version = self.config_version

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if config_version is not UNSET:
            field_dict["configVersion"] = config_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        config_version = d.pop("configVersion", UNSET)

        publish_draft_response = cls(
            config_version=config_version,
        )

        return publish_draft_response
