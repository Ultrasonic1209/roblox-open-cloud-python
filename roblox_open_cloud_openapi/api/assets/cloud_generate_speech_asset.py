from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generate_speech_asset_request import GenerateSpeechAssetRequest
from ...models.operation import Operation
from ...types import Response


def _get_kwargs(
    universe_id: str,
    *,
    body: GenerateSpeechAssetRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cloud/v2/universes/{universe_id}:generateSpeechAsset".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Operation | None:
    if response.status_code == 200:
        response_200 = Operation.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Operation]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: GenerateSpeechAssetRequest,
) -> Response[Operation]:
    """Generate Speech Asset

     Generates an English speech audio asset from the specified text.

    This endpoint requires the `asset:read` and `asset:write` scopes in
    addition to the `universe:write` scope.

    The response returns an `Operation` object that must be prefixed with
    `/assets/v1`. For example, the URL to discover the result of the operation
    could be
    `https://apis.roblox.com/assets/v1/operations/8b42ef30-9c17-4526-b8cf-2ff0136ca94d`.

    Args:
        universe_id (str):
        body (GenerateSpeechAssetRequest): Specifies the text from which to generate speech and
            the voice style.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Operation]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: GenerateSpeechAssetRequest,
) -> Operation | None:
    """Generate Speech Asset

     Generates an English speech audio asset from the specified text.

    This endpoint requires the `asset:read` and `asset:write` scopes in
    addition to the `universe:write` scope.

    The response returns an `Operation` object that must be prefixed with
    `/assets/v1`. For example, the URL to discover the result of the operation
    could be
    `https://apis.roblox.com/assets/v1/operations/8b42ef30-9c17-4526-b8cf-2ff0136ca94d`.

    Args:
        universe_id (str):
        body (GenerateSpeechAssetRequest): Specifies the text from which to generate speech and
            the voice style.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Operation
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: GenerateSpeechAssetRequest,
) -> Response[Operation]:
    """Generate Speech Asset

     Generates an English speech audio asset from the specified text.

    This endpoint requires the `asset:read` and `asset:write` scopes in
    addition to the `universe:write` scope.

    The response returns an `Operation` object that must be prefixed with
    `/assets/v1`. For example, the URL to discover the result of the operation
    could be
    `https://apis.roblox.com/assets/v1/operations/8b42ef30-9c17-4526-b8cf-2ff0136ca94d`.

    Args:
        universe_id (str):
        body (GenerateSpeechAssetRequest): Specifies the text from which to generate speech and
            the voice style.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Operation]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: GenerateSpeechAssetRequest,
) -> Operation | None:
    """Generate Speech Asset

     Generates an English speech audio asset from the specified text.

    This endpoint requires the `asset:read` and `asset:write` scopes in
    addition to the `universe:write` scope.

    The response returns an `Operation` object that must be prefixed with
    `/assets/v1`. For example, the URL to discover the result of the operation
    could be
    `https://apis.roblox.com/assets/v1/operations/8b42ef30-9c17-4526-b8cf-2ff0136ca94d`.

    Args:
        universe_id (str):
        body (GenerateSpeechAssetRequest): Specifies the text from which to generate speech and
            the voice style.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Operation
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
