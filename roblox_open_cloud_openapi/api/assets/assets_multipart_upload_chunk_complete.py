from http import HTTPStatus
from typing import TYPE_CHECKING, Any, cast
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
from ...types import UNSET, Response

"""
{'x-roblox-scopes': [{'name': 'asset:write', 'description': 'Required.'}], 'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 100}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 100}}, 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.assets_upload_api_status import AssetsUploadApiStatus
from ...models.multipart_upload_chunk_complete_request import MultipartUploadChunkCompleteRequest
from ...types import Unset


def _get_kwargs(
    operation_id: str,
    *,
    body: MultipartUploadChunkCompleteRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/assets/v1/operations/{operation_id}:multipartUploadChunkComplete".format(
            operation_id=quote(str(operation_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | AssetsUploadApiStatus | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = AssetsUploadApiStatus.from_dict(response.text)

        return response_400

    if response.status_code == 401:
        response_401 = AssetsUploadApiStatus.from_dict(response.text)

        return response_401

    if response.status_code == 403:
        response_403 = AssetsUploadApiStatus.from_dict(response.text)

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | AssetsUploadApiStatus]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    operation_id: str,
    *,
    client: AuthenticatedClient,
    body: MultipartUploadChunkCompleteRequest | Unset = UNSET,
) -> Response[Any | AssetsUploadApiStatus]:
    """Records a chunk upload complete.

    Args:
        operation_id (str):
        body (MultipartUploadChunkCompleteRequest | Unset): Request of
            Roblox.AssetsManagement.AssetsUploadApi.MultipartUploadChunkCompleteOperation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetsUploadApiStatus]
    """

    kwargs = _get_kwargs(
        operation_id=operation_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    operation_id: str,
    *,
    client: AuthenticatedClient,
    body: MultipartUploadChunkCompleteRequest | Unset = UNSET,
) -> Any | AssetsUploadApiStatus | None:
    """Records a chunk upload complete.

    Args:
        operation_id (str):
        body (MultipartUploadChunkCompleteRequest | Unset): Request of
            Roblox.AssetsManagement.AssetsUploadApi.MultipartUploadChunkCompleteOperation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetsUploadApiStatus
    """

    return sync_detailed(
        operation_id=operation_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    operation_id: str,
    *,
    client: AuthenticatedClient,
    body: MultipartUploadChunkCompleteRequest | Unset = UNSET,
) -> Response[Any | AssetsUploadApiStatus]:
    """Records a chunk upload complete.

    Args:
        operation_id (str):
        body (MultipartUploadChunkCompleteRequest | Unset): Request of
            Roblox.AssetsManagement.AssetsUploadApi.MultipartUploadChunkCompleteOperation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetsUploadApiStatus]
    """

    kwargs = _get_kwargs(
        operation_id=operation_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    operation_id: str,
    *,
    client: AuthenticatedClient,
    body: MultipartUploadChunkCompleteRequest | Unset = UNSET,
) -> Any | AssetsUploadApiStatus | None:
    """Records a chunk upload complete.

    Args:
        operation_id (str):
        body (MultipartUploadChunkCompleteRequest | Unset): Request of
            Roblox.AssetsManagement.AssetsUploadApi.MultipartUploadChunkCompleteOperation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetsUploadApiStatus
    """

    return (
        await asyncio_detailed(
            operation_id=operation_id,
            client=client,
            body=body,
        )
    ).parsed
