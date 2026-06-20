from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.creator_store_asset_type_0 import CreatorStoreAssetType0
from ...models.problem_details_type_0 import ProblemDetailsType0
from ...types import Response


def _get_kwargs(
    id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/toolbox-service/v2/assets/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
                "x-roblox-stability": "BETA",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 1000},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 1000},
                },
                "x-roblox-scopes": [{"name": "creator-store-product:read"}],
            },
            "openapi-id": "Toolbox_GetAssetDetails",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> CreatorStoreAssetType0 | None | None | ProblemDetailsType0 | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> CreatorStoreAssetType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_creator_store_asset_type_0 = CreatorStoreAssetType0.from_dict(data)

                return componentsschemas_creator_store_asset_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreatorStoreAssetType0 | None, data)

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 403:

        def _parse_response_403(data: object) -> None | ProblemDetailsType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_problem_details_type_0 = ProblemDetailsType0.from_dict(data)

                return componentsschemas_problem_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProblemDetailsType0, data)

        response_403 = _parse_response_403(response.json())

        return response_403

    if response.status_code == 404:

        def _parse_response_404(data: object) -> None | ProblemDetailsType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_problem_details_type_0 = ProblemDetailsType0.from_dict(data)

                return componentsschemas_problem_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProblemDetailsType0, data)

        response_404 = _parse_response_404(response.json())

        return response_404

    if response.status_code == 429:

        def _parse_response_429(data: object) -> None | ProblemDetailsType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_problem_details_type_0 = ProblemDetailsType0.from_dict(data)

                return componentsschemas_problem_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProblemDetailsType0, data)

        response_429 = _parse_response_429(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[CreatorStoreAssetType0 | None | None | ProblemDetailsType0]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[CreatorStoreAssetType0 | None | None | ProblemDetailsType0]:
    """Get Creator Store Asset Details

     Get details for a single Creator Store asset.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatorStoreAssetType0 | None | None | ProblemDetailsType0]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
) -> CreatorStoreAssetType0 | None | None | ProblemDetailsType0 | None:
    """Get Creator Store Asset Details

     Get details for a single Creator Store asset.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatorStoreAssetType0 | None | None | ProblemDetailsType0
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[CreatorStoreAssetType0 | None | None | ProblemDetailsType0]:
    """Get Creator Store Asset Details

     Get details for a single Creator Store asset.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatorStoreAssetType0 | None | None | ProblemDetailsType0]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
) -> CreatorStoreAssetType0 | None | None | ProblemDetailsType0 | None:
    """Get Creator Store Asset Details

     Get details for a single Creator Store asset.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatorStoreAssetType0 | None | None | ProblemDetailsType0
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
