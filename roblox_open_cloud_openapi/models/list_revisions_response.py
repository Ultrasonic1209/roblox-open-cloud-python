from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.revision_response import RevisionResponse


T = TypeVar("T", bound="ListRevisionsResponse")


@_attrs_define
class ListRevisionsResponse:
    """Response model for listing revisions.

    Attributes:
        revisions (list[RevisionResponse] | None | Unset): The list of revisions.
    """

    revisions: list[RevisionResponse] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        revisions: list[dict[str, Any]] | None | Unset
        if isinstance(self.revisions, Unset):
            revisions = UNSET
        elif isinstance(self.revisions, list):
            revisions = []
            for revisions_type_0_item_data in self.revisions:
                revisions_type_0_item = revisions_type_0_item_data.to_dict()
                revisions.append(revisions_type_0_item)

        else:
            revisions = self.revisions

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if revisions is not UNSET:
            field_dict["revisions"] = revisions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.revision_response import RevisionResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_revisions(data: object) -> list[RevisionResponse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                revisions_type_0 = []
                _revisions_type_0 = data
                for revisions_type_0_item_data in _revisions_type_0:
                    revisions_type_0_item = RevisionResponse.from_dict(revisions_type_0_item_data)

                    revisions_type_0.append(revisions_type_0_item)

                return revisions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RevisionResponse] | None | Unset, data)

        revisions = _parse_revisions(d.pop("revisions", UNSET))

        list_revisions_response = cls(
            revisions=revisions,
        )

        return list_revisions_response
