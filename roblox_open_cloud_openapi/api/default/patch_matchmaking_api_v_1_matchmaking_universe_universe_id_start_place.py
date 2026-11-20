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


from ...models.set_start_place_override_enabled_request_body import SetStartPlaceOverrideEnabledRequestBody
from ...models.set_start_place_override_enabled_response import SetStartPlaceOverrideEnabledResponse
from ...types import Unset


def _get_kwargs(
    universe_id: int,
    *,
    body: SetStartPlaceOverrideEnabledRequestBody
    | SetStartPlaceOverrideEnabledRequestBody
    | SetStartPlaceOverrideEnabledRequestBody
    | SetStartPlaceOverrideEnabledRequestBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/matchmaking-api/v1/matchmaking/universe/{universe_id}/start-place".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
    }

    if isinstance(body, SetStartPlaceOverrideEnabledRequestBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, SetStartPlaceOverrideEnabledRequestBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, SetStartPlaceOverrideEnabledRequestBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, SetStartPlaceOverrideEnabledRequestBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SetStartPlaceOverrideEnabledResponse | None:
    if response.status_code == 200:
        response_200 = SetStartPlaceOverrideEnabledResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SetStartPlaceOverrideEnabledResponse]:
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
    body: SetStartPlaceOverrideEnabledRequestBody
    | SetStartPlaceOverrideEnabledRequestBody
    | SetStartPlaceOverrideEnabledRequestBody
    | SetStartPlaceOverrideEnabledRequestBody
    | Unset = UNSET,
) -> Response[SetStartPlaceOverrideEnabledResponse]:
    """Turns the start place override for a universe on or off. A new override starts turned off.

    Args:
        universe_id (int):
        body (SetStartPlaceOverrideEnabledRequestBody | Unset): Request body for turning a
            universe's start place override on or off. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideEnabledRequestBody | Unset): Request body for turning a
            universe's start place override on or off. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideEnabledRequestBody | Unset): Request body for turning a
            universe's start place override on or off. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideEnabledRequestBody | Unset): Request body for turning a
            universe's start place override on or off. The universe is
            identified by the route, so it is not part of the body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetStartPlaceOverrideEnabledResponse]
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
    body: SetStartPlaceOverrideEnabledRequestBody
    | SetStartPlaceOverrideEnabledRequestBody
    | SetStartPlaceOverrideEnabledRequestBody
    | SetStartPlaceOverrideEnabledRequestBody
    | Unset = UNSET,
) -> SetStartPlaceOverrideEnabledResponse | None:
    """Turns the start place override for a universe on or off. A new override starts turned off.

    Args:
        universe_id (int):
        body (SetStartPlaceOverrideEnabledRequestBody | Unset): Request body for turning a
            universe's start place override on or off. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideEnabledRequestBody | Unset): Request body for turning a
            universe's start place override on or off. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideEnabledRequestBody | Unset): Request body for turning a
            universe's start place override on or off. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideEnabledRequestBody | Unset): Request body for turning a
            universe's start place override on or off. The universe is
            identified by the route, so it is not part of the body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetStartPlaceOverrideEnabledResponse
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
    body: SetStartPlaceOverrideEnabledRequestBody
    | SetStartPlaceOverrideEnabledRequestBody
    | SetStartPlaceOverrideEnabledRequestBody
    | SetStartPlaceOverrideEnabledRequestBody
    | Unset = UNSET,
) -> Response[SetStartPlaceOverrideEnabledResponse]:
    """Turns the start place override for a universe on or off. A new override starts turned off.

    Args:
        universe_id (int):
        body (SetStartPlaceOverrideEnabledRequestBody | Unset): Request body for turning a
            universe's start place override on or off. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideEnabledRequestBody | Unset): Request body for turning a
            universe's start place override on or off. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideEnabledRequestBody | Unset): Request body for turning a
            universe's start place override on or off. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideEnabledRequestBody | Unset): Request body for turning a
            universe's start place override on or off. The universe is
            identified by the route, so it is not part of the body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetStartPlaceOverrideEnabledResponse]
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
    body: SetStartPlaceOverrideEnabledRequestBody
    | SetStartPlaceOverrideEnabledRequestBody
    | SetStartPlaceOverrideEnabledRequestBody
    | SetStartPlaceOverrideEnabledRequestBody
    | Unset = UNSET,
) -> SetStartPlaceOverrideEnabledResponse | None:
    """Turns the start place override for a universe on or off. A new override starts turned off.

    Args:
        universe_id (int):
        body (SetStartPlaceOverrideEnabledRequestBody | Unset): Request body for turning a
            universe's start place override on or off. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideEnabledRequestBody | Unset): Request body for turning a
            universe's start place override on or off. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideEnabledRequestBody | Unset): Request body for turning a
            universe's start place override on or off. The universe is
            identified by the route, so it is not part of the body.
        body (SetStartPlaceOverrideEnabledRequestBody | Unset): Request body for turning a
            universe's start place override on or off. The universe is
            identified by the route, so it is not part of the body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetStartPlaceOverrideEnabledResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
