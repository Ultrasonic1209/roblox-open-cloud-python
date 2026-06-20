from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cloud_get_subscription_view import CloudGetSubscriptionView
from ...models.subscription import Subscription
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: str,
    subscription_product_id: str,
    subscription_id: str,
    *,
    view: CloudGetSubscriptionView | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_view: str | Unset = UNSET
    if not isinstance(view, Unset):
        json_view = view.value

    params["view"] = json_view

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/universes/{universe_id}/subscription-products/{subscription_product_id}/subscriptions/{subscription_id}".format(
            universe_id=quote(str(universe_id), safe=""),
            subscription_product_id=quote(str(subscription_product_id), safe=""),
            subscription_id=quote(str(subscription_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
                "x-roblox-scopes": [
                    {"name": "universe:write"},
                    {"name": "universe.subscription-product.subscription:read"},
                ],
                "x-roblox-docs": {
                    "category": "Monetization",
                    "methodProperties": {
                        "scopes": ["universe:write", "universe.subscription-product.subscription:read"]
                    },
                    "resource": {"$ref": "#/components/schemas/Subscription", "name": "Subscription"},
                },
                "x-roblox-stability": "BETA",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 500},
                    "perOauth2Authorization": {"period": "SECOND", "maxInPeriod": 3},
                },
            },
            "openapi-id": "Cloud_GetSubscription",
        },
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Subscription | None:
    if response.status_code == 200:
        response_200 = Subscription.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Subscription]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    subscription_product_id: str,
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    view: CloudGetSubscriptionView | Unset = UNSET,
) -> Response[Subscription]:
    """Get Subscription

     Get the subscription.

    The `universe.subscription-product.subscription:read` scope only allows
    reading subscriptions of the user making the request. Because of this, the
    subscription ID must match the user ID of the user making the request. Note
    that this scope might be more relevant for OAuth 2.0 apps.

    To read all subscriptions made by users for a particular universe, use the
    `universe:write` scope instead.

    Args:
        universe_id (str):
        subscription_product_id (str):
        subscription_id (str):
        view (CloudGetSubscriptionView | Unset):  Example: VIEW_UNSPECIFIED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Subscription]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        subscription_product_id=subscription_product_id,
        subscription_id=subscription_id,
        view=view,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    subscription_product_id: str,
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    view: CloudGetSubscriptionView | Unset = UNSET,
) -> Subscription | None:
    """Get Subscription

     Get the subscription.

    The `universe.subscription-product.subscription:read` scope only allows
    reading subscriptions of the user making the request. Because of this, the
    subscription ID must match the user ID of the user making the request. Note
    that this scope might be more relevant for OAuth 2.0 apps.

    To read all subscriptions made by users for a particular universe, use the
    `universe:write` scope instead.

    Args:
        universe_id (str):
        subscription_product_id (str):
        subscription_id (str):
        view (CloudGetSubscriptionView | Unset):  Example: VIEW_UNSPECIFIED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Subscription
    """

    return sync_detailed(
        universe_id=universe_id,
        subscription_product_id=subscription_product_id,
        subscription_id=subscription_id,
        client=client,
        view=view,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    subscription_product_id: str,
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    view: CloudGetSubscriptionView | Unset = UNSET,
) -> Response[Subscription]:
    """Get Subscription

     Get the subscription.

    The `universe.subscription-product.subscription:read` scope only allows
    reading subscriptions of the user making the request. Because of this, the
    subscription ID must match the user ID of the user making the request. Note
    that this scope might be more relevant for OAuth 2.0 apps.

    To read all subscriptions made by users for a particular universe, use the
    `universe:write` scope instead.

    Args:
        universe_id (str):
        subscription_product_id (str):
        subscription_id (str):
        view (CloudGetSubscriptionView | Unset):  Example: VIEW_UNSPECIFIED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Subscription]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        subscription_product_id=subscription_product_id,
        subscription_id=subscription_id,
        view=view,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    subscription_product_id: str,
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    view: CloudGetSubscriptionView | Unset = UNSET,
) -> Subscription | None:
    """Get Subscription

     Get the subscription.

    The `universe.subscription-product.subscription:read` scope only allows
    reading subscriptions of the user making the request. Because of this, the
    subscription ID must match the user ID of the user making the request. Note
    that this scope might be more relevant for OAuth 2.0 apps.

    To read all subscriptions made by users for a particular universe, use the
    `universe:write` scope instead.

    Args:
        universe_id (str):
        subscription_product_id (str):
        subscription_id (str):
        view (CloudGetSubscriptionView | Unset):  Example: VIEW_UNSPECIFIED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Subscription
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            subscription_product_id=subscription_product_id,
            subscription_id=subscription_id,
            client=client,
            view=view,
        )
    ).parsed
