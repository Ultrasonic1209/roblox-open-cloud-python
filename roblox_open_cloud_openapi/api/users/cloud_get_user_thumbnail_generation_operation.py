from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ocv2_operations_operation import OCV2OperationsOperation
from ...types import Response


def _get_kwargs(
    user_id: str,
    operation_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/users/{user_id}/operations/{operation_id}".format(
            user_id=quote(str(user_id), safe=""),
            operation_id=quote(str(operation_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OCV2OperationsOperation | None:
    if response.status_code == 200:
        response_200 = OCV2OperationsOperation.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OCV2OperationsOperation]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    operation_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OCV2OperationsOperation]:
    """Get User Thumbnail Generation Operation

     Retrieves the status of the operation to [generate a user thumbnail](https://create.roblox.com/docs/
    cloud/reference/features/users#Cloud_GenerateUserThumbnail).

    Args:
        user_id (str):
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OCV2OperationsOperation]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        operation_id=operation_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    operation_id: str,
    *,
    client: AuthenticatedClient,
) -> OCV2OperationsOperation | None:
    """Get User Thumbnail Generation Operation

     Retrieves the status of the operation to [generate a user thumbnail](https://create.roblox.com/docs/
    cloud/reference/features/users#Cloud_GenerateUserThumbnail).

    Args:
        user_id (str):
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OCV2OperationsOperation
    """

    return sync_detailed(
        user_id=user_id,
        operation_id=operation_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    operation_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OCV2OperationsOperation]:
    """Get User Thumbnail Generation Operation

     Retrieves the status of the operation to [generate a user thumbnail](https://create.roblox.com/docs/
    cloud/reference/features/users#Cloud_GenerateUserThumbnail).

    Args:
        user_id (str):
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OCV2OperationsOperation]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        operation_id=operation_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    operation_id: str,
    *,
    client: AuthenticatedClient,
) -> OCV2OperationsOperation | None:
    """Get User Thumbnail Generation Operation

     Retrieves the status of the operation to [generate a user thumbnail](https://create.roblox.com/docs/
    cloud/reference/features/users#Cloud_GenerateUserThumbnail).

    Args:
        user_id (str):
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OCV2OperationsOperation
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            operation_id=operation_id,
            client=client,
        )
    ).parsed
