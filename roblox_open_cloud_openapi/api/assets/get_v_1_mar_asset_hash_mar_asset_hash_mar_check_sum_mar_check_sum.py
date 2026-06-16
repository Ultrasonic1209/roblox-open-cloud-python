import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_web_assets_asset_response_item_v1 import RobloxWebAssetsAssetResponseItemV1
from ...types import Unset


def _get_kwargs(
    mar_asset_hash: str,
    mar_check_sum: str,
    *,
    skip_signing_scripts: bool | Unset = False,
    client_insert: int | Unset = UNSET,
    scriptinsert: int | Unset = UNSET,
    module_place_id: int | Unset = UNSET,
    serverplaceid: int | Unset = UNSET,
    expected_asset_type: str | Unset = "",
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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/marAssetHash/{mar_asset_hash}/marCheckSum/{mar_check_sum}".format(
            mar_asset_hash=quote(str(mar_asset_hash), safe=""),
            mar_check_sum=quote(str(mar_check_sum), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebAssetsAssetResponseItemV1 | None:
    if response.status_code == 200:
        response_200 = RobloxWebAssetsAssetResponseItemV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxWebAssetsAssetResponseItemV1]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#assetdelivery_get_v1_marAssetHash__marAssetHash__marCheckSum__marCheckSum_"
)
def sync_detailed(
    mar_asset_hash: str,
    mar_check_sum: str,
    *,
    client: AuthenticatedClient,
    skip_signing_scripts: bool | Unset = False,
    client_insert: int | Unset = UNSET,
    scriptinsert: int | Unset = UNSET,
    module_place_id: int | Unset = UNSET,
    serverplaceid: int | Unset = UNSET,
    expected_asset_type: str | Unset = "",
    accept_encoding: str,
    roblox_place_id: int,
    asset_type: str,
    accept: str,
    asset_format: str,
    roblox_asset_format: str,
) -> Response[Any | RobloxWebAssetsAssetResponseItemV1]:
    """Retrieves an asset by its mar (moderation agnostic) hash and mar (moderation agnostic) checksum.

    Args:
        mar_asset_hash (str):
        mar_check_sum (str):
        skip_signing_scripts (bool | Unset):  Default: False.
        client_insert (int | Unset):
        scriptinsert (int | Unset):
        module_place_id (int | Unset):
        serverplaceid (int | Unset):
        expected_asset_type (str | Unset):  Default: ''.
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
        Response[Any | RobloxWebAssetsAssetResponseItemV1]
    """

    kwargs = _get_kwargs(
        mar_asset_hash=mar_asset_hash,
        mar_check_sum=mar_check_sum,
        skip_signing_scripts=skip_signing_scripts,
        client_insert=client_insert,
        scriptinsert=scriptinsert,
        module_place_id=module_place_id,
        serverplaceid=serverplaceid,
        expected_asset_type=expected_asset_type,
        accept_encoding=accept_encoding,
        roblox_place_id=roblox_place_id,
        asset_type=asset_type,
        accept=accept,
        asset_format=asset_format,
        roblox_asset_format=roblox_asset_format,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#assetdelivery_get_v1_marAssetHash__marAssetHash__marCheckSum__marCheckSum_"
)
def sync(
    mar_asset_hash: str,
    mar_check_sum: str,
    *,
    client: AuthenticatedClient,
    skip_signing_scripts: bool | Unset = False,
    client_insert: int | Unset = UNSET,
    scriptinsert: int | Unset = UNSET,
    module_place_id: int | Unset = UNSET,
    serverplaceid: int | Unset = UNSET,
    expected_asset_type: str | Unset = "",
    accept_encoding: str,
    roblox_place_id: int,
    asset_type: str,
    accept: str,
    asset_format: str,
    roblox_asset_format: str,
) -> Any | RobloxWebAssetsAssetResponseItemV1 | None:
    """Retrieves an asset by its mar (moderation agnostic) hash and mar (moderation agnostic) checksum.

    Args:
        mar_asset_hash (str):
        mar_check_sum (str):
        skip_signing_scripts (bool | Unset):  Default: False.
        client_insert (int | Unset):
        scriptinsert (int | Unset):
        module_place_id (int | Unset):
        serverplaceid (int | Unset):
        expected_asset_type (str | Unset):  Default: ''.
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
        Any | RobloxWebAssetsAssetResponseItemV1
    """

    return sync_detailed(
        mar_asset_hash=mar_asset_hash,
        mar_check_sum=mar_check_sum,
        client=client,
        skip_signing_scripts=skip_signing_scripts,
        client_insert=client_insert,
        scriptinsert=scriptinsert,
        module_place_id=module_place_id,
        serverplaceid=serverplaceid,
        expected_asset_type=expected_asset_type,
        accept_encoding=accept_encoding,
        roblox_place_id=roblox_place_id,
        asset_type=asset_type,
        accept=accept,
        asset_format=asset_format,
        roblox_asset_format=roblox_asset_format,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#assetdelivery_get_v1_marAssetHash__marAssetHash__marCheckSum__marCheckSum_"
)
async def asyncio_detailed(
    mar_asset_hash: str,
    mar_check_sum: str,
    *,
    client: AuthenticatedClient,
    skip_signing_scripts: bool | Unset = False,
    client_insert: int | Unset = UNSET,
    scriptinsert: int | Unset = UNSET,
    module_place_id: int | Unset = UNSET,
    serverplaceid: int | Unset = UNSET,
    expected_asset_type: str | Unset = "",
    accept_encoding: str,
    roblox_place_id: int,
    asset_type: str,
    accept: str,
    asset_format: str,
    roblox_asset_format: str,
) -> Response[Any | RobloxWebAssetsAssetResponseItemV1]:
    """Retrieves an asset by its mar (moderation agnostic) hash and mar (moderation agnostic) checksum.

    Args:
        mar_asset_hash (str):
        mar_check_sum (str):
        skip_signing_scripts (bool | Unset):  Default: False.
        client_insert (int | Unset):
        scriptinsert (int | Unset):
        module_place_id (int | Unset):
        serverplaceid (int | Unset):
        expected_asset_type (str | Unset):  Default: ''.
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
        Response[Any | RobloxWebAssetsAssetResponseItemV1]
    """

    kwargs = _get_kwargs(
        mar_asset_hash=mar_asset_hash,
        mar_check_sum=mar_check_sum,
        skip_signing_scripts=skip_signing_scripts,
        client_insert=client_insert,
        scriptinsert=scriptinsert,
        module_place_id=module_place_id,
        serverplaceid=serverplaceid,
        expected_asset_type=expected_asset_type,
        accept_encoding=accept_encoding,
        roblox_place_id=roblox_place_id,
        asset_type=asset_type,
        accept=accept,
        asset_format=asset_format,
        roblox_asset_format=roblox_asset_format,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#assetdelivery_get_v1_marAssetHash__marAssetHash__marCheckSum__marCheckSum_"
)
async def asyncio(
    mar_asset_hash: str,
    mar_check_sum: str,
    *,
    client: AuthenticatedClient,
    skip_signing_scripts: bool | Unset = False,
    client_insert: int | Unset = UNSET,
    scriptinsert: int | Unset = UNSET,
    module_place_id: int | Unset = UNSET,
    serverplaceid: int | Unset = UNSET,
    expected_asset_type: str | Unset = "",
    accept_encoding: str,
    roblox_place_id: int,
    asset_type: str,
    accept: str,
    asset_format: str,
    roblox_asset_format: str,
) -> Any | RobloxWebAssetsAssetResponseItemV1 | None:
    """Retrieves an asset by its mar (moderation agnostic) hash and mar (moderation agnostic) checksum.

    Args:
        mar_asset_hash (str):
        mar_check_sum (str):
        skip_signing_scripts (bool | Unset):  Default: False.
        client_insert (int | Unset):
        scriptinsert (int | Unset):
        module_place_id (int | Unset):
        serverplaceid (int | Unset):
        expected_asset_type (str | Unset):  Default: ''.
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
        Any | RobloxWebAssetsAssetResponseItemV1
    """

    return (
        await asyncio_detailed(
            mar_asset_hash=mar_asset_hash,
            mar_check_sum=mar_check_sum,
            client=client,
            skip_signing_scripts=skip_signing_scripts,
            client_insert=client_insert,
            scriptinsert=scriptinsert,
            module_place_id=module_place_id,
            serverplaceid=serverplaceid,
            expected_asset_type=expected_asset_type,
            accept_encoding=accept_encoding,
            roblox_place_id=roblox_place_id,
            asset_type=asset_type,
            accept=accept,
            asset_format=asset_format,
            roblox_asset_format=roblox_asset_format,
        )
    ).parsed
