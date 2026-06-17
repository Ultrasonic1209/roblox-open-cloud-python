import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_web_web_api_models_api_array_response_roblox_game_internationalization_api_name_description import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiNameDescription,
)


def _get_kwargs(
    developer_product_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://gameinternationalization.roblox.com/v1/developer-products/{developer_product_id}/name-description".format(
            developer_product_id=quote(str(developer_product_id), safe=""),
        ),
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            "x-roblox-recommended-alternatives": [
                {
                    "url": "https://apis.roblox.com/legacy-game-internationalization/v1/developer-products/{developerProductId}/name-description",
                    "httpMethod": "GET",
                    "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/developer-products#get_legacy_game_internationalization_v1_developer_products__developerProductId__name_description",
                }
            ],
        },
        "openapi-id": "get_v1_developer-products_developerProductId_name-description",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiNameDescription | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiNameDescription.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiNameDescription]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/developer-products#gameinternationalization_get_v1_developer_products__developerProductId__name_description"
)
def sync_detailed(
    developer_product_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiNameDescription]:
    """Get all names and descriptions of a developer product

    Args:
        developer_product_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiNameDescription]
    """

    kwargs = _get_kwargs(
        developer_product_id=developer_product_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/developer-products#gameinternationalization_get_v1_developer_products__developerProductId__name_description"
)
def sync(
    developer_product_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiNameDescription | None:
    """Get all names and descriptions of a developer product

    Args:
        developer_product_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiNameDescription
    """

    return sync_detailed(
        developer_product_id=developer_product_id,
        client=client,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/developer-products#gameinternationalization_get_v1_developer_products__developerProductId__name_description"
)
async def asyncio_detailed(
    developer_product_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiNameDescription]:
    """Get all names and descriptions of a developer product

    Args:
        developer_product_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiNameDescription]
    """

    kwargs = _get_kwargs(
        developer_product_id=developer_product_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/developer-products#gameinternationalization_get_v1_developer_products__developerProductId__name_description"
)
async def asyncio(
    developer_product_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiNameDescription | None:
    """Get all names and descriptions of a developer product

    Args:
        developer_product_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiNameDescription
    """

    return (
        await asyncio_detailed(
            developer_product_id=developer_product_id,
            client=client,
        )
    ).parsed
