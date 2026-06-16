from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_assets_thumbnails_api_format import GetV1AssetsThumbnailsApiFormat
from ...models.get_v1_assets_thumbnails_api_return_policy import GetV1AssetsThumbnailsApiReturnPolicy
from ...models.get_v1_assets_thumbnails_api_size import GetV1AssetsThumbnailsApiSize
from ...models.roblox_web_web_api_models_api_array_response_roblox_web_responses_thumbnails_thumbnail_response import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    asset_ids: list[int],
    return_policy: GetV1AssetsThumbnailsApiReturnPolicy | Unset = GetV1AssetsThumbnailsApiReturnPolicy.PLACEHOLDER,
    size: GetV1AssetsThumbnailsApiSize | Unset = GetV1AssetsThumbnailsApiSize.VALUE_0,
    format_: GetV1AssetsThumbnailsApiFormat | Unset = GetV1AssetsThumbnailsApiFormat.PNG,
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
        "url": "/v1/assets#ThumbnailsApi",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]:
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
    return_policy: GetV1AssetsThumbnailsApiReturnPolicy | Unset = GetV1AssetsThumbnailsApiReturnPolicy.PLACEHOLDER,
    size: GetV1AssetsThumbnailsApiSize | Unset = GetV1AssetsThumbnailsApiSize.VALUE_0,
    format_: GetV1AssetsThumbnailsApiFormat | Unset = GetV1AssetsThumbnailsApiFormat.PNG,
    is_circular: bool | Unset = False,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]:
    """Thumbnails assets.

    Args:
        asset_ids (list[int]):
        return_policy (GetV1AssetsThumbnailsApiReturnPolicy | Unset):  Default:
            GetV1AssetsThumbnailsApiReturnPolicy.PLACEHOLDER.
        size (GetV1AssetsThumbnailsApiSize | Unset):  Default:
            GetV1AssetsThumbnailsApiSize.VALUE_0.
        format_ (GetV1AssetsThumbnailsApiFormat | Unset):  Default:
            GetV1AssetsThumbnailsApiFormat.PNG.
        is_circular (bool | Unset):  Default: False.
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]
    """

    kwargs = _get_kwargs(
        asset_ids=asset_ids,
        return_policy=return_policy,
        size=size,
        format_=format_,
        is_circular=is_circular,
        roblox_place_id=roblox_place_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    asset_ids: list[int],
    return_policy: GetV1AssetsThumbnailsApiReturnPolicy | Unset = GetV1AssetsThumbnailsApiReturnPolicy.PLACEHOLDER,
    size: GetV1AssetsThumbnailsApiSize | Unset = GetV1AssetsThumbnailsApiSize.VALUE_0,
    format_: GetV1AssetsThumbnailsApiFormat | Unset = GetV1AssetsThumbnailsApiFormat.PNG,
    is_circular: bool | Unset = False,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse | None:
    """Thumbnails assets.

    Args:
        asset_ids (list[int]):
        return_policy (GetV1AssetsThumbnailsApiReturnPolicy | Unset):  Default:
            GetV1AssetsThumbnailsApiReturnPolicy.PLACEHOLDER.
        size (GetV1AssetsThumbnailsApiSize | Unset):  Default:
            GetV1AssetsThumbnailsApiSize.VALUE_0.
        format_ (GetV1AssetsThumbnailsApiFormat | Unset):  Default:
            GetV1AssetsThumbnailsApiFormat.PNG.
        is_circular (bool | Unset):  Default: False.
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse
    """

    return sync_detailed(
        client=client,
        asset_ids=asset_ids,
        return_policy=return_policy,
        size=size,
        format_=format_,
        is_circular=is_circular,
        roblox_place_id=roblox_place_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    asset_ids: list[int],
    return_policy: GetV1AssetsThumbnailsApiReturnPolicy | Unset = GetV1AssetsThumbnailsApiReturnPolicy.PLACEHOLDER,
    size: GetV1AssetsThumbnailsApiSize | Unset = GetV1AssetsThumbnailsApiSize.VALUE_0,
    format_: GetV1AssetsThumbnailsApiFormat | Unset = GetV1AssetsThumbnailsApiFormat.PNG,
    is_circular: bool | Unset = False,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]:
    """Thumbnails assets.

    Args:
        asset_ids (list[int]):
        return_policy (GetV1AssetsThumbnailsApiReturnPolicy | Unset):  Default:
            GetV1AssetsThumbnailsApiReturnPolicy.PLACEHOLDER.
        size (GetV1AssetsThumbnailsApiSize | Unset):  Default:
            GetV1AssetsThumbnailsApiSize.VALUE_0.
        format_ (GetV1AssetsThumbnailsApiFormat | Unset):  Default:
            GetV1AssetsThumbnailsApiFormat.PNG.
        is_circular (bool | Unset):  Default: False.
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]
    """

    kwargs = _get_kwargs(
        asset_ids=asset_ids,
        return_policy=return_policy,
        size=size,
        format_=format_,
        is_circular=is_circular,
        roblox_place_id=roblox_place_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    asset_ids: list[int],
    return_policy: GetV1AssetsThumbnailsApiReturnPolicy | Unset = GetV1AssetsThumbnailsApiReturnPolicy.PLACEHOLDER,
    size: GetV1AssetsThumbnailsApiSize | Unset = GetV1AssetsThumbnailsApiSize.VALUE_0,
    format_: GetV1AssetsThumbnailsApiFormat | Unset = GetV1AssetsThumbnailsApiFormat.PNG,
    is_circular: bool | Unset = False,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse | None:
    """Thumbnails assets.

    Args:
        asset_ids (list[int]):
        return_policy (GetV1AssetsThumbnailsApiReturnPolicy | Unset):  Default:
            GetV1AssetsThumbnailsApiReturnPolicy.PLACEHOLDER.
        size (GetV1AssetsThumbnailsApiSize | Unset):  Default:
            GetV1AssetsThumbnailsApiSize.VALUE_0.
        format_ (GetV1AssetsThumbnailsApiFormat | Unset):  Default:
            GetV1AssetsThumbnailsApiFormat.PNG.
        is_circular (bool | Unset):  Default: False.
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            asset_ids=asset_ids,
            return_policy=return_policy,
            size=size,
            format_=format_,
            is_circular=is_circular,
            roblox_place_id=roblox_place_id,
        )
    ).parsed
