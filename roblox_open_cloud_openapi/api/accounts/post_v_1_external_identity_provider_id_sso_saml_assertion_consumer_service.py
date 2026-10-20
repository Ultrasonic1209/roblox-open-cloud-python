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
{}
"""


from ...models.post_v1_external_identity_provider_id_sso_saml_assertion_consumer_service_body import (
    PostV1ExternalIdentityProviderIdSsoSamlAssertionConsumerServiceBody,
)
from ...types import Unset


def _get_kwargs(
    identity_provider_id: int,
    *,
    body: PostV1ExternalIdentityProviderIdSsoSamlAssertionConsumerServiceBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://auth.roblox.com/v1/external/{identity_provider_id}/sso/saml/assertion-consumer-service".format(
            identity_provider_id=quote(str(identity_provider_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 302:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    identity_provider_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostV1ExternalIdentityProviderIdSsoSamlAssertionConsumerServiceBody | Unset = UNSET,
) -> Response[Any]:
    """SAML Assertion Consumer Service endpoint that external identity provider calls post user
    authentication.

    Args:
        identity_provider_id (int):
        body (PostV1ExternalIdentityProviderIdSsoSamlAssertionConsumerServiceBody | Unset):

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

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    identity_provider_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostV1ExternalIdentityProviderIdSsoSamlAssertionConsumerServiceBody | Unset = UNSET,
) -> Response[Any]:
    """SAML Assertion Consumer Service endpoint that external identity provider calls post user
    authentication.

    Args:
        identity_provider_id (int):
        body (PostV1ExternalIdentityProviderIdSsoSamlAssertionConsumerServiceBody | Unset):

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

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
