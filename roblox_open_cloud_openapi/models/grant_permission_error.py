from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.asset_permissions_error_code import AssetPermissionsErrorCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="GrantPermissionError")


@_attrs_define
class GrantPermissionError:
    """Single error for BatchGrantPermissionsResponse.

    Attributes:
        asset_id (int | Unset): Failed asset ID.
        code (AssetPermissionsErrorCode | Unset): Enums for customized error code in error responses.
    """

    asset_id: int | Unset = UNSET
    code: AssetPermissionsErrorCode | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        code: str | Unset = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = d.pop("assetId", UNSET)

        _code = d.pop("code", UNSET)
        code: AssetPermissionsErrorCode | Unset
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = AssetPermissionsErrorCode(_code)

        grant_permission_error = cls(
            asset_id=asset_id,
            code=code,
        )

        return grant_permission_error
