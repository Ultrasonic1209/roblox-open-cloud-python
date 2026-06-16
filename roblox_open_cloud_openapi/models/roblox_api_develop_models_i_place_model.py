from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="RobloxApiDevelopModelsIPlaceModel")


@_attrs_define
class RobloxApiDevelopModelsIPlaceModel:
    """A model containing information about a place"""

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        roblox_api_develop_models_i_place_model = cls()

        return roblox_api_develop_models_i_place_model
