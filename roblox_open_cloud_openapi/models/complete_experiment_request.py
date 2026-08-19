from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompleteExperimentRequest")


@_attrs_define
class CompleteExperimentRequest:
    """Request body for
    `POST /v1/experimentation/universes/{universeId}/experiments/{experimentId}:complete`.

        Attributes:
            variant_id (None | str | Unset): ID of the variant to roll out as the winning variant. If omitted, the
                experiment is
                stopped without rolling out a winner.
    """

    variant_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        variant_id: None | str | Unset
        if isinstance(self.variant_id, Unset):
            variant_id = UNSET
        else:
            variant_id = self.variant_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if variant_id is not UNSET:
            field_dict["variantId"] = variant_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_variant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variant_id = _parse_variant_id(d.pop("variantId", UNSET))

        complete_experiment_request = cls(
            variant_id=variant_id,
        )

        return complete_experiment_request
