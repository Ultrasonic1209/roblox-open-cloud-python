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
{'x-roblox-recommended-alternatives': [{'url': 'https://apis.roblox.com/cloud/v2/users/{user_id}/asset-quotas', 'httpMethod': 'GET'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""

import sys

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_publish_api_asset_quotas_response import RobloxPublishApiAssetQuotasResponse
from ...types import Unset


def _get_kwargs(
    *,
    resource_type: str,
    asset_type: str,
    use_dummy_data: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["resourceType"] = resource_type

    params["assetType"] = asset_type

    params["useDummyData"] = use_dummy_data

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://publish.roblox.com/v1/asset-quotas",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxPublishApiAssetQuotasResponse | None:
    if response.status_code == 200:
        response_200 = RobloxPublishApiAssetQuotasResponse.from_dict(response.json())

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
) -> Response[Any | RobloxPublishApiAssetQuotasResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#publish_get_v1_asset_quotas"
)
def sync_detailed(
    *,
    client: AuthenticatedClient,
    resource_type: str,
    asset_type: str,
    use_dummy_data: bool | Unset = False,
) -> Response[Any | RobloxPublishApiAssetQuotasResponse]:
    """List asset quotas of the given resource type and asset type.

    Args:
        resource_type (str):
        asset_type (str):
        use_dummy_data (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxPublishApiAssetQuotasResponse]
    """

    kwargs = _get_kwargs(
        resource_type=resource_type,
        asset_type=asset_type,
        use_dummy_data=use_dummy_data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#publish_get_v1_asset_quotas"
)
def sync(
    *,
    client: AuthenticatedClient,
    resource_type: str,
    asset_type: str,
    use_dummy_data: bool | Unset = False,
) -> Any | RobloxPublishApiAssetQuotasResponse | None:
    """List asset quotas of the given resource type and asset type.

    Args:
        resource_type (str):
        asset_type (str):
        use_dummy_data (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxPublishApiAssetQuotasResponse
    """

    return sync_detailed(
        client=client,
        resource_type=resource_type,
        asset_type=asset_type,
        use_dummy_data=use_dummy_data,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#publish_get_v1_asset_quotas"
)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    resource_type: str,
    asset_type: str,
    use_dummy_data: bool | Unset = False,
) -> Response[Any | RobloxPublishApiAssetQuotasResponse]:
    """List asset quotas of the given resource type and asset type.

    Args:
        resource_type (str):
        asset_type (str):
        use_dummy_data (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxPublishApiAssetQuotasResponse]
    """

    kwargs = _get_kwargs(
        resource_type=resource_type,
        asset_type=asset_type,
        use_dummy_data=use_dummy_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#publish_get_v1_asset_quotas"
)
async def asyncio(
    *,
    client: AuthenticatedClient,
    resource_type: str,
    asset_type: str,
    use_dummy_data: bool | Unset = False,
) -> Any | RobloxPublishApiAssetQuotasResponse | None:
    """List asset quotas of the given resource type and asset type.

    Args:
        resource_type (str):
        asset_type (str):
        use_dummy_data (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxPublishApiAssetQuotasResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            resource_type=resource_type,
            asset_type=asset_type,
            use_dummy_data=use_dummy_data,
        )
    ).parsed
