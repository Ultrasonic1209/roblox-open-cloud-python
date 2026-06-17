from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details_type_0 import ProblemDetailsType0
from ...models.search_category_type import SearchCategoryType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    target_type: SearchCategoryType | Unset = UNSET,
    target_id: int | Unset = UNSET,
    collection_name: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_target_type: str | Unset = UNSET
    if not isinstance(target_type, Unset):
        json_target_type = target_type.value

    params["targetType"] = json_target_type

    params["targetId"] = target_id

    params["collectionName"] = collection_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/toolbox-service/v1/saves",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | None | ProblemDetailsType0 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
    target_type: SearchCategoryType | Unset = UNSET,
    target_id: int | Unset = UNSET,
    collection_name: str | Unset = UNSET,
) -> Response[Any | None | ProblemDetailsType0]:
    """Deletes a save.

    Args:
        target_type (SearchCategoryType | Unset): This represents a "subset" of
            Toolbox.Service.CategoryType options and represent the full set
            of "categories" (or asset types) that can be searched upon from the toolbox search API.
        target_id (int | Unset):
        collection_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | None | ProblemDetailsType0]
    """

    kwargs = _get_kwargs(
        target_type=target_type,
        target_id=target_id,
        collection_name=collection_name,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    target_type: SearchCategoryType | Unset = UNSET,
    target_id: int | Unset = UNSET,
    collection_name: str | Unset = UNSET,
) -> Any | None | ProblemDetailsType0 | None:
    """Deletes a save.

    Args:
        target_type (SearchCategoryType | Unset): This represents a "subset" of
            Toolbox.Service.CategoryType options and represent the full set
            of "categories" (or asset types) that can be searched upon from the toolbox search API.
        target_id (int | Unset):
        collection_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | None | ProblemDetailsType0
    """

    return sync_detailed(
        client=client,
        target_type=target_type,
        target_id=target_id,
        collection_name=collection_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    target_type: SearchCategoryType | Unset = UNSET,
    target_id: int | Unset = UNSET,
    collection_name: str | Unset = UNSET,
) -> Response[Any | None | ProblemDetailsType0]:
    """Deletes a save.

    Args:
        target_type (SearchCategoryType | Unset): This represents a "subset" of
            Toolbox.Service.CategoryType options and represent the full set
            of "categories" (or asset types) that can be searched upon from the toolbox search API.
        target_id (int | Unset):
        collection_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | None | ProblemDetailsType0]
    """

    kwargs = _get_kwargs(
        target_type=target_type,
        target_id=target_id,
        collection_name=collection_name,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    target_type: SearchCategoryType | Unset = UNSET,
    target_id: int | Unset = UNSET,
    collection_name: str | Unset = UNSET,
) -> Any | None | ProblemDetailsType0 | None:
    """Deletes a save.

    Args:
        target_type (SearchCategoryType | Unset): This represents a "subset" of
            Toolbox.Service.CategoryType options and represent the full set
            of "categories" (or asset types) that can be searched upon from the toolbox search API.
        target_id (int | Unset):
        collection_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | None | ProblemDetailsType0
    """

    return (
        await asyncio_detailed(
            client=client,
            target_type=target_type,
            target_id=target_id,
            collection_name=collection_name,
        )
    ).parsed
