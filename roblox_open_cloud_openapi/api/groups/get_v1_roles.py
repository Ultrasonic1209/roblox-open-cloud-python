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
{'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.roblox_web_web_api_models_api_array_response_roblox_groups_api_group_role_detail_response import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupRoleDetailResponse,
)


def _get_kwargs(
    *,
    ids: list[int],
    include_private: bool,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids = ids

    params["ids"] = json_ids

    params["includePrivate"] = include_private

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://groups.roblox.com/v1/roles",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupRoleDetailResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupRoleDetailResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupRoleDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int],
    include_private: bool,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupRoleDetailResponse]:
    """Gets the Roles by their ids.

    Args:
        ids (list[int]):
        include_private (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupRoleDetailResponse]
    """

    kwargs = _get_kwargs(
        ids=ids,
        include_private=include_private,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int],
    include_private: bool,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupRoleDetailResponse | None:
    """Gets the Roles by their ids.

    Args:
        ids (list[int]):
        include_private (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupRoleDetailResponse
    """

    return sync_detailed(
        client=client,
        ids=ids,
        include_private=include_private,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int],
    include_private: bool,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupRoleDetailResponse]:
    """Gets the Roles by their ids.

    Args:
        ids (list[int]):
        include_private (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupRoleDetailResponse]
    """

    kwargs = _get_kwargs(
        ids=ids,
        include_private=include_private,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int],
    include_private: bool,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupRoleDetailResponse | None:
    """Gets the Roles by their ids.

    Args:
        ids (list[int]):
        include_private (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupRoleDetailResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            include_private=include_private,
        )
    ).parsed
