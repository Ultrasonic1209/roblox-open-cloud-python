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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 60}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 60}}, 'x-roblox-scopes': [{'name': 'universe.analytics:read', 'targetResourceSpecifier': 'universe'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


import datetime

from ...models.action_result import ActionResult
from ...models.error_log_detail_response import ErrorLogDetailResponse
from ...types import Unset


def _get_kwargs(
    universe_id: int,
    *,
    message_hash_ids: list[str] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    place_id: int | Unset = UNSET,
    place_versions: list[int] | Unset = UNSET,
    first_seen_place_version: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_message_hash_ids: list[str] | Unset = UNSET
    if not isinstance(message_hash_ids, Unset):
        json_message_hash_ids = message_hash_ids

    params["messageHashIds"] = json_message_hash_ids

    params["keyword"] = keyword

    json_start_time: str | Unset = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time: str | Unset = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    params["placeId"] = place_id

    json_place_versions: list[int] | Unset = UNSET
    if not isinstance(place_versions, Unset):
        json_place_versions = place_versions

    params["placeVersions"] = json_place_versions

    params["firstSeenPlaceVersion"] = first_seen_place_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/universe-performance-raqi/v1/events/logging/universe/{universe_id}/log-details".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActionResult | ErrorLogDetailResponse | None:
    if response.status_code == 200:
        response_200 = ErrorLogDetailResponse.from_dict(response.text)

        return response_200

    if response.status_code == 400:
        response_400 = ActionResult.from_dict(response.text)

        return response_400

    if response.status_code == 401:
        response_401 = ActionResult.from_dict(response.text)

        return response_401

    if response.status_code == 403:
        response_403 = ActionResult.from_dict(response.text)

        return response_403

    if response.status_code == 500:
        response_500 = ActionResult.from_dict(response.text)

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ActionResult | ErrorLogDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    message_hash_ids: list[str] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    place_id: int | Unset = UNSET,
    place_versions: list[int] | Unset = UNSET,
    first_seen_place_version: int | Unset = UNSET,
) -> Response[ActionResult | ErrorLogDetailResponse]:
    """Get logs based on message hash ids, keywords, placeVersions, start/end time.

    Args:
        universe_id (int):
        message_hash_ids (list[str] | Unset):
        keyword (str | Unset):
        start_time (datetime.datetime | Unset):
        end_time (datetime.datetime | Unset):
        place_id (int | Unset):
        place_versions (list[int] | Unset):
        first_seen_place_version (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionResult | ErrorLogDetailResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        message_hash_ids=message_hash_ids,
        keyword=keyword,
        start_time=start_time,
        end_time=end_time,
        place_id=place_id,
        place_versions=place_versions,
        first_seen_place_version=first_seen_place_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    message_hash_ids: list[str] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    place_id: int | Unset = UNSET,
    place_versions: list[int] | Unset = UNSET,
    first_seen_place_version: int | Unset = UNSET,
) -> ActionResult | ErrorLogDetailResponse | None:
    """Get logs based on message hash ids, keywords, placeVersions, start/end time.

    Args:
        universe_id (int):
        message_hash_ids (list[str] | Unset):
        keyword (str | Unset):
        start_time (datetime.datetime | Unset):
        end_time (datetime.datetime | Unset):
        place_id (int | Unset):
        place_versions (list[int] | Unset):
        first_seen_place_version (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionResult | ErrorLogDetailResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        message_hash_ids=message_hash_ids,
        keyword=keyword,
        start_time=start_time,
        end_time=end_time,
        place_id=place_id,
        place_versions=place_versions,
        first_seen_place_version=first_seen_place_version,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    message_hash_ids: list[str] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    place_id: int | Unset = UNSET,
    place_versions: list[int] | Unset = UNSET,
    first_seen_place_version: int | Unset = UNSET,
) -> Response[ActionResult | ErrorLogDetailResponse]:
    """Get logs based on message hash ids, keywords, placeVersions, start/end time.

    Args:
        universe_id (int):
        message_hash_ids (list[str] | Unset):
        keyword (str | Unset):
        start_time (datetime.datetime | Unset):
        end_time (datetime.datetime | Unset):
        place_id (int | Unset):
        place_versions (list[int] | Unset):
        first_seen_place_version (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionResult | ErrorLogDetailResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        message_hash_ids=message_hash_ids,
        keyword=keyword,
        start_time=start_time,
        end_time=end_time,
        place_id=place_id,
        place_versions=place_versions,
        first_seen_place_version=first_seen_place_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    message_hash_ids: list[str] | Unset = UNSET,
    keyword: str | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    place_id: int | Unset = UNSET,
    place_versions: list[int] | Unset = UNSET,
    first_seen_place_version: int | Unset = UNSET,
) -> ActionResult | ErrorLogDetailResponse | None:
    """Get logs based on message hash ids, keywords, placeVersions, start/end time.

    Args:
        universe_id (int):
        message_hash_ids (list[str] | Unset):
        keyword (str | Unset):
        start_time (datetime.datetime | Unset):
        end_time (datetime.datetime | Unset):
        place_id (int | Unset):
        place_versions (list[int] | Unset):
        first_seen_place_version (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionResult | ErrorLogDetailResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            message_hash_ids=message_hash_ids,
            keyword=keyword,
            start_time=start_time,
            end_time=end_time,
            place_id=place_id,
            place_versions=place_versions,
            first_seen_place_version=first_seen_place_version,
        )
    ).parsed
