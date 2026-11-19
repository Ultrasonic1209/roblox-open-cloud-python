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
{'x-roblox-scopes': [{'name': 'asset:write', 'description': 'Required.'}], 'x-roblox-cloud-api-operation': True, 'x-roblox-cloud-api-operation-name': 'Get Operation', 'x-roblox-cloud-api-operation-code-samples': [{'language': 'Get Operation', 'script': "curl --location 'https://apis.roblox.com/assets/v1/operations/{operationId}' \\\n--header 'x-api-key: {apiKey}'\n"}], 'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 300}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 300}}, 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.assets_upload_api_operation import AssetsUploadApiOperation
from ...models.assets_upload_api_status import AssetsUploadApiStatus


def _get_kwargs(
    operation_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/assets/v1/operations/{operation_id}".format(
            operation_id=quote(str(operation_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AssetsUploadApiOperation | AssetsUploadApiStatus | None:
    if response.status_code == 200:
        response_200 = AssetsUploadApiOperation.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AssetsUploadApiStatus.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AssetsUploadApiStatus.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AssetsUploadApiStatus.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = AssetsUploadApiStatus.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AssetsUploadApiOperation | AssetsUploadApiStatus]:
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
) -> Response[AssetsUploadApiOperation | AssetsUploadApiStatus]:
    """Get the result of an asset creation or update.

     Get the result of an asset creation or update using the returned Operation ID.

    Args:
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetsUploadApiOperation | AssetsUploadApiStatus]
    """

    kwargs = _get_kwargs(
        operation_id=operation_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    operation_id: str,
    *,
    client: AuthenticatedClient,
) -> AssetsUploadApiOperation | AssetsUploadApiStatus | None:
    """Get the result of an asset creation or update.

     Get the result of an asset creation or update using the returned Operation ID.

    Args:
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetsUploadApiOperation | AssetsUploadApiStatus
    """

    return sync_detailed(
        operation_id=operation_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    operation_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AssetsUploadApiOperation | AssetsUploadApiStatus]:
    """Get the result of an asset creation or update.

     Get the result of an asset creation or update using the returned Operation ID.

    Args:
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetsUploadApiOperation | AssetsUploadApiStatus]
    """

    kwargs = _get_kwargs(
        operation_id=operation_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    operation_id: str,
    *,
    client: AuthenticatedClient,
) -> AssetsUploadApiOperation | AssetsUploadApiStatus | None:
    """Get the result of an asset creation or update.

     Get the result of an asset creation or update using the returned Operation ID.

    Args:
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetsUploadApiOperation | AssetsUploadApiStatus
    """

    return (
        await asyncio_detailed(
            operation_id=operation_id,
            client=client,
        )
    ).parsed
