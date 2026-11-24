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
from ...types import Response

"""
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 60}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 60}}, 'x-roblox-scopes': [{'name': 'research.role:read'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.internal_controller_http_controller_error_body import InternalControllerHttpControllerErrorBody
from ...models.internal_controller_http_controller_researcher_roles_response import (
    InternalControllerHttpControllerResearcherRolesResponse,
)


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/vlop-api/v1/researcher/roles",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerResearcherRolesResponse | None:
    if response.status_code == 200:
        response_200 = InternalControllerHttpControllerResearcherRolesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = InternalControllerHttpControllerErrorBody.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = InternalControllerHttpControllerErrorBody.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = InternalControllerHttpControllerErrorBody.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = InternalControllerHttpControllerErrorBody.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerResearcherRolesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerResearcherRolesResponse]:
    """Get the caller's researcher-role grants

     Returns every DSA researcher-role grant held by the authenticated caller, newest first: the tier (QR
    qualified / VR vetted), its state (APPROVED or REVOKED), when it was granted, and when access ends.
    Holding no grants is not an error; the list is simply empty. Grants are written by Safety Platform
    decisions, so this is a read-only view of them. expires_at is the expiry recorded from the approval
    decision and is returned only for an APPROVED grant; it is absent for a REVOKED grant, whose access
    has already ended, and for a grant recorded with no expiry. An APPROVED grant whose expires_at has
    passed no longer authorizes the query API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerResearcherRolesResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerResearcherRolesResponse | None:
    """Get the caller's researcher-role grants

     Returns every DSA researcher-role grant held by the authenticated caller, newest first: the tier (QR
    qualified / VR vetted), its state (APPROVED or REVOKED), when it was granted, and when access ends.
    Holding no grants is not an error; the list is simply empty. Grants are written by Safety Platform
    decisions, so this is a read-only view of them. expires_at is the expiry recorded from the approval
    decision and is returned only for an APPROVED grant; it is absent for a REVOKED grant, whose access
    has already ended, and for a grant recorded with no expiry. An APPROVED grant whose expires_at has
    passed no longer authorizes the query API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerResearcherRolesResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerResearcherRolesResponse]:
    """Get the caller's researcher-role grants

     Returns every DSA researcher-role grant held by the authenticated caller, newest first: the tier (QR
    qualified / VR vetted), its state (APPROVED or REVOKED), when it was granted, and when access ends.
    Holding no grants is not an error; the list is simply empty. Grants are written by Safety Platform
    decisions, so this is a read-only view of them. expires_at is the expiry recorded from the approval
    decision and is returned only for an APPROVED grant; it is absent for a REVOKED grant, whose access
    has already ended, and for a grant recorded with no expiry. An APPROVED grant whose expires_at has
    passed no longer authorizes the query API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerResearcherRolesResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerResearcherRolesResponse | None:
    """Get the caller's researcher-role grants

     Returns every DSA researcher-role grant held by the authenticated caller, newest first: the tier (QR
    qualified / VR vetted), its state (APPROVED or REVOKED), when it was granted, and when access ends.
    Holding no grants is not an error; the list is simply empty. Grants are written by Safety Platform
    decisions, so this is a read-only view of them. expires_at is the expiry recorded from the approval
    decision and is returned only for an APPROVED grant; it is absent for a REVOKED grant, whose access
    has already ended, and for a grant recorded with no expiry. An APPROVED grant whose expires_at has
    passed no longer authorizes the query API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerResearcherRolesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
