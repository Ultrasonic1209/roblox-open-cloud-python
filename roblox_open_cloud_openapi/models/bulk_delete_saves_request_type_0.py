from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.delete_save_request_type_0 import DeleteSaveRequestType0


T = TypeVar("T", bound="BulkDeleteSavesRequestType0")


@_attrs_define
class BulkDeleteSavesRequestType0:
    """Request model for bulk deleting saves

    Attributes:
        targets (list[DeleteSaveRequestType0 | None] | None): A list of saves being deleted
    """

    targets: list[DeleteSaveRequestType0 | None] | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.delete_save_request_type_0 import DeleteSaveRequestType0

        targets: list[dict[str, Any] | None] | None
        if isinstance(self.targets, list):
            targets = []
            for targets_type_0_item_data in self.targets:
                targets_type_0_item: dict[str, Any] | None
                if isinstance(targets_type_0_item_data, DeleteSaveRequestType0):
                    targets_type_0_item = targets_type_0_item_data.to_dict()
                else:
                    targets_type_0_item = targets_type_0_item_data
                targets.append(targets_type_0_item)

        else:
            targets = self.targets

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "targets": targets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delete_save_request_type_0 import DeleteSaveRequestType0

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_targets(data: object) -> list[DeleteSaveRequestType0 | None] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                targets_type_0 = []
                _targets_type_0 = data
                for targets_type_0_item_data in _targets_type_0:

                    def _parse_targets_type_0_item(data: object) -> DeleteSaveRequestType0 | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_delete_save_request_type_0 = DeleteSaveRequestType0.from_dict(data)

                            return componentsschemas_delete_save_request_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(DeleteSaveRequestType0 | None, data)

                    targets_type_0_item = _parse_targets_type_0_item(targets_type_0_item_data)

                    targets_type_0.append(targets_type_0_item)

                return targets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DeleteSaveRequestType0 | None] | None, data)

        targets = _parse_targets(d.pop("targets"))

        bulk_delete_saves_request_type_0 = cls(
            targets=targets,
        )

        return bulk_delete_saves_request_type_0
