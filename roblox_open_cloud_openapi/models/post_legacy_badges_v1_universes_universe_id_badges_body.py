from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.post_legacy_badges_v1_universes_universe_id_badges_body_payment_source_type import (
    PostLegacyBadgesV1UniversesUniverseIdBadgesBodyPaymentSourceType,
)
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="PostLegacyBadgesV1UniversesUniverseIdBadgesBody")


@_attrs_define
class PostLegacyBadgesV1UniversesUniverseIdBadgesBody:
    """
    Attributes:
        name (str | Unset): The badge name.
        description (str | Unset): The badge description.
        payment_source_type (PostLegacyBadgesV1UniversesUniverseIdBadgesBodyPaymentSourceType | Unset): Whether or not
            to pay for the badge with user funds, or group funds. ['User' = 1, 'Group' = 2]
        files (File | Unset): The badge icon. Optional: when omitted and a curated default badge icon is configured on
            the service, the badge is created with that default icon. When provided, exactly one file
            must be supplied.
        expected_cost (int | Unset): User expected cost of a badge.
        is_active (bool | Unset): Whether or not the badge should be created in the active state.
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    payment_source_type: PostLegacyBadgesV1UniversesUniverseIdBadgesBodyPaymentSourceType | Unset = UNSET
    files: File | Unset = UNSET
    expected_cost: int | Unset = UNSET
    is_active: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        payment_source_type: int | Unset = UNSET
        if not isinstance(self.payment_source_type, Unset):
            payment_source_type = self.payment_source_type.value

        files: FileTypes | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_tuple()

        expected_cost = self.expected_cost

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if payment_source_type is not UNSET:
            field_dict["paymentSourceType"] = payment_source_type
        if files is not UNSET:
            field_dict["files"] = files
        if expected_cost is not UNSET:
            field_dict["expectedCost"] = expected_cost
        if is_active is not UNSET:
            field_dict["isActive"] = is_active

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.payment_source_type, Unset):
            files.append(("paymentSourceType", (None, str(self.payment_source_type.value).encode(), "text/plain")))

        if not isinstance(self.files, Unset):
            files.append(("files", self.files.to_tuple()))

        if not isinstance(self.expected_cost, Unset):
            files.append(("expectedCost", (None, str(self.expected_cost).encode(), "text/plain")))

        if not isinstance(self.is_active, Unset):
            files.append(("isActive", (None, str(self.is_active).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _payment_source_type = d.pop("paymentSourceType", UNSET)
        payment_source_type: PostLegacyBadgesV1UniversesUniverseIdBadgesBodyPaymentSourceType | Unset
        if isinstance(_payment_source_type, Unset):
            payment_source_type = UNSET
        else:
            payment_source_type = PostLegacyBadgesV1UniversesUniverseIdBadgesBodyPaymentSourceType(_payment_source_type)

        _files = d.pop("files", UNSET)
        files: File | Unset
        if isinstance(_files, Unset):
            files = UNSET
        else:
            files = File(payload=BytesIO(_files))

        expected_cost = d.pop("expectedCost", UNSET)

        is_active = d.pop("isActive", UNSET)

        post_legacy_badges_v1_universes_universe_id_badges_body = cls(
            name=name,
            description=description,
            payment_source_type=payment_source_type,
            files=files,
            expected_cost=expected_cost,
            is_active=is_active,
        )

        post_legacy_badges_v1_universes_universe_id_badges_body.additional_properties = d
        return post_legacy_badges_v1_universes_universe_id_badges_body

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
