from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_account_information_api_models_promotion_channels_by_user_id_response import (
    RobloxAccountInformationApiModelsPromotionChannelsByUserIdResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    *,
    always_return_urls: bool | Unset = False,
    filter_link: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["alwaysReturnUrls"] = always_return_urls

    params["filterLink"] = filter_link

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/users/{user_id}/promotion-channels".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxAccountInformationApiModelsPromotionChannelsByUserIdResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAccountInformationApiModelsPromotionChannelsByUserIdResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxAccountInformationApiModelsPromotionChannelsByUserIdResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    always_return_urls: bool | Unset = False,
    filter_link: bool | Unset = False,
) -> Response[Any | RobloxAccountInformationApiModelsPromotionChannelsByUserIdResponse]:
    """Get promotion channels for a given user ID

    Args:
        user_id (int):
        always_return_urls (bool | Unset):  Default: False.
        filter_link (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAccountInformationApiModelsPromotionChannelsByUserIdResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        always_return_urls=always_return_urls,
        filter_link=filter_link,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    always_return_urls: bool | Unset = False,
    filter_link: bool | Unset = False,
) -> Any | RobloxAccountInformationApiModelsPromotionChannelsByUserIdResponse | None:
    """Get promotion channels for a given user ID

    Args:
        user_id (int):
        always_return_urls (bool | Unset):  Default: False.
        filter_link (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAccountInformationApiModelsPromotionChannelsByUserIdResponse
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        always_return_urls=always_return_urls,
        filter_link=filter_link,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    always_return_urls: bool | Unset = False,
    filter_link: bool | Unset = False,
) -> Response[Any | RobloxAccountInformationApiModelsPromotionChannelsByUserIdResponse]:
    """Get promotion channels for a given user ID

    Args:
        user_id (int):
        always_return_urls (bool | Unset):  Default: False.
        filter_link (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAccountInformationApiModelsPromotionChannelsByUserIdResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        always_return_urls=always_return_urls,
        filter_link=filter_link,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    always_return_urls: bool | Unset = False,
    filter_link: bool | Unset = False,
) -> Any | RobloxAccountInformationApiModelsPromotionChannelsByUserIdResponse | None:
    """Get promotion channels for a given user ID

    Args:
        user_id (int):
        always_return_urls (bool | Unset):  Default: False.
        filter_link (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAccountInformationApiModelsPromotionChannelsByUserIdResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            always_return_urls=always_return_urls,
            filter_link=filter_link,
        )
    ).parsed
