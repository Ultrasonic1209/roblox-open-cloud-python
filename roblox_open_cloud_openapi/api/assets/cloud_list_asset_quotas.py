from http import HTTPStatus
from typing import TYPE_CHECKING, Any
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
{'x-roblox-scopes': [{'name': 'asset:read', 'description': 'Required for the user in the path.'}], 'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 60}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 60}}, 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.assets_upload_api_status import AssetsUploadApiStatus
from ...models.list_asset_quotas_response import ListAssetQuotasResponse
from ...types import Unset


def _get_kwargs(
    user_id: int,
    *,
    max_page_size: int | Unset = 10,
    page_token: str | Unset = "",
    filter_: str | Unset = "",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["maxPageSize"] = max_page_size

    params["pageToken"] = page_token

    params["filter"] = filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/users/{user_id}/asset-quotas".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AssetsUploadApiStatus | ListAssetQuotasResponse | None:
    if response.status_code == 200:
        response_200 = ListAssetQuotasResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AssetsUploadApiStatus.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AssetsUploadApiStatus.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AssetsUploadApiStatus.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AssetsUploadApiStatus | ListAssetQuotasResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = 10,
    page_token: str | Unset = "",
    filter_: str | Unset = "",
) -> Response[AssetsUploadApiStatus | ListAssetQuotasResponse]:
    """List Asset Quotas

     Returns a list of asset quotas.

    Args:
        user_id (int):
        max_page_size (int | Unset):  Default: 10.
        page_token (str | Unset):  Default: ''.
        filter_ (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetsUploadApiStatus | ListAssetQuotasResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        max_page_size=max_page_size,
        page_token=page_token,
        filter_=filter_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = 10,
    page_token: str | Unset = "",
    filter_: str | Unset = "",
) -> AssetsUploadApiStatus | ListAssetQuotasResponse | None:
    """List Asset Quotas

     Returns a list of asset quotas.

    Args:
        user_id (int):
        max_page_size (int | Unset):  Default: 10.
        page_token (str | Unset):  Default: ''.
        filter_ (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetsUploadApiStatus | ListAssetQuotasResponse
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        max_page_size=max_page_size,
        page_token=page_token,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = 10,
    page_token: str | Unset = "",
    filter_: str | Unset = "",
) -> Response[AssetsUploadApiStatus | ListAssetQuotasResponse]:
    """List Asset Quotas

     Returns a list of asset quotas.

    Args:
        user_id (int):
        max_page_size (int | Unset):  Default: 10.
        page_token (str | Unset):  Default: ''.
        filter_ (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetsUploadApiStatus | ListAssetQuotasResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        max_page_size=max_page_size,
        page_token=page_token,
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = 10,
    page_token: str | Unset = "",
    filter_: str | Unset = "",
) -> AssetsUploadApiStatus | ListAssetQuotasResponse | None:
    """List Asset Quotas

     Returns a list of asset quotas.

    Args:
        user_id (int):
        max_page_size (int | Unset):  Default: 10.
        page_token (str | Unset):  Default: ''.
        filter_ (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetsUploadApiStatus | ListAssetQuotasResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            max_page_size=max_page_size,
            page_token=page_token,
            filter_=filter_,
        )
    ).parsed
