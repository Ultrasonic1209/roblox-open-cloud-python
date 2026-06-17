from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_account_information_api_models_phone_request import RobloxAccountInformationApiModelsPhoneRequest
from ...models.roblox_web_web_api_api_empty_response_model import RobloxWebWebAPIApiEmptyResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RobloxAccountInformationApiModelsPhoneRequest | RobloxAccountInformationApiModelsPhoneRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://accountinformation.roblox.com/v1/phone/delete",
    }

    if isinstance(body, RobloxAccountInformationApiModelsPhoneRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxAccountInformationApiModelsPhoneRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIApiEmptyResponseModel.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

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
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAccountInformationApiModelsPhoneRequest | RobloxAccountInformationApiModelsPhoneRequest | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Delete Phone

    Args:
        body (RobloxAccountInformationApiModelsPhoneRequest): The phone request
        body (RobloxAccountInformationApiModelsPhoneRequest): The phone request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
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
    body: RobloxAccountInformationApiModelsPhoneRequest | RobloxAccountInformationApiModelsPhoneRequest | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Delete Phone

    Args:
        body (RobloxAccountInformationApiModelsPhoneRequest): The phone request
        body (RobloxAccountInformationApiModelsPhoneRequest): The phone request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAccountInformationApiModelsPhoneRequest | RobloxAccountInformationApiModelsPhoneRequest | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Delete Phone

    Args:
        body (RobloxAccountInformationApiModelsPhoneRequest): The phone request
        body (RobloxAccountInformationApiModelsPhoneRequest): The phone request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxAccountInformationApiModelsPhoneRequest | RobloxAccountInformationApiModelsPhoneRequest | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Delete Phone

    Args:
        body (RobloxAccountInformationApiModelsPhoneRequest): The phone request
        body (RobloxAccountInformationApiModelsPhoneRequest): The phone request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
