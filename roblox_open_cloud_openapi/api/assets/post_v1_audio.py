from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_publish_api_publish_audio_response import RobloxPublishApiPublishAudioResponse
from ...models.roblox_publish_api_upload_audio_request import RobloxPublishApiUploadAudioRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RobloxPublishApiUploadAudioRequest | RobloxPublishApiUploadAudioRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://publish.roblox.com/v1/audio",
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "post_v1_audio",
    }

    if isinstance(body, RobloxPublishApiUploadAudioRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxPublishApiUploadAudioRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxPublishApiPublishAudioResponse | None:
    if response.status_code == 200:
        response_200 = RobloxPublishApiPublishAudioResponse.from_dict(response.json())

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
) -> Response[Any | RobloxPublishApiPublishAudioResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxPublishApiUploadAudioRequest | RobloxPublishApiUploadAudioRequest | Unset = UNSET,
) -> Response[Any | RobloxPublishApiPublishAudioResponse]:
    """Published an audio file and returns the new asset info.

    Args:
        body (RobloxPublishApiUploadAudioRequest): A request model for uploading an audio file.
        body (RobloxPublishApiUploadAudioRequest): A request model for uploading an audio file.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxPublishApiPublishAudioResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RobloxPublishApiUploadAudioRequest | RobloxPublishApiUploadAudioRequest | Unset = UNSET,
) -> Any | RobloxPublishApiPublishAudioResponse | None:
    """Published an audio file and returns the new asset info.

    Args:
        body (RobloxPublishApiUploadAudioRequest): A request model for uploading an audio file.
        body (RobloxPublishApiUploadAudioRequest): A request model for uploading an audio file.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxPublishApiPublishAudioResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxPublishApiUploadAudioRequest | RobloxPublishApiUploadAudioRequest | Unset = UNSET,
) -> Response[Any | RobloxPublishApiPublishAudioResponse]:
    """Published an audio file and returns the new asset info.

    Args:
        body (RobloxPublishApiUploadAudioRequest): A request model for uploading an audio file.
        body (RobloxPublishApiUploadAudioRequest): A request model for uploading an audio file.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxPublishApiPublishAudioResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxPublishApiUploadAudioRequest | RobloxPublishApiUploadAudioRequest | Unset = UNSET,
) -> Any | RobloxPublishApiPublishAudioResponse | None:
    """Published an audio file and returns the new asset info.

    Args:
        body (RobloxPublishApiUploadAudioRequest): A request model for uploading an audio file.
        body (RobloxPublishApiUploadAudioRequest): A request model for uploading an audio file.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxPublishApiPublishAudioResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
