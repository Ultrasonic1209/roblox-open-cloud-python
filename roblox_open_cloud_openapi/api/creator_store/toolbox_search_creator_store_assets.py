from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details_type_0 import ProblemDetailsType0
from ...models.search_creator_store_assets_request_type_0 import SearchCreatorStoreAssetsRequestType0
from ...models.search_creator_store_assets_response_type_0 import SearchCreatorStoreAssetsResponseType0
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: None
    | SearchCreatorStoreAssetsRequestType0
    | None
    | SearchCreatorStoreAssetsRequestType0
    | None
    | SearchCreatorStoreAssetsRequestType0
    | None
    | SearchCreatorStoreAssetsRequestType0
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/toolbox-service/v2/assets:search",
    }

    if isinstance(body, None | SearchCreatorStoreAssetsRequestType0):
        if isinstance(body, SearchCreatorStoreAssetsRequestType0):
            _kwargs["json"] = body.to_dict()
        else:
            _kwargs["json"] = body

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, None | SearchCreatorStoreAssetsRequestType0):
        if isinstance(body, SearchCreatorStoreAssetsRequestType0):
            _kwargs["json"] = body.to_dict()
        else:
            _kwargs["json"] = body

        headers["Content-Type"] = "application/json"
    if isinstance(body, None | SearchCreatorStoreAssetsRequestType0):
        if isinstance(body, SearchCreatorStoreAssetsRequestType0):
            _kwargs["json"] = body.to_dict()
        else:
            _kwargs["json"] = body

        headers["Content-Type"] = "text/json"
    if isinstance(body, None | SearchCreatorStoreAssetsRequestType0):
        if isinstance(body, SearchCreatorStoreAssetsRequestType0):
            _kwargs["json"] = body.to_dict()
        else:
            _kwargs["json"] = body

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | None | ProblemDetailsType0 | None | SearchCreatorStoreAssetsResponseType0 | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> None | SearchCreatorStoreAssetsResponseType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_search_creator_store_assets_response_type_0 = (
                    SearchCreatorStoreAssetsResponseType0.from_dict(data)
                )

                return componentsschemas_search_creator_store_assets_response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchCreatorStoreAssetsResponseType0, data)

        response_200 = _parse_response_200(response.json())

        return response_200

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

    if response.status_code == 429:

        def _parse_response_429(data: object) -> None | ProblemDetailsType0:
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

        response_429 = _parse_response_429(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | None | ProblemDetailsType0 | None | SearchCreatorStoreAssetsResponseType0]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: None
    | SearchCreatorStoreAssetsRequestType0
    | None
    | SearchCreatorStoreAssetsRequestType0
    | None
    | SearchCreatorStoreAssetsRequestType0
    | None
    | SearchCreatorStoreAssetsRequestType0
    | Unset = UNSET,
) -> Response[Any | None | ProblemDetailsType0 | None | SearchCreatorStoreAssetsResponseType0]:
    """Search Creator Store Assets

     Search Creator Store for assets.

    Args:
        body (None | SearchCreatorStoreAssetsRequestType0 | Unset): Request model for searching
            Creator Store assets.
        body (None | SearchCreatorStoreAssetsRequestType0 | Unset): Request model for searching
            Creator Store assets.
        body (None | SearchCreatorStoreAssetsRequestType0 | Unset): Request model for searching
            Creator Store assets.
        body (None | SearchCreatorStoreAssetsRequestType0 | Unset): Request model for searching
            Creator Store assets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | None | ProblemDetailsType0 | None | SearchCreatorStoreAssetsResponseType0]
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
    body: None
    | SearchCreatorStoreAssetsRequestType0
    | None
    | SearchCreatorStoreAssetsRequestType0
    | None
    | SearchCreatorStoreAssetsRequestType0
    | None
    | SearchCreatorStoreAssetsRequestType0
    | Unset = UNSET,
) -> Any | None | ProblemDetailsType0 | None | SearchCreatorStoreAssetsResponseType0 | None:
    """Search Creator Store Assets

     Search Creator Store for assets.

    Args:
        body (None | SearchCreatorStoreAssetsRequestType0 | Unset): Request model for searching
            Creator Store assets.
        body (None | SearchCreatorStoreAssetsRequestType0 | Unset): Request model for searching
            Creator Store assets.
        body (None | SearchCreatorStoreAssetsRequestType0 | Unset): Request model for searching
            Creator Store assets.
        body (None | SearchCreatorStoreAssetsRequestType0 | Unset): Request model for searching
            Creator Store assets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | None | ProblemDetailsType0 | None | SearchCreatorStoreAssetsResponseType0
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: None
    | SearchCreatorStoreAssetsRequestType0
    | None
    | SearchCreatorStoreAssetsRequestType0
    | None
    | SearchCreatorStoreAssetsRequestType0
    | None
    | SearchCreatorStoreAssetsRequestType0
    | Unset = UNSET,
) -> Response[Any | None | ProblemDetailsType0 | None | SearchCreatorStoreAssetsResponseType0]:
    """Search Creator Store Assets

     Search Creator Store for assets.

    Args:
        body (None | SearchCreatorStoreAssetsRequestType0 | Unset): Request model for searching
            Creator Store assets.
        body (None | SearchCreatorStoreAssetsRequestType0 | Unset): Request model for searching
            Creator Store assets.
        body (None | SearchCreatorStoreAssetsRequestType0 | Unset): Request model for searching
            Creator Store assets.
        body (None | SearchCreatorStoreAssetsRequestType0 | Unset): Request model for searching
            Creator Store assets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | None | ProblemDetailsType0 | None | SearchCreatorStoreAssetsResponseType0]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: None
    | SearchCreatorStoreAssetsRequestType0
    | None
    | SearchCreatorStoreAssetsRequestType0
    | None
    | SearchCreatorStoreAssetsRequestType0
    | None
    | SearchCreatorStoreAssetsRequestType0
    | Unset = UNSET,
) -> Any | None | ProblemDetailsType0 | None | SearchCreatorStoreAssetsResponseType0 | None:
    """Search Creator Store Assets

     Search Creator Store for assets.

    Args:
        body (None | SearchCreatorStoreAssetsRequestType0 | Unset): Request model for searching
            Creator Store assets.
        body (None | SearchCreatorStoreAssetsRequestType0 | Unset): Request model for searching
            Creator Store assets.
        body (None | SearchCreatorStoreAssetsRequestType0 | Unset): Request model for searching
            Creator Store assets.
        body (None | SearchCreatorStoreAssetsRequestType0 | Unset): Request model for searching
            Creator Store assets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | None | ProblemDetailsType0 | None | SearchCreatorStoreAssetsResponseType0
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
