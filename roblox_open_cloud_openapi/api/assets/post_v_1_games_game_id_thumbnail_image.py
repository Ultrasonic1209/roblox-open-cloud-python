from http import HTTPStatus
from typing import TYPE_CHECKING, Any, cast
from urllib.parse import quote

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
{'x-roblox-recommended-alternatives': [{'url': 'https://apis.roblox.com/assets/v1/assets', 'httpMethod': 'POST', 'description': 'First step: create or upload the image asset.'}, {'url': 'https://apis.roblox.com/assets/v1/assets/{assetId}?updateMask=icon', 'httpMethod': 'PATCH', 'description': 'Second step: set the created asset as the experience icon.'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""

import sys

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.post_v1_games_game_id_thumbnail_image_body import PostV1GamesGameIdThumbnailImageBody
from ...models.roblox_publish_api_upload_response import RobloxPublishApiUploadResponse
from ...types import Unset


def _get_kwargs(
    game_id: int,
    *,
    body: PostV1GamesGameIdThumbnailImageBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://publish.roblox.com/v1/games/{game_id}/thumbnail/image".format(
            game_id=quote(str(game_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxPublishApiUploadResponse | None:
    if response.status_code == 200:
        response_200 = RobloxPublishApiUploadResponse.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxPublishApiUploadResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#publish_post_v1_games__gameId__thumbnail_image"
)
def sync_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
    body: PostV1GamesGameIdThumbnailImageBody | Unset = UNSET,
) -> Response[Any | RobloxPublishApiUploadResponse]:
    """Uploads a game thumbnail.

    Args:
        game_id (int):
        body (PostV1GamesGameIdThumbnailImageBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxPublishApiUploadResponse]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#publish_post_v1_games__gameId__thumbnail_image"
)
def sync(
    game_id: int,
    *,
    client: AuthenticatedClient,
    body: PostV1GamesGameIdThumbnailImageBody | Unset = UNSET,
) -> Any | RobloxPublishApiUploadResponse | None:
    """Uploads a game thumbnail.

    Args:
        game_id (int):
        body (PostV1GamesGameIdThumbnailImageBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxPublishApiUploadResponse
    """

    return sync_detailed(
        game_id=game_id,
        client=client,
        body=body,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#publish_post_v1_games__gameId__thumbnail_image"
)
async def asyncio_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
    body: PostV1GamesGameIdThumbnailImageBody | Unset = UNSET,
) -> Response[Any | RobloxPublishApiUploadResponse]:
    """Uploads a game thumbnail.

    Args:
        game_id (int):
        body (PostV1GamesGameIdThumbnailImageBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxPublishApiUploadResponse]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#publish_post_v1_games__gameId__thumbnail_image"
)
async def asyncio(
    game_id: int,
    *,
    client: AuthenticatedClient,
    body: PostV1GamesGameIdThumbnailImageBody | Unset = UNSET,
) -> Any | RobloxPublishApiUploadResponse | None:
    """Uploads a game thumbnail.

    Args:
        game_id (int):
        body (PostV1GamesGameIdThumbnailImageBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxPublishApiUploadResponse
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            client=client,
            body=body,
        )
    ).parsed
