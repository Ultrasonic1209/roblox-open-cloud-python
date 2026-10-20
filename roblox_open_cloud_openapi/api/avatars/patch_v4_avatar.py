from http import HTTPStatus
from typing import TYPE_CHECKING, Any, cast

if TYPE_CHECKING:
    import httpx2 as httpx
else:
    try:
        import httpx2 as httpx
    except ModuleNotFoundError:
        try:
            import httpx
        except ModuleNotFoundError:
            raise RuntimeError(
                "This module requires the httpx2 package to be installed.\n"
                "You can install it with:\n"
                "    $ pip install httpx2\n"
            ) from None


from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

"""
{'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.roblox_api_avatar_models_v4_request_update_avatar_definition_request_v4 import (
    RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4,
)
from ...models.roblox_api_avatar_models_v4_response_update_avatar_definition_response_v4 import (
    RobloxApiAvatarModelsV4ResponseUpdateAvatarDefinitionResponseV4,
)
from ...types import Unset


def _get_kwargs(
    *,
    body: RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4
    | RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4
    | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(roblox_place_id, Unset):
        headers["Roblox-Place-Id"] = str(roblox_place_id)

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "https://avatar.roblox.com/v4/avatar",
    }

    if isinstance(body, RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxApiAvatarModelsV4ResponseUpdateAvatarDefinitionResponseV4 | None:
    if response.status_code == 200:
        response_200 = RobloxApiAvatarModelsV4ResponseUpdateAvatarDefinitionResponseV4.from_dict(response.json())

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
) -> Response[Any | RobloxApiAvatarModelsV4ResponseUpdateAvatarDefinitionResponseV4]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4
    | RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4
    | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsV4ResponseUpdateAvatarDefinitionResponseV4]:
    """Sets the avatar to the incoming avatar using field masks.

     Only allows items that you own, are not expired, and are wearable asset types.
    Any assets being worn before this method is called are automatically removed.

    Args:
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4): Request model for
            updating an avatar definition (V4).
        body (RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4): Request model for
            updating an avatar definition (V4).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsV4ResponseUpdateAvatarDefinitionResponseV4]
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
    body: RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4
    | RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4
    | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsV4ResponseUpdateAvatarDefinitionResponseV4 | None:
    """Sets the avatar to the incoming avatar using field masks.

     Only allows items that you own, are not expired, and are wearable asset types.
    Any assets being worn before this method is called are automatically removed.

    Args:
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4): Request model for
            updating an avatar definition (V4).
        body (RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4): Request model for
            updating an avatar definition (V4).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsV4ResponseUpdateAvatarDefinitionResponseV4
    """

    return sync_detailed(
        client=client,
        body=body,
        roblox_place_id=roblox_place_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4
    | RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4
    | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsV4ResponseUpdateAvatarDefinitionResponseV4]:
    """Sets the avatar to the incoming avatar using field masks.

     Only allows items that you own, are not expired, and are wearable asset types.
    Any assets being worn before this method is called are automatically removed.

    Args:
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4): Request model for
            updating an avatar definition (V4).
        body (RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4): Request model for
            updating an avatar definition (V4).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsV4ResponseUpdateAvatarDefinitionResponseV4]
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
    body: RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4
    | RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4
    | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsV4ResponseUpdateAvatarDefinitionResponseV4 | None:
    """Sets the avatar to the incoming avatar using field masks.

     Only allows items that you own, are not expired, and are wearable asset types.
    Any assets being worn before this method is called are automatically removed.

    Args:
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4): Request model for
            updating an avatar definition (V4).
        body (RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4): Request model for
            updating an avatar definition (V4).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsV4ResponseUpdateAvatarDefinitionResponseV4
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            roblox_place_id=roblox_place_id,
        )
    ).parsed
