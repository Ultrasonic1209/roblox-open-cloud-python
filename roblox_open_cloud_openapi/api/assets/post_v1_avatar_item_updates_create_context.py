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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'SECOND', 'maxInPeriod': 10}}, 'x-roblox-scopes': [{'name': 'marketplace.item:write', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.roblox_item_configuration_api_models_request_avatar_item_update_create_avatar_item_update_context_request import (
    RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContextRequest,
)
from ...models.roblox_item_configuration_api_models_response_avatar_item_update_create_avatar_item_update_context_response import (
    RobloxItemConfigurationApiModelsResponseAvatarItemUpdateCreateAvatarItemUpdateContextResponse,
)


def _get_kwargs(
    *,
    body: RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContextRequest
    | RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContextRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://itemconfiguration.roblox.com/v1/avatar-item-updates/create-context",
    }

    if isinstance(body, RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContextRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContextRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxItemConfigurationApiModelsResponseAvatarItemUpdateCreateAvatarItemUpdateContextResponse | None:
    if response.status_code == 200:
        response_200 = (
            RobloxItemConfigurationApiModelsResponseAvatarItemUpdateCreateAvatarItemUpdateContextResponse.from_dict(
                response.json()
            )
        )

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

    if response.status_code == 408:
        response_408 = cast(Any, None)
        return response_408

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxItemConfigurationApiModelsResponseAvatarItemUpdateCreateAvatarItemUpdateContextResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContextRequest
    | RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContextRequest
    | Unset = UNSET,
) -> Response[Any | RobloxItemConfigurationApiModelsResponseAvatarItemUpdateCreateAvatarItemUpdateContextResponse]:
    """Mint an avatar item update context (parent operation) for an existing catalog item. Studio
    threads the returned operationId as the ParentOperationId of the staging asset upload.

    Args:
        body (RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContext
            Request): DTO of the incoming request from the client to create an avatar item update
            context, which mints
            the parent update operation for an existing catalog avatar item.
        body (RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContext
            Request): DTO of the incoming request from the client to create an avatar item update
            context, which mints
            the parent update operation for an existing catalog avatar item.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiModelsResponseAvatarItemUpdateCreateAvatarItemUpdateContextResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContextRequest
    | RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContextRequest
    | Unset = UNSET,
) -> Any | RobloxItemConfigurationApiModelsResponseAvatarItemUpdateCreateAvatarItemUpdateContextResponse | None:
    """Mint an avatar item update context (parent operation) for an existing catalog item. Studio
    threads the returned operationId as the ParentOperationId of the staging asset upload.

    Args:
        body (RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContext
            Request): DTO of the incoming request from the client to create an avatar item update
            context, which mints
            the parent update operation for an existing catalog avatar item.
        body (RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContext
            Request): DTO of the incoming request from the client to create an avatar item update
            context, which mints
            the parent update operation for an existing catalog avatar item.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiModelsResponseAvatarItemUpdateCreateAvatarItemUpdateContextResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContextRequest
    | RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContextRequest
    | Unset = UNSET,
) -> Response[Any | RobloxItemConfigurationApiModelsResponseAvatarItemUpdateCreateAvatarItemUpdateContextResponse]:
    """Mint an avatar item update context (parent operation) for an existing catalog item. Studio
    threads the returned operationId as the ParentOperationId of the staging asset upload.

    Args:
        body (RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContext
            Request): DTO of the incoming request from the client to create an avatar item update
            context, which mints
            the parent update operation for an existing catalog avatar item.
        body (RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContext
            Request): DTO of the incoming request from the client to create an avatar item update
            context, which mints
            the parent update operation for an existing catalog avatar item.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiModelsResponseAvatarItemUpdateCreateAvatarItemUpdateContextResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContextRequest
    | RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContextRequest
    | Unset = UNSET,
) -> Any | RobloxItemConfigurationApiModelsResponseAvatarItemUpdateCreateAvatarItemUpdateContextResponse | None:
    """Mint an avatar item update context (parent operation) for an existing catalog item. Studio
    threads the returned operationId as the ParentOperationId of the staging asset upload.

    Args:
        body (RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContext
            Request): DTO of the incoming request from the client to create an avatar item update
            context, which mints
            the parent update operation for an existing catalog avatar item.
        body (RobloxItemConfigurationApiModelsRequestAvatarItemUpdateCreateAvatarItemUpdateContext
            Request): DTO of the incoming request from the client to create an avatar item update
            context, which mints
            the parent update operation for an existing catalog avatar item.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiModelsResponseAvatarItemUpdateCreateAvatarItemUpdateContextResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
