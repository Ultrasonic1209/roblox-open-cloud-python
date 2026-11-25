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
from ...types import UNSET, Response

"""
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 1000}}, 'x-roblox-scopes': [{'name': 'scope:read', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.application_authorizations_api_models_response_error_response import (
    ApplicationAuthorizationsApiModelsResponseErrorResponse,
)
from ...models.application_authorizations_api_models_response_scopes_configuration_response import (
    ApplicationAuthorizationsApiModelsResponseScopesConfigurationResponse,
)
from ...types import Unset


def _get_kwargs(
    *,
    locale: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["locale"] = locale

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/oauth/v1/scopes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ApplicationAuthorizationsApiModelsResponseErrorResponse
    | ApplicationAuthorizationsApiModelsResponseScopesConfigurationResponse
    | None
):
    if response.status_code == 200:
        response_200 = ApplicationAuthorizationsApiModelsResponseScopesConfigurationResponse.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = ApplicationAuthorizationsApiModelsResponseErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ApplicationAuthorizationsApiModelsResponseErrorResponse
    | ApplicationAuthorizationsApiModelsResponseScopesConfigurationResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    locale: str | Unset = UNSET,
) -> Response[
    ApplicationAuthorizationsApiModelsResponseErrorResponse
    | ApplicationAuthorizationsApiModelsResponseScopesConfigurationResponse
]:
    """
    Args:
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplicationAuthorizationsApiModelsResponseErrorResponse | ApplicationAuthorizationsApiModelsResponseScopesConfigurationResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    locale: str | Unset = UNSET,
) -> (
    ApplicationAuthorizationsApiModelsResponseErrorResponse
    | ApplicationAuthorizationsApiModelsResponseScopesConfigurationResponse
    | None
):
    """
    Args:
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApplicationAuthorizationsApiModelsResponseErrorResponse | ApplicationAuthorizationsApiModelsResponseScopesConfigurationResponse
    """

    return sync_detailed(
        client=client,
        locale=locale,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    locale: str | Unset = UNSET,
) -> Response[
    ApplicationAuthorizationsApiModelsResponseErrorResponse
    | ApplicationAuthorizationsApiModelsResponseScopesConfigurationResponse
]:
    """
    Args:
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplicationAuthorizationsApiModelsResponseErrorResponse | ApplicationAuthorizationsApiModelsResponseScopesConfigurationResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    locale: str | Unset = UNSET,
) -> (
    ApplicationAuthorizationsApiModelsResponseErrorResponse
    | ApplicationAuthorizationsApiModelsResponseScopesConfigurationResponse
    | None
):
    """
    Args:
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApplicationAuthorizationsApiModelsResponseErrorResponse | ApplicationAuthorizationsApiModelsResponseScopesConfigurationResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            locale=locale,
        )
    ).parsed
