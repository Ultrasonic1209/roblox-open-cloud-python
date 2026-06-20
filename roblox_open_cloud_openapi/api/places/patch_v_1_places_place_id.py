import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_api_develop_models_place_configuration_model import RobloxApiDevelopModelsPlaceConfigurationModel
from ...models.roblox_api_develop_models_place_model import RobloxApiDevelopModelsPlaceModel


def _get_kwargs(
    place_id: int,
    *,
    body: RobloxApiDevelopModelsPlaceConfigurationModel | RobloxApiDevelopModelsPlaceConfigurationModel | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "https://develop.roblox.com/v1/places/{place_id}".format(
            place_id=quote(str(place_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
                "x-roblox-recommended-alternatives": [
                    {
                        "url": "https://develop.roblox.com/v2/places/{placeId}",
                        "httpMethod": "PATCH",
                        "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/places#develop_patch_v2_places__placeId_",
                    }
                ],
            },
            "openapi-id": "patch_v1_places_placeId",
        },
    }

    if isinstance(body, RobloxApiDevelopModelsPlaceConfigurationModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxApiDevelopModelsPlaceConfigurationModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxApiDevelopModelsPlaceModel | None:
    if response.status_code == 200:
        response_200 = RobloxApiDevelopModelsPlaceModel.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxApiDevelopModelsPlaceModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/places#develop_patch_v1_places__placeId_"
)
def sync_detailed(
    place_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxApiDevelopModelsPlaceConfigurationModel | RobloxApiDevelopModelsPlaceConfigurationModel | Unset = UNSET,
) -> Response[Any | RobloxApiDevelopModelsPlaceModel]:
    """Updates the place configuration for the place with the id placeId

     Currently the only supported functionality for updating the configuration is around Name, and
    Description.

    Args:
        place_id (int):
        body (RobloxApiDevelopModelsPlaceConfigurationModel): A model containing information about
            a place to be configured
        body (RobloxApiDevelopModelsPlaceConfigurationModel): A model containing information about
            a place to be configured

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiDevelopModelsPlaceModel]
    """

    kwargs = _get_kwargs(
        place_id=place_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/places#develop_patch_v1_places__placeId_"
)
def sync(
    place_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxApiDevelopModelsPlaceConfigurationModel | RobloxApiDevelopModelsPlaceConfigurationModel | Unset = UNSET,
) -> Any | RobloxApiDevelopModelsPlaceModel | None:
    """Updates the place configuration for the place with the id placeId

     Currently the only supported functionality for updating the configuration is around Name, and
    Description.

    Args:
        place_id (int):
        body (RobloxApiDevelopModelsPlaceConfigurationModel): A model containing information about
            a place to be configured
        body (RobloxApiDevelopModelsPlaceConfigurationModel): A model containing information about
            a place to be configured

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiDevelopModelsPlaceModel
    """

    return sync_detailed(
        place_id=place_id,
        client=client,
        body=body,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/places#develop_patch_v1_places__placeId_"
)
async def asyncio_detailed(
    place_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxApiDevelopModelsPlaceConfigurationModel | RobloxApiDevelopModelsPlaceConfigurationModel | Unset = UNSET,
) -> Response[Any | RobloxApiDevelopModelsPlaceModel]:
    """Updates the place configuration for the place with the id placeId

     Currently the only supported functionality for updating the configuration is around Name, and
    Description.

    Args:
        place_id (int):
        body (RobloxApiDevelopModelsPlaceConfigurationModel): A model containing information about
            a place to be configured
        body (RobloxApiDevelopModelsPlaceConfigurationModel): A model containing information about
            a place to be configured

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiDevelopModelsPlaceModel]
    """

    kwargs = _get_kwargs(
        place_id=place_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/places#develop_patch_v1_places__placeId_"
)
async def asyncio(
    place_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxApiDevelopModelsPlaceConfigurationModel | RobloxApiDevelopModelsPlaceConfigurationModel | Unset = UNSET,
) -> Any | RobloxApiDevelopModelsPlaceModel | None:
    """Updates the place configuration for the place with the id placeId

     Currently the only supported functionality for updating the configuration is around Name, and
    Description.

    Args:
        place_id (int):
        body (RobloxApiDevelopModelsPlaceConfigurationModel): A model containing information about
            a place to be configured
        body (RobloxApiDevelopModelsPlaceConfigurationModel): A model containing information about
            a place to be configured

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiDevelopModelsPlaceModel
    """

    return (
        await asyncio_detailed(
            place_id=place_id,
            client=client,
            body=body,
        )
    ).parsed
