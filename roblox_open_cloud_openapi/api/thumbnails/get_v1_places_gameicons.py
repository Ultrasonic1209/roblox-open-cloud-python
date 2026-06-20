from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_places_gameicons_format import GetV1PlacesGameiconsFormat
from ...models.get_v1_places_gameicons_return_policy import GetV1PlacesGameiconsReturnPolicy
from ...models.get_v1_places_gameicons_size import GetV1PlacesGameiconsSize
from ...models.roblox_web_web_api_models_api_array_response_roblox_web_responses_thumbnails_thumbnail_response import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    place_ids: list[int],
    return_policy: GetV1PlacesGameiconsReturnPolicy | Unset = GetV1PlacesGameiconsReturnPolicy.PLACEHOLDER,
    size: GetV1PlacesGameiconsSize | Unset = GetV1PlacesGameiconsSize.VALUE_0,
    format_: GetV1PlacesGameiconsFormat | Unset = GetV1PlacesGameiconsFormat.PNG,
    is_circular: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_place_ids = place_ids

    params["placeIds"] = json_place_ids

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
        "url": "https://thumbnails.roblox.com/v1/places/gameicons",
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "STABLE",
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "get_v1_places_gameicons",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    place_ids: list[int],
    return_policy: GetV1PlacesGameiconsReturnPolicy | Unset = GetV1PlacesGameiconsReturnPolicy.PLACEHOLDER,
    size: GetV1PlacesGameiconsSize | Unset = GetV1PlacesGameiconsSize.VALUE_0,
    format_: GetV1PlacesGameiconsFormat | Unset = GetV1PlacesGameiconsFormat.PNG,
    is_circular: bool | Unset = False,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]:
    """Fetches game icon URLs for a list of places. Ids that do not correspond to a valid place will be
    filtered out.

    Args:
        place_ids (list[int]):
        return_policy (GetV1PlacesGameiconsReturnPolicy | Unset):  Default:
            GetV1PlacesGameiconsReturnPolicy.PLACEHOLDER.
        size (GetV1PlacesGameiconsSize | Unset):  Default: GetV1PlacesGameiconsSize.VALUE_0.
        format_ (GetV1PlacesGameiconsFormat | Unset):  Default: GetV1PlacesGameiconsFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]
    """

    kwargs = _get_kwargs(
        place_ids=place_ids,
        return_policy=return_policy,
        size=size,
        format_=format_,
        is_circular=is_circular,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    place_ids: list[int],
    return_policy: GetV1PlacesGameiconsReturnPolicy | Unset = GetV1PlacesGameiconsReturnPolicy.PLACEHOLDER,
    size: GetV1PlacesGameiconsSize | Unset = GetV1PlacesGameiconsSize.VALUE_0,
    format_: GetV1PlacesGameiconsFormat | Unset = GetV1PlacesGameiconsFormat.PNG,
    is_circular: bool | Unset = False,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse | None:
    """Fetches game icon URLs for a list of places. Ids that do not correspond to a valid place will be
    filtered out.

    Args:
        place_ids (list[int]):
        return_policy (GetV1PlacesGameiconsReturnPolicy | Unset):  Default:
            GetV1PlacesGameiconsReturnPolicy.PLACEHOLDER.
        size (GetV1PlacesGameiconsSize | Unset):  Default: GetV1PlacesGameiconsSize.VALUE_0.
        format_ (GetV1PlacesGameiconsFormat | Unset):  Default: GetV1PlacesGameiconsFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse
    """

    return sync_detailed(
        client=client,
        place_ids=place_ids,
        return_policy=return_policy,
        size=size,
        format_=format_,
        is_circular=is_circular,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    place_ids: list[int],
    return_policy: GetV1PlacesGameiconsReturnPolicy | Unset = GetV1PlacesGameiconsReturnPolicy.PLACEHOLDER,
    size: GetV1PlacesGameiconsSize | Unset = GetV1PlacesGameiconsSize.VALUE_0,
    format_: GetV1PlacesGameiconsFormat | Unset = GetV1PlacesGameiconsFormat.PNG,
    is_circular: bool | Unset = False,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]:
    """Fetches game icon URLs for a list of places. Ids that do not correspond to a valid place will be
    filtered out.

    Args:
        place_ids (list[int]):
        return_policy (GetV1PlacesGameiconsReturnPolicy | Unset):  Default:
            GetV1PlacesGameiconsReturnPolicy.PLACEHOLDER.
        size (GetV1PlacesGameiconsSize | Unset):  Default: GetV1PlacesGameiconsSize.VALUE_0.
        format_ (GetV1PlacesGameiconsFormat | Unset):  Default: GetV1PlacesGameiconsFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse]
    """

    kwargs = _get_kwargs(
        place_ids=place_ids,
        return_policy=return_policy,
        size=size,
        format_=format_,
        is_circular=is_circular,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    place_ids: list[int],
    return_policy: GetV1PlacesGameiconsReturnPolicy | Unset = GetV1PlacesGameiconsReturnPolicy.PLACEHOLDER,
    size: GetV1PlacesGameiconsSize | Unset = GetV1PlacesGameiconsSize.VALUE_0,
    format_: GetV1PlacesGameiconsFormat | Unset = GetV1PlacesGameiconsFormat.PNG,
    is_circular: bool | Unset = False,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse | None:
    """Fetches game icon URLs for a list of places. Ids that do not correspond to a valid place will be
    filtered out.

    Args:
        place_ids (list[int]):
        return_policy (GetV1PlacesGameiconsReturnPolicy | Unset):  Default:
            GetV1PlacesGameiconsReturnPolicy.PLACEHOLDER.
        size (GetV1PlacesGameiconsSize | Unset):  Default: GetV1PlacesGameiconsSize.VALUE_0.
        format_ (GetV1PlacesGameiconsFormat | Unset):  Default: GetV1PlacesGameiconsFormat.PNG.
        is_circular (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxWebResponsesThumbnailsThumbnailResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            place_ids=place_ids,
            return_policy=return_policy,
            size=size,
            format_=format_,
            is_circular=is_circular,
        )
    ).parsed
