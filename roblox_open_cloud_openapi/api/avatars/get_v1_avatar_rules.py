from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_api_avatar_models_avatar_rules_model import RobloxApiAvatarModelsAvatarRulesModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    roblox_place_id: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(roblox_place_id, Unset):
        headers["Roblox-Place-Id"] = str(roblox_place_id)

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/avatar-rules",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RobloxApiAvatarModelsAvatarRulesModel | None:
    if response.status_code == 200:
        response_200 = RobloxApiAvatarModelsAvatarRulesModel.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RobloxApiAvatarModelsAvatarRulesModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    roblox_place_id: int | Unset = UNSET,
) -> Response[RobloxApiAvatarModelsAvatarRulesModel]:
    """Returns the business rules related to avatars.

     BodyColorsPalette is a list of valid brickColors you can choose for your avatar.
    WearableAssetTypes contains a list of asset types with names, ids, and the maximum number that you
    can wear at a time.
    Does not include packages because they cannot be worn on your avatar directly.
    PlayerAvatarTypes are the types of avatars you can choose between.

    Args:
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxApiAvatarModelsAvatarRulesModel]
    """

    kwargs = _get_kwargs(
        roblox_place_id=roblox_place_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    roblox_place_id: int | Unset = UNSET,
) -> RobloxApiAvatarModelsAvatarRulesModel | None:
    """Returns the business rules related to avatars.

     BodyColorsPalette is a list of valid brickColors you can choose for your avatar.
    WearableAssetTypes contains a list of asset types with names, ids, and the maximum number that you
    can wear at a time.
    Does not include packages because they cannot be worn on your avatar directly.
    PlayerAvatarTypes are the types of avatars you can choose between.

    Args:
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxApiAvatarModelsAvatarRulesModel
    """

    return sync_detailed(
        client=client,
        roblox_place_id=roblox_place_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    roblox_place_id: int | Unset = UNSET,
) -> Response[RobloxApiAvatarModelsAvatarRulesModel]:
    """Returns the business rules related to avatars.

     BodyColorsPalette is a list of valid brickColors you can choose for your avatar.
    WearableAssetTypes contains a list of asset types with names, ids, and the maximum number that you
    can wear at a time.
    Does not include packages because they cannot be worn on your avatar directly.
    PlayerAvatarTypes are the types of avatars you can choose between.

    Args:
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxApiAvatarModelsAvatarRulesModel]
    """

    kwargs = _get_kwargs(
        roblox_place_id=roblox_place_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    roblox_place_id: int | Unset = UNSET,
) -> RobloxApiAvatarModelsAvatarRulesModel | None:
    """Returns the business rules related to avatars.

     BodyColorsPalette is a list of valid brickColors you can choose for your avatar.
    WearableAssetTypes contains a list of asset types with names, ids, and the maximum number that you
    can wear at a time.
    Does not include packages because they cannot be worn on your avatar directly.
    PlayerAvatarTypes are the types of avatars you can choose between.

    Args:
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxApiAvatarModelsAvatarRulesModel
    """

    return (
        await asyncio_detailed(
            client=client,
            roblox_place_id=roblox_place_id,
        )
    ).parsed
