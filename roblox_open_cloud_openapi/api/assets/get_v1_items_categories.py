from http import HTTPStatus
from typing import TYPE_CHECKING, Any, cast

if TYPE_CHECKING:
    import httpx2 as httpx
else:
    try:
        import httpx2 as httpx
    except ModuleNotFoundError:
        try:
            import httpx
        except ModuleNotFoundError:
            raise RuntimeError(
                "This module requires the httpx2 package to be installed.\n"
                "You can install it with:\n"
                "    $ pip install httpx2\n"
            ) from None


from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

"""
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'SECOND', 'maxInPeriod': 10}}, 'x-roblox-scopes': [{'name': 'marketplace.item:read', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.get_v1_items_categories_category_domain import GetV1ItemsCategoriesCategoryDomain
from ...models.roblox_item_configuration_api_models_response_get_categories_response import (
    RobloxItemConfigurationApiModelsResponseGetCategoriesResponse,
)
from ...types import Unset


def _get_kwargs(
    *,
    category_domain: GetV1ItemsCategoriesCategoryDomain | Unset = GetV1ItemsCategoriesCategoryDomain.VALUE_0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_category_domain: int | Unset = UNSET
    if not isinstance(category_domain, Unset):
        json_category_domain = category_domain.value

    params["categoryDomain"] = json_category_domain

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://itemconfiguration.roblox.com/v1/items/categories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxItemConfigurationApiModelsResponseGetCategoriesResponse | None:
    if response.status_code == 200:
        response_200 = RobloxItemConfigurationApiModelsResponseGetCategoriesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxItemConfigurationApiModelsResponseGetCategoriesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    category_domain: GetV1ItemsCategoriesCategoryDomain | Unset = GetV1ItemsCategoriesCategoryDomain.VALUE_0,
) -> Response[Any | RobloxItemConfigurationApiModelsResponseGetCategoriesResponse]:
    """Gets a category hierarchy (by category domain) used to render category chips,
    e.g. on the creator dashboard.

    Args:
        category_domain (GetV1ItemsCategoriesCategoryDomain | Unset):  Default:
            GetV1ItemsCategoriesCategoryDomain.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiModelsResponseGetCategoriesResponse]
    """

    kwargs = _get_kwargs(
        category_domain=category_domain,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    category_domain: GetV1ItemsCategoriesCategoryDomain | Unset = GetV1ItemsCategoriesCategoryDomain.VALUE_0,
) -> Any | RobloxItemConfigurationApiModelsResponseGetCategoriesResponse | None:
    """Gets a category hierarchy (by category domain) used to render category chips,
    e.g. on the creator dashboard.

    Args:
        category_domain (GetV1ItemsCategoriesCategoryDomain | Unset):  Default:
            GetV1ItemsCategoriesCategoryDomain.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiModelsResponseGetCategoriesResponse
    """

    return sync_detailed(
        client=client,
        category_domain=category_domain,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    category_domain: GetV1ItemsCategoriesCategoryDomain | Unset = GetV1ItemsCategoriesCategoryDomain.VALUE_0,
) -> Response[Any | RobloxItemConfigurationApiModelsResponseGetCategoriesResponse]:
    """Gets a category hierarchy (by category domain) used to render category chips,
    e.g. on the creator dashboard.

    Args:
        category_domain (GetV1ItemsCategoriesCategoryDomain | Unset):  Default:
            GetV1ItemsCategoriesCategoryDomain.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiModelsResponseGetCategoriesResponse]
    """

    kwargs = _get_kwargs(
        category_domain=category_domain,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    category_domain: GetV1ItemsCategoriesCategoryDomain | Unset = GetV1ItemsCategoriesCategoryDomain.VALUE_0,
) -> Any | RobloxItemConfigurationApiModelsResponseGetCategoriesResponse | None:
    """Gets a category hierarchy (by category domain) used to render category chips,
    e.g. on the creator dashboard.

    Args:
        category_domain (GetV1ItemsCategoriesCategoryDomain | Unset):  Default:
            GetV1ItemsCategoriesCategoryDomain.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiModelsResponseGetCategoriesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            category_domain=category_domain,
        )
    ).parsed
