from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.luau_execution_session_task_binary_input import LuauExecutionSessionTaskBinaryInput
from ...types import Response


def _get_kwargs(
    universe_id: str,
    *,
    body: LuauExecutionSessionTaskBinaryInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cloud/v2/universes/{universe_id}/luau-execution-session-task-binary-inputs".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
                "x-roblox-scopes": [{"name": "universe.place.luau-execution-session:write"}],
                "x-roblox-docs": {
                    "category": "Luau execution",
                    "methodProperties": {"scopes": ["universe.place.luau-execution-session:write"]},
                    "resource": {
                        "$ref": "#/components/schemas/LuauExecutionSessionTaskBinaryInput",
                        "name": "LuauExecutionSessionTaskBinaryInput",
                    },
                },
                "x-roblox-stability": "STABLE",
                "x-roblox-rate-limits": {"perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 5}},
            },
            "openapi-id": "Cloud_CreateLuauExecutionSessionTaskBinaryInput",
        },
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> LuauExecutionSessionTaskBinaryInput | None:
    if response.status_code == 200:
        response_200 = LuauExecutionSessionTaskBinaryInput.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[LuauExecutionSessionTaskBinaryInput]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: LuauExecutionSessionTaskBinaryInput,
) -> Response[LuauExecutionSessionTaskBinaryInput]:
    """Create Luau Execution Session Task Binary Input

     Create a new `LuauExecutionSessionTaskBinaryInput`.

    Args:
        universe_id (str):
        body (LuauExecutionSessionTaskBinaryInput): Represents a large binary input that can be
            given to a
            `LuauExecutionSessionTask`.

            Each `LuauExecutionSessionTaskBinaryInput` is associated with a presigned URL
            which can be used to upload an arbitrary object. After uploading the object,
            the path of the `LuauExecutionSessionTaskBinaryInput` can be passed when
            creating a `LuauExecutionSessionTask` to make the object available to the
            task.

            Within the task, the contents of the object are made available within a table
            passed as the first argument to the script, with the key `BinaryInput`. The
            following example demonstrates how to retrieve the data:

            ```
            local taskInput: LuauExecutionTaskInput = ({...})[1]
            local buf: buffer = taskInput.BinaryInput
            ```

            Each `LuauExecutionSessionTaskBinaryInput` is valid for 15 minutes from the
            time of creation. Within that time, in desired, you can use it to create
            multiple tasks for the same universe.

            The uploaded binary object must be no larger than 100 MiB.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LuauExecutionSessionTaskBinaryInput]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: LuauExecutionSessionTaskBinaryInput,
) -> LuauExecutionSessionTaskBinaryInput | None:
    """Create Luau Execution Session Task Binary Input

     Create a new `LuauExecutionSessionTaskBinaryInput`.

    Args:
        universe_id (str):
        body (LuauExecutionSessionTaskBinaryInput): Represents a large binary input that can be
            given to a
            `LuauExecutionSessionTask`.

            Each `LuauExecutionSessionTaskBinaryInput` is associated with a presigned URL
            which can be used to upload an arbitrary object. After uploading the object,
            the path of the `LuauExecutionSessionTaskBinaryInput` can be passed when
            creating a `LuauExecutionSessionTask` to make the object available to the
            task.

            Within the task, the contents of the object are made available within a table
            passed as the first argument to the script, with the key `BinaryInput`. The
            following example demonstrates how to retrieve the data:

            ```
            local taskInput: LuauExecutionTaskInput = ({...})[1]
            local buf: buffer = taskInput.BinaryInput
            ```

            Each `LuauExecutionSessionTaskBinaryInput` is valid for 15 minutes from the
            time of creation. Within that time, in desired, you can use it to create
            multiple tasks for the same universe.

            The uploaded binary object must be no larger than 100 MiB.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LuauExecutionSessionTaskBinaryInput
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: LuauExecutionSessionTaskBinaryInput,
) -> Response[LuauExecutionSessionTaskBinaryInput]:
    """Create Luau Execution Session Task Binary Input

     Create a new `LuauExecutionSessionTaskBinaryInput`.

    Args:
        universe_id (str):
        body (LuauExecutionSessionTaskBinaryInput): Represents a large binary input that can be
            given to a
            `LuauExecutionSessionTask`.

            Each `LuauExecutionSessionTaskBinaryInput` is associated with a presigned URL
            which can be used to upload an arbitrary object. After uploading the object,
            the path of the `LuauExecutionSessionTaskBinaryInput` can be passed when
            creating a `LuauExecutionSessionTask` to make the object available to the
            task.

            Within the task, the contents of the object are made available within a table
            passed as the first argument to the script, with the key `BinaryInput`. The
            following example demonstrates how to retrieve the data:

            ```
            local taskInput: LuauExecutionTaskInput = ({...})[1]
            local buf: buffer = taskInput.BinaryInput
            ```

            Each `LuauExecutionSessionTaskBinaryInput` is valid for 15 minutes from the
            time of creation. Within that time, in desired, you can use it to create
            multiple tasks for the same universe.

            The uploaded binary object must be no larger than 100 MiB.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LuauExecutionSessionTaskBinaryInput]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: LuauExecutionSessionTaskBinaryInput,
) -> LuauExecutionSessionTaskBinaryInput | None:
    """Create Luau Execution Session Task Binary Input

     Create a new `LuauExecutionSessionTaskBinaryInput`.

    Args:
        universe_id (str):
        body (LuauExecutionSessionTaskBinaryInput): Represents a large binary input that can be
            given to a
            `LuauExecutionSessionTask`.

            Each `LuauExecutionSessionTaskBinaryInput` is associated with a presigned URL
            which can be used to upload an arbitrary object. After uploading the object,
            the path of the `LuauExecutionSessionTaskBinaryInput` can be passed when
            creating a `LuauExecutionSessionTask` to make the object available to the
            task.

            Within the task, the contents of the object are made available within a table
            passed as the first argument to the script, with the key `BinaryInput`. The
            following example demonstrates how to retrieve the data:

            ```
            local taskInput: LuauExecutionTaskInput = ({...})[1]
            local buf: buffer = taskInput.BinaryInput
            ```

            Each `LuauExecutionSessionTaskBinaryInput` is valid for 15 minutes from the
            time of creation. Within that time, in desired, you can use it to create
            multiple tasks for the same universe.

            The uploaded binary object must be no larger than 100 MiB.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LuauExecutionSessionTaskBinaryInput
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
