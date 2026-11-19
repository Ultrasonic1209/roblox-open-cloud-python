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


from ...models.get_v1_permissions_action_allowed_for_item_type_action import (
    GetV1PermissionsActionAllowedForItemTypeAction,
)
from ...models.get_v1_permissions_action_allowed_for_item_type_asset_type import (
    GetV1PermissionsActionAllowedForItemTypeAssetType,
)
from ...models.get_v1_permissions_action_allowed_for_item_type_bundle_type import (
    GetV1PermissionsActionAllowedForItemTypeBundleType,
)
from ...models.get_v1_permissions_action_allowed_for_item_type_look_type import (
    GetV1PermissionsActionAllowedForItemTypeLookType,
)
from ...models.roblox_item_configuration_api_models_response_is_action_allowed_for_item_type_response import (
    RobloxItemConfigurationApiModelsResponseIsActionAllowedForItemTypeResponse,
)
from ...types import Unset


def _get_kwargs(
    *,
    action: GetV1PermissionsActionAllowedForItemTypeAction,
    group_id: int | Unset = UNSET,
    asset_type: GetV1PermissionsActionAllowedForItemTypeAssetType | Unset = UNSET,
    bundle_type: GetV1PermissionsActionAllowedForItemTypeBundleType | Unset = UNSET,
    look_type: GetV1PermissionsActionAllowedForItemTypeLookType | Unset = UNSET,
    trusted_creator_check: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_action = action.value
    params["action"] = json_action

    params["groupId"] = group_id

    json_asset_type: int | Unset = UNSET
    if not isinstance(asset_type, Unset):
        json_asset_type = asset_type.value

    params["assetType"] = json_asset_type

    json_bundle_type: int | Unset = UNSET
    if not isinstance(bundle_type, Unset):
        json_bundle_type = bundle_type.value

    params["bundleType"] = json_bundle_type

    json_look_type: int | Unset = UNSET
    if not isinstance(look_type, Unset):
        json_look_type = look_type.value

    params["lookType"] = json_look_type

    params["trustedCreatorCheck"] = trusted_creator_check

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://itemconfiguration.roblox.com/v1/permissions/action-allowed-for-item-type",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxItemConfigurationApiModelsResponseIsActionAllowedForItemTypeResponse | None:
    if response.status_code == 200:
        response_200 = RobloxItemConfigurationApiModelsResponseIsActionAllowedForItemTypeResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxItemConfigurationApiModelsResponseIsActionAllowedForItemTypeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    action: GetV1PermissionsActionAllowedForItemTypeAction,
    group_id: int | Unset = UNSET,
    asset_type: GetV1PermissionsActionAllowedForItemTypeAssetType | Unset = UNSET,
    bundle_type: GetV1PermissionsActionAllowedForItemTypeBundleType | Unset = UNSET,
    look_type: GetV1PermissionsActionAllowedForItemTypeLookType | Unset = UNSET,
    trusted_creator_check: bool | Unset = False,
) -> Response[Any | RobloxItemConfigurationApiModelsResponseIsActionAllowedForItemTypeResponse]:
    """Returns whether the authenticated user (or group on their behalf) may perform the given marketplace
    action
    for a specific asset, bundle, or look type.

    Args:
        action (GetV1PermissionsActionAllowedForItemTypeAction):
        group_id (int | Unset):
        asset_type (GetV1PermissionsActionAllowedForItemTypeAssetType | Unset):
        bundle_type (GetV1PermissionsActionAllowedForItemTypeBundleType | Unset):
        look_type (GetV1PermissionsActionAllowedForItemTypeLookType | Unset):
        trusted_creator_check (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiModelsResponseIsActionAllowedForItemTypeResponse]
    """

    kwargs = _get_kwargs(
        action=action,
        group_id=group_id,
        asset_type=asset_type,
        bundle_type=bundle_type,
        look_type=look_type,
        trusted_creator_check=trusted_creator_check,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    action: GetV1PermissionsActionAllowedForItemTypeAction,
    group_id: int | Unset = UNSET,
    asset_type: GetV1PermissionsActionAllowedForItemTypeAssetType | Unset = UNSET,
    bundle_type: GetV1PermissionsActionAllowedForItemTypeBundleType | Unset = UNSET,
    look_type: GetV1PermissionsActionAllowedForItemTypeLookType | Unset = UNSET,
    trusted_creator_check: bool | Unset = False,
) -> Any | RobloxItemConfigurationApiModelsResponseIsActionAllowedForItemTypeResponse | None:
    """Returns whether the authenticated user (or group on their behalf) may perform the given marketplace
    action
    for a specific asset, bundle, or look type.

    Args:
        action (GetV1PermissionsActionAllowedForItemTypeAction):
        group_id (int | Unset):
        asset_type (GetV1PermissionsActionAllowedForItemTypeAssetType | Unset):
        bundle_type (GetV1PermissionsActionAllowedForItemTypeBundleType | Unset):
        look_type (GetV1PermissionsActionAllowedForItemTypeLookType | Unset):
        trusted_creator_check (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiModelsResponseIsActionAllowedForItemTypeResponse
    """

    return sync_detailed(
        client=client,
        action=action,
        group_id=group_id,
        asset_type=asset_type,
        bundle_type=bundle_type,
        look_type=look_type,
        trusted_creator_check=trusted_creator_check,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    action: GetV1PermissionsActionAllowedForItemTypeAction,
    group_id: int | Unset = UNSET,
    asset_type: GetV1PermissionsActionAllowedForItemTypeAssetType | Unset = UNSET,
    bundle_type: GetV1PermissionsActionAllowedForItemTypeBundleType | Unset = UNSET,
    look_type: GetV1PermissionsActionAllowedForItemTypeLookType | Unset = UNSET,
    trusted_creator_check: bool | Unset = False,
) -> Response[Any | RobloxItemConfigurationApiModelsResponseIsActionAllowedForItemTypeResponse]:
    """Returns whether the authenticated user (or group on their behalf) may perform the given marketplace
    action
    for a specific asset, bundle, or look type.

    Args:
        action (GetV1PermissionsActionAllowedForItemTypeAction):
        group_id (int | Unset):
        asset_type (GetV1PermissionsActionAllowedForItemTypeAssetType | Unset):
        bundle_type (GetV1PermissionsActionAllowedForItemTypeBundleType | Unset):
        look_type (GetV1PermissionsActionAllowedForItemTypeLookType | Unset):
        trusted_creator_check (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiModelsResponseIsActionAllowedForItemTypeResponse]
    """

    kwargs = _get_kwargs(
        action=action,
        group_id=group_id,
        asset_type=asset_type,
        bundle_type=bundle_type,
        look_type=look_type,
        trusted_creator_check=trusted_creator_check,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    action: GetV1PermissionsActionAllowedForItemTypeAction,
    group_id: int | Unset = UNSET,
    asset_type: GetV1PermissionsActionAllowedForItemTypeAssetType | Unset = UNSET,
    bundle_type: GetV1PermissionsActionAllowedForItemTypeBundleType | Unset = UNSET,
    look_type: GetV1PermissionsActionAllowedForItemTypeLookType | Unset = UNSET,
    trusted_creator_check: bool | Unset = False,
) -> Any | RobloxItemConfigurationApiModelsResponseIsActionAllowedForItemTypeResponse | None:
    """Returns whether the authenticated user (or group on their behalf) may perform the given marketplace
    action
    for a specific asset, bundle, or look type.

    Args:
        action (GetV1PermissionsActionAllowedForItemTypeAction):
        group_id (int | Unset):
        asset_type (GetV1PermissionsActionAllowedForItemTypeAssetType | Unset):
        bundle_type (GetV1PermissionsActionAllowedForItemTypeBundleType | Unset):
        look_type (GetV1PermissionsActionAllowedForItemTypeLookType | Unset):
        trusted_creator_check (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiModelsResponseIsActionAllowedForItemTypeResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            group_id=group_id,
            asset_type=asset_type,
            bundle_type=bundle_type,
            look_type=look_type,
            trusted_creator_check=trusted_creator_check,
        )
    ).parsed
