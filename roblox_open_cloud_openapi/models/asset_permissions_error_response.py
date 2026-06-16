from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_permissions_error import AssetPermissionsError


T = TypeVar("T", bound="AssetPermissionsErrorResponse")


@_attrs_define
class AssetPermissionsErrorResponse:
    """The error object for responses.

    Attributes:
        error (AssetPermissionsError | Unset): The error object for results.
    """

    error: AssetPermissionsError | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_permissions_error import AssetPermissionsError

        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: AssetPermissionsError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = AssetPermissionsError.from_dict(_error)

        asset_permissions_error_response = cls(
            error=error,
        )

        return asset_permissions_error_response
