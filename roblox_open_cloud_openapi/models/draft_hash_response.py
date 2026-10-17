from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DraftHashResponse")


@_attrs_define
class DraftHashResponse:
    """Response model containing the draft hash.

    Attributes:
        draft_hash (None | str | Unset): The hash of the draft for concurrency control.
    """

    draft_hash: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        draft_hash: None | str | Unset
        if isinstance(self.draft_hash, Unset):
            draft_hash = UNSET
        else:
            draft_hash = self.draft_hash

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if draft_hash is not UNSET:
            field_dict["draftHash"] = draft_hash

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_draft_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        draft_hash = _parse_draft_hash(d.pop("draftHash", UNSET))

        draft_hash_response = cls(
            draft_hash=draft_hash,
        )

        return draft_hash_response
