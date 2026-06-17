from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_developer_products_icons_format import GetV1DeveloperProductsIconsFormat
from ...models.get_v1_developer_products_icons_size import GetV1DeveloperProductsIconsSize
from ...models.roblox_web_web_api_models_api_array_response_roblox_web_responses_thumbnails_thumbnail_response import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    developer_product_ids: list[int],
    size: GetV1DeveloperProductsIconsSize | Unset = GetV1DeveloperProductsIconsSize.VALUE_0,
    format_: GetV1DeveloperProductsIconsFormat | Unset = GetV1DeveloperProductsIconsFormat.PNG,
    is_circular: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_developer_product_ids = developer_product_ids

    params["developerProductIds"] = json_developer_product_ids

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
        "url": "https://thumbnails.roblox.com/v1/developer-products/icons",
        "params": params,
        "openapi-extensions": {
            "x-roblox-stability": "STABLE",
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
        },
        "openapi-id": "get_v1_developer-products_icons",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
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
    developer_product_ids: list[int],
    size: GetV1DeveloperProductsIconsSize | Unset = GetV1DeveloperProductsIconsSize.VALUE_0,
    format_: GetV1DeveloperProductsIconsFormat | Unset = GetV1DeveloperProductsIconsFormat.PNG,
    is_circular: bool | Unset = False,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]:
    """Thumbnails developer product icons.

    Args:
        developer_product_ids (list[int]):
        size (GetV1DeveloperProductsIconsSize | Unset):  Default:
            GetV1DeveloperProductsIconsSize.VALUE_0.
        format_ (GetV1DeveloperProductsIconsFormat | Unset):  Default:
            GetV1DeveloperProductsIconsFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]
    """

    kwargs = _get_kwargs(
        developer_product_ids=developer_product_ids,
        size=size,
        format_=format_,
        is_circular=is_circular,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    developer_product_ids: list[int],
    size: GetV1DeveloperProductsIconsSize | Unset = GetV1DeveloperProductsIconsSize.VALUE_0,
    format_: GetV1DeveloperProductsIconsFormat | Unset = GetV1DeveloperProductsIconsFormat.PNG,
    is_circular: bool | Unset = False,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse | None:
    """Thumbnails developer product icons.

    Args:
        developer_product_ids (list[int]):
        size (GetV1DeveloperProductsIconsSize | Unset):  Default:
            GetV1DeveloperProductsIconsSize.VALUE_0.
        format_ (GetV1DeveloperProductsIconsFormat | Unset):  Default:
            GetV1DeveloperProductsIconsFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse
    """

    return sync_detailed(
        client=client,
        developer_product_ids=developer_product_ids,
        size=size,
        format_=format_,
        is_circular=is_circular,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    developer_product_ids: list[int],
    size: GetV1DeveloperProductsIconsSize | Unset = GetV1DeveloperProductsIconsSize.VALUE_0,
    format_: GetV1DeveloperProductsIconsFormat | Unset = GetV1DeveloperProductsIconsFormat.PNG,
    is_circular: bool | Unset = False,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]:
    """Thumbnails developer product icons.

    Args:
        developer_product_ids (list[int]):
        size (GetV1DeveloperProductsIconsSize | Unset):  Default:
            GetV1DeveloperProductsIconsSize.VALUE_0.
        format_ (GetV1DeveloperProductsIconsFormat | Unset):  Default:
            GetV1DeveloperProductsIconsFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]
    """

    kwargs = _get_kwargs(
        developer_product_ids=developer_product_ids,
        size=size,
        format_=format_,
        is_circular=is_circular,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    developer_product_ids: list[int],
    size: GetV1DeveloperProductsIconsSize | Unset = GetV1DeveloperProductsIconsSize.VALUE_0,
    format_: GetV1DeveloperProductsIconsFormat | Unset = GetV1DeveloperProductsIconsFormat.PNG,
    is_circular: bool | Unset = False,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse | None:
    """Thumbnails developer product icons.

    Args:
        developer_product_ids (list[int]):
        size (GetV1DeveloperProductsIconsSize | Unset):  Default:
            GetV1DeveloperProductsIconsSize.VALUE_0.
        format_ (GetV1DeveloperProductsIconsFormat | Unset):  Default:
            GetV1DeveloperProductsIconsFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            developer_product_ids=developer_product_ids,
            size=size,
            format_=format_,
            is_circular=is_circular,
        )
    ).parsed
