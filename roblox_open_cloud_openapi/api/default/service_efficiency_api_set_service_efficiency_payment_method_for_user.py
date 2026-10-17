from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_service_efficiency_payment_method_response import SetServiceEfficiencyPaymentMethodResponse
from ...types import UNSET, Response


def _get_kwargs(
    user_id: int,
    *,
    payment_profile_id: str,
    payment_profile_owner_type: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["paymentProfileId"] = payment_profile_id

    params["paymentProfileOwnerType"] = payment_profile_owner_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/service-efficiency-api/v1/payment_profiles/users/{user_id}/service_efficiency".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "EXPERIMENTAL",
                "x-roblox-rate-limits": {"perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100}},
                "x-roblox-scopes": [{"name": "extended-services:write", "targetResourceSpecifier": ""}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "ServiceEfficiencyApi_SetServiceEfficiencyPaymentMethodForUser",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | SetServiceEfficiencyPaymentMethodResponse | None:
    if response.status_code == 200:
        response_200 = SetServiceEfficiencyPaymentMethodResponse.from_dict(response.json())

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

    if response.status_code == 412:
        response_412 = cast(Any, None)
        return response_412

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
) -> Response[Any | SetServiceEfficiencyPaymentMethodResponse]:
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
    payment_profile_id: str,
    payment_profile_owner_type: str,
) -> Response[Any | SetServiceEfficiencyPaymentMethodResponse]:
    """Operation to Set the Service Efficiency Payment Method for a User.

    Args:
        user_id (int):
        payment_profile_id (str):
        payment_profile_owner_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetServiceEfficiencyPaymentMethodResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        payment_profile_id=payment_profile_id,
        payment_profile_owner_type=payment_profile_owner_type,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    payment_profile_id: str,
    payment_profile_owner_type: str,
) -> Any | SetServiceEfficiencyPaymentMethodResponse | None:
    """Operation to Set the Service Efficiency Payment Method for a User.

    Args:
        user_id (int):
        payment_profile_id (str):
        payment_profile_owner_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetServiceEfficiencyPaymentMethodResponse
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        payment_profile_id=payment_profile_id,
        payment_profile_owner_type=payment_profile_owner_type,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    payment_profile_id: str,
    payment_profile_owner_type: str,
) -> Response[Any | SetServiceEfficiencyPaymentMethodResponse]:
    """Operation to Set the Service Efficiency Payment Method for a User.

    Args:
        user_id (int):
        payment_profile_id (str):
        payment_profile_owner_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetServiceEfficiencyPaymentMethodResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        payment_profile_id=payment_profile_id,
        payment_profile_owner_type=payment_profile_owner_type,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    payment_profile_id: str,
    payment_profile_owner_type: str,
) -> Any | SetServiceEfficiencyPaymentMethodResponse | None:
    """Operation to Set the Service Efficiency Payment Method for a User.

    Args:
        user_id (int):
        payment_profile_id (str):
        payment_profile_owner_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetServiceEfficiencyPaymentMethodResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            payment_profile_id=payment_profile_id,
            payment_profile_owner_type=payment_profile_owner_type,
        )
    ).parsed
