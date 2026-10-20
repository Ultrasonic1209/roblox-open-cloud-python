from http import HTTPStatus
from typing import TYPE_CHECKING, Any
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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 60}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 60}}, 'x-roblox-scopes': [{'name': 'universe.analytics:write', 'targetResourceSpecifier': ''}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.reorder_universe_regex_http_request import ReorderUniverseRegexHttpRequest
from ...models.universe_regex_mutation_http_response import UniverseRegexMutationHttpResponse
from ...types import Unset


def _get_kwargs(
    id: int,
    *,
    body: ReorderUniverseRegexHttpRequest
    | ReorderUniverseRegexHttpRequest
    | ReorderUniverseRegexHttpRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/log-attribute-http-service/v1/universe-regexes/{id}/reorder".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, ReorderUniverseRegexHttpRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, ReorderUniverseRegexHttpRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, ReorderUniverseRegexHttpRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UniverseRegexMutationHttpResponse | None:
    if response.status_code == 200:
        response_200 = UniverseRegexMutationHttpResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UniverseRegexMutationHttpResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: ReorderUniverseRegexHttpRequest
    | ReorderUniverseRegexHttpRequest
    | ReorderUniverseRegexHttpRequest
    | Unset = UNSET,
) -> Response[UniverseRegexMutationHttpResponse]:
    """
    Args:
        id (int):
        body (ReorderUniverseRegexHttpRequest | Unset):
        body (ReorderUniverseRegexHttpRequest | Unset):
        body (ReorderUniverseRegexHttpRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UniverseRegexMutationHttpResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: ReorderUniverseRegexHttpRequest
    | ReorderUniverseRegexHttpRequest
    | ReorderUniverseRegexHttpRequest
    | Unset = UNSET,
) -> UniverseRegexMutationHttpResponse | None:
    """
    Args:
        id (int):
        body (ReorderUniverseRegexHttpRequest | Unset):
        body (ReorderUniverseRegexHttpRequest | Unset):
        body (ReorderUniverseRegexHttpRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UniverseRegexMutationHttpResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: ReorderUniverseRegexHttpRequest
    | ReorderUniverseRegexHttpRequest
    | ReorderUniverseRegexHttpRequest
    | Unset = UNSET,
) -> Response[UniverseRegexMutationHttpResponse]:
    """
    Args:
        id (int):
        body (ReorderUniverseRegexHttpRequest | Unset):
        body (ReorderUniverseRegexHttpRequest | Unset):
        body (ReorderUniverseRegexHttpRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UniverseRegexMutationHttpResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: ReorderUniverseRegexHttpRequest
    | ReorderUniverseRegexHttpRequest
    | ReorderUniverseRegexHttpRequest
    | Unset = UNSET,
) -> UniverseRegexMutationHttpResponse | None:
    """
    Args:
        id (int):
        body (ReorderUniverseRegexHttpRequest | Unset):
        body (ReorderUniverseRegexHttpRequest | Unset):
        body (ReorderUniverseRegexHttpRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UniverseRegexMutationHttpResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
