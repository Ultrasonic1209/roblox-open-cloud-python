from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_web_assets_asset_response_item_v2 import RobloxWebAssetsAssetResponseItemV2
from ...models.roblox_web_assets_batch_asset_request_item import RobloxWebAssetsBatchAssetRequestItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[RobloxWebAssetsBatchAssetRequestItem] | list[RobloxWebAssetsBatchAssetRequestItem] | Unset = UNSET,
    roblox_place_id: int,
    accept: str,
    roblox_browser_asset_request: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Roblox-Place-Id"] = str(roblox_place_id)

    headers["Accept"] = accept

    headers["Roblox-Browser-Asset-Request"] = roblox_browser_asset_request

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://assetdelivery.roblox.com/v2/assets/batch",
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "post_v2_assets_batch",
    }

    if isinstance(body, list[RobloxWebAssetsBatchAssetRequestItem]):
        _kwargs["json"] = []
        for body_item_data in body:
            body_item = body_item_data.to_dict()
            _kwargs["json"].append(body_item)

        headers["Content-Type"] = "application/json"
    if isinstance(body, list[RobloxWebAssetsBatchAssetRequestItem]):
        _kwargs["json"] = []
        for body_item_data in body:
            body_item = body_item_data.to_dict()
            _kwargs["json"].append(body_item)

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> list[RobloxWebAssetsAssetResponseItemV2] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RobloxWebAssetsAssetResponseItemV2.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[list[RobloxWebAssetsAssetResponseItemV2]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: list[RobloxWebAssetsBatchAssetRequestItem] | list[RobloxWebAssetsBatchAssetRequestItem] | Unset = UNSET,
    roblox_place_id: int,
    accept: str,
    roblox_browser_asset_request: str,
) -> Response[list[RobloxWebAssetsAssetResponseItemV2]]:
    """
    Args:
        roblox_place_id (int):
        accept (str):
        roblox_browser_asset_request (str):
        body (list[RobloxWebAssetsBatchAssetRequestItem]):
        body (list[RobloxWebAssetsBatchAssetRequestItem]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[RobloxWebAssetsAssetResponseItemV2]]
    """

    kwargs = _get_kwargs(
        body=body,
        roblox_place_id=roblox_place_id,
        accept=accept,
        roblox_browser_asset_request=roblox_browser_asset_request,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: list[RobloxWebAssetsBatchAssetRequestItem] | list[RobloxWebAssetsBatchAssetRequestItem] | Unset = UNSET,
    roblox_place_id: int,
    accept: str,
    roblox_browser_asset_request: str,
) -> list[RobloxWebAssetsAssetResponseItemV2] | None:
    """
    Args:
        roblox_place_id (int):
        accept (str):
        roblox_browser_asset_request (str):
        body (list[RobloxWebAssetsBatchAssetRequestItem]):
        body (list[RobloxWebAssetsBatchAssetRequestItem]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[RobloxWebAssetsAssetResponseItemV2]
    """

    return sync_detailed(
        client=client,
        body=body,
        roblox_place_id=roblox_place_id,
        accept=accept,
        roblox_browser_asset_request=roblox_browser_asset_request,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: list[RobloxWebAssetsBatchAssetRequestItem] | list[RobloxWebAssetsBatchAssetRequestItem] | Unset = UNSET,
    roblox_place_id: int,
    accept: str,
    roblox_browser_asset_request: str,
) -> Response[list[RobloxWebAssetsAssetResponseItemV2]]:
    """
    Args:
        roblox_place_id (int):
        accept (str):
        roblox_browser_asset_request (str):
        body (list[RobloxWebAssetsBatchAssetRequestItem]):
        body (list[RobloxWebAssetsBatchAssetRequestItem]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[RobloxWebAssetsAssetResponseItemV2]]
    """

    kwargs = _get_kwargs(
        body=body,
        roblox_place_id=roblox_place_id,
        accept=accept,
        roblox_browser_asset_request=roblox_browser_asset_request,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: list[RobloxWebAssetsBatchAssetRequestItem] | list[RobloxWebAssetsBatchAssetRequestItem] | Unset = UNSET,
    roblox_place_id: int,
    accept: str,
    roblox_browser_asset_request: str,
) -> list[RobloxWebAssetsAssetResponseItemV2] | None:
    """
    Args:
        roblox_place_id (int):
        accept (str):
        roblox_browser_asset_request (str):
        body (list[RobloxWebAssetsBatchAssetRequestItem]):
        body (list[RobloxWebAssetsBatchAssetRequestItem]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[RobloxWebAssetsAssetResponseItemV2]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            roblox_place_id=roblox_place_id,
            accept=accept,
            roblox_browser_asset_request=roblox_browser_asset_request,
        )
    ).parsed
