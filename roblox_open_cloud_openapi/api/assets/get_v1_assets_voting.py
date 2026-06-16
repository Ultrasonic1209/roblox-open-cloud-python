import sys
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_web_web_api_models_api_array_response_roblox_api_develop_models_response_asset_voting_model import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsResponseAssetVotingModel,
)


def _get_kwargs(
    *,
    asset_ids: list[int],
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_asset_ids = asset_ids

    params["assetIds"] = json_asset_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/voting",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsResponseAssetVotingModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsResponseAssetVotingModel.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsResponseAssetVotingModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#develop_get_v1_assets_voting"
)
def sync_detailed(
    *,
    client: AuthenticatedClient,
    asset_ids: list[int],
) -> Response[RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsResponseAssetVotingModel]:
    """Gets the voting information of the given assets

     Please use toolbox service to get asset voting information.

    Args:
        asset_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsResponseAssetVotingModel]
    """

    kwargs = _get_kwargs(
        asset_ids=asset_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#develop_get_v1_assets_voting"
)
def sync(
    *,
    client: AuthenticatedClient,
    asset_ids: list[int],
) -> RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsResponseAssetVotingModel | None:
    """Gets the voting information of the given assets

     Please use toolbox service to get asset voting information.

    Args:
        asset_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsResponseAssetVotingModel
    """

    return sync_detailed(
        client=client,
        asset_ids=asset_ids,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#develop_get_v1_assets_voting"
)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    asset_ids: list[int],
) -> Response[RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsResponseAssetVotingModel]:
    """Gets the voting information of the given assets

     Please use toolbox service to get asset voting information.

    Args:
        asset_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsResponseAssetVotingModel]
    """

    kwargs = _get_kwargs(
        asset_ids=asset_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#develop_get_v1_assets_voting"
)
async def asyncio(
    *,
    client: AuthenticatedClient,
    asset_ids: list[int],
) -> RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsResponseAssetVotingModel | None:
    """Gets the voting information of the given assets

     Please use toolbox service to get asset voting information.

    Args:
        asset_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsResponseAssetVotingModel
    """

    return (
        await asyncio_detailed(
            client=client,
            asset_ids=asset_ids,
        )
    ).parsed
