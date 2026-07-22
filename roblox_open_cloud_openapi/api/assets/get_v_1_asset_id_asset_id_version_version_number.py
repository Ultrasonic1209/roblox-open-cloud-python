import sys
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated


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
        "url": "https://assetdelivery.roblox.com/v1/assetId/{asset_id}/version/{version_number}".format(
            asset_id=quote(str(asset_id), safe=""),
            version_number=quote(str(version_number), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
                "x-roblox-recommended-alternatives": [
                    {
                        "url": "https://assetdelivery.roblox.com/v2/assetId/{assetId}/version/{versionNumber}",
                        "httpMethod": "GET",
                        "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/assets#assetdelivery_get_v2_assetId__assetId__version__versionNumber_",
                    }
                ],
            },
            "openapi-id": "get_v1_assetId_assetId_version_versionNumber",
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
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#assetdelivery_get_v1_assetId__assetId__version__versionNumber_"
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
    accept_encoding: str,
    roblox_place_id: int,
    asset_type: str,
    accept: str,
    asset_format: str,
    roblox_asset_format: str,
) -> Response[Any]:
    """Retrieves an asset by its ID and version number.

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


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#assetdelivery_get_v1_assetId__assetId__version__versionNumber_"
)
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
    accept_encoding: str,
    roblox_place_id: int,
    asset_type: str,
    accept: str,
    asset_format: str,
    roblox_asset_format: str,
) -> Response[Any]:
    """Retrieves an asset by its ID and version number.

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
