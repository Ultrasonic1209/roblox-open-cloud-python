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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'SECOND', 'maxInPeriod': 10}}, 'x-roblox-scopes': [{'name': 'marketplace.item:read', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.get_v1_asset_types_asset_type_agents_action_type import GetV1AssetTypesAssetTypeAgentsActionType
from ...models.get_v1_asset_types_asset_type_agents_agent_type import GetV1AssetTypesAssetTypeAgentsAgentType
from ...models.get_v1_asset_types_asset_type_agents_asset_type import GetV1AssetTypesAssetTypeAgentsAssetType
from ...models.roblox_item_configuration_api_allowed_agents_asset_type_action_response import (
    RobloxItemConfigurationApiAllowedAgentsAssetTypeActionResponse,
)


def _get_kwargs(
    asset_type: GetV1AssetTypesAssetTypeAgentsAssetType,
    *,
    action_type: GetV1AssetTypesAssetTypeAgentsActionType,
    agent_type: GetV1AssetTypesAssetTypeAgentsAgentType,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_action_type = action_type.value
    params["ActionType"] = json_action_type

    json_agent_type = agent_type.value
    params["AgentType"] = json_agent_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://itemconfiguration.roblox.com/v1/asset-types/{asset_type}/agents".format(
            asset_type=quote(str(asset_type), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxItemConfigurationApiAllowedAgentsAssetTypeActionResponse | None:
    if response.status_code == 200:
        response_200 = RobloxItemConfigurationApiAllowedAgentsAssetTypeActionResponse.from_dict(response.json())

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
) -> Response[Any | RobloxItemConfigurationApiAllowedAgentsAssetTypeActionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_type: GetV1AssetTypesAssetTypeAgentsAssetType,
    *,
    client: AuthenticatedClient,
    action_type: GetV1AssetTypesAssetTypeAgentsActionType,
    agent_type: GetV1AssetTypesAssetTypeAgentsAgentType,
) -> Response[Any | RobloxItemConfigurationApiAllowedAgentsAssetTypeActionResponse]:
    """Gets agents of type requestModel.AgentType who are allowed to perform requestModel.ActionType for
    assetType.

    Args:
        asset_type (GetV1AssetTypesAssetTypeAgentsAssetType):
        action_type (GetV1AssetTypesAssetTypeAgentsActionType):
        agent_type (GetV1AssetTypesAssetTypeAgentsAgentType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiAllowedAgentsAssetTypeActionResponse]
    """

    kwargs = _get_kwargs(
        asset_type=asset_type,
        action_type=action_type,
        agent_type=agent_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_type: GetV1AssetTypesAssetTypeAgentsAssetType,
    *,
    client: AuthenticatedClient,
    action_type: GetV1AssetTypesAssetTypeAgentsActionType,
    agent_type: GetV1AssetTypesAssetTypeAgentsAgentType,
) -> Any | RobloxItemConfigurationApiAllowedAgentsAssetTypeActionResponse | None:
    """Gets agents of type requestModel.AgentType who are allowed to perform requestModel.ActionType for
    assetType.

    Args:
        asset_type (GetV1AssetTypesAssetTypeAgentsAssetType):
        action_type (GetV1AssetTypesAssetTypeAgentsActionType):
        agent_type (GetV1AssetTypesAssetTypeAgentsAgentType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiAllowedAgentsAssetTypeActionResponse
    """

    return sync_detailed(
        asset_type=asset_type,
        client=client,
        action_type=action_type,
        agent_type=agent_type,
    ).parsed


async def asyncio_detailed(
    asset_type: GetV1AssetTypesAssetTypeAgentsAssetType,
    *,
    client: AuthenticatedClient,
    action_type: GetV1AssetTypesAssetTypeAgentsActionType,
    agent_type: GetV1AssetTypesAssetTypeAgentsAgentType,
) -> Response[Any | RobloxItemConfigurationApiAllowedAgentsAssetTypeActionResponse]:
    """Gets agents of type requestModel.AgentType who are allowed to perform requestModel.ActionType for
    assetType.

    Args:
        asset_type (GetV1AssetTypesAssetTypeAgentsAssetType):
        action_type (GetV1AssetTypesAssetTypeAgentsActionType):
        agent_type (GetV1AssetTypesAssetTypeAgentsAgentType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiAllowedAgentsAssetTypeActionResponse]
    """

    kwargs = _get_kwargs(
        asset_type=asset_type,
        action_type=action_type,
        agent_type=agent_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_type: GetV1AssetTypesAssetTypeAgentsAssetType,
    *,
    client: AuthenticatedClient,
    action_type: GetV1AssetTypesAssetTypeAgentsActionType,
    agent_type: GetV1AssetTypesAssetTypeAgentsAgentType,
) -> Any | RobloxItemConfigurationApiAllowedAgentsAssetTypeActionResponse | None:
    """Gets agents of type requestModel.AgentType who are allowed to perform requestModel.ActionType for
    assetType.

    Args:
        asset_type (GetV1AssetTypesAssetTypeAgentsAssetType):
        action_type (GetV1AssetTypesAssetTypeAgentsActionType):
        agent_type (GetV1AssetTypesAssetTypeAgentsAgentType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiAllowedAgentsAssetTypeActionResponse
    """

    return (
        await asyncio_detailed(
            asset_type=asset_type,
            client=client,
            action_type=action_type,
            agent_type=agent_type,
        )
    ).parsed
