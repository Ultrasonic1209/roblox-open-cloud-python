from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataStoreLocation")


@_attrs_define
class DataStoreLocation:
    """Describes where an attribute value exists in DataStore.

    Attributes:
        data_store_name (None | str | Unset): The DataStore name.
        scope (None | str | Unset): The scope of the key in DataStore.
        key_template (None | str | Unset): The key of a DataStore value, with {UserId} replaced by the player's actual
            ID when fetching values.
        value_path (None | str | Unset): A JSON path to a value if it lives in a JSON object.
    """

    data_store_name: None | str | Unset = UNSET
    scope: None | str | Unset = UNSET
    key_template: None | str | Unset = UNSET
    value_path: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        data_store_name: None | str | Unset
        if isinstance(self.data_store_name, Unset):
            data_store_name = UNSET
        else:
            data_store_name = self.data_store_name

        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope

        key_template: None | str | Unset
        if isinstance(self.key_template, Unset):
            key_template = UNSET
        else:
            key_template = self.key_template

        value_path: None | str | Unset
        if isinstance(self.value_path, Unset):
            value_path = UNSET
        else:
            value_path = self.value_path

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if data_store_name is not UNSET:
            field_dict["dataStoreName"] = data_store_name
        if scope is not UNSET:
            field_dict["scope"] = scope
        if key_template is not UNSET:
            field_dict["keyTemplate"] = key_template
        if value_path is not UNSET:
            field_dict["valuePath"] = value_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_data_store_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_store_name = _parse_data_store_name(d.pop("dataStoreName", UNSET))

        def _parse_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))

        def _parse_key_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_template = _parse_key_template(d.pop("keyTemplate", UNSET))

        def _parse_value_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_path = _parse_value_path(d.pop("valuePath", UNSET))

        data_store_location = cls(
            data_store_name=data_store_name,
            scope=scope,
            key_template=key_template,
            value_path=value_path,
        )

        return data_store_location
