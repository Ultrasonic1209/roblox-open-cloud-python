from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.grant_permission_error import GrantPermissionError


T = TypeVar("T", bound="BatchGrantPermissionsResponse")


@_attrs_define
class BatchGrantPermissionsResponse:
    """Response object to grant one permission to multiple assets.

    Attributes:
        success_asset_ids (list[int] | None | Unset): The list of asset IDs that granted successfully.
        errors (list[GrantPermissionError] | None | Unset): The list of grants that had errors.
    """

    success_asset_ids: list[int] | None | Unset = UNSET
    errors: list[GrantPermissionError] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        success_asset_ids: list[int] | None | Unset
        if isinstance(self.success_asset_ids, Unset):
            success_asset_ids = UNSET
        elif isinstance(self.success_asset_ids, list):
            success_asset_ids = self.success_asset_ids

        else:
            success_asset_ids = self.success_asset_ids

        errors: list[dict[str, Any]] | None | Unset
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = []
            for errors_type_0_item_data in self.errors:
                errors_type_0_item = errors_type_0_item_data.to_dict()
                errors.append(errors_type_0_item)

        else:
            errors = self.errors

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if success_asset_ids is not UNSET:
            field_dict["successAssetIds"] = success_asset_ids
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grant_permission_error import GrantPermissionError

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_success_asset_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                success_asset_ids_type_0 = cast(list[int], data)

                return success_asset_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        success_asset_ids = _parse_success_asset_ids(d.pop("successAssetIds", UNSET))

        def _parse_errors(data: object) -> list[GrantPermissionError] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = []
                _errors_type_0 = data
                for errors_type_0_item_data in _errors_type_0:
                    errors_type_0_item = GrantPermissionError.from_dict(errors_type_0_item_data)

                    errors_type_0.append(errors_type_0_item)

                return errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GrantPermissionError] | None | Unset, data)

        errors = _parse_errors(d.pop("errors", UNSET))

        batch_grant_permissions_response = cls(
            success_asset_ids=success_asset_ids,
            errors=errors,
        )

        return batch_grant_permissions_response
