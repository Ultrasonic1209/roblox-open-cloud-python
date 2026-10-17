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
{'x-roblox-cloud-api-operation': True, 'x-roblox-cloud-api-operation-name': 'Get Asset', 'x-roblox-stability': 'BETA', 'x-roblox-scopes': [{'name': 'asset:read'}], 'x-roblox-cloud-api-operation-code-samples': [{'language': 'Get Asset without readMask', 'script': "curl --location --request GET 'https://apis.roblox.com/assets/v1/assets/{assetId}' \\\n--header 'x-api-key: {apiKey}'"}, {'language': 'Get Asset with readMask', 'script': "curl --location --request GET 'https://apis.roblox.com/assets/v1/assets/{assetId}?readMask={read_mask}' \\\n--header 'x-api-key: {apiKey}'"}], 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 120}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 120}}, 'x-roblox-engine-usability': {'apiKeyWithHttpService': True}}
"""


from ...models.asset import Asset
from ...types import Unset


def _get_kwargs(
    asset_id: str,
    *,
    read_mask: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["readMask"] = read_mask

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/assets/v1/assets/{asset_id}".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Asset | None:
    if response.status_code == 200:
        response_200 = Asset.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Asset]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient,
    read_mask: str | Unset = UNSET,
) -> Response[Any | Asset]:
    """Retrieve specific asset metadata. Include the `readMask` parameter for additional asset metadata.

     Retrieve specific asset metadata.

    Args:
        asset_id (str):
        read_mask (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Asset]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        read_mask=read_mask,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    *,
    client: AuthenticatedClient,
    read_mask: str | Unset = UNSET,
) -> Any | Asset | None:
    """Retrieve specific asset metadata. Include the `readMask` parameter for additional asset metadata.

     Retrieve specific asset metadata.

    Args:
        asset_id (str):
        read_mask (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Asset
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        read_mask=read_mask,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient,
    read_mask: str | Unset = UNSET,
) -> Response[Any | Asset]:
    """Retrieve specific asset metadata. Include the `readMask` parameter for additional asset metadata.

     Retrieve specific asset metadata.

    Args:
        asset_id (str):
        read_mask (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Asset]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        read_mask=read_mask,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    *,
    client: AuthenticatedClient,
    read_mask: str | Unset = UNSET,
) -> Any | Asset | None:
    """Retrieve specific asset metadata. Include the `readMask` parameter for additional asset metadata.

     Retrieve specific asset metadata.

    Args:
        asset_id (str):
        read_mask (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Asset
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            read_mask=read_mask,
        )
    ).parsed
