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
{'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 600}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 600}}, 'x-roblox-scopes': [{'name': 'ad.campaign:read'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.creative import Creative
from ...models.error_envelope import ErrorEnvelope
from ...types import Unset


def _get_kwargs(
    id: str,
    *,
    group_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["groupId"] = group_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ads-management/v1/creatives/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Creative | ErrorEnvelope | None:
    if response.status_code == 200:
        response_200 = Creative.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ErrorEnvelope.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ErrorEnvelope.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Creative | ErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    group_id: str | Unset = UNSET,
) -> Response[Creative | ErrorEnvelope]:
    """Get a creative

     Returns the Roblox asset registered in the selected ads account. The path id is Creative.assetId, a
    decimal Roblox asset ID, not Creative.id (the library registration UUID). For example, assetId
    "1234567890" uses /creatives/1234567890. A registration UUID returns 404. groupId selects the group
    ads account; absent groupId selects the personal ads account. The caller needs group advertising
    permission. Unknown and inaccessible creatives return the same 404.

    Args:
        id (str):
        group_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Creative | ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        group_id=group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    group_id: str | Unset = UNSET,
) -> Creative | ErrorEnvelope | None:
    """Get a creative

     Returns the Roblox asset registered in the selected ads account. The path id is Creative.assetId, a
    decimal Roblox asset ID, not Creative.id (the library registration UUID). For example, assetId
    "1234567890" uses /creatives/1234567890. A registration UUID returns 404. groupId selects the group
    ads account; absent groupId selects the personal ads account. The caller needs group advertising
    permission. Unknown and inaccessible creatives return the same 404.

    Args:
        id (str):
        group_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Creative | ErrorEnvelope
    """

    return sync_detailed(
        id=id,
        client=client,
        group_id=group_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    group_id: str | Unset = UNSET,
) -> Response[Creative | ErrorEnvelope]:
    """Get a creative

     Returns the Roblox asset registered in the selected ads account. The path id is Creative.assetId, a
    decimal Roblox asset ID, not Creative.id (the library registration UUID). For example, assetId
    "1234567890" uses /creatives/1234567890. A registration UUID returns 404. groupId selects the group
    ads account; absent groupId selects the personal ads account. The caller needs group advertising
    permission. Unknown and inaccessible creatives return the same 404.

    Args:
        id (str):
        group_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Creative | ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        group_id=group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    group_id: str | Unset = UNSET,
) -> Creative | ErrorEnvelope | None:
    """Get a creative

     Returns the Roblox asset registered in the selected ads account. The path id is Creative.assetId, a
    decimal Roblox asset ID, not Creative.id (the library registration UUID). For example, assetId
    "1234567890" uses /creatives/1234567890. A registration UUID returns 404. groupId selects the group
    ads account; absent groupId selects the personal ads account. The caller needs group advertising
    permission. Unknown and inaccessible creatives return the same 404.

    Args:
        id (str):
        group_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Creative | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            group_id=group_id,
        )
    ).parsed
