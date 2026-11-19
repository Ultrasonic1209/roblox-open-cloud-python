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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.roblox_economy_api_models_purchasable_detail_response import (
    RobloxEconomyApiModelsPurchasableDetailResponse,
)


def _get_kwargs(
    product_id: int,
    *,
    show_purchasable_opt: bool,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["showPurchasableOpt"] = show_purchasable_opt

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://economy.roblox.com/v1/products/{product_id}".format(
            product_id=quote(str(product_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxEconomyApiModelsPurchasableDetailResponse | None:
    if response.status_code == 200:
        response_200 = RobloxEconomyApiModelsPurchasableDetailResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxEconomyApiModelsPurchasableDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product_id: int,
    *,
    client: AuthenticatedClient,
    show_purchasable_opt: bool,
) -> Response[Any | RobloxEconomyApiModelsPurchasableDetailResponse]:
    """Retrieves the product purchasable details given its id.

    Args:
        product_id (int):
        show_purchasable_opt (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxEconomyApiModelsPurchasableDetailResponse]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        show_purchasable_opt=show_purchasable_opt,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product_id: int,
    *,
    client: AuthenticatedClient,
    show_purchasable_opt: bool,
) -> Any | RobloxEconomyApiModelsPurchasableDetailResponse | None:
    """Retrieves the product purchasable details given its id.

    Args:
        product_id (int):
        show_purchasable_opt (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxEconomyApiModelsPurchasableDetailResponse
    """

    return sync_detailed(
        product_id=product_id,
        client=client,
        show_purchasable_opt=show_purchasable_opt,
    ).parsed


async def asyncio_detailed(
    product_id: int,
    *,
    client: AuthenticatedClient,
    show_purchasable_opt: bool,
) -> Response[Any | RobloxEconomyApiModelsPurchasableDetailResponse]:
    """Retrieves the product purchasable details given its id.

    Args:
        product_id (int):
        show_purchasable_opt (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxEconomyApiModelsPurchasableDetailResponse]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        show_purchasable_opt=show_purchasable_opt,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_id: int,
    *,
    client: AuthenticatedClient,
    show_purchasable_opt: bool,
) -> Any | RobloxEconomyApiModelsPurchasableDetailResponse | None:
    """Retrieves the product purchasable details given its id.

    Args:
        product_id (int):
        show_purchasable_opt (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxEconomyApiModelsPurchasableDetailResponse
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
            show_purchasable_opt=show_purchasable_opt,
        )
    ).parsed
