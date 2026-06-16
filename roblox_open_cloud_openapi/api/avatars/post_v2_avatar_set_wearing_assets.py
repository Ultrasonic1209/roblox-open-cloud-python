from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_api_avatar_models_wear_request_model import RobloxApiAvatarModelsWearRequestModel
from ...models.roblox_api_avatar_models_wear_response_model import RobloxApiAvatarModelsWearResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RobloxApiAvatarModelsWearRequestModel | RobloxApiAvatarModelsWearRequestModel | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(roblox_place_id, Unset):
        headers["Roblox-Place-Id"] = str(roblox_place_id)

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/avatar/set-wearing-assets",
    }

    if isinstance(body, RobloxApiAvatarModelsWearRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxApiAvatarModelsWearRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxApiAvatarModelsWearResponseModel | None:
    if response.status_code == 200:
        response_200 = RobloxApiAvatarModelsWearResponseModel.from_dict(response.json())

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

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxApiAvatarModelsWearResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxApiAvatarModelsWearRequestModel | RobloxApiAvatarModelsWearRequestModel | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsWearResponseModel]:
    """Sets the avatar's current assets to the list.

     Only allows items that you own, are not expired, and are wearable asset types.
    Any assets being worn before this method is called are automatically removed.

    Args:
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsWearRequestModel): A model that contains a list of AssetWear
            models
        body (RobloxApiAvatarModelsWearRequestModel): A model that contains a list of AssetWear
            models

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsWearResponseModel]
    """

    kwargs = _get_kwargs(
        body=body,
        roblox_place_id=roblox_place_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RobloxApiAvatarModelsWearRequestModel | RobloxApiAvatarModelsWearRequestModel | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsWearResponseModel | None:
    """Sets the avatar's current assets to the list.

     Only allows items that you own, are not expired, and are wearable asset types.
    Any assets being worn before this method is called are automatically removed.

    Args:
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsWearRequestModel): A model that contains a list of AssetWear
            models
        body (RobloxApiAvatarModelsWearRequestModel): A model that contains a list of AssetWear
            models

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsWearResponseModel
    """

    return sync_detailed(
        client=client,
        body=body,
        roblox_place_id=roblox_place_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxApiAvatarModelsWearRequestModel | RobloxApiAvatarModelsWearRequestModel | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsWearResponseModel]:
    """Sets the avatar's current assets to the list.

     Only allows items that you own, are not expired, and are wearable asset types.
    Any assets being worn before this method is called are automatically removed.

    Args:
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsWearRequestModel): A model that contains a list of AssetWear
            models
        body (RobloxApiAvatarModelsWearRequestModel): A model that contains a list of AssetWear
            models

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsWearResponseModel]
    """

    kwargs = _get_kwargs(
        body=body,
        roblox_place_id=roblox_place_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxApiAvatarModelsWearRequestModel | RobloxApiAvatarModelsWearRequestModel | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsWearResponseModel | None:
    """Sets the avatar's current assets to the list.

     Only allows items that you own, are not expired, and are wearable asset types.
    Any assets being worn before this method is called are automatically removed.

    Args:
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsWearRequestModel): A model that contains a list of AssetWear
            models
        body (RobloxApiAvatarModelsWearRequestModel): A model that contains a list of AssetWear
            models

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsWearResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            roblox_place_id=roblox_place_id,
        )
    ).parsed
