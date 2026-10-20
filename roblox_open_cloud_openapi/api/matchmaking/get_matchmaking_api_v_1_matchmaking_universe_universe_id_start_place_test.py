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


from ...models.test_start_place_override_response import TestStartPlaceOverrideResponse
from ...types import Unset


def _get_kwargs(
    universe_id: int,
    *,
    user_id: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["userId"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/matchmaking-api/v1/matchmaking/universe/{universe_id}/start-place/test".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TestStartPlaceOverrideResponse | None:
    if response.status_code == 200:
        response_200 = TestStartPlaceOverrideResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TestStartPlaceOverrideResponse]:
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
    user_id: int | Unset = UNSET,
) -> Response[TestStartPlaceOverrideResponse]:
    """Tests a user's saved start place in a universe against the place checks gamejoin makes.

    Args:
        universe_id (int):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TestStartPlaceOverrideResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    user_id: int | Unset = UNSET,
) -> TestStartPlaceOverrideResponse | None:
    """Tests a user's saved start place in a universe against the place checks gamejoin makes.

    Args:
        universe_id (int):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TestStartPlaceOverrideResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    user_id: int | Unset = UNSET,
) -> Response[TestStartPlaceOverrideResponse]:
    """Tests a user's saved start place in a universe against the place checks gamejoin makes.

    Args:
        universe_id (int):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TestStartPlaceOverrideResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    user_id: int | Unset = UNSET,
) -> TestStartPlaceOverrideResponse | None:
    """Tests a user's saved start place in a universe against the place checks gamejoin makes.

    Args:
        universe_id (int):
        user_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TestStartPlaceOverrideResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            user_id=user_id,
        )
    ).parsed
