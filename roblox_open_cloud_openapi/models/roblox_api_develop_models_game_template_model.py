from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_develop_models_universe_model import RobloxApiDevelopModelsUniverseModel


T = TypeVar("T", bound="RobloxApiDevelopModelsGameTemplateModel")


@_attrs_define
class RobloxApiDevelopModelsGameTemplateModel:
    """Represents a game template in API endpoint responses.

    Attributes:
        game_template_type (str | Unset): The type of this game template.
        has_tutorials (bool | Unset): Whether this game template has tutorials.
        universe (RobloxApiDevelopModelsUniverseModel | Unset): Represents a universe in API endpoint results.
    """

    game_template_type: str | Unset = UNSET
    has_tutorials: bool | Unset = UNSET
    universe: RobloxApiDevelopModelsUniverseModel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        game_template_type = self.game_template_type

        has_tutorials = self.has_tutorials

        universe: dict[str, Any] | Unset = UNSET
        if not isinstance(self.universe, Unset):
            universe = self.universe.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if game_template_type is not UNSET:
            field_dict["gameTemplateType"] = game_template_type
        if has_tutorials is not UNSET:
            field_dict["hasTutorials"] = has_tutorials
        if universe is not UNSET:
            field_dict["universe"] = universe

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_develop_models_universe_model import RobloxApiDevelopModelsUniverseModel

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        game_template_type = d.pop("gameTemplateType", UNSET)

        has_tutorials = d.pop("hasTutorials", UNSET)

        _universe = d.pop("universe", UNSET)
        universe: RobloxApiDevelopModelsUniverseModel | Unset
        if isinstance(_universe, Unset):
            universe = UNSET
        else:
            universe = RobloxApiDevelopModelsUniverseModel.from_dict(_universe)

        roblox_api_develop_models_game_template_model = cls(
            game_template_type=game_template_type,
            has_tutorials=has_tutorials,
            universe=universe,
        )

        return roblox_api_develop_models_game_template_model
