from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_web_web_api_models_api_array_response_roblox_api_develop_models_game_template_model import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsGameTemplateModel,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/gametemplates",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsGameTemplateModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsGameTemplateModel.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsGameTemplateModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsGameTemplateModel]:
    """Gets a page of templates that can be used to start off making games.

     Templates subject to change without notice.
    Sort order of templates specified by Roblox.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsGameTemplateModel]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsGameTemplateModel | None:
    """Gets a page of templates that can be used to start off making games.

     Templates subject to change without notice.
    Sort order of templates specified by Roblox.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsGameTemplateModel
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsGameTemplateModel]:
    """Gets a page of templates that can be used to start off making games.

     Templates subject to change without notice.
    Sort order of templates specified by Roblox.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsGameTemplateModel]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsGameTemplateModel | None:
    """Gets a page of templates that can be used to start off making games.

     Templates subject to change without notice.
    Sort order of templates specified by Roblox.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsGameTemplateModel
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
