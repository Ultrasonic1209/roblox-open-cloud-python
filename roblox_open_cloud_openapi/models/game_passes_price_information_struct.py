from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.game_passes_pricing_feature import GamePassesPricingFeature

T = TypeVar("T", bound="GamePassesPriceInformationStruct")


@_attrs_define
class GamePassesPriceInformationStruct:
    """The pricing configuration information.

    Attributes:
        default_price_in_robux (int | None): The configured default price in Robux.
        enabled_features (list[GamePassesPricingFeature]): The enabled pricing features for the game pass.
    """

    default_price_in_robux: int | None
    enabled_features: list[GamePassesPricingFeature]

    def to_dict(self) -> dict[str, Any]:
        default_price_in_robux: int | None
        default_price_in_robux = self.default_price_in_robux

        enabled_features = []
        for enabled_features_item_data in self.enabled_features:
            enabled_features_item = enabled_features_item_data.value
            enabled_features.append(enabled_features_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "defaultPriceInRobux": default_price_in_robux,
                "enabledFeatures": enabled_features,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_default_price_in_robux(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        default_price_in_robux = _parse_default_price_in_robux(d.pop("defaultPriceInRobux"))

        enabled_features = []
        _enabled_features = d.pop("enabledFeatures")
        for enabled_features_item_data in _enabled_features:
            enabled_features_item = GamePassesPricingFeature(enabled_features_item_data)

            enabled_features.append(enabled_features_item)

        game_passes_price_information_struct = cls(
            default_price_in_robux=default_price_in_robux,
            enabled_features=enabled_features,
        )

        return game_passes_price_information_struct
