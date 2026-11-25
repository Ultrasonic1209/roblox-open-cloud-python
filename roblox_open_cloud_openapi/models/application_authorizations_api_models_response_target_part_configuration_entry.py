from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationAuthorizationsApiModelsResponseTargetPartConfigurationEntry")


@_attrs_define
class ApplicationAuthorizationsApiModelsResponseTargetPartConfigurationEntry:
    """
    Attributes:
        name (str):
        type_ (None | str | Unset):
        constraints (list[str] | None | Unset):
        translation_key (None | str | Unset):
    """

    name: str
    type_: None | str | Unset = UNSET
    constraints: list[str] | None | Unset = UNSET
    translation_key: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        constraints: list[str] | None | Unset
        if isinstance(self.constraints, Unset):
            constraints = UNSET
        elif isinstance(self.constraints, list):
            constraints = self.constraints

        else:
            constraints = self.constraints

        translation_key: None | str | Unset
        if isinstance(self.translation_key, Unset):
            translation_key = UNSET
        else:
            translation_key = self.translation_key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if constraints is not UNSET:
            field_dict["constraints"] = constraints
        if translation_key is not UNSET:
            field_dict["translationKey"] = translation_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_constraints(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                constraints_type_0 = cast(list[str], data)

                return constraints_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        constraints = _parse_constraints(d.pop("constraints", UNSET))

        def _parse_translation_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        translation_key = _parse_translation_key(d.pop("translationKey", UNSET))

        application_authorizations_api_models_response_target_part_configuration_entry = cls(
            name=name,
            type_=type_,
            constraints=constraints,
            translation_key=translation_key,
        )

        return application_authorizations_api_models_response_target_part_configuration_entry
