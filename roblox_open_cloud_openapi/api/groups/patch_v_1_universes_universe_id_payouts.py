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
{'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.organizations_service_api_error_response import OrganizationsServiceApiErrorResponse
from ...models.public_all_group_universe_payouts_response_model import PublicAllGroupUniversePayoutsResponseModel
from ...models.public_update_universe_recurring_payouts_request_model import (
    PublicUpdateUniverseRecurringPayoutsRequestModel,
)


def _get_kwargs(
    universe_id: int,
    *,
    body: PublicUpdateUniverseRecurringPayoutsRequestModel
    | PublicUpdateUniverseRecurringPayoutsRequestModel
    | PublicUpdateUniverseRecurringPayoutsRequestModel
    | PublicUpdateUniverseRecurringPayoutsRequestModel
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "https://groups.roblox.com/v1/universes/{universe_id}/payouts".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
    }

    if isinstance(body, PublicUpdateUniverseRecurringPayoutsRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, PublicUpdateUniverseRecurringPayoutsRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PublicUpdateUniverseRecurringPayoutsRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, PublicUpdateUniverseRecurringPayoutsRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OrganizationsServiceApiErrorResponse | PublicAllGroupUniversePayoutsResponseModel | None:
    if response.status_code == 200:
        response_200 = PublicAllGroupUniversePayoutsResponseModel.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = OrganizationsServiceApiErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = OrganizationsServiceApiErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OrganizationsServiceApiErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = OrganizationsServiceApiErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OrganizationsServiceApiErrorResponse | PublicAllGroupUniversePayoutsResponseModel]:
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
    body: PublicUpdateUniverseRecurringPayoutsRequestModel
    | PublicUpdateUniverseRecurringPayoutsRequestModel
    | PublicUpdateUniverseRecurringPayoutsRequestModel
    | PublicUpdateUniverseRecurringPayoutsRequestModel
    | Unset = UNSET,
) -> Response[OrganizationsServiceApiErrorResponse | PublicAllGroupUniversePayoutsResponseModel]:
    """Updates recurring payouts for a group-owned universe.

    Args:
        universe_id (int):
        body (PublicUpdateUniverseRecurringPayoutsRequestModel): Request for updating recurring
            payouts through the public groups API.
        body (PublicUpdateUniverseRecurringPayoutsRequestModel): Request for updating recurring
            payouts through the public groups API.
        body (PublicUpdateUniverseRecurringPayoutsRequestModel): Request for updating recurring
            payouts through the public groups API.
        body (PublicUpdateUniverseRecurringPayoutsRequestModel): Request for updating recurring
            payouts through the public groups API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationsServiceApiErrorResponse | PublicAllGroupUniversePayoutsResponseModel]
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
    body: PublicUpdateUniverseRecurringPayoutsRequestModel
    | PublicUpdateUniverseRecurringPayoutsRequestModel
    | PublicUpdateUniverseRecurringPayoutsRequestModel
    | PublicUpdateUniverseRecurringPayoutsRequestModel
    | Unset = UNSET,
) -> OrganizationsServiceApiErrorResponse | PublicAllGroupUniversePayoutsResponseModel | None:
    """Updates recurring payouts for a group-owned universe.

    Args:
        universe_id (int):
        body (PublicUpdateUniverseRecurringPayoutsRequestModel): Request for updating recurring
            payouts through the public groups API.
        body (PublicUpdateUniverseRecurringPayoutsRequestModel): Request for updating recurring
            payouts through the public groups API.
        body (PublicUpdateUniverseRecurringPayoutsRequestModel): Request for updating recurring
            payouts through the public groups API.
        body (PublicUpdateUniverseRecurringPayoutsRequestModel): Request for updating recurring
            payouts through the public groups API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrganizationsServiceApiErrorResponse | PublicAllGroupUniversePayoutsResponseModel
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
    body: PublicUpdateUniverseRecurringPayoutsRequestModel
    | PublicUpdateUniverseRecurringPayoutsRequestModel
    | PublicUpdateUniverseRecurringPayoutsRequestModel
    | PublicUpdateUniverseRecurringPayoutsRequestModel
    | Unset = UNSET,
) -> Response[OrganizationsServiceApiErrorResponse | PublicAllGroupUniversePayoutsResponseModel]:
    """Updates recurring payouts for a group-owned universe.

    Args:
        universe_id (int):
        body (PublicUpdateUniverseRecurringPayoutsRequestModel): Request for updating recurring
            payouts through the public groups API.
        body (PublicUpdateUniverseRecurringPayoutsRequestModel): Request for updating recurring
            payouts through the public groups API.
        body (PublicUpdateUniverseRecurringPayoutsRequestModel): Request for updating recurring
            payouts through the public groups API.
        body (PublicUpdateUniverseRecurringPayoutsRequestModel): Request for updating recurring
            payouts through the public groups API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationsServiceApiErrorResponse | PublicAllGroupUniversePayoutsResponseModel]
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
    body: PublicUpdateUniverseRecurringPayoutsRequestModel
    | PublicUpdateUniverseRecurringPayoutsRequestModel
    | PublicUpdateUniverseRecurringPayoutsRequestModel
    | PublicUpdateUniverseRecurringPayoutsRequestModel
    | Unset = UNSET,
) -> OrganizationsServiceApiErrorResponse | PublicAllGroupUniversePayoutsResponseModel | None:
    """Updates recurring payouts for a group-owned universe.

    Args:
        universe_id (int):
        body (PublicUpdateUniverseRecurringPayoutsRequestModel): Request for updating recurring
            payouts through the public groups API.
        body (PublicUpdateUniverseRecurringPayoutsRequestModel): Request for updating recurring
            payouts through the public groups API.
        body (PublicUpdateUniverseRecurringPayoutsRequestModel): Request for updating recurring
            payouts through the public groups API.
        body (PublicUpdateUniverseRecurringPayoutsRequestModel): Request for updating recurring
            payouts through the public groups API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrganizationsServiceApiErrorResponse | PublicAllGroupUniversePayoutsResponseModel
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
