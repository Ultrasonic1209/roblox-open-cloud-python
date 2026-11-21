from http import HTTPStatus
from typing import TYPE_CHECKING, Any, cast

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


from ...models.roblox_authentication_api_models_response_external_identity_gateway_link_candidate_response import (
    RobloxAuthenticationApiModelsResponseExternalIdentityGatewayLinkCandidateResponse,
)


def _get_kwargs(
    *,
    link_candidate_token_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["linkCandidateTokenId"] = link_candidate_token_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://auth.roblox.com/v1/external/link-candidate",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayLinkCandidateResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAuthenticationApiModelsResponseExternalIdentityGatewayLinkCandidateResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayLinkCandidateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    link_candidate_token_id: str,
) -> Response[Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayLinkCandidateResponse]:
    """The user ids a provider sign-in matched, and the Google or Apple email on the token. Flow 1 holds
    the
    token id in a cookie. Flows 2 and 3 send it as `linkCandidateTokenId`. Reading does not consume
    the token, so the picker can be opened again.

    Args:
        link_candidate_token_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayLinkCandidateResponse]
    """

    kwargs = _get_kwargs(
        link_candidate_token_id=link_candidate_token_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    link_candidate_token_id: str,
) -> Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayLinkCandidateResponse | None:
    """The user ids a provider sign-in matched, and the Google or Apple email on the token. Flow 1 holds
    the
    token id in a cookie. Flows 2 and 3 send it as `linkCandidateTokenId`. Reading does not consume
    the token, so the picker can be opened again.

    Args:
        link_candidate_token_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayLinkCandidateResponse
    """

    return sync_detailed(
        client=client,
        link_candidate_token_id=link_candidate_token_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    link_candidate_token_id: str,
) -> Response[Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayLinkCandidateResponse]:
    """The user ids a provider sign-in matched, and the Google or Apple email on the token. Flow 1 holds
    the
    token id in a cookie. Flows 2 and 3 send it as `linkCandidateTokenId`. Reading does not consume
    the token, so the picker can be opened again.

    Args:
        link_candidate_token_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayLinkCandidateResponse]
    """

    kwargs = _get_kwargs(
        link_candidate_token_id=link_candidate_token_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    link_candidate_token_id: str,
) -> Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayLinkCandidateResponse | None:
    """The user ids a provider sign-in matched, and the Google or Apple email on the token. Flow 1 holds
    the
    token id in a cookie. Flows 2 and 3 send it as `linkCandidateTokenId`. Reading does not consume
    the token, so the picker can be opened again.

    Args:
        link_candidate_token_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayLinkCandidateResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            link_candidate_token_id=link_candidate_token_id,
        )
    ).parsed
