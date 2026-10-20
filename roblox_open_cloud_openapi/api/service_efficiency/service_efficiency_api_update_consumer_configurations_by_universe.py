from http import HTTPStatus
from typing import TYPE_CHECKING, Any, cast
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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 5000}}, 'x-roblox-scopes': [{'name': 'extended-services:write', 'targetResourceSpecifier': 'universes'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.consumer_configuration_request import ConsumerConfigurationRequest
from ...models.consumer_configuration_response import ConsumerConfigurationResponse
from ...types import Unset


def _get_kwargs(
    universe_id: int,
    *,
    body: ConsumerConfigurationRequest
    | ConsumerConfigurationRequest
    | ConsumerConfigurationRequest
    | ConsumerConfigurationRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/service-efficiency-api/v1/configurations/universes/{universe_id}".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
    }

    if isinstance(body, ConsumerConfigurationRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, ConsumerConfigurationRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, ConsumerConfigurationRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, ConsumerConfigurationRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ConsumerConfigurationResponse | None:
    if response.status_code == 200:
        response_200 = ConsumerConfigurationResponse.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ConsumerConfigurationResponse]:
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
    body: ConsumerConfigurationRequest
    | ConsumerConfigurationRequest
    | ConsumerConfigurationRequest
    | ConsumerConfigurationRequest
    | Unset = UNSET,
) -> Response[Any | ConsumerConfigurationResponse]:
    """Operation to Update ConsumerConfiguration for a universe.

    Args:
        universe_id (int):
        body (ConsumerConfigurationRequest | Unset): Request for updating consumer configuration.
        body (ConsumerConfigurationRequest | Unset): Request for updating consumer configuration.
        body (ConsumerConfigurationRequest | Unset): Request for updating consumer configuration.
        body (ConsumerConfigurationRequest | Unset): Request for updating consumer configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConsumerConfigurationResponse]
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
    body: ConsumerConfigurationRequest
    | ConsumerConfigurationRequest
    | ConsumerConfigurationRequest
    | ConsumerConfigurationRequest
    | Unset = UNSET,
) -> Any | ConsumerConfigurationResponse | None:
    """Operation to Update ConsumerConfiguration for a universe.

    Args:
        universe_id (int):
        body (ConsumerConfigurationRequest | Unset): Request for updating consumer configuration.
        body (ConsumerConfigurationRequest | Unset): Request for updating consumer configuration.
        body (ConsumerConfigurationRequest | Unset): Request for updating consumer configuration.
        body (ConsumerConfigurationRequest | Unset): Request for updating consumer configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConsumerConfigurationResponse
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
    body: ConsumerConfigurationRequest
    | ConsumerConfigurationRequest
    | ConsumerConfigurationRequest
    | ConsumerConfigurationRequest
    | Unset = UNSET,
) -> Response[Any | ConsumerConfigurationResponse]:
    """Operation to Update ConsumerConfiguration for a universe.

    Args:
        universe_id (int):
        body (ConsumerConfigurationRequest | Unset): Request for updating consumer configuration.
        body (ConsumerConfigurationRequest | Unset): Request for updating consumer configuration.
        body (ConsumerConfigurationRequest | Unset): Request for updating consumer configuration.
        body (ConsumerConfigurationRequest | Unset): Request for updating consumer configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConsumerConfigurationResponse]
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
    body: ConsumerConfigurationRequest
    | ConsumerConfigurationRequest
    | ConsumerConfigurationRequest
    | ConsumerConfigurationRequest
    | Unset = UNSET,
) -> Any | ConsumerConfigurationResponse | None:
    """Operation to Update ConsumerConfiguration for a universe.

    Args:
        universe_id (int):
        body (ConsumerConfigurationRequest | Unset): Request for updating consumer configuration.
        body (ConsumerConfigurationRequest | Unset): Request for updating consumer configuration.
        body (ConsumerConfigurationRequest | Unset): Request for updating consumer configuration.
        body (ConsumerConfigurationRequest | Unset): Request for updating consumer configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConsumerConfigurationResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
