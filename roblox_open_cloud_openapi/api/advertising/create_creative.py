from http import HTTPStatus
from typing import TYPE_CHECKING, Any

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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 60}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 60}}, 'x-roblox-scopes': [{'name': 'ad.campaign:write'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.create_creative_request import CreateCreativeRequest
from ...models.creative import Creative
from ...models.error_envelope import ErrorEnvelope
from ...types import Unset


def _get_kwargs(
    *,
    body: CreateCreativeRequest,
    group_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["groupId"] = group_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ads-management/v1/creatives",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Creative | ErrorEnvelope | None:
    if response.status_code == 201:
        response_201 = Creative.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = ErrorEnvelope.from_dict(response.json())

        return response_409

    if response.status_code == 429:
        response_429 = ErrorEnvelope.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ErrorEnvelope.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Creative | ErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateCreativeRequest,
    group_id: str | Unset = UNSET,
) -> Response[Creative | ErrorEnvelope]:
    """Add an asset to the creative library

     Saves an existing Open Cloud image asset to the creative library ahead of campaign creation.
    Dimensions and moderation state are derived by the service. Registering an asset that is already
    active in the selected billing account's library returns 409 ALREADY_EXISTS, regardless of the
    supplied universeId. You cannot change an active entry's universeId by re-registering the asset.
    Archived entries are unarchived and updated with the supplied fields.

    Args:
        group_id (str | Unset):
        body (CreateCreativeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Creative | ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        body=body,
        group_id=group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateCreativeRequest,
    group_id: str | Unset = UNSET,
) -> Creative | ErrorEnvelope | None:
    """Add an asset to the creative library

     Saves an existing Open Cloud image asset to the creative library ahead of campaign creation.
    Dimensions and moderation state are derived by the service. Registering an asset that is already
    active in the selected billing account's library returns 409 ALREADY_EXISTS, regardless of the
    supplied universeId. You cannot change an active entry's universeId by re-registering the asset.
    Archived entries are unarchived and updated with the supplied fields.

    Args:
        group_id (str | Unset):
        body (CreateCreativeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Creative | ErrorEnvelope
    """

    return sync_detailed(
        client=client,
        body=body,
        group_id=group_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateCreativeRequest,
    group_id: str | Unset = UNSET,
) -> Response[Creative | ErrorEnvelope]:
    """Add an asset to the creative library

     Saves an existing Open Cloud image asset to the creative library ahead of campaign creation.
    Dimensions and moderation state are derived by the service. Registering an asset that is already
    active in the selected billing account's library returns 409 ALREADY_EXISTS, regardless of the
    supplied universeId. You cannot change an active entry's universeId by re-registering the asset.
    Archived entries are unarchived and updated with the supplied fields.

    Args:
        group_id (str | Unset):
        body (CreateCreativeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Creative | ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        body=body,
        group_id=group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateCreativeRequest,
    group_id: str | Unset = UNSET,
) -> Creative | ErrorEnvelope | None:
    """Add an asset to the creative library

     Saves an existing Open Cloud image asset to the creative library ahead of campaign creation.
    Dimensions and moderation state are derived by the service. Registering an asset that is already
    active in the selected billing account's library returns 409 ALREADY_EXISTS, regardless of the
    supplied universeId. You cannot change an active entry's universeId by re-registering the asset.
    Archived entries are unarchived and updated with the supplied fields.

    Args:
        group_id (str | Unset):
        body (CreateCreativeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Creative | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            group_id=group_id,
        )
    ).parsed
