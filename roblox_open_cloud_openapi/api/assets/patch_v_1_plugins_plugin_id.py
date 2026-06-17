from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_develop_api_update_plugin_request import RobloxDevelopApiUpdatePluginRequest
from ...models.roblox_web_web_api_api_empty_response_model import RobloxWebWebAPIApiEmptyResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    plugin_id: int,
    *,
    body: RobloxDevelopApiUpdatePluginRequest | RobloxDevelopApiUpdatePluginRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "https://develop.roblox.com/v1/plugins/{plugin_id}".format(
            plugin_id=quote(str(plugin_id), safe=""),
        ),
    }

    if isinstance(body, RobloxDevelopApiUpdatePluginRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxDevelopApiUpdatePluginRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIApiEmptyResponseModel.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    plugin_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxDevelopApiUpdatePluginRequest | RobloxDevelopApiUpdatePluginRequest | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Updates a plugin.

    Args:
        plugin_id (int):
        body (RobloxDevelopApiUpdatePluginRequest): A request model for updating a plugin.
        body (RobloxDevelopApiUpdatePluginRequest): A request model for updating a plugin.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        plugin_id=plugin_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    plugin_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxDevelopApiUpdatePluginRequest | RobloxDevelopApiUpdatePluginRequest | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Updates a plugin.

    Args:
        plugin_id (int):
        body (RobloxDevelopApiUpdatePluginRequest): A request model for updating a plugin.
        body (RobloxDevelopApiUpdatePluginRequest): A request model for updating a plugin.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return sync_detailed(
        plugin_id=plugin_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    plugin_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxDevelopApiUpdatePluginRequest | RobloxDevelopApiUpdatePluginRequest | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Updates a plugin.

    Args:
        plugin_id (int):
        body (RobloxDevelopApiUpdatePluginRequest): A request model for updating a plugin.
        body (RobloxDevelopApiUpdatePluginRequest): A request model for updating a plugin.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        plugin_id=plugin_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    plugin_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxDevelopApiUpdatePluginRequest | RobloxDevelopApiUpdatePluginRequest | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Updates a plugin.

    Args:
        plugin_id (int):
        body (RobloxDevelopApiUpdatePluginRequest): A request model for updating a plugin.
        body (RobloxDevelopApiUpdatePluginRequest): A request model for updating a plugin.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return (
        await asyncio_detailed(
            plugin_id=plugin_id,
            client=client,
            body=body,
        )
    ).parsed
