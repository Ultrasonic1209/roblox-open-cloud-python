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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'SECOND', 'maxInPeriod': 10}}, 'x-roblox-scopes': [{'name': 'marketplace.item:read', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.get_v1_permissions_groups_action import GetV1PermissionsGroupsAction
from ...models.roblox_item_configuration_api_models_request_allowed_groups_for_action_response import (
    RobloxItemConfigurationApiModelsRequestAllowedGroupsForActionResponse,
)


def _get_kwargs(
    *,
    action: GetV1PermissionsGroupsAction,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_action = action.value
    params["action"] = json_action

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://itemconfiguration.roblox.com/v1/permissions/groups",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxItemConfigurationApiModelsRequestAllowedGroupsForActionResponse | None:
    if response.status_code == 200:
        response_200 = RobloxItemConfigurationApiModelsRequestAllowedGroupsForActionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxItemConfigurationApiModelsRequestAllowedGroupsForActionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    action: GetV1PermissionsGroupsAction,
) -> Response[Any | RobloxItemConfigurationApiModelsRequestAllowedGroupsForActionResponse]:
    """Returns a list of allowed groups for a given Roblox.ItemConfiguration.Api.Enums.MarketplaceAction.

    Args:
        action (GetV1PermissionsGroupsAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiModelsRequestAllowedGroupsForActionResponse]
    """

    kwargs = _get_kwargs(
        action=action,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    action: GetV1PermissionsGroupsAction,
) -> Any | RobloxItemConfigurationApiModelsRequestAllowedGroupsForActionResponse | None:
    """Returns a list of allowed groups for a given Roblox.ItemConfiguration.Api.Enums.MarketplaceAction.

    Args:
        action (GetV1PermissionsGroupsAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiModelsRequestAllowedGroupsForActionResponse
    """

    return sync_detailed(
        client=client,
        action=action,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    action: GetV1PermissionsGroupsAction,
) -> Response[Any | RobloxItemConfigurationApiModelsRequestAllowedGroupsForActionResponse]:
    """Returns a list of allowed groups for a given Roblox.ItemConfiguration.Api.Enums.MarketplaceAction.

    Args:
        action (GetV1PermissionsGroupsAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiModelsRequestAllowedGroupsForActionResponse]
    """

    kwargs = _get_kwargs(
        action=action,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    action: GetV1PermissionsGroupsAction,
) -> Any | RobloxItemConfigurationApiModelsRequestAllowedGroupsForActionResponse | None:
    """Returns a list of allowed groups for a given Roblox.ItemConfiguration.Api.Enums.MarketplaceAction.

    Args:
        action (GetV1PermissionsGroupsAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiModelsRequestAllowedGroupsForActionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
        )
    ).parsed
