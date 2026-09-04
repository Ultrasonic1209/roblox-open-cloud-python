from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    identity_provider_id: int,
    *,
    body: Any | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://auth.roblox.com/v1/external/{identity_provider_id}/sso/oauth/callback".format(
            identity_provider_id=quote(str(identity_provider_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "post_v1_external_identityProviderId_sso_oauth_callback",
        },
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | None:
    if response.status_code == 302:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    identity_provider_id: int,
    *,
    client: AuthenticatedClient,
    body: Any | Unset = UNSET,
) -> Response[Any]:
    """OAuth callback for identity providers that POST the authorization code as form fields (Apple
    form_post).
    Extra form fields such as Apple's first-auth `id_token` and `user` are ignored;
    web login exchanges code via PKCE and does not treat a form id_token as proof.

    Args:
        identity_provider_id (int):
        body (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        identity_provider_id=identity_provider_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    identity_provider_id: int,
    *,
    client: AuthenticatedClient,
    body: Any | Unset = UNSET,
) -> Response[Any]:
    """OAuth callback for identity providers that POST the authorization code as form fields (Apple
    form_post).
    Extra form fields such as Apple's first-auth `id_token` and `user` are ignored;
    web login exchanges code via PKCE and does not treat a form id_token as proof.

    Args:
        identity_provider_id (int):
        body (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        identity_provider_id=identity_provider_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)
