from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.translate_text_request import TranslateTextRequest
from ...models.translate_text_response import TranslateTextResponse
from ...types import Response


def _get_kwargs(
    universe_id: str,
    *,
    body: TranslateTextRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cloud/v2/universes/{universe_id}:translateText".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TranslateTextResponse | None:
    if response.status_code == 200:
        response_200 = TranslateTextResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TranslateTextResponse]:
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
    body: TranslateTextRequest,
) -> Response[TranslateTextResponse]:
    """Translate Text

     Translates the provided text from one language to another.

    Args:
        universe_id (str):
        body (TranslateTextRequest): Contains the text to be translated, the source language
            (optional), and a
            list of target languages for translation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TranslateTextResponse]
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
    body: TranslateTextRequest,
) -> TranslateTextResponse | None:
    """Translate Text

     Translates the provided text from one language to another.

    Args:
        universe_id (str):
        body (TranslateTextRequest): Contains the text to be translated, the source language
            (optional), and a
            list of target languages for translation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TranslateTextResponse
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
    body: TranslateTextRequest,
) -> Response[TranslateTextResponse]:
    """Translate Text

     Translates the provided text from one language to another.

    Args:
        universe_id (str):
        body (TranslateTextRequest): Contains the text to be translated, the source language
            (optional), and a
            list of target languages for translation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TranslateTextResponse]
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
    body: TranslateTextRequest,
) -> TranslateTextResponse | None:
    """Translate Text

     Translates the provided text from one language to another.

    Args:
        universe_id (str):
        body (TranslateTextRequest): Contains the text to be translated, the source language
            (optional), and a
            list of target languages for translation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TranslateTextResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
