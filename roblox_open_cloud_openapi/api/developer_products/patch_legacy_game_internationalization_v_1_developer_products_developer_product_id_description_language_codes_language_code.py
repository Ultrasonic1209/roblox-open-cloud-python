from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_game_internationalization_api_update_developer_product_description_request import (
    RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionRequest,
)
from ...models.roblox_game_internationalization_api_update_developer_product_description_response import (
    RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    developer_product_id: int,
    language_code: str,
    *,
    body: RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionRequest
    | RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/legacy-game-internationalization/v1/developer-products/{developer_product_id}/description/language-codes/{language_code}".format(
            developer_product_id=quote(str(developer_product_id), safe=""),
            language_code=quote(str(language_code), safe=""),
        ),
    }

    if isinstance(body, RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionResponse.from_dict(
            response.json()
        )

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
) -> Response[Any | RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionResponse]:
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
    body: RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionRequest
    | RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionRequest
    | Unset = UNSET,
) -> Response[Any | RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionResponse]:
    """Update localized description of a developer product

    Args:
        developer_product_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionRequest): A
            request model for updating developer product description
        body (RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionRequest): A
            request model for updating developer product description

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionResponse]
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
    body: RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionRequest
    | RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionRequest
    | Unset = UNSET,
) -> Any | RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionResponse | None:
    """Update localized description of a developer product

    Args:
        developer_product_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionRequest): A
            request model for updating developer product description
        body (RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionRequest): A
            request model for updating developer product description

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionResponse
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
    body: RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionRequest
    | RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionRequest
    | Unset = UNSET,
) -> Response[Any | RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionResponse]:
    """Update localized description of a developer product

    Args:
        developer_product_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionRequest): A
            request model for updating developer product description
        body (RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionRequest): A
            request model for updating developer product description

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionResponse]
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
    body: RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionRequest
    | RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionRequest
    | Unset = UNSET,
) -> Any | RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionResponse | None:
    """Update localized description of a developer product

    Args:
        developer_product_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionRequest): A
            request model for updating developer product description
        body (RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionRequest): A
            request model for updating developer product description

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiUpdateDeveloperProductDescriptionResponse
    """

    return (
        await asyncio_detailed(
            developer_product_id=developer_product_id,
            language_code=language_code,
            client=client,
            body=body,
        )
    ).parsed
