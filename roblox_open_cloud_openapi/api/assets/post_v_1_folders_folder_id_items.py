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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'SECOND', 'maxInPeriod': 1}}, 'x-roblox-scopes': [{'name': 'marketplace.item:write', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.roblox_item_configuration_api_models_request_folder_add_items_request import (
    RobloxItemConfigurationApiModelsRequestFolderAddItemsRequest,
)
from ...models.roblox_web_web_api_api_empty_response_model import RobloxWebWebAPIApiEmptyResponseModel


def _get_kwargs(
    folder_id: str,
    *,
    body: RobloxItemConfigurationApiModelsRequestFolderAddItemsRequest
    | RobloxItemConfigurationApiModelsRequestFolderAddItemsRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://itemconfiguration.roblox.com/v1/folders/{folder_id}/items".format(
            folder_id=quote(str(folder_id), safe=""),
        ),
    }

    if isinstance(body, RobloxItemConfigurationApiModelsRequestFolderAddItemsRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxItemConfigurationApiModelsRequestFolderAddItemsRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIApiEmptyResponseModel.from_dict(response.json())

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

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    folder_id: str,
    *,
    client: AuthenticatedClient,
    body: RobloxItemConfigurationApiModelsRequestFolderAddItemsRequest
    | RobloxItemConfigurationApiModelsRequestFolderAddItemsRequest
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Adds one or more items to a folder.

    Args:
        folder_id (str):
        body (RobloxItemConfigurationApiModelsRequestFolderAddItemsRequest): Request model for
            adding one or more items to a folder.
        body (RobloxItemConfigurationApiModelsRequestFolderAddItemsRequest): Request model for
            adding one or more items to a folder.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        folder_id=folder_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    folder_id: str,
    *,
    client: AuthenticatedClient,
    body: RobloxItemConfigurationApiModelsRequestFolderAddItemsRequest
    | RobloxItemConfigurationApiModelsRequestFolderAddItemsRequest
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Adds one or more items to a folder.

    Args:
        folder_id (str):
        body (RobloxItemConfigurationApiModelsRequestFolderAddItemsRequest): Request model for
            adding one or more items to a folder.
        body (RobloxItemConfigurationApiModelsRequestFolderAddItemsRequest): Request model for
            adding one or more items to a folder.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return sync_detailed(
        folder_id=folder_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    folder_id: str,
    *,
    client: AuthenticatedClient,
    body: RobloxItemConfigurationApiModelsRequestFolderAddItemsRequest
    | RobloxItemConfigurationApiModelsRequestFolderAddItemsRequest
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Adds one or more items to a folder.

    Args:
        folder_id (str):
        body (RobloxItemConfigurationApiModelsRequestFolderAddItemsRequest): Request model for
            adding one or more items to a folder.
        body (RobloxItemConfigurationApiModelsRequestFolderAddItemsRequest): Request model for
            adding one or more items to a folder.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        folder_id=folder_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    folder_id: str,
    *,
    client: AuthenticatedClient,
    body: RobloxItemConfigurationApiModelsRequestFolderAddItemsRequest
    | RobloxItemConfigurationApiModelsRequestFolderAddItemsRequest
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Adds one or more items to a folder.

    Args:
        folder_id (str):
        body (RobloxItemConfigurationApiModelsRequestFolderAddItemsRequest): Request model for
            adding one or more items to a folder.
        body (RobloxItemConfigurationApiModelsRequestFolderAddItemsRequest): Request model for
            adding one or more items to a folder.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return (
        await asyncio_detailed(
            folder_id=folder_id,
            client=client,
            body=body,
        )
    ).parsed
