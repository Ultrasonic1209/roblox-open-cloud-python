from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_friends_api_captcha_status_response_model import RobloxFriendsApiCaptchaStatusResponseModel
from ...models.roblox_web_captcha_models_request_captcha_token_request import (
    RobloxWebCaptchaModelsRequestCaptchaTokenRequest,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    target_user_id: int,
    *,
    body: RobloxWebCaptchaModelsRequestCaptchaTokenRequest
    | RobloxWebCaptchaModelsRequestCaptchaTokenRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://friends.roblox.com/v1/users/{target_user_id}/follow".format(
            target_user_id=quote(str(target_user_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "post_v1_users_targetUserId_follow",
        },
    }

    if isinstance(body, RobloxWebCaptchaModelsRequestCaptchaTokenRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxWebCaptchaModelsRequestCaptchaTokenRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxFriendsApiCaptchaStatusResponseModel | None:
    if response.status_code == 200:
        response_200 = RobloxFriendsApiCaptchaStatusResponseModel.from_dict(response.json())

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
) -> Response[Any | RobloxFriendsApiCaptchaStatusResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    target_user_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxWebCaptchaModelsRequestCaptchaTokenRequest
    | RobloxWebCaptchaModelsRequestCaptchaTokenRequest
    | Unset = UNSET,
) -> Response[Any | RobloxFriendsApiCaptchaStatusResponseModel]:
    """Creates the following between a user and user with targetUserId

    Args:
        target_user_id (int):
        body (RobloxWebCaptchaModelsRequestCaptchaTokenRequest | Unset):
        body (RobloxWebCaptchaModelsRequestCaptchaTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxFriendsApiCaptchaStatusResponseModel]
    """

    kwargs = _get_kwargs(
        target_user_id=target_user_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    target_user_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxWebCaptchaModelsRequestCaptchaTokenRequest
    | RobloxWebCaptchaModelsRequestCaptchaTokenRequest
    | Unset = UNSET,
) -> Any | RobloxFriendsApiCaptchaStatusResponseModel | None:
    """Creates the following between a user and user with targetUserId

    Args:
        target_user_id (int):
        body (RobloxWebCaptchaModelsRequestCaptchaTokenRequest | Unset):
        body (RobloxWebCaptchaModelsRequestCaptchaTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxFriendsApiCaptchaStatusResponseModel
    """

    return sync_detailed(
        target_user_id=target_user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    target_user_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxWebCaptchaModelsRequestCaptchaTokenRequest
    | RobloxWebCaptchaModelsRequestCaptchaTokenRequest
    | Unset = UNSET,
) -> Response[Any | RobloxFriendsApiCaptchaStatusResponseModel]:
    """Creates the following between a user and user with targetUserId

    Args:
        target_user_id (int):
        body (RobloxWebCaptchaModelsRequestCaptchaTokenRequest | Unset):
        body (RobloxWebCaptchaModelsRequestCaptchaTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxFriendsApiCaptchaStatusResponseModel]
    """

    kwargs = _get_kwargs(
        target_user_id=target_user_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    target_user_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxWebCaptchaModelsRequestCaptchaTokenRequest
    | RobloxWebCaptchaModelsRequestCaptchaTokenRequest
    | Unset = UNSET,
) -> Any | RobloxFriendsApiCaptchaStatusResponseModel | None:
    """Creates the following between a user and user with targetUserId

    Args:
        target_user_id (int):
        body (RobloxWebCaptchaModelsRequestCaptchaTokenRequest | Unset):
        body (RobloxWebCaptchaModelsRequestCaptchaTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxFriendsApiCaptchaStatusResponseModel
    """

    return (
        await asyncio_detailed(
            target_user_id=target_user_id,
            client=client,
            body=body,
        )
    ).parsed
