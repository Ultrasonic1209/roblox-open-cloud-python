from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_develop_models_game_template_model import RobloxApiDevelopModelsGameTemplateModel


T = TypeVar("T", bound="RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsGameTemplateModel")


@_attrs_define
class RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsGameTemplateModel:
    """
    Attributes:
        data (list[RobloxApiDevelopModelsGameTemplateModel] | Unset):
    """

    data: list[RobloxApiDevelopModelsGameTemplateModel] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_develop_models_game_template_model import RobloxApiDevelopModelsGameTemplateModel

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[RobloxApiDevelopModelsGameTemplateModel] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = RobloxApiDevelopModelsGameTemplateModel.from_dict(data_item_data)

                data.append(data_item)

        roblox_web_web_api_models_api_array_response_roblox_api_develop_models_game_template_model = cls(
            data=data,
        )

        return roblox_web_web_api_models_api_array_response_roblox_api_develop_models_game_template_model
