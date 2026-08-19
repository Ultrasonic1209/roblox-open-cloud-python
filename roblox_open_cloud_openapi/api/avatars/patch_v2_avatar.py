import sys
from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_api_avatar_models_update_avatar_request_model import RobloxApiAvatarModelsUpdateAvatarRequestModel
from ...models.roblox_api_avatar_models_update_avatar_response_model import (
    RobloxApiAvatarModelsUpdateAvatarResponseModel,
)


def _get_kwargs(
    *,
    body: RobloxApiAvatarModelsUpdateAvatarRequestModel | RobloxApiAvatarModelsUpdateAvatarRequestModel | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(roblox_place_id, Unset):
        headers["Roblox-Place-Id"] = str(roblox_place_id)

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "https://avatar.roblox.com/v2/avatar",
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "patch_v2_avatar",
        },
    }

    if isinstance(body, RobloxApiAvatarModelsUpdateAvatarRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxApiAvatarModelsUpdateAvatarRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxApiAvatarModelsUpdateAvatarResponseModel | None:
    if response.status_code == 200:
        response_200 = RobloxApiAvatarModelsUpdateAvatarResponseModel.from_dict(response.json())

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
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxApiAvatarModelsUpdateAvatarResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/avatars#avatar_patch_v2_avatar"
)
def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxApiAvatarModelsUpdateAvatarRequestModel | RobloxApiAvatarModelsUpdateAvatarRequestModel | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsUpdateAvatarResponseModel]:
    """Sets the avatar to the incoming avatar using field masks.

     Only allows items that you own, are not expired, and are wearable asset types.
    Any assets being worn before this method is called are automatically removed.

    Please use PATCH v4/avatar

    Args:
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsUpdateAvatarRequestModel): A model containing details about an
            avatar update request.
        body (RobloxApiAvatarModelsUpdateAvatarRequestModel): A model containing details about an
            avatar update request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsUpdateAvatarResponseModel]
    """

    kwargs = _get_kwargs(
        body=body,
        roblox_place_id=roblox_place_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/avatars#avatar_patch_v2_avatar"
)
def sync(
    *,
    client: AuthenticatedClient,
    body: RobloxApiAvatarModelsUpdateAvatarRequestModel | RobloxApiAvatarModelsUpdateAvatarRequestModel | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsUpdateAvatarResponseModel | None:
    """Sets the avatar to the incoming avatar using field masks.

     Only allows items that you own, are not expired, and are wearable asset types.
    Any assets being worn before this method is called are automatically removed.

    Please use PATCH v4/avatar

    Args:
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsUpdateAvatarRequestModel): A model containing details about an
            avatar update request.
        body (RobloxApiAvatarModelsUpdateAvatarRequestModel): A model containing details about an
            avatar update request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsUpdateAvatarResponseModel
    """

    return sync_detailed(
        client=client,
        body=body,
        roblox_place_id=roblox_place_id,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/avatars#avatar_patch_v2_avatar"
)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxApiAvatarModelsUpdateAvatarRequestModel | RobloxApiAvatarModelsUpdateAvatarRequestModel | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsUpdateAvatarResponseModel]:
    """Sets the avatar to the incoming avatar using field masks.

     Only allows items that you own, are not expired, and are wearable asset types.
    Any assets being worn before this method is called are automatically removed.

    Please use PATCH v4/avatar

    Args:
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsUpdateAvatarRequestModel): A model containing details about an
            avatar update request.
        body (RobloxApiAvatarModelsUpdateAvatarRequestModel): A model containing details about an
            avatar update request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsUpdateAvatarResponseModel]
    """

    kwargs = _get_kwargs(
        body=body,
        roblox_place_id=roblox_place_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/avatars#avatar_patch_v2_avatar"
)
async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxApiAvatarModelsUpdateAvatarRequestModel | RobloxApiAvatarModelsUpdateAvatarRequestModel | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsUpdateAvatarResponseModel | None:
    """Sets the avatar to the incoming avatar using field masks.

     Only allows items that you own, are not expired, and are wearable asset types.
    Any assets being worn before this method is called are automatically removed.

    Please use PATCH v4/avatar

    Args:
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsUpdateAvatarRequestModel): A model containing details about an
            avatar update request.
        body (RobloxApiAvatarModelsUpdateAvatarRequestModel): A model containing details about an
            avatar update request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsUpdateAvatarResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            roblox_place_id=roblox_place_id,
        )
    ).parsed
