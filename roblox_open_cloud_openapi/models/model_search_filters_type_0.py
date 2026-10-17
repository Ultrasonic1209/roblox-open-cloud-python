from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.model_instance_type import ModelInstanceType
from ..models.model_sub_type import ModelSubType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelSearchFiltersType0")


@_attrs_define
class ModelSearchFiltersType0:
    """Model-specific search filter parameters.

    Attributes:
        included_sub_types (list[ModelSubType] | None | Unset): If included, search for assets only with these subtypes.
        excluded_sub_types (list[ModelSubType] | None | Unset): If included, excludes assets with these subtypes.
        included_instance_types (list[ModelInstanceType] | None | Unset): This filters that the following
            [Instance](https://create.roblox.com/docs/reference/engine/classes/Instance) types are included in the model.
    """

    included_sub_types: list[ModelSubType] | None | Unset = UNSET
    excluded_sub_types: list[ModelSubType] | None | Unset = UNSET
    included_instance_types: list[ModelInstanceType] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        included_sub_types: list[str] | None | Unset
        if isinstance(self.included_sub_types, Unset):
            included_sub_types = UNSET
        elif isinstance(self.included_sub_types, list):
            included_sub_types = []
            for included_sub_types_type_0_item_data in self.included_sub_types:
                included_sub_types_type_0_item = included_sub_types_type_0_item_data.value
                included_sub_types.append(included_sub_types_type_0_item)

        else:
            included_sub_types = self.included_sub_types

        excluded_sub_types: list[str] | None | Unset
        if isinstance(self.excluded_sub_types, Unset):
            excluded_sub_types = UNSET
        elif isinstance(self.excluded_sub_types, list):
            excluded_sub_types = []
            for excluded_sub_types_type_0_item_data in self.excluded_sub_types:
                excluded_sub_types_type_0_item = excluded_sub_types_type_0_item_data.value
                excluded_sub_types.append(excluded_sub_types_type_0_item)

        else:
            excluded_sub_types = self.excluded_sub_types

        included_instance_types: list[str] | None | Unset
        if isinstance(self.included_instance_types, Unset):
            included_instance_types = UNSET
        elif isinstance(self.included_instance_types, list):
            included_instance_types = []
            for included_instance_types_type_0_item_data in self.included_instance_types:
                included_instance_types_type_0_item = included_instance_types_type_0_item_data.value
                included_instance_types.append(included_instance_types_type_0_item)

        else:
            included_instance_types = self.included_instance_types

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if included_sub_types is not UNSET:
            field_dict["includedSubTypes"] = included_sub_types
        if excluded_sub_types is not UNSET:
            field_dict["excludedSubTypes"] = excluded_sub_types
        if included_instance_types is not UNSET:
            field_dict["includedInstanceTypes"] = included_instance_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_included_sub_types(data: object) -> list[ModelSubType] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                included_sub_types_type_0 = []
                _included_sub_types_type_0 = data
                for included_sub_types_type_0_item_data in _included_sub_types_type_0:
                    included_sub_types_type_0_item = ModelSubType(included_sub_types_type_0_item_data)

                    included_sub_types_type_0.append(included_sub_types_type_0_item)

                return included_sub_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ModelSubType] | None | Unset, data)

        included_sub_types = _parse_included_sub_types(d.pop("includedSubTypes", UNSET))

        def _parse_excluded_sub_types(data: object) -> list[ModelSubType] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                excluded_sub_types_type_0 = []
                _excluded_sub_types_type_0 = data
                for excluded_sub_types_type_0_item_data in _excluded_sub_types_type_0:
                    excluded_sub_types_type_0_item = ModelSubType(excluded_sub_types_type_0_item_data)

                    excluded_sub_types_type_0.append(excluded_sub_types_type_0_item)

                return excluded_sub_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ModelSubType] | None | Unset, data)

        excluded_sub_types = _parse_excluded_sub_types(d.pop("excludedSubTypes", UNSET))

        def _parse_included_instance_types(data: object) -> list[ModelInstanceType] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                included_instance_types_type_0 = []
                _included_instance_types_type_0 = data
                for included_instance_types_type_0_item_data in _included_instance_types_type_0:
                    included_instance_types_type_0_item = ModelInstanceType(included_instance_types_type_0_item_data)

                    included_instance_types_type_0.append(included_instance_types_type_0_item)

                return included_instance_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ModelInstanceType] | None | Unset, data)

        included_instance_types = _parse_included_instance_types(d.pop("includedInstanceTypes", UNSET))

        model_search_filters_type_0 = cls(
            included_sub_types=included_sub_types,
            excluded_sub_types=excluded_sub_types,
            included_instance_types=included_instance_types,
        )

        return model_search_filters_type_0
