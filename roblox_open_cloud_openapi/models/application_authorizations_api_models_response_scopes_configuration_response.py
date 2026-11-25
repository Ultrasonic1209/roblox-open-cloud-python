from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.application_authorizations_api_models_response_operation_configuration_entry import (
        ApplicationAuthorizationsApiModelsResponseOperationConfigurationEntry,
    )
    from ..models.application_authorizations_api_models_response_product_configuration_entry import (
        ApplicationAuthorizationsApiModelsResponseProductConfigurationEntry,
    )
    from ..models.application_authorizations_api_models_response_scope_configuration_entry import (
        ApplicationAuthorizationsApiModelsResponseScopeConfigurationEntry,
    )
    from ..models.application_authorizations_api_models_response_scope_type_configuration_entry import (
        ApplicationAuthorizationsApiModelsResponseScopeTypeConfigurationEntry,
    )
    from ..models.application_authorizations_api_models_response_target_part_configuration_entry import (
        ApplicationAuthorizationsApiModelsResponseTargetPartConfigurationEntry,
    )
    from ..models.application_authorizations_api_models_response_target_type_configuration_entry import (
        ApplicationAuthorizationsApiModelsResponseTargetTypeConfigurationEntry,
    )


T = TypeVar("T", bound="ApplicationAuthorizationsApiModelsResponseScopesConfigurationResponse")


@_attrs_define
class ApplicationAuthorizationsApiModelsResponseScopesConfigurationResponse:
    """
    Attributes:
        scopes (list[ApplicationAuthorizationsApiModelsResponseScopeConfigurationEntry]):
        scope_types (list[ApplicationAuthorizationsApiModelsResponseScopeTypeConfigurationEntry]):
        target_types (list[ApplicationAuthorizationsApiModelsResponseTargetTypeConfigurationEntry]):
        target_parts (list[ApplicationAuthorizationsApiModelsResponseTargetPartConfigurationEntry]):
        products (list[ApplicationAuthorizationsApiModelsResponseProductConfigurationEntry]):
        operations (list[ApplicationAuthorizationsApiModelsResponseOperationConfigurationEntry]):
        oidc_scopes (list[str]):
    """

    scopes: list[ApplicationAuthorizationsApiModelsResponseScopeConfigurationEntry]
    scope_types: list[ApplicationAuthorizationsApiModelsResponseScopeTypeConfigurationEntry]
    target_types: list[ApplicationAuthorizationsApiModelsResponseTargetTypeConfigurationEntry]
    target_parts: list[ApplicationAuthorizationsApiModelsResponseTargetPartConfigurationEntry]
    products: list[ApplicationAuthorizationsApiModelsResponseProductConfigurationEntry]
    operations: list[ApplicationAuthorizationsApiModelsResponseOperationConfigurationEntry]
    oidc_scopes: list[str]

    def to_dict(self) -> dict[str, Any]:
        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.to_dict()
            scopes.append(scopes_item)

        scope_types = []
        for scope_types_item_data in self.scope_types:
            scope_types_item = scope_types_item_data.to_dict()
            scope_types.append(scope_types_item)

        target_types = []
        for target_types_item_data in self.target_types:
            target_types_item = target_types_item_data.to_dict()
            target_types.append(target_types_item)

        target_parts = []
        for target_parts_item_data in self.target_parts:
            target_parts_item = target_parts_item_data.to_dict()
            target_parts.append(target_parts_item)

        products = []
        for products_item_data in self.products:
            products_item = products_item_data.to_dict()
            products.append(products_item)

        operations = []
        for operations_item_data in self.operations:
            operations_item = operations_item_data.to_dict()
            operations.append(operations_item)

        oidc_scopes = self.oidc_scopes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "scopes": scopes,
                "scopeTypes": scope_types,
                "targetTypes": target_types,
                "targetParts": target_parts,
                "products": products,
                "operations": operations,
                "oidcScopes": oidc_scopes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.application_authorizations_api_models_response_operation_configuration_entry import (
            ApplicationAuthorizationsApiModelsResponseOperationConfigurationEntry,  # noqa: PLC0415
        )
        from ..models.application_authorizations_api_models_response_product_configuration_entry import (
            ApplicationAuthorizationsApiModelsResponseProductConfigurationEntry,  # noqa: PLC0415
        )
        from ..models.application_authorizations_api_models_response_scope_configuration_entry import (
            ApplicationAuthorizationsApiModelsResponseScopeConfigurationEntry,  # noqa: PLC0415
        )
        from ..models.application_authorizations_api_models_response_scope_type_configuration_entry import (
            ApplicationAuthorizationsApiModelsResponseScopeTypeConfigurationEntry,  # noqa: PLC0415
        )
        from ..models.application_authorizations_api_models_response_target_part_configuration_entry import (
            ApplicationAuthorizationsApiModelsResponseTargetPartConfigurationEntry,  # noqa: PLC0415
        )
        from ..models.application_authorizations_api_models_response_target_type_configuration_entry import (
            ApplicationAuthorizationsApiModelsResponseTargetTypeConfigurationEntry,  # noqa: PLC0415
        )

        d = dict(src_dict)
        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = ApplicationAuthorizationsApiModelsResponseScopeConfigurationEntry.from_dict(scopes_item_data)

            scopes.append(scopes_item)

        scope_types = []
        _scope_types = d.pop("scopeTypes")
        for scope_types_item_data in _scope_types:
            scope_types_item = ApplicationAuthorizationsApiModelsResponseScopeTypeConfigurationEntry.from_dict(
                scope_types_item_data
            )

            scope_types.append(scope_types_item)

        target_types = []
        _target_types = d.pop("targetTypes")
        for target_types_item_data in _target_types:
            target_types_item = ApplicationAuthorizationsApiModelsResponseTargetTypeConfigurationEntry.from_dict(
                target_types_item_data
            )

            target_types.append(target_types_item)

        target_parts = []
        _target_parts = d.pop("targetParts")
        for target_parts_item_data in _target_parts:
            target_parts_item = ApplicationAuthorizationsApiModelsResponseTargetPartConfigurationEntry.from_dict(
                target_parts_item_data
            )

            target_parts.append(target_parts_item)

        products = []
        _products = d.pop("products")
        for products_item_data in _products:
            products_item = ApplicationAuthorizationsApiModelsResponseProductConfigurationEntry.from_dict(
                products_item_data
            )

            products.append(products_item)

        operations = []
        _operations = d.pop("operations")
        for operations_item_data in _operations:
            operations_item = ApplicationAuthorizationsApiModelsResponseOperationConfigurationEntry.from_dict(
                operations_item_data
            )

            operations.append(operations_item)

        oidc_scopes = cast(list[str], d.pop("oidcScopes"))

        application_authorizations_api_models_response_scopes_configuration_response = cls(
            scopes=scopes,
            scope_types=scope_types,
            target_types=target_types,
            target_parts=target_parts,
            products=products,
            operations=operations,
            oidc_scopes=oidc_scopes,
        )

        return application_authorizations_api_models_response_scopes_configuration_response
