from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_trades_api_models_v2_item_target_item_type import RobloxTradesApiModelsV2ItemTargetItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTradesApiModelsV2ItemTarget")


@_attrs_define
class RobloxTradesApiModelsV2ItemTarget:
    """The underlying of a tradable item.

    Attributes:
        item_type (RobloxTradesApiModelsV2ItemTargetItemType | Unset): The type of the underlying. ['Unknown' = 0,
            'Asset' = 1, 'Bundle' = 2]
        target_id (str | Unset): The id of the underlying.
    """

    item_type: RobloxTradesApiModelsV2ItemTargetItemType | Unset = UNSET
    target_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        item_type: str | Unset = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        target_id = self.target_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if item_type is not UNSET:
            field_dict["itemType"] = item_type
        if target_id is not UNSET:
            field_dict["targetId"] = target_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _item_type = d.pop("itemType", UNSET)
        item_type: RobloxTradesApiModelsV2ItemTargetItemType | Unset
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = RobloxTradesApiModelsV2ItemTargetItemType(_item_type)

        target_id = d.pop("targetId", UNSET)

        roblox_trades_api_models_v2_item_target = cls(
            item_type=item_type,
            target_id=target_id,
        )

        return roblox_trades_api_models_v2_item_target
