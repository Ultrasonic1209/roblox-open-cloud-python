import sys
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_api_avatar_models_outfit_update_model_v2 import RobloxApiAvatarModelsOutfitUpdateModelV2
from ...models.roblox_web_web_api_api_empty_response_model import RobloxWebWebAPIApiEmptyResponseModel
from ...types import Unset


def _get_kwargs(
    *,
    body: RobloxApiAvatarModelsOutfitUpdateModelV2 | RobloxApiAvatarModelsOutfitUpdateModelV2 | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(roblox_place_id, Unset):
        headers["Roblox-Place-Id"] = str(roblox_place_id)

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/outfits/create",
    }

    if isinstance(body, RobloxApiAvatarModelsOutfitUpdateModelV2):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxApiAvatarModelsOutfitUpdateModelV2):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIApiEmptyResponseModel.from_dict(response.json())

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
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/avatars#avatar_post_v2_outfits_create"
)
def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxApiAvatarModelsOutfitUpdateModelV2 | RobloxApiAvatarModelsOutfitUpdateModelV2 | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Creates a new outfit.

     Fails if any of the assetIds are not owned by the user, or not wearable types.
    The name property of the request is optional as one will be auto-generated when the request has a
    null name.

    please use v3/outfits/create

    Args:
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsOutfitUpdateModelV2): A model containing details needed to
            update or create an outfit
        body (RobloxApiAvatarModelsOutfitUpdateModelV2): A model containing details needed to
            update or create an outfit

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        body=body,
        roblox_place_id=roblox_place_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/avatars#avatar_post_v2_outfits_create"
)
def sync(
    *,
    client: AuthenticatedClient,
    body: RobloxApiAvatarModelsOutfitUpdateModelV2 | RobloxApiAvatarModelsOutfitUpdateModelV2 | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Creates a new outfit.

     Fails if any of the assetIds are not owned by the user, or not wearable types.
    The name property of the request is optional as one will be auto-generated when the request has a
    null name.

    please use v3/outfits/create

    Args:
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsOutfitUpdateModelV2): A model containing details needed to
            update or create an outfit
        body (RobloxApiAvatarModelsOutfitUpdateModelV2): A model containing details needed to
            update or create an outfit

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return sync_detailed(
        client=client,
        body=body,
        roblox_place_id=roblox_place_id,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/avatars#avatar_post_v2_outfits_create"
)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxApiAvatarModelsOutfitUpdateModelV2 | RobloxApiAvatarModelsOutfitUpdateModelV2 | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Creates a new outfit.

     Fails if any of the assetIds are not owned by the user, or not wearable types.
    The name property of the request is optional as one will be auto-generated when the request has a
    null name.

    please use v3/outfits/create

    Args:
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsOutfitUpdateModelV2): A model containing details needed to
            update or create an outfit
        body (RobloxApiAvatarModelsOutfitUpdateModelV2): A model containing details needed to
            update or create an outfit

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        body=body,
        roblox_place_id=roblox_place_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/avatars#avatar_post_v2_outfits_create"
)
async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxApiAvatarModelsOutfitUpdateModelV2 | RobloxApiAvatarModelsOutfitUpdateModelV2 | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Creates a new outfit.

     Fails if any of the assetIds are not owned by the user, or not wearable types.
    The name property of the request is optional as one will be auto-generated when the request has a
    null name.

    please use v3/outfits/create

    Args:
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsOutfitUpdateModelV2): A model containing details needed to
            update or create an outfit
        body (RobloxApiAvatarModelsOutfitUpdateModelV2): A model containing details needed to
            update or create an outfit

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            roblox_place_id=roblox_place_id,
        )
    ).parsed
