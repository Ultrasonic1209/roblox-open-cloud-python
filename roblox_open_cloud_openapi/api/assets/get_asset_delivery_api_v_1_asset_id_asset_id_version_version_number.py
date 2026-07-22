from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: int,
    version_number: int,
    *,
    skip_signing_scripts: bool | Unset = False,
    client_insert: int | Unset = UNSET,
    scriptinsert: int | Unset = UNSET,
    module_place_id: int | Unset = UNSET,
    serverplaceid: int | Unset = UNSET,
    expected_asset_type: str | Unset = "",
    do_not_fallback_to_baseline_representation: bool | Unset = False,
    content_representation_priority_list: str | Unset = "",
    access_context: str | Unset = UNSET,
    usage_context: int | Unset = UNSET,
    accept_encoding: str | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
    asset_type: str | Unset = UNSET,
    accept: str | Unset = UNSET,
    asset_format: str | Unset = UNSET,
    roblox_asset_format: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_encoding, Unset):
        headers["Accept-Encoding"] = accept_encoding

    if not isinstance(roblox_place_id, Unset):
        headers["Roblox-Place-Id"] = str(roblox_place_id)

    if not isinstance(asset_type, Unset):
        headers["AssetType"] = asset_type

    if not isinstance(accept, Unset):
        headers["Accept"] = accept

    if not isinstance(asset_format, Unset):
        headers["AssetFormat"] = asset_format

    if not isinstance(roblox_asset_format, Unset):
        headers["Roblox-AssetFormat"] = roblox_asset_format

    params: dict[str, Any] = {}

    params["skipSigningScripts"] = skip_signing_scripts

    params["clientInsert"] = client_insert

    params["scriptinsert"] = scriptinsert

    params["modulePlaceId"] = module_place_id

    params["serverplaceid"] = serverplaceid

    params["expectedAssetType"] = expected_asset_type

    params["doNotFallbackToBaselineRepresentation"] = do_not_fallback_to_baseline_representation

    params["contentRepresentationPriorityList"] = content_representation_priority_list

    params["accessContext"] = access_context

    params["usageContext"] = usage_context

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/asset-delivery-api/v1/assetId/{asset_id}/version/{version_number}".format(
            asset_id=quote(str(asset_id), safe=""),
            version_number=quote(str(version_number), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 1000},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 1000},
                },
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
                "x-roblox-scopes": [{"name": "legacy-asset:manage"}],
            },
            "openapi-id": "get_asset-delivery-api_v1_assetId_assetId_version_versionNumber",
        },
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 401:
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
    asset_id: int,
    version_number: int,
    *,
    client: AuthenticatedClient,
    skip_signing_scripts: bool | Unset = False,
    client_insert: int | Unset = UNSET,
    scriptinsert: int | Unset = UNSET,
    module_place_id: int | Unset = UNSET,
    serverplaceid: int | Unset = UNSET,
    expected_asset_type: str | Unset = "",
    do_not_fallback_to_baseline_representation: bool | Unset = False,
    content_representation_priority_list: str | Unset = "",
    access_context: str | Unset = UNSET,
    usage_context: int | Unset = UNSET,
    accept_encoding: str | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
    asset_type: str | Unset = UNSET,
    accept: str | Unset = UNSET,
    asset_format: str | Unset = UNSET,
    roblox_asset_format: str | Unset = UNSET,
) -> Response[Any]:
    """Retrieves an asset by its ID and version number with OpenCloud auth.

     Refer to the assetId endpoint for details on usage.
    This endpoint is expected to be called with API key authentication through `apis.roblox.com/asset-
    delivery-api/v1/assetId/{assetId}/version/{versionNumber}`.
    While you are able to make requests to this endpoint with Cookie authentication via
    `assetdelivery.roblox.com/v1/openCloud/assetId/{assetId}/version/{versionNumber}`, we highly
    discourage use this way.
    Expect unannounced removal of this second route in the future.

    Args:
        asset_id (int):
        version_number (int):
        skip_signing_scripts (bool | Unset):  Default: False.
        client_insert (int | Unset):
        scriptinsert (int | Unset):
        module_place_id (int | Unset):
        serverplaceid (int | Unset):
        expected_asset_type (str | Unset):  Default: ''.
        do_not_fallback_to_baseline_representation (bool | Unset):  Default: False.
        content_representation_priority_list (str | Unset):  Default: ''.
        access_context (str | Unset):
        usage_context (int | Unset):
        accept_encoding (str | Unset):
        roblox_place_id (int | Unset):
        asset_type (str | Unset):
        accept (str | Unset):
        asset_format (str | Unset):
        roblox_asset_format (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_number=version_number,
        skip_signing_scripts=skip_signing_scripts,
        client_insert=client_insert,
        scriptinsert=scriptinsert,
        module_place_id=module_place_id,
        serverplaceid=serverplaceid,
        expected_asset_type=expected_asset_type,
        do_not_fallback_to_baseline_representation=do_not_fallback_to_baseline_representation,
        content_representation_priority_list=content_representation_priority_list,
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


async def asyncio_detailed(
    asset_id: int,
    version_number: int,
    *,
    client: AuthenticatedClient,
    skip_signing_scripts: bool | Unset = False,
    client_insert: int | Unset = UNSET,
    scriptinsert: int | Unset = UNSET,
    module_place_id: int | Unset = UNSET,
    serverplaceid: int | Unset = UNSET,
    expected_asset_type: str | Unset = "",
    do_not_fallback_to_baseline_representation: bool | Unset = False,
    content_representation_priority_list: str | Unset = "",
    access_context: str | Unset = UNSET,
    usage_context: int | Unset = UNSET,
    accept_encoding: str | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
    asset_type: str | Unset = UNSET,
    accept: str | Unset = UNSET,
    asset_format: str | Unset = UNSET,
    roblox_asset_format: str | Unset = UNSET,
) -> Response[Any]:
    """Retrieves an asset by its ID and version number with OpenCloud auth.

     Refer to the assetId endpoint for details on usage.
    This endpoint is expected to be called with API key authentication through `apis.roblox.com/asset-
    delivery-api/v1/assetId/{assetId}/version/{versionNumber}`.
    While you are able to make requests to this endpoint with Cookie authentication via
    `assetdelivery.roblox.com/v1/openCloud/assetId/{assetId}/version/{versionNumber}`, we highly
    discourage use this way.
    Expect unannounced removal of this second route in the future.

    Args:
        asset_id (int):
        version_number (int):
        skip_signing_scripts (bool | Unset):  Default: False.
        client_insert (int | Unset):
        scriptinsert (int | Unset):
        module_place_id (int | Unset):
        serverplaceid (int | Unset):
        expected_asset_type (str | Unset):  Default: ''.
        do_not_fallback_to_baseline_representation (bool | Unset):  Default: False.
        content_representation_priority_list (str | Unset):  Default: ''.
        access_context (str | Unset):
        usage_context (int | Unset):
        accept_encoding (str | Unset):
        roblox_place_id (int | Unset):
        asset_type (str | Unset):
        accept (str | Unset):
        asset_format (str | Unset):
        roblox_asset_format (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_number=version_number,
        skip_signing_scripts=skip_signing_scripts,
        client_insert=client_insert,
        scriptinsert=scriptinsert,
        module_place_id=module_place_id,
        serverplaceid=serverplaceid,
        expected_asset_type=expected_asset_type,
        do_not_fallback_to_baseline_representation=do_not_fallback_to_baseline_representation,
        content_representation_priority_list=content_representation_priority_list,
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
