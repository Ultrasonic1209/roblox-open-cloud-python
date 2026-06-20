from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_contacts_api_request_set_user_tag_request_model import (
    RobloxContactsApiRequestSetUserTagRequestModel,
)
from ...models.roblox_contacts_api_response_set_user_tag_response_model import (
    RobloxContactsApiResponseSetUserTagResponseModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RobloxContactsApiRequestSetUserTagRequestModel
    | RobloxContactsApiRequestSetUserTagRequestModel
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://contacts.roblox.com/v1/user/tag",
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "post_v1_user_tag",
        },
    }

    if isinstance(body, RobloxContactsApiRequestSetUserTagRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxContactsApiRequestSetUserTagRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxContactsApiResponseSetUserTagResponseModel | None:
    if response.status_code == 200:
        response_200 = RobloxContactsApiResponseSetUserTagResponseModel.from_dict(response.json())

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

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxContactsApiResponseSetUserTagResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxContactsApiRequestSetUserTagRequestModel
    | RobloxContactsApiRequestSetUserTagRequestModel
    | Unset = UNSET,
) -> Response[Any | RobloxContactsApiResponseSetUserTagResponseModel]:
    """Sets the tag for a user

    Args:
        body (RobloxContactsApiRequestSetUserTagRequestModel):
        body (RobloxContactsApiRequestSetUserTagRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxContactsApiResponseSetUserTagResponseModel]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RobloxContactsApiRequestSetUserTagRequestModel
    | RobloxContactsApiRequestSetUserTagRequestModel
    | Unset = UNSET,
) -> Any | RobloxContactsApiResponseSetUserTagResponseModel | None:
    """Sets the tag for a user

    Args:
        body (RobloxContactsApiRequestSetUserTagRequestModel):
        body (RobloxContactsApiRequestSetUserTagRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxContactsApiResponseSetUserTagResponseModel
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxContactsApiRequestSetUserTagRequestModel
    | RobloxContactsApiRequestSetUserTagRequestModel
    | Unset = UNSET,
) -> Response[Any | RobloxContactsApiResponseSetUserTagResponseModel]:
    """Sets the tag for a user

    Args:
        body (RobloxContactsApiRequestSetUserTagRequestModel):
        body (RobloxContactsApiRequestSetUserTagRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxContactsApiResponseSetUserTagResponseModel]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxContactsApiRequestSetUserTagRequestModel
    | RobloxContactsApiRequestSetUserTagRequestModel
    | Unset = UNSET,
) -> Any | RobloxContactsApiResponseSetUserTagResponseModel | None:
    """Sets the tag for a user

    Args:
        body (RobloxContactsApiRequestSetUserTagRequestModel):
        body (RobloxContactsApiRequestSetUserTagRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxContactsApiResponseSetUserTagResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
