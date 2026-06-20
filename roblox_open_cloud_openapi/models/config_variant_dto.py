from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.config_variant_type import ConfigVariantType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigVariantDto")


@_attrs_define
class ConfigVariantDto:
    """A non-default branch on a config entry (public API discriminated variant).

    Attributes:
        type_ (ConfigVariantType | Unset): Discriminator for entries in CreatorConfigsPublicApi.Models.ConfigVariantDto
            variant lists (full config and revision snapshots).

            conditional
        variant_type_id (None | str | Unset): Identifier for this variant within
            CreatorConfigsPublicApi.Models.ConfigVariantDto.Type (e.g. conditional rule id for
            CreatorConfigsPublicApi.Models.ConfigVariantType.Conditional).
        value (Any | Unset):
    """

    type_: ConfigVariantType | Unset = UNSET
    variant_type_id: None | str | Unset = UNSET
    value: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        variant_type_id: None | str | Unset
        if isinstance(self.variant_type_id, Unset):
            variant_type_id = UNSET
        else:
            variant_type_id = self.variant_type_id

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if variant_type_id is not UNSET:
            field_dict["variantTypeId"] = variant_type_id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _type_ = d.pop("type", UNSET)
        type_: ConfigVariantType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ConfigVariantType(_type_)

        def _parse_variant_type_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variant_type_id = _parse_variant_type_id(d.pop("variantTypeId", UNSET))

        value = d.pop("value", UNSET)

        config_variant_dto = cls(
            type_=type_,
            variant_type_id=variant_type_id,
            value=value,
        )

        return config_variant_dto
