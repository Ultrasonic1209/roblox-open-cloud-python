from http import HTTPStatus
from typing import TYPE_CHECKING, Any
from urllib.parse import quote

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
from ...types import Response

"""
{'x-roblox-stability': 'STABLE', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 1000}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 10}}, 'x-roblox-engine-usability': {'apiKeyWithHttpService': True}}
"""


from ...models.open_cloud_users_operation import OpenCloudUsersOperation


def _get_kwargs(
    user_id: str,
    operation_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/users/{user_id}/operations/{operation_id}".format(
            user_id=quote(str(user_id), safe=""),
            operation_id=quote(str(operation_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OpenCloudUsersOperation | None:
    if response.status_code == 200:
        response_200 = OpenCloudUsersOperation.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OpenCloudUsersOperation]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    operation_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OpenCloudUsersOperation]:
    """Get User Thumbnail Generation Operation

     Gets the status and result of a
    [Generate User Thumbnail](https://create.roblox.com/docs/cloud/reference/features/users#Cloud_Genera
    teUserThumbnail)
    long-running operation.

    Call this with the operation `path` returned by Generate User Thumbnail,
    polling until `done` is `true`. Once complete, the operation contains
    either `response` or `error`:

    - If `response` is set, `response.imageUri` contains the generated
      thumbnail URL.
    - If `error` is set, the thumbnail couldn't be generated and `response` is
      not set. `error.code` and `error.message` describe the reason.

    Always check for `error` before reading `response.imageUri`.

    Args:
        user_id (str):
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpenCloudUsersOperation]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        operation_id=operation_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    operation_id: str,
    *,
    client: AuthenticatedClient,
) -> OpenCloudUsersOperation | None:
    """Get User Thumbnail Generation Operation

     Gets the status and result of a
    [Generate User Thumbnail](https://create.roblox.com/docs/cloud/reference/features/users#Cloud_Genera
    teUserThumbnail)
    long-running operation.

    Call this with the operation `path` returned by Generate User Thumbnail,
    polling until `done` is `true`. Once complete, the operation contains
    either `response` or `error`:

    - If `response` is set, `response.imageUri` contains the generated
      thumbnail URL.
    - If `error` is set, the thumbnail couldn't be generated and `response` is
      not set. `error.code` and `error.message` describe the reason.

    Always check for `error` before reading `response.imageUri`.

    Args:
        user_id (str):
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpenCloudUsersOperation
    """

    return sync_detailed(
        user_id=user_id,
        operation_id=operation_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    operation_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OpenCloudUsersOperation]:
    """Get User Thumbnail Generation Operation

     Gets the status and result of a
    [Generate User Thumbnail](https://create.roblox.com/docs/cloud/reference/features/users#Cloud_Genera
    teUserThumbnail)
    long-running operation.

    Call this with the operation `path` returned by Generate User Thumbnail,
    polling until `done` is `true`. Once complete, the operation contains
    either `response` or `error`:

    - If `response` is set, `response.imageUri` contains the generated
      thumbnail URL.
    - If `error` is set, the thumbnail couldn't be generated and `response` is
      not set. `error.code` and `error.message` describe the reason.

    Always check for `error` before reading `response.imageUri`.

    Args:
        user_id (str):
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpenCloudUsersOperation]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        operation_id=operation_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    operation_id: str,
    *,
    client: AuthenticatedClient,
) -> OpenCloudUsersOperation | None:
    """Get User Thumbnail Generation Operation

     Gets the status and result of a
    [Generate User Thumbnail](https://create.roblox.com/docs/cloud/reference/features/users#Cloud_Genera
    teUserThumbnail)
    long-running operation.

    Call this with the operation `path` returned by Generate User Thumbnail,
    polling until `done` is `true`. Once complete, the operation contains
    either `response` or `error`:

    - If `response` is set, `response.imageUri` contains the generated
      thumbnail URL.
    - If `error` is set, the thumbnail couldn't be generated and `response` is
      not set. `error.code` and `error.message` describe the reason.

    Always check for `error` before reading `response.imageUri`.

    Args:
        user_id (str):
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpenCloudUsersOperation
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            operation_id=operation_id,
            client=client,
        )
    ).parsed
