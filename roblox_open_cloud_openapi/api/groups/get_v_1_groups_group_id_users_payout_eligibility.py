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


from ...models.roblox_economy_api_models_user_group_payout_eligibility_response_model import (
    RobloxEconomyApiModelsUserGroupPayoutEligibilityResponseModel,
)


def _get_kwargs(
    group_id: int,
    *,
    user_ids: list[int],
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_user_ids = user_ids

    params["userIds"] = json_user_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://economy.roblox.com/v1/groups/{group_id}/users-payout-eligibility".format(
            group_id=quote(str(group_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxEconomyApiModelsUserGroupPayoutEligibilityResponseModel | None:
    if response.status_code == 200:
        response_200 = RobloxEconomyApiModelsUserGroupPayoutEligibilityResponseModel.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxEconomyApiModelsUserGroupPayoutEligibilityResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    user_ids: list[int],
) -> Response[Any | RobloxEconomyApiModelsUserGroupPayoutEligibilityResponseModel]:
    """Gets the group payout eligibility for a group of users.

    Args:
        group_id (int):
        user_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxEconomyApiModelsUserGroupPayoutEligibilityResponseModel]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        user_ids=user_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
    user_ids: list[int],
) -> Any | RobloxEconomyApiModelsUserGroupPayoutEligibilityResponseModel | None:
    """Gets the group payout eligibility for a group of users.

    Args:
        group_id (int):
        user_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxEconomyApiModelsUserGroupPayoutEligibilityResponseModel
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        user_ids=user_ids,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    user_ids: list[int],
) -> Response[Any | RobloxEconomyApiModelsUserGroupPayoutEligibilityResponseModel]:
    """Gets the group payout eligibility for a group of users.

    Args:
        group_id (int):
        user_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxEconomyApiModelsUserGroupPayoutEligibilityResponseModel]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        user_ids=user_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
    user_ids: list[int],
) -> Any | RobloxEconomyApiModelsUserGroupPayoutEligibilityResponseModel | None:
    """Gets the group payout eligibility for a group of users.

    Args:
        group_id (int):
        user_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxEconomyApiModelsUserGroupPayoutEligibilityResponseModel
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            user_ids=user_ids,
        )
    ).parsed
