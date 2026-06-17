from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.game_passes_price_information_struct import GamePassesPriceInformationStruct


T = TypeVar("T", bound="GamePassConfigV2")


@_attrs_define
class GamePassConfigV2:
    """Creator-facing representation of a game pass configuration.

    Attributes:
        game_pass_id (int): The game pass ID.
        name (str): The name of the game pass.
        description (str): The description of the game pass.
        is_for_sale (bool): Whether the game pass is currently on sale.
        icon_asset_id (int): The icon image (thumbnail) asset ID of the game pass.
        created_timestamp (datetime.datetime): The timestamp when the game pass was created.
        updated_timestamp (datetime.datetime): The timestamp when the game pass was last updated.
        price_information (GamePassesPriceInformationStruct | None): The pricing configuration associated with the game
            pass.
        is_managed_pricing_enabled (bool): Whether managed pricing is enabled for the game pass.
    """

    game_pass_id: int
    name: str
    description: str
    is_for_sale: bool
    icon_asset_id: int
    created_timestamp: datetime.datetime
    updated_timestamp: datetime.datetime
    price_information: GamePassesPriceInformationStruct | None
    is_managed_pricing_enabled: bool

    def to_dict(self) -> dict[str, Any]:
        from ..models.game_passes_price_information_struct import GamePassesPriceInformationStruct

        game_pass_id = self.game_pass_id

        name = self.name

        description = self.description

        is_for_sale = self.is_for_sale

        icon_asset_id = self.icon_asset_id

        created_timestamp = self.created_timestamp.isoformat()

        updated_timestamp = self.updated_timestamp.isoformat()

        price_information: dict[str, Any] | None
        if isinstance(self.price_information, GamePassesPriceInformationStruct):
            price_information = self.price_information.to_dict()
        else:
            price_information = self.price_information

        is_managed_pricing_enabled = self.is_managed_pricing_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "gamePassId": game_pass_id,
                "name": name,
                "description": description,
                "isForSale": is_for_sale,
                "iconAssetId": icon_asset_id,
                "createdTimestamp": created_timestamp,
                "updatedTimestamp": updated_timestamp,
                "priceInformation": price_information,
                "isManagedPricingEnabled": is_managed_pricing_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.game_passes_price_information_struct import GamePassesPriceInformationStruct

        d = dict(src_dict)
        game_pass_id = d.pop("gamePassId")

        name = d.pop("name")

        description = d.pop("description")

        is_for_sale = d.pop("isForSale")

        icon_asset_id = d.pop("iconAssetId")

        created_timestamp = datetime.datetime.fromisoformat(d.pop("createdTimestamp"))

        updated_timestamp = datetime.datetime.fromisoformat(d.pop("updatedTimestamp"))

        def _parse_price_information(data: object) -> GamePassesPriceInformationStruct | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                price_information_type_1 = GamePassesPriceInformationStruct.from_dict(data)

                return price_information_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GamePassesPriceInformationStruct | None, data)

        price_information = _parse_price_information(d.pop("priceInformation"))

        is_managed_pricing_enabled = d.pop("isManagedPricingEnabled")

        game_pass_config_v2 = cls(
            game_pass_id=game_pass_id,
            name=name,
            description=description,
            is_for_sale=is_for_sale,
            icon_asset_id=icon_asset_id,
            created_timestamp=created_timestamp,
            updated_timestamp=updated_timestamp,
            price_information=price_information,
            is_managed_pricing_enabled=is_managed_pricing_enabled,
        )

        return game_pass_config_v2
