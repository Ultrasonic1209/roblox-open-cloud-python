from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_assetsthumbnails_roblox_com_format import GetV1AssetsthumbnailsRobloxComFormat
from ...models.get_v1_assetsthumbnails_roblox_com_return_policy import GetV1AssetsthumbnailsRobloxComReturnPolicy
from ...models.get_v1_assetsthumbnails_roblox_com_size import GetV1AssetsthumbnailsRobloxComSize
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    asset_ids: list[int],
    return_policy: GetV1AssetsthumbnailsRobloxComReturnPolicy
    | Unset = GetV1AssetsthumbnailsRobloxComReturnPolicy.PLACEHOLDER,
    size: GetV1AssetsthumbnailsRobloxComSize | Unset = GetV1AssetsthumbnailsRobloxComSize.VALUE_0,
    format_: GetV1AssetsthumbnailsRobloxComFormat | Unset = GetV1AssetsthumbnailsRobloxComFormat.PNG,
    is_circular: bool | Unset = False,
    roblox_place_id: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(roblox_place_id, Unset):
        headers["Roblox-Place-Id"] = str(roblox_place_id)

    params: dict[str, Any] = {}

    json_asset_ids = asset_ids

    params["assetIds"] = json_asset_ids

    json_return_policy: str | Unset = UNSET
    if not isinstance(return_policy, Unset):
        json_return_policy = return_policy.value

    params["returnPolicy"] = json_return_policy

    json_size: str | Unset = UNSET
    if not isinstance(size, Unset):
        json_size = size.value

    params["size"] = json_size

    json_format_: str | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params["isCircular"] = is_circular

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://thumbnails.roblox.com/v1/assets#thumbnails.roblox.com",
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "STABLE",
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "get_v1_assets#thumbnails.roblox.com",
        },
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 403:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    asset_ids: list[int],
    return_policy: GetV1AssetsthumbnailsRobloxComReturnPolicy
    | Unset = GetV1AssetsthumbnailsRobloxComReturnPolicy.PLACEHOLDER,
    size: GetV1AssetsthumbnailsRobloxComSize | Unset = GetV1AssetsthumbnailsRobloxComSize.VALUE_0,
    format_: GetV1AssetsthumbnailsRobloxComFormat | Unset = GetV1AssetsthumbnailsRobloxComFormat.PNG,
    is_circular: bool | Unset = False,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any]:
    """Thumbnails assets.

    Args:
        asset_ids (list[int]):
        return_policy (GetV1AssetsthumbnailsRobloxComReturnPolicy | Unset):  Default:
            GetV1AssetsthumbnailsRobloxComReturnPolicy.PLACEHOLDER.
        size (GetV1AssetsthumbnailsRobloxComSize | Unset):  Default:
            GetV1AssetsthumbnailsRobloxComSize.VALUE_0.
        format_ (GetV1AssetsthumbnailsRobloxComFormat | Unset):  Default:
            GetV1AssetsthumbnailsRobloxComFormat.PNG.
        is_circular (bool | Unset):  Default: False.
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        asset_ids=asset_ids,
        return_policy=return_policy,
        size=size,
        format_=format_,
        is_circular=is_circular,
        roblox_place_id=roblox_place_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    asset_ids: list[int],
    return_policy: GetV1AssetsthumbnailsRobloxComReturnPolicy
    | Unset = GetV1AssetsthumbnailsRobloxComReturnPolicy.PLACEHOLDER,
    size: GetV1AssetsthumbnailsRobloxComSize | Unset = GetV1AssetsthumbnailsRobloxComSize.VALUE_0,
    format_: GetV1AssetsthumbnailsRobloxComFormat | Unset = GetV1AssetsthumbnailsRobloxComFormat.PNG,
    is_circular: bool | Unset = False,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any]:
    """Thumbnails assets.

    Args:
        asset_ids (list[int]):
        return_policy (GetV1AssetsthumbnailsRobloxComReturnPolicy | Unset):  Default:
            GetV1AssetsthumbnailsRobloxComReturnPolicy.PLACEHOLDER.
        size (GetV1AssetsthumbnailsRobloxComSize | Unset):  Default:
            GetV1AssetsthumbnailsRobloxComSize.VALUE_0.
        format_ (GetV1AssetsthumbnailsRobloxComFormat | Unset):  Default:
            GetV1AssetsthumbnailsRobloxComFormat.PNG.
        is_circular (bool | Unset):  Default: False.
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        asset_ids=asset_ids,
        return_policy=return_policy,
        size=size,
        format_=format_,
        is_circular=is_circular,
        roblox_place_id=roblox_place_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)
