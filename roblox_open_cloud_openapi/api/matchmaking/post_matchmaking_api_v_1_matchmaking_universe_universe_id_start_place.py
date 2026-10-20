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
{'x-roblox-stability': 'BETA', 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.set_start_place_override_request_body import SetStartPlaceOverrideRequestBody
from ...models.set_start_place_override_response import SetStartPlaceOverrideResponse
from ...types import Unset


def _get_kwargs(
    universe_id: int,
    *,
    body: SetStartPlaceOverrideRequestBody
    | SetStartPlaceOverrideRequestBody
    | SetStartPlaceOverrideRequestBody
    | SetStartPlaceOverrideRequestBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/matchmaking-api/v1/matchmaking/universe/{universe_id}/start-place".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
    }

    if isinstance(body, SetStartPlaceOverrideRequestBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, SetStartPlaceOverrideRequestBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, SetStartPlaceOverrideRequestBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, SetStartPlaceOverrideRequestBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SetStartPlaceOverrideResponse | None:
    if response.status_code == 200:
        response_200 = SetStartPlaceOverrideResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SetStartPlaceOverrideResponse]:
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
    body: SetStartPlaceOverrideRequestBody
    | SetStartPlaceOverrideRequestBody
    | SetStartPlaceOverrideRequestBody
    | SetStartPlaceOverrideRequestBody
    | Unset = UNSET,
) -> Response[SetStartPlaceOverrideResponse]:
    """Sets (creates or updates) the start place override for a universe.

    Args:
        universe_id (int):
        body (SetStartPlaceOverrideRequestBody | Unset): Request body for setting the start place
            override for a universe. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideRequestBody | Unset): Request body for setting the start place
            override for a universe. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideRequestBody | Unset): Request body for setting the start place
            override for a universe. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideRequestBody | Unset): Request body for setting the start place
            override for a universe. The universe is
            identified by the route, so it is not part of the body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetStartPlaceOverrideResponse]
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
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: SetStartPlaceOverrideRequestBody
    | SetStartPlaceOverrideRequestBody
    | SetStartPlaceOverrideRequestBody
    | SetStartPlaceOverrideRequestBody
    | Unset = UNSET,
) -> SetStartPlaceOverrideResponse | None:
    """Sets (creates or updates) the start place override for a universe.

    Args:
        universe_id (int):
        body (SetStartPlaceOverrideRequestBody | Unset): Request body for setting the start place
            override for a universe. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideRequestBody | Unset): Request body for setting the start place
            override for a universe. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideRequestBody | Unset): Request body for setting the start place
            override for a universe. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideRequestBody | Unset): Request body for setting the start place
            override for a universe. The universe is
            identified by the route, so it is not part of the body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetStartPlaceOverrideResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: SetStartPlaceOverrideRequestBody
    | SetStartPlaceOverrideRequestBody
    | SetStartPlaceOverrideRequestBody
    | SetStartPlaceOverrideRequestBody
    | Unset = UNSET,
) -> Response[SetStartPlaceOverrideResponse]:
    """Sets (creates or updates) the start place override for a universe.

    Args:
        universe_id (int):
        body (SetStartPlaceOverrideRequestBody | Unset): Request body for setting the start place
            override for a universe. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideRequestBody | Unset): Request body for setting the start place
            override for a universe. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideRequestBody | Unset): Request body for setting the start place
            override for a universe. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideRequestBody | Unset): Request body for setting the start place
            override for a universe. The universe is
            identified by the route, so it is not part of the body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetStartPlaceOverrideResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: SetStartPlaceOverrideRequestBody
    | SetStartPlaceOverrideRequestBody
    | SetStartPlaceOverrideRequestBody
    | SetStartPlaceOverrideRequestBody
    | Unset = UNSET,
) -> SetStartPlaceOverrideResponse | None:
    """Sets (creates or updates) the start place override for a universe.

    Args:
        universe_id (int):
        body (SetStartPlaceOverrideRequestBody | Unset): Request body for setting the start place
            override for a universe. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideRequestBody | Unset): Request body for setting the start place
            override for a universe. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideRequestBody | Unset): Request body for setting the start place
            override for a universe. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideRequestBody | Unset): Request body for setting the start place
            override for a universe. The universe is
            identified by the route, so it is not part of the body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetStartPlaceOverrideResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
