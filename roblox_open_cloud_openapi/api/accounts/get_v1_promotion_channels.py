from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_account_information_api_models_promotion_channels_response import (
    RobloxAccountInformationApiModelsPromotionChannelsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    always_return_urls: bool | Unset = False,
    filter_link: bool | Unset = False,
    only_shorten_twitter: bool | Unset = True,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["alwaysReturnUrls"] = always_return_urls

    params["filterLink"] = filter_link

    params["onlyShortenTwitter"] = only_shorten_twitter

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://accountinformation.roblox.com/v1/promotion-channels",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxAccountInformationApiModelsPromotionChannelsResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAccountInformationApiModelsPromotionChannelsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxAccountInformationApiModelsPromotionChannelsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    always_return_urls: bool | Unset = False,
    filter_link: bool | Unset = False,
    only_shorten_twitter: bool | Unset = True,
) -> Response[Any | RobloxAccountInformationApiModelsPromotionChannelsResponse]:
    """Get the user's promotion channels

    Args:
        always_return_urls (bool | Unset):  Default: False.
        filter_link (bool | Unset):  Default: False.
        only_shorten_twitter (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAccountInformationApiModelsPromotionChannelsResponse]
    """

    kwargs = _get_kwargs(
        always_return_urls=always_return_urls,
        filter_link=filter_link,
        only_shorten_twitter=only_shorten_twitter,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    always_return_urls: bool | Unset = False,
    filter_link: bool | Unset = False,
    only_shorten_twitter: bool | Unset = True,
) -> Any | RobloxAccountInformationApiModelsPromotionChannelsResponse | None:
    """Get the user's promotion channels

    Args:
        always_return_urls (bool | Unset):  Default: False.
        filter_link (bool | Unset):  Default: False.
        only_shorten_twitter (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAccountInformationApiModelsPromotionChannelsResponse
    """

    return sync_detailed(
        client=client,
        always_return_urls=always_return_urls,
        filter_link=filter_link,
        only_shorten_twitter=only_shorten_twitter,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    always_return_urls: bool | Unset = False,
    filter_link: bool | Unset = False,
    only_shorten_twitter: bool | Unset = True,
) -> Response[Any | RobloxAccountInformationApiModelsPromotionChannelsResponse]:
    """Get the user's promotion channels

    Args:
        always_return_urls (bool | Unset):  Default: False.
        filter_link (bool | Unset):  Default: False.
        only_shorten_twitter (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAccountInformationApiModelsPromotionChannelsResponse]
    """

    kwargs = _get_kwargs(
        always_return_urls=always_return_urls,
        filter_link=filter_link,
        only_shorten_twitter=only_shorten_twitter,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    always_return_urls: bool | Unset = False,
    filter_link: bool | Unset = False,
    only_shorten_twitter: bool | Unset = True,
) -> Any | RobloxAccountInformationApiModelsPromotionChannelsResponse | None:
    """Get the user's promotion channels

    Args:
        always_return_urls (bool | Unset):  Default: False.
        filter_link (bool | Unset):  Default: False.
        only_shorten_twitter (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAccountInformationApiModelsPromotionChannelsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            always_return_urls=always_return_urls,
            filter_link=filter_link,
            only_shorten_twitter=only_shorten_twitter,
        )
    ).parsed
