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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 100}}, 'x-roblox-scopes': [{'name': 'extended-services:write', 'targetResourceSpecifier': ''}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.delete_payment_profile_response import DeletePaymentProfileResponse


def _get_kwargs(
    user_id: int,
    *,
    payment_profile_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["paymentProfileId"] = payment_profile_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/service-efficiency-api/v1/payment_profiles/users/{user_id}".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeletePaymentProfileResponse | None:
    if response.status_code == 200:
        response_200 = DeletePaymentProfileResponse.from_dict(response.json())

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
) -> Response[Any | DeletePaymentProfileResponse]:
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
) -> Response[Any | DeletePaymentProfileResponse]:
    """Operation to Delete a Payment Profile for a User.

    Args:
        user_id (int):
        payment_profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeletePaymentProfileResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        payment_profile_id=payment_profile_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    payment_profile_id: str,
) -> Any | DeletePaymentProfileResponse | None:
    """Operation to Delete a Payment Profile for a User.

    Args:
        user_id (int):
        payment_profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeletePaymentProfileResponse
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        payment_profile_id=payment_profile_id,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    payment_profile_id: str,
) -> Response[Any | DeletePaymentProfileResponse]:
    """Operation to Delete a Payment Profile for a User.

    Args:
        user_id (int):
        payment_profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeletePaymentProfileResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        payment_profile_id=payment_profile_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    payment_profile_id: str,
) -> Any | DeletePaymentProfileResponse | None:
    """Operation to Delete a Payment Profile for a User.

    Args:
        user_id (int):
        payment_profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeletePaymentProfileResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            payment_profile_id=payment_profile_id,
        )
    ).parsed
