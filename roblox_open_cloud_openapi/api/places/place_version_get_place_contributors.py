from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_place_contributors_response import GetPlaceContributorsResponse
from ...models.operation_error_response import OperationErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    place_id: int,
    *,
    cursor: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/place-version-history-api/v1/{place_id}/contributors".format(
            place_id=quote(str(place_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "EXPERIMENTAL",
                "x-roblox-rate-limits": {"perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 1000}},
                "x-roblox-scopes": [{"name": "universe.place:read", "targetResourceSpecifier": ""}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "PlaceVersion_GetPlaceContributors",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> GetPlaceContributorsResponse | OperationErrorResponse | None:
    if response.status_code == 200:
        response_200 = GetPlaceContributorsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = OperationErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = OperationErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OperationErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = OperationErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[GetPlaceContributorsResponse | OperationErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    place_id: int,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> Response[GetPlaceContributorsResponse | OperationErrorResponse]:
    """Endpoint used to fetch all previous contributors of a place.

    Args:
        place_id (int):
        cursor (str | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPlaceContributorsResponse | OperationErrorResponse]
    """

    kwargs = _get_kwargs(
        place_id=place_id,
        cursor=cursor,
        page_size=page_size,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    place_id: int,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> GetPlaceContributorsResponse | OperationErrorResponse | None:
    """Endpoint used to fetch all previous contributors of a place.

    Args:
        place_id (int):
        cursor (str | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPlaceContributorsResponse | OperationErrorResponse
    """

    return sync_detailed(
        place_id=place_id,
        client=client,
        cursor=cursor,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    place_id: int,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> Response[GetPlaceContributorsResponse | OperationErrorResponse]:
    """Endpoint used to fetch all previous contributors of a place.

    Args:
        place_id (int):
        cursor (str | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPlaceContributorsResponse | OperationErrorResponse]
    """

    kwargs = _get_kwargs(
        place_id=place_id,
        cursor=cursor,
        page_size=page_size,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    place_id: int,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> GetPlaceContributorsResponse | OperationErrorResponse | None:
    """Endpoint used to fetch all previous contributors of a place.

    Args:
        place_id (int):
        cursor (str | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPlaceContributorsResponse | OperationErrorResponse
    """

    return (
        await asyncio_detailed(
            place_id=place_id,
            client=client,
            cursor=cursor,
            page_size=page_size,
        )
    ).parsed
