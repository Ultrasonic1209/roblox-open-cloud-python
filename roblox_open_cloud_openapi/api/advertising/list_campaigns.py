from http import HTTPStatus
from typing import TYPE_CHECKING, Any

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


import datetime

from ...models.error_envelope import ErrorEnvelope
from ...types import Unset


def _get_kwargs(
    *,
    group_id: str | Unset = UNSET,
    target_universe_ids: list[str] | Unset = UNSET,
    ended_after: datetime.datetime | Unset = UNSET,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["groupId"] = group_id

    json_target_universe_ids: list[str] | Unset = UNSET
    if not isinstance(target_universe_ids, Unset):
        json_target_universe_ids = target_universe_ids

    params["targetUniverseIds"] = json_target_universe_ids

    json_ended_after: str | Unset = UNSET
    if not isinstance(ended_after, Unset):
        json_ended_after = ended_after.isoformat()
    params["endedAfter"] = json_ended_after

    params["maxPageSize"] = max_page_size

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ads-management/v1/campaigns",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | None:
    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())

        return response_403

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    group_id: str | Unset = UNSET,
    target_universe_ids: list[str] | Unset = UNSET,
    ended_after: datetime.datetime | Unset = UNSET,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[ErrorEnvelope]:
    """List campaigns

     Lists the campaigns in the caller's billing account. Results are paginated with a cursor
    (pageToken); each page returns up to maxPageSize campaigns (default 50, max 100). groupId lists a
    group's billing account instead, and targetUniverseIds lists the campaigns of those experiences
    across billing accounts; campaigns that ended more than 730 days ago aren't included, and a page can
    hold fewer than maxPageSize campaigns while more remain. When nextPageToken is present, use it to
    continue even if the current page is empty.

    Args:
        group_id (str | Unset):
        target_universe_ids (list[str] | Unset):
        ended_after (datetime.datetime | Unset):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        target_universe_ids=target_universe_ids,
        ended_after=ended_after,
        max_page_size=max_page_size,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    group_id: str | Unset = UNSET,
    target_universe_ids: list[str] | Unset = UNSET,
    ended_after: datetime.datetime | Unset = UNSET,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> ErrorEnvelope | None:
    """List campaigns

     Lists the campaigns in the caller's billing account. Results are paginated with a cursor
    (pageToken); each page returns up to maxPageSize campaigns (default 50, max 100). groupId lists a
    group's billing account instead, and targetUniverseIds lists the campaigns of those experiences
    across billing accounts; campaigns that ended more than 730 days ago aren't included, and a page can
    hold fewer than maxPageSize campaigns while more remain. When nextPageToken is present, use it to
    continue even if the current page is empty.

    Args:
        group_id (str | Unset):
        target_universe_ids (list[str] | Unset):
        ended_after (datetime.datetime | Unset):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope
    """

    return sync_detailed(
        client=client,
        group_id=group_id,
        target_universe_ids=target_universe_ids,
        ended_after=ended_after,
        max_page_size=max_page_size,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    group_id: str | Unset = UNSET,
    target_universe_ids: list[str] | Unset = UNSET,
    ended_after: datetime.datetime | Unset = UNSET,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[ErrorEnvelope]:
    """List campaigns

     Lists the campaigns in the caller's billing account. Results are paginated with a cursor
    (pageToken); each page returns up to maxPageSize campaigns (default 50, max 100). groupId lists a
    group's billing account instead, and targetUniverseIds lists the campaigns of those experiences
    across billing accounts; campaigns that ended more than 730 days ago aren't included, and a page can
    hold fewer than maxPageSize campaigns while more remain. When nextPageToken is present, use it to
    continue even if the current page is empty.

    Args:
        group_id (str | Unset):
        target_universe_ids (list[str] | Unset):
        ended_after (datetime.datetime | Unset):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        target_universe_ids=target_universe_ids,
        ended_after=ended_after,
        max_page_size=max_page_size,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    group_id: str | Unset = UNSET,
    target_universe_ids: list[str] | Unset = UNSET,
    ended_after: datetime.datetime | Unset = UNSET,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> ErrorEnvelope | None:
    """List campaigns

     Lists the campaigns in the caller's billing account. Results are paginated with a cursor
    (pageToken); each page returns up to maxPageSize campaigns (default 50, max 100). groupId lists a
    group's billing account instead, and targetUniverseIds lists the campaigns of those experiences
    across billing accounts; campaigns that ended more than 730 days ago aren't included, and a page can
    hold fewer than maxPageSize campaigns while more remain. When nextPageToken is present, use it to
    continue even if the current page is empty.

    Args:
        group_id (str | Unset):
        target_universe_ids (list[str] | Unset):
        ended_after (datetime.datetime | Unset):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            group_id=group_id,
            target_universe_ids=target_universe_ids,
            ended_after=ended_after,
            max_page_size=max_page_size,
            page_token=page_token,
        )
    ).parsed
