from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_save_request_type_0 import CreateSaveRequestType0
from ...models.problem_details_type_0 import ProblemDetailsType0
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateSaveRequestType0
    | None
    | CreateSaveRequestType0
    | None
    | CreateSaveRequestType0
    | None
    | CreateSaveRequestType0
    | None
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/toolbox-service/v1/saves",
        "openapi-extensions": {
            "x-roblox-stability": "BETA",
            "x-roblox-rate-limits": {
                "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 200},
                "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 200},
            },
            "x-roblox-scopes": [{"name": "creator-store-save:write", "targetResourceSpecifier": ""}],
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
        },
        "openapi-id": "Saves_CreateSave",
    }

    if isinstance(body, CreateSaveRequestType0 | None):
        if isinstance(body, CreateSaveRequestType0):
            _kwargs["json"] = body.to_dict()
        else:
            _kwargs["json"] = body

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, CreateSaveRequestType0 | None):
        if isinstance(body, CreateSaveRequestType0):
            _kwargs["json"] = body.to_dict()
        else:
            _kwargs["json"] = body

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateSaveRequestType0 | None):
        if isinstance(body, CreateSaveRequestType0):
            _kwargs["json"] = body.to_dict()
        else:
            _kwargs["json"] = body

        headers["Content-Type"] = "text/json"
    if isinstance(body, CreateSaveRequestType0 | None):
        if isinstance(body, CreateSaveRequestType0):
            _kwargs["json"] = body.to_dict()
        else:
            _kwargs["json"] = body

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | None | ProblemDetailsType0 | None:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 400:

        def _parse_response_400(data: object) -> None | ProblemDetailsType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_problem_details_type_0 = ProblemDetailsType0.from_dict(data)

                return componentsschemas_problem_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProblemDetailsType0, data)

        response_400 = _parse_response_400(response.json())

        return response_400

    if response.status_code == 404:

        def _parse_response_404(data: object) -> None | ProblemDetailsType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_problem_details_type_0 = ProblemDetailsType0.from_dict(data)

                return componentsschemas_problem_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProblemDetailsType0, data)

        response_404 = _parse_response_404(response.json())

        return response_404

    if response.status_code == 409:

        def _parse_response_409(data: object) -> None | ProblemDetailsType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_problem_details_type_0 = ProblemDetailsType0.from_dict(data)

                return componentsschemas_problem_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProblemDetailsType0, data)

        response_409 = _parse_response_409(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | None | ProblemDetailsType0]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateSaveRequestType0
    | None
    | CreateSaveRequestType0
    | None
    | CreateSaveRequestType0
    | None
    | CreateSaveRequestType0
    | None
    | Unset = UNSET,
) -> Response[Any | None | ProblemDetailsType0]:
    """Creates a save.

    Args:
        body (CreateSaveRequestType0 | None | Unset): Request model for creating a save
        body (CreateSaveRequestType0 | None | Unset): Request model for creating a save
        body (CreateSaveRequestType0 | None | Unset): Request model for creating a save
        body (CreateSaveRequestType0 | None | Unset): Request model for creating a save

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | None | ProblemDetailsType0]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateSaveRequestType0
    | None
    | CreateSaveRequestType0
    | None
    | CreateSaveRequestType0
    | None
    | CreateSaveRequestType0
    | None
    | Unset = UNSET,
) -> Any | None | ProblemDetailsType0 | None:
    """Creates a save.

    Args:
        body (CreateSaveRequestType0 | None | Unset): Request model for creating a save
        body (CreateSaveRequestType0 | None | Unset): Request model for creating a save
        body (CreateSaveRequestType0 | None | Unset): Request model for creating a save
        body (CreateSaveRequestType0 | None | Unset): Request model for creating a save

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | None | ProblemDetailsType0
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateSaveRequestType0
    | None
    | CreateSaveRequestType0
    | None
    | CreateSaveRequestType0
    | None
    | CreateSaveRequestType0
    | None
    | Unset = UNSET,
) -> Response[Any | None | ProblemDetailsType0]:
    """Creates a save.

    Args:
        body (CreateSaveRequestType0 | None | Unset): Request model for creating a save
        body (CreateSaveRequestType0 | None | Unset): Request model for creating a save
        body (CreateSaveRequestType0 | None | Unset): Request model for creating a save
        body (CreateSaveRequestType0 | None | Unset): Request model for creating a save

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | None | ProblemDetailsType0]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateSaveRequestType0
    | None
    | CreateSaveRequestType0
    | None
    | CreateSaveRequestType0
    | None
    | CreateSaveRequestType0
    | None
    | Unset = UNSET,
) -> Any | None | ProblemDetailsType0 | None:
    """Creates a save.

    Args:
        body (CreateSaveRequestType0 | None | Unset): Request model for creating a save
        body (CreateSaveRequestType0 | None | Unset): Request model for creating a save
        body (CreateSaveRequestType0 | None | Unset): Request model for creating a save
        body (CreateSaveRequestType0 | None | Unset): Request model for creating a save

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | None | ProblemDetailsType0
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
