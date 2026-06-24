from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_games_icons_format import GetV1GamesIconsFormat
from ...models.get_v1_games_icons_return_policy import GetV1GamesIconsReturnPolicy
from ...models.get_v1_games_icons_size import GetV1GamesIconsSize
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    universe_ids: list[int],
    return_policy: GetV1GamesIconsReturnPolicy | Unset = GetV1GamesIconsReturnPolicy.PLACEHOLDER,
    size: GetV1GamesIconsSize | Unset = GetV1GamesIconsSize.VALUE_0,
    format_: GetV1GamesIconsFormat | Unset = GetV1GamesIconsFormat.PNG,
    is_circular: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_universe_ids = universe_ids

    params["universeIds"] = json_universe_ids

    json_return_policy: str | Unset = UNSET
    if not isinstance(return_policy, Unset):
        json_return_policy = return_policy.value

    params["returnPolicy"] = json_return_policy

    json_size: str | Unset = UNSET
    if not isinstance(size, Unset):
        json_size = size.value

    params["size"] = json_size

    json_format_: str | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params["isCircular"] = is_circular

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://thumbnails.roblox.com/v1/games/icons",
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "STABLE",
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "get_v1_games_icons",
        },
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 403:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int],
    return_policy: GetV1GamesIconsReturnPolicy | Unset = GetV1GamesIconsReturnPolicy.PLACEHOLDER,
    size: GetV1GamesIconsSize | Unset = GetV1GamesIconsSize.VALUE_0,
    format_: GetV1GamesIconsFormat | Unset = GetV1GamesIconsFormat.PNG,
    is_circular: bool | Unset = False,
) -> Response[Any]:
    """Fetches game icon URLs for a list of universes' root places. Ids that do not correspond to a valid
    universe will be filtered out.
    The ordering of the results is not guaranteed to be the same as the inputs. In order to correlated
    inputs with outputs please
    use the 'targetId' of the objects in the result array.

    Args:
        universe_ids (list[int]):
        return_policy (GetV1GamesIconsReturnPolicy | Unset):  Default:
            GetV1GamesIconsReturnPolicy.PLACEHOLDER.
        size (GetV1GamesIconsSize | Unset):  Default: GetV1GamesIconsSize.VALUE_0.
        format_ (GetV1GamesIconsFormat | Unset):  Default: GetV1GamesIconsFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        universe_ids=universe_ids,
        return_policy=return_policy,
        size=size,
        format_=format_,
        is_circular=is_circular,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int],
    return_policy: GetV1GamesIconsReturnPolicy | Unset = GetV1GamesIconsReturnPolicy.PLACEHOLDER,
    size: GetV1GamesIconsSize | Unset = GetV1GamesIconsSize.VALUE_0,
    format_: GetV1GamesIconsFormat | Unset = GetV1GamesIconsFormat.PNG,
    is_circular: bool | Unset = False,
) -> Response[Any]:
    """Fetches game icon URLs for a list of universes' root places. Ids that do not correspond to a valid
    universe will be filtered out.
    The ordering of the results is not guaranteed to be the same as the inputs. In order to correlated
    inputs with outputs please
    use the 'targetId' of the objects in the result array.

    Args:
        universe_ids (list[int]):
        return_policy (GetV1GamesIconsReturnPolicy | Unset):  Default:
            GetV1GamesIconsReturnPolicy.PLACEHOLDER.
        size (GetV1GamesIconsSize | Unset):  Default: GetV1GamesIconsSize.VALUE_0.
        format_ (GetV1GamesIconsFormat | Unset):  Default: GetV1GamesIconsFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        universe_ids=universe_ids,
        return_policy=return_policy,
        size=size,
        format_=format_,
        is_circular=is_circular,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)
