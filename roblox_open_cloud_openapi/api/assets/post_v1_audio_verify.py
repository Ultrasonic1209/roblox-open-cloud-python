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
{'x-roblox-recommended-alternatives': [{'url': 'https://apis.roblox.com/assets/v1/assets', 'httpMethod': 'POST', 'description': 'Validation occurs during asset creation; no separate verification call is needed.'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""

import sys

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_publish_api_verify_audio_request import RobloxPublishApiVerifyAudioRequest
from ...models.roblox_publish_api_verify_audio_response import RobloxPublishApiVerifyAudioResponse


def _get_kwargs(
    *,
    body: RobloxPublishApiVerifyAudioRequest | RobloxPublishApiVerifyAudioRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://publish.roblox.com/v1/audio/verify",
    }

    if isinstance(body, RobloxPublishApiVerifyAudioRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxPublishApiVerifyAudioRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxPublishApiVerifyAudioResponse | None:
    if response.status_code == 200:
        response_200 = RobloxPublishApiVerifyAudioResponse.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxPublishApiVerifyAudioResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#publish_post_v1_audio_verify"
)
def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxPublishApiVerifyAudioRequest | RobloxPublishApiVerifyAudioRequest | Unset = UNSET,
) -> Response[Any | RobloxPublishApiVerifyAudioResponse]:
    """Verifies an audio file and returns a product that you can purchase to publish the audio file.

    Args:
        body (RobloxPublishApiVerifyAudioRequest): Request model to publish an audio asset.
        body (RobloxPublishApiVerifyAudioRequest): Request model to publish an audio asset.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxPublishApiVerifyAudioResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#publish_post_v1_audio_verify"
)
def sync(
    *,
    client: AuthenticatedClient,
    body: RobloxPublishApiVerifyAudioRequest | RobloxPublishApiVerifyAudioRequest | Unset = UNSET,
) -> Any | RobloxPublishApiVerifyAudioResponse | None:
    """Verifies an audio file and returns a product that you can purchase to publish the audio file.

    Args:
        body (RobloxPublishApiVerifyAudioRequest): Request model to publish an audio asset.
        body (RobloxPublishApiVerifyAudioRequest): Request model to publish an audio asset.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxPublishApiVerifyAudioResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#publish_post_v1_audio_verify"
)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxPublishApiVerifyAudioRequest | RobloxPublishApiVerifyAudioRequest | Unset = UNSET,
) -> Response[Any | RobloxPublishApiVerifyAudioResponse]:
    """Verifies an audio file and returns a product that you can purchase to publish the audio file.

    Args:
        body (RobloxPublishApiVerifyAudioRequest): Request model to publish an audio asset.
        body (RobloxPublishApiVerifyAudioRequest): Request model to publish an audio asset.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxPublishApiVerifyAudioResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#publish_post_v1_audio_verify"
)
async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxPublishApiVerifyAudioRequest | RobloxPublishApiVerifyAudioRequest | Unset = UNSET,
) -> Any | RobloxPublishApiVerifyAudioResponse | None:
    """Verifies an audio file and returns a product that you can purchase to publish the audio file.

    Args:
        body (RobloxPublishApiVerifyAudioRequest): Request model to publish an audio asset.
        body (RobloxPublishApiVerifyAudioRequest): Request model to publish an audio asset.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxPublishApiVerifyAudioResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
