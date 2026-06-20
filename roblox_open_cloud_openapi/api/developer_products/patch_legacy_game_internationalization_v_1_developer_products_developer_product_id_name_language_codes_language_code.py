from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_game_internationalization_api_update_developer_product_name_request import (
    RobloxGameInternationalizationApiUpdateDeveloperProductNameRequest,
)
from ...models.roblox_game_internationalization_api_update_developer_product_name_response import (
    RobloxGameInternationalizationApiUpdateDeveloperProductNameResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    developer_product_id: int,
    language_code: str,
    *,
    body: RobloxGameInternationalizationApiUpdateDeveloperProductNameRequest
    | RobloxGameInternationalizationApiUpdateDeveloperProductNameRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/legacy-game-internationalization/v1/developer-products/{developer_product_id}/name/language-codes/{language_code}".format(
            developer_product_id=quote(str(developer_product_id), safe=""),
            language_code=quote(str(language_code), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 100},
                },
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
                "x-roblox-scopes": [{"name": "legacy-developer-product:manage"}],
            },
            "openapi-id": "patch_legacy-game-internationalization_v1_developer-products_developerProductId_name_language-codes_languageCode",
        },
    }

    if isinstance(body, RobloxGameInternationalizationApiUpdateDeveloperProductNameRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxGameInternationalizationApiUpdateDeveloperProductNameRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxGameInternationalizationApiUpdateDeveloperProductNameResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGameInternationalizationApiUpdateDeveloperProductNameResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxGameInternationalizationApiUpdateDeveloperProductNameResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    developer_product_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiUpdateDeveloperProductNameRequest
    | RobloxGameInternationalizationApiUpdateDeveloperProductNameRequest
    | Unset = UNSET,
) -> Response[Any | RobloxGameInternationalizationApiUpdateDeveloperProductNameResponse]:
    """Update localized name of a developer product

    Args:
        developer_product_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiUpdateDeveloperProductNameRequest): A request model
            for updating developer product name
        body (RobloxGameInternationalizationApiUpdateDeveloperProductNameRequest): A request model
            for updating developer product name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiUpdateDeveloperProductNameResponse]
    """

    kwargs = _get_kwargs(
        developer_product_id=developer_product_id,
        language_code=language_code,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    developer_product_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiUpdateDeveloperProductNameRequest
    | RobloxGameInternationalizationApiUpdateDeveloperProductNameRequest
    | Unset = UNSET,
) -> Any | RobloxGameInternationalizationApiUpdateDeveloperProductNameResponse | None:
    """Update localized name of a developer product

    Args:
        developer_product_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiUpdateDeveloperProductNameRequest): A request model
            for updating developer product name
        body (RobloxGameInternationalizationApiUpdateDeveloperProductNameRequest): A request model
            for updating developer product name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiUpdateDeveloperProductNameResponse
    """

    return sync_detailed(
        developer_product_id=developer_product_id,
        language_code=language_code,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    developer_product_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiUpdateDeveloperProductNameRequest
    | RobloxGameInternationalizationApiUpdateDeveloperProductNameRequest
    | Unset = UNSET,
) -> Response[Any | RobloxGameInternationalizationApiUpdateDeveloperProductNameResponse]:
    """Update localized name of a developer product

    Args:
        developer_product_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiUpdateDeveloperProductNameRequest): A request model
            for updating developer product name
        body (RobloxGameInternationalizationApiUpdateDeveloperProductNameRequest): A request model
            for updating developer product name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiUpdateDeveloperProductNameResponse]
    """

    kwargs = _get_kwargs(
        developer_product_id=developer_product_id,
        language_code=language_code,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    developer_product_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiUpdateDeveloperProductNameRequest
    | RobloxGameInternationalizationApiUpdateDeveloperProductNameRequest
    | Unset = UNSET,
) -> Any | RobloxGameInternationalizationApiUpdateDeveloperProductNameResponse | None:
    """Update localized name of a developer product

    Args:
        developer_product_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiUpdateDeveloperProductNameRequest): A request model
            for updating developer product name
        body (RobloxGameInternationalizationApiUpdateDeveloperProductNameRequest): A request model
            for updating developer product name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiUpdateDeveloperProductNameResponse
    """

    return (
        await asyncio_detailed(
            developer_product_id=developer_product_id,
            language_code=language_code,
            client=client,
            body=body,
        )
    ).parsed
