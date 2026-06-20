import sys
from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated


def _get_kwargs(
    *,
    id: int | Unset = UNSET,
    user_asset_id: int | Unset = UNSET,
    asset_version_id: int | Unset = UNSET,
    version: int | Unset = UNSET,
    universe_id: int | Unset = UNSET,
    client_insert: int | Unset = UNSET,
    scriptinsert: int | Unset = UNSET,
    module_place_id: int | Unset = UNSET,
    serverplaceid: str | Unset = UNSET,
    asset_name: str | Unset = UNSET,
    hash_: str | Unset = UNSET,
    mar_asset_hash: str | Unset = UNSET,
    mar_check_sum: str | Unset = UNSET,
    expected_asset_type: str | Unset = "",
    skip_signing_scripts: bool | Unset = False,
    permission_context: str | Unset = UNSET,
    do_not_fallback_to_baseline_representation: bool | Unset = False,
    content_representation_priority_list: str | Unset = "",
    asset_resolution_mode: str | Unset = UNSET,
    access_context: str | Unset = UNSET,
    usage_context: int | Unset = UNSET,
    accept_encoding: str,
    roblox_place_id: int,
    asset_type: str,
    accept: str,
    asset_format: str,
    roblox_asset_format: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Accept-Encoding"] = accept_encoding

    headers["Roblox-Place-Id"] = str(roblox_place_id)

    headers["AssetType"] = asset_type

    headers["Accept"] = accept

    headers["AssetFormat"] = asset_format

    headers["Roblox-AssetFormat"] = roblox_asset_format

    params: dict[str, Any] = {}

    params["id"] = id

    params["userAssetId"] = user_asset_id

    params["assetVersionId"] = asset_version_id

    params["version"] = version

    params["universeId"] = universe_id

    params["clientInsert"] = client_insert

    params["scriptinsert"] = scriptinsert

    params["modulePlaceId"] = module_place_id

    params["serverplaceid"] = serverplaceid

    params["assetName"] = asset_name

    params["hash"] = hash_

    params["marAssetHash"] = mar_asset_hash

    params["marCheckSum"] = mar_check_sum

    params["expectedAssetType"] = expected_asset_type

    params["skipSigningScripts"] = skip_signing_scripts

    params["permissionContext"] = permission_context

    params["doNotFallbackToBaselineRepresentation"] = do_not_fallback_to_baseline_representation

    params["contentRepresentationPriorityList"] = content_representation_priority_list

    params["assetResolutionMode"] = asset_resolution_mode

    params["accessContext"] = access_context

    params["usageContext"] = usage_context

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://assetdelivery.roblox.com/v1/asset",
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
                "x-roblox-recommended-alternatives": [
                    {
                        "url": "https://assetdelivery.roblox.com/v2/asset",
                        "httpMethod": "GET",
                        "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/assets#assetdelivery_get_v2_asset",
                    }
                ],
            },
            "openapi-id": "get_v1_asset",
        },
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | None:
    if response.status_code == 200:
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


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#assetdelivery_get_v1_asset"
)
def sync_detailed(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    user_asset_id: int | Unset = UNSET,
    asset_version_id: int | Unset = UNSET,
    version: int | Unset = UNSET,
    universe_id: int | Unset = UNSET,
    client_insert: int | Unset = UNSET,
    scriptinsert: int | Unset = UNSET,
    module_place_id: int | Unset = UNSET,
    serverplaceid: str | Unset = UNSET,
    asset_name: str | Unset = UNSET,
    hash_: str | Unset = UNSET,
    mar_asset_hash: str | Unset = UNSET,
    mar_check_sum: str | Unset = UNSET,
    expected_asset_type: str | Unset = "",
    skip_signing_scripts: bool | Unset = False,
    permission_context: str | Unset = UNSET,
    do_not_fallback_to_baseline_representation: bool | Unset = False,
    content_representation_priority_list: str | Unset = "",
    asset_resolution_mode: str | Unset = UNSET,
    access_context: str | Unset = UNSET,
    usage_context: int | Unset = UNSET,
    accept_encoding: str,
    roblox_place_id: int,
    asset_type: str,
    accept: str,
    asset_format: str,
    roblox_asset_format: str,
) -> Response[Any]:
    """
    Args:
        id (int | Unset):
        user_asset_id (int | Unset):
        asset_version_id (int | Unset):
        version (int | Unset):
        universe_id (int | Unset):
        client_insert (int | Unset):
        scriptinsert (int | Unset):
        module_place_id (int | Unset):
        serverplaceid (str | Unset):
        asset_name (str | Unset):
        hash_ (str | Unset):
        mar_asset_hash (str | Unset):
        mar_check_sum (str | Unset):
        expected_asset_type (str | Unset):  Default: ''.
        skip_signing_scripts (bool | Unset):  Default: False.
        permission_context (str | Unset):
        do_not_fallback_to_baseline_representation (bool | Unset):  Default: False.
        content_representation_priority_list (str | Unset):  Default: ''.
        asset_resolution_mode (str | Unset):
        access_context (str | Unset):
        usage_context (int | Unset):
        accept_encoding (str):
        roblox_place_id (int):
        asset_type (str):
        accept (str):
        asset_format (str):
        roblox_asset_format (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        user_asset_id=user_asset_id,
        asset_version_id=asset_version_id,
        version=version,
        universe_id=universe_id,
        client_insert=client_insert,
        scriptinsert=scriptinsert,
        module_place_id=module_place_id,
        serverplaceid=serverplaceid,
        asset_name=asset_name,
        hash_=hash_,
        mar_asset_hash=mar_asset_hash,
        mar_check_sum=mar_check_sum,
        expected_asset_type=expected_asset_type,
        skip_signing_scripts=skip_signing_scripts,
        permission_context=permission_context,
        do_not_fallback_to_baseline_representation=do_not_fallback_to_baseline_representation,
        content_representation_priority_list=content_representation_priority_list,
        asset_resolution_mode=asset_resolution_mode,
        access_context=access_context,
        usage_context=usage_context,
        accept_encoding=accept_encoding,
        roblox_place_id=roblox_place_id,
        asset_type=asset_type,
        accept=accept,
        asset_format=asset_format,
        roblox_asset_format=roblox_asset_format,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#assetdelivery_get_v1_asset"
)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int | Unset = UNSET,
    user_asset_id: int | Unset = UNSET,
    asset_version_id: int | Unset = UNSET,
    version: int | Unset = UNSET,
    universe_id: int | Unset = UNSET,
    client_insert: int | Unset = UNSET,
    scriptinsert: int | Unset = UNSET,
    module_place_id: int | Unset = UNSET,
    serverplaceid: str | Unset = UNSET,
    asset_name: str | Unset = UNSET,
    hash_: str | Unset = UNSET,
    mar_asset_hash: str | Unset = UNSET,
    mar_check_sum: str | Unset = UNSET,
    expected_asset_type: str | Unset = "",
    skip_signing_scripts: bool | Unset = False,
    permission_context: str | Unset = UNSET,
    do_not_fallback_to_baseline_representation: bool | Unset = False,
    content_representation_priority_list: str | Unset = "",
    asset_resolution_mode: str | Unset = UNSET,
    access_context: str | Unset = UNSET,
    usage_context: int | Unset = UNSET,
    accept_encoding: str,
    roblox_place_id: int,
    asset_type: str,
    accept: str,
    asset_format: str,
    roblox_asset_format: str,
) -> Response[Any]:
    """
    Args:
        id (int | Unset):
        user_asset_id (int | Unset):
        asset_version_id (int | Unset):
        version (int | Unset):
        universe_id (int | Unset):
        client_insert (int | Unset):
        scriptinsert (int | Unset):
        module_place_id (int | Unset):
        serverplaceid (str | Unset):
        asset_name (str | Unset):
        hash_ (str | Unset):
        mar_asset_hash (str | Unset):
        mar_check_sum (str | Unset):
        expected_asset_type (str | Unset):  Default: ''.
        skip_signing_scripts (bool | Unset):  Default: False.
        permission_context (str | Unset):
        do_not_fallback_to_baseline_representation (bool | Unset):  Default: False.
        content_representation_priority_list (str | Unset):  Default: ''.
        asset_resolution_mode (str | Unset):
        access_context (str | Unset):
        usage_context (int | Unset):
        accept_encoding (str):
        roblox_place_id (int):
        asset_type (str):
        accept (str):
        asset_format (str):
        roblox_asset_format (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        user_asset_id=user_asset_id,
        asset_version_id=asset_version_id,
        version=version,
        universe_id=universe_id,
        client_insert=client_insert,
        scriptinsert=scriptinsert,
        module_place_id=module_place_id,
        serverplaceid=serverplaceid,
        asset_name=asset_name,
        hash_=hash_,
        mar_asset_hash=mar_asset_hash,
        mar_check_sum=mar_check_sum,
        expected_asset_type=expected_asset_type,
        skip_signing_scripts=skip_signing_scripts,
        permission_context=permission_context,
        do_not_fallback_to_baseline_representation=do_not_fallback_to_baseline_representation,
        content_representation_priority_list=content_representation_priority_list,
        asset_resolution_mode=asset_resolution_mode,
        access_context=access_context,
        usage_context=usage_context,
        accept_encoding=accept_encoding,
        roblox_place_id=roblox_place_id,
        asset_type=asset_type,
        accept=accept,
        asset_format=asset_format,
        roblox_asset_format=roblox_asset_format,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)
