from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.developer_product_config_v2 import DeveloperProductConfigV2


T = TypeVar("T", bound="ListDeveloperProductConfigsV2Response")


@_attrs_define
class ListDeveloperProductConfigsV2Response:
    """Response that contains the list of developer products with their corresponding configuration details and pagination
    information.

        Attributes:
            developer_products (list[DeveloperProductConfigV2]): The list of developer products with their corresponding
                configuration details.
            next_page_token (None | str): The next page token.
    """

    developer_products: list[DeveloperProductConfigV2]
    next_page_token: None | str

    def to_dict(self) -> dict[str, Any]:
        developer_products = []
        for developer_products_item_data in self.developer_products:
            developer_products_item = developer_products_item_data.to_dict()
            developer_products.append(developer_products_item)

        next_page_token: None | str
        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "developerProducts": developer_products,
                "nextPageToken": next_page_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.developer_product_config_v2 import DeveloperProductConfigV2

        d = dict(src_dict)
        developer_products = []
        _developer_products = d.pop("developerProducts")
        for developer_products_item_data in _developer_products:
            developer_products_item = DeveloperProductConfigV2.from_dict(developer_products_item_data)

            developer_products.append(developer_products_item)

        def _parse_next_page_token(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken"))

        list_developer_product_configs_v2_response = cls(
            developer_products=developer_products,
            next_page_token=next_page_token,
        )

        return list_developer_product_configs_v2_response
