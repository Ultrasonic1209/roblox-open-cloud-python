from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatorStoreCapabilitiesModelType0")


@_attrs_define
class CreatorStoreCapabilitiesModelType0:
    """Represents the capabilities that a model has (e.g. sandboxing).
    Only present for model asset types; AMRS includes it in the response when available.

        Attributes:
            should_sandbox (bool | Unset): Controls whether the model will be sandboxed upon insertion when it has scripts.
    """

    should_sandbox: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        should_sandbox = self.should_sandbox

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if should_sandbox is not UNSET:
            field_dict["shouldSandbox"] = should_sandbox

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        should_sandbox = d.pop("shouldSandbox", UNSET)

        creator_store_capabilities_model_type_0 = cls(
            should_sandbox=should_sandbox,
        )

        return creator_store_capabilities_model_type_0
