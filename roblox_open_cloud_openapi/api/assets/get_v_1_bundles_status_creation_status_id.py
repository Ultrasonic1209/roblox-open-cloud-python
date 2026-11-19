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
from ...types import Response

"""
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'SECOND', 'maxInPeriod': 10}}, 'x-roblox-scopes': [{'name': 'marketplace.item:read', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.roblox_item_configuration_api_models_response_bundle_get_bundle_creation_status_response import (
    RobloxItemConfigurationApiModelsResponseBundleGetBundleCreationStatusResponse,
)


def _get_kwargs(
    creation_status_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://itemconfiguration.roblox.com/v1/bundles/status/{creation_status_id}".format(
            creation_status_id=quote(str(creation_status_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxItemConfigurationApiModelsResponseBundleGetBundleCreationStatusResponse | None:
    if response.status_code == 200:
        response_200 = RobloxItemConfigurationApiModelsResponseBundleGetBundleCreationStatusResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

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
) -> Response[Any | RobloxItemConfigurationApiModelsResponseBundleGetBundleCreationStatusResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    creation_status_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxItemConfigurationApiModelsResponseBundleGetBundleCreationStatusResponse]:
    """Get status on the CreateBundle request that was previously queued up.

    Args:
        creation_status_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiModelsResponseBundleGetBundleCreationStatusResponse]
    """

    kwargs = _get_kwargs(
        creation_status_id=creation_status_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    creation_status_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxItemConfigurationApiModelsResponseBundleGetBundleCreationStatusResponse | None:
    """Get status on the CreateBundle request that was previously queued up.

    Args:
        creation_status_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiModelsResponseBundleGetBundleCreationStatusResponse
    """

    return sync_detailed(
        creation_status_id=creation_status_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    creation_status_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxItemConfigurationApiModelsResponseBundleGetBundleCreationStatusResponse]:
    """Get status on the CreateBundle request that was previously queued up.

    Args:
        creation_status_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiModelsResponseBundleGetBundleCreationStatusResponse]
    """

    kwargs = _get_kwargs(
        creation_status_id=creation_status_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    creation_status_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxItemConfigurationApiModelsResponseBundleGetBundleCreationStatusResponse | None:
    """Get status on the CreateBundle request that was previously queued up.

    Args:
        creation_status_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiModelsResponseBundleGetBundleCreationStatusResponse
    """

    return (
        await asyncio_detailed(
            creation_status_id=creation_status_id,
            client=client,
        )
    ).parsed
