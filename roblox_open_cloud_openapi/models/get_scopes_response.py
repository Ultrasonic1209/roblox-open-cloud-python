from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_opencloud_scopeconfiguration_v2_operation import RobloxOpencloudScopeconfigurationV2Operation
    from ..models.roblox_opencloud_scopeconfiguration_v2_product import RobloxOpencloudScopeconfigurationV2Product
    from ..models.roblox_opencloud_scopeconfiguration_v2_scope import RobloxOpencloudScopeconfigurationV2Scope
    from ..models.roblox_opencloud_scopeconfiguration_v2_scope_type import RobloxOpencloudScopeconfigurationV2ScopeType
    from ..models.roblox_opencloud_scopeconfiguration_v2_target_part import (
        RobloxOpencloudScopeconfigurationV2TargetPart,
    )
    from ..models.roblox_opencloud_scopeconfiguration_v2_target_type import (
        RobloxOpencloudScopeconfigurationV2TargetType,
    )


T = TypeVar("T", bound="GetScopesResponse")


@_attrs_define
class GetScopesResponse:
    """
    Attributes:
        scopes (list[RobloxOpencloudScopeconfigurationV2Scope] | Unset):
        scope_types (list[RobloxOpencloudScopeconfigurationV2ScopeType] | Unset):
        target_types (list[RobloxOpencloudScopeconfigurationV2TargetType] | Unset):
        target_parts (list[RobloxOpencloudScopeconfigurationV2TargetPart] | Unset):
        operations (list[RobloxOpencloudScopeconfigurationV2Operation] | Unset):
        products (list[RobloxOpencloudScopeconfigurationV2Product] | Unset):
    """

    scopes: list[RobloxOpencloudScopeconfigurationV2Scope] | Unset = UNSET
    scope_types: list[RobloxOpencloudScopeconfigurationV2ScopeType] | Unset = UNSET
    target_types: list[RobloxOpencloudScopeconfigurationV2TargetType] | Unset = UNSET
    target_parts: list[RobloxOpencloudScopeconfigurationV2TargetPart] | Unset = UNSET
    operations: list[RobloxOpencloudScopeconfigurationV2Operation] | Unset = UNSET
    products: list[RobloxOpencloudScopeconfigurationV2Product] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        scopes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = []
            for scopes_item_data in self.scopes:
                scopes_item = scopes_item_data.to_dict()
                scopes.append(scopes_item)

        scope_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.scope_types, Unset):
            scope_types = []
            for scope_types_item_data in self.scope_types:
                scope_types_item = scope_types_item_data.to_dict()
                scope_types.append(scope_types_item)

        target_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.target_types, Unset):
            target_types = []
            for target_types_item_data in self.target_types:
                target_types_item = target_types_item_data.to_dict()
                target_types.append(target_types_item)

        target_parts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.target_parts, Unset):
            target_parts = []
            for target_parts_item_data in self.target_parts:
                target_parts_item = target_parts_item_data.to_dict()
                target_parts.append(target_parts_item)

        operations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.operations, Unset):
            operations = []
            for operations_item_data in self.operations:
                operations_item = operations_item_data.to_dict()
                operations.append(operations_item)

        products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if scope_types is not UNSET:
            field_dict["scopeTypes"] = scope_types
        if target_types is not UNSET:
            field_dict["targetTypes"] = target_types
        if target_parts is not UNSET:
            field_dict["targetParts"] = target_parts
        if operations is not UNSET:
            field_dict["operations"] = operations
        if products is not UNSET:
            field_dict["products"] = products

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_opencloud_scopeconfiguration_v2_operation import (
            RobloxOpencloudScopeconfigurationV2Operation,  # noqa: PLC0415
        )
        from ..models.roblox_opencloud_scopeconfiguration_v2_product import RobloxOpencloudScopeconfigurationV2Product  # noqa: PLC0415
        from ..models.roblox_opencloud_scopeconfiguration_v2_scope import RobloxOpencloudScopeconfigurationV2Scope  # noqa: PLC0415
        from ..models.roblox_opencloud_scopeconfiguration_v2_scope_type import (
            RobloxOpencloudScopeconfigurationV2ScopeType,  # noqa: PLC0415
        )
        from ..models.roblox_opencloud_scopeconfiguration_v2_target_part import (
            RobloxOpencloudScopeconfigurationV2TargetPart,  # noqa: PLC0415
        )
        from ..models.roblox_opencloud_scopeconfiguration_v2_target_type import (
            RobloxOpencloudScopeconfigurationV2TargetType,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _scopes = d.pop("scopes", UNSET)
        scopes: list[RobloxOpencloudScopeconfigurationV2Scope] | Unset = UNSET
        if _scopes is not UNSET:
            scopes = []
            for scopes_item_data in _scopes:
                scopes_item = RobloxOpencloudScopeconfigurationV2Scope.from_dict(scopes_item_data)

                scopes.append(scopes_item)

        _scope_types = d.pop("scopeTypes", UNSET)
        scope_types: list[RobloxOpencloudScopeconfigurationV2ScopeType] | Unset = UNSET
        if _scope_types is not UNSET:
            scope_types = []
            for scope_types_item_data in _scope_types:
                scope_types_item = RobloxOpencloudScopeconfigurationV2ScopeType.from_dict(scope_types_item_data)

                scope_types.append(scope_types_item)

        _target_types = d.pop("targetTypes", UNSET)
        target_types: list[RobloxOpencloudScopeconfigurationV2TargetType] | Unset = UNSET
        if _target_types is not UNSET:
            target_types = []
            for target_types_item_data in _target_types:
                target_types_item = RobloxOpencloudScopeconfigurationV2TargetType.from_dict(target_types_item_data)

                target_types.append(target_types_item)

        _target_parts = d.pop("targetParts", UNSET)
        target_parts: list[RobloxOpencloudScopeconfigurationV2TargetPart] | Unset = UNSET
        if _target_parts is not UNSET:
            target_parts = []
            for target_parts_item_data in _target_parts:
                target_parts_item = RobloxOpencloudScopeconfigurationV2TargetPart.from_dict(target_parts_item_data)

                target_parts.append(target_parts_item)

        _operations = d.pop("operations", UNSET)
        operations: list[RobloxOpencloudScopeconfigurationV2Operation] | Unset = UNSET
        if _operations is not UNSET:
            operations = []
            for operations_item_data in _operations:
                operations_item = RobloxOpencloudScopeconfigurationV2Operation.from_dict(operations_item_data)

                operations.append(operations_item)

        _products = d.pop("products", UNSET)
        products: list[RobloxOpencloudScopeconfigurationV2Product] | Unset = UNSET
        if _products is not UNSET:
            products = []
            for products_item_data in _products:
                products_item = RobloxOpencloudScopeconfigurationV2Product.from_dict(products_item_data)

                products.append(products_item)

        get_scopes_response = cls(
            scopes=scopes,
            scope_types=scope_types,
            target_types=target_types,
            target_parts=target_parts,
            operations=operations,
            products=products,
        )

        return get_scopes_response
