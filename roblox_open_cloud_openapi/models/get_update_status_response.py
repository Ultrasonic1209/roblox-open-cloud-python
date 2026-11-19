from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.game_update_status import GameUpdateStatus


T = TypeVar("T", bound="GetUpdateStatusResponse")


@_attrs_define
class GetUpdateStatusResponse:
    """Get Update Status response.

    Attributes:
        update_status_list (list[GameUpdateStatus] | None): The status of the game update.
    """

    update_status_list: list[GameUpdateStatus] | None

    def to_dict(self) -> dict[str, Any]:
        update_status_list: list[dict[str, Any]] | None
        if isinstance(self.update_status_list, list):
            update_status_list = []
            for update_status_list_type_0_item_data in self.update_status_list:
                update_status_list_type_0_item = update_status_list_type_0_item_data.to_dict()
                update_status_list.append(update_status_list_type_0_item)

        else:
            update_status_list = self.update_status_list

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "updateStatusList": update_status_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.game_update_status import GameUpdateStatus  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_update_status_list(data: object) -> list[GameUpdateStatus] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                update_status_list_type_0 = []
                _update_status_list_type_0 = data
                for update_status_list_type_0_item_data in _update_status_list_type_0:
                    update_status_list_type_0_item = GameUpdateStatus.from_dict(update_status_list_type_0_item_data)

                    update_status_list_type_0.append(update_status_list_type_0_item)

                return update_status_list_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GameUpdateStatus] | None, data)

        update_status_list = _parse_update_status_list(d.pop("updateStatusList"))

        get_update_status_response = cls(
            update_status_list=update_status_list,
        )

        return get_update_status_response
