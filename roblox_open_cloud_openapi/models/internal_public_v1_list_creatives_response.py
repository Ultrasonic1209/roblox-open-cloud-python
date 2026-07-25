from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_public_v1_creative import InternalPublicV1Creative


T = TypeVar("T", bound="InternalPublicV1ListCreativesResponse")


@_attrs_define
class InternalPublicV1ListCreativesResponse:
    """
    Attributes:
        creatives (list[InternalPublicV1Creative] | Unset): The page of creatives.
        next_page_token (str | Unset): The cursor for the next page. Pass it as pageToken to fetch the next page.
            Absent on the last page.
    """

    creatives: list[InternalPublicV1Creative] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creatives: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.creatives, Unset):
            creatives = []
            for creatives_item_data in self.creatives:
                creatives_item = creatives_item_data.to_dict()
                creatives.append(creatives_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creatives is not UNSET:
            field_dict["creatives"] = creatives
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_public_v1_creative import InternalPublicV1Creative

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _creatives = d.pop("creatives", UNSET)
        creatives: list[InternalPublicV1Creative] | Unset = UNSET
        if _creatives is not UNSET:
            creatives = []
            for creatives_item_data in _creatives:
                creatives_item = InternalPublicV1Creative.from_dict(creatives_item_data)

                creatives.append(creatives_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        internal_public_v1_list_creatives_response = cls(
            creatives=creatives,
            next_page_token=next_page_token,
        )

        internal_public_v1_list_creatives_response.additional_properties = d
        return internal_public_v1_list_creatives_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
