from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cloud_get_luau_execution_session_task_view import CloudGetLuauExecutionSessionTaskView
from ...models.luau_execution_session_task import LuauExecutionSessionTask
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: str,
    place_id: str,
    version_id: str,
    luau_execution_session_id: str,
    task_id: str,
    *,
    view: CloudGetLuauExecutionSessionTaskView | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_view: str | Unset = UNSET
    if not isinstance(view, Unset):
        json_view = view.value

    params["view"] = json_view

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/universes/{universe_id}/places/{place_id}/versions/{version_id}/luau-execution-sessions/{luau_execution_session_id}/tasks/{task_id}".format(
            universe_id=quote(str(universe_id), safe=""),
            place_id=quote(str(place_id), safe=""),
            version_id=quote(str(version_id), safe=""),
            luau_execution_session_id=quote(str(luau_execution_session_id), safe=""),
            task_id=quote(str(task_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LuauExecutionSessionTask | None:
    if response.status_code == 200:
        response_200 = LuauExecutionSessionTask.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LuauExecutionSessionTask]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    place_id: str,
    version_id: str,
    luau_execution_session_id: str,
    task_id: str,
    *,
    client: AuthenticatedClient,
    view: CloudGetLuauExecutionSessionTaskView | Unset = UNSET,
) -> Response[LuauExecutionSessionTask]:
    """Get Luau Execution Session Task

     Gets information about a task.

    Quotas:
    * 45 calls per minute per API key owner or IP address

    Args:
        universe_id (str):
        place_id (str):
        version_id (str):
        luau_execution_session_id (str):
        task_id (str):
        view (CloudGetLuauExecutionSessionTaskView | Unset):  Example: VIEW_UNSPECIFIED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LuauExecutionSessionTask]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        place_id=place_id,
        version_id=version_id,
        luau_execution_session_id=luau_execution_session_id,
        task_id=task_id,
        view=view,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    place_id: str,
    version_id: str,
    luau_execution_session_id: str,
    task_id: str,
    *,
    client: AuthenticatedClient,
    view: CloudGetLuauExecutionSessionTaskView | Unset = UNSET,
) -> LuauExecutionSessionTask | None:
    """Get Luau Execution Session Task

     Gets information about a task.

    Quotas:
    * 45 calls per minute per API key owner or IP address

    Args:
        universe_id (str):
        place_id (str):
        version_id (str):
        luau_execution_session_id (str):
        task_id (str):
        view (CloudGetLuauExecutionSessionTaskView | Unset):  Example: VIEW_UNSPECIFIED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LuauExecutionSessionTask
    """

    return sync_detailed(
        universe_id=universe_id,
        place_id=place_id,
        version_id=version_id,
        luau_execution_session_id=luau_execution_session_id,
        task_id=task_id,
        client=client,
        view=view,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    place_id: str,
    version_id: str,
    luau_execution_session_id: str,
    task_id: str,
    *,
    client: AuthenticatedClient,
    view: CloudGetLuauExecutionSessionTaskView | Unset = UNSET,
) -> Response[LuauExecutionSessionTask]:
    """Get Luau Execution Session Task

     Gets information about a task.

    Quotas:
    * 45 calls per minute per API key owner or IP address

    Args:
        universe_id (str):
        place_id (str):
        version_id (str):
        luau_execution_session_id (str):
        task_id (str):
        view (CloudGetLuauExecutionSessionTaskView | Unset):  Example: VIEW_UNSPECIFIED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LuauExecutionSessionTask]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        place_id=place_id,
        version_id=version_id,
        luau_execution_session_id=luau_execution_session_id,
        task_id=task_id,
        view=view,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    place_id: str,
    version_id: str,
    luau_execution_session_id: str,
    task_id: str,
    *,
    client: AuthenticatedClient,
    view: CloudGetLuauExecutionSessionTaskView | Unset = UNSET,
) -> LuauExecutionSessionTask | None:
    """Get Luau Execution Session Task

     Gets information about a task.

    Quotas:
    * 45 calls per minute per API key owner or IP address

    Args:
        universe_id (str):
        place_id (str):
        version_id (str):
        luau_execution_session_id (str):
        task_id (str):
        view (CloudGetLuauExecutionSessionTaskView | Unset):  Example: VIEW_UNSPECIFIED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LuauExecutionSessionTask
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            place_id=place_id,
            version_id=version_id,
            luau_execution_session_id=luau_execution_session_id,
            task_id=task_id,
            client=client,
            view=view,
        )
    ).parsed
