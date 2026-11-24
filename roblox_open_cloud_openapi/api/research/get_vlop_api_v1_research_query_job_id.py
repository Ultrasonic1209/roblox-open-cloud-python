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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 60}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 60}}, 'x-roblox-scopes': [{'name': 'research:query'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.internal_controller_http_controller_error_body import InternalControllerHttpControllerErrorBody
from ...models.internal_controller_http_controller_query_status_response import (
    InternalControllerHttpControllerQueryStatusResponse,
)


def _get_kwargs(
    job_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/vlop-api/v1/research/query/{job_id}".format(
            job_id=quote(str(job_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerQueryStatusResponse | None:
    if response.status_code == 200:
        response_200 = InternalControllerHttpControllerQueryStatusResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = InternalControllerHttpControllerErrorBody.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = InternalControllerHttpControllerErrorBody.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = InternalControllerHttpControllerErrorBody.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = InternalControllerHttpControllerErrorBody.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = InternalControllerHttpControllerErrorBody.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = InternalControllerHttpControllerErrorBody.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerQueryStatusResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerQueryStatusResponse]:
    """Get a researcher query's status

     Returns the current lifecycle state of a query job. The caller must hold an active qualified
    researcher (QR) role grant, and only the researcher who submitted the job may read it.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerQueryStatusResponse]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    *,
    client: AuthenticatedClient,
) -> InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerQueryStatusResponse | None:
    """Get a researcher query's status

     Returns the current lifecycle state of a query job. The caller must hold an active qualified
    researcher (QR) role grant, and only the researcher who submitted the job may read it.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerQueryStatusResponse
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerQueryStatusResponse]:
    """Get a researcher query's status

     Returns the current lifecycle state of a query job. The caller must hold an active qualified
    researcher (QR) role grant, and only the researcher who submitted the job may read it.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerQueryStatusResponse]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient,
) -> InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerQueryStatusResponse | None:
    """Get a researcher query's status

     Returns the current lifecycle state of a query job. The caller must hold an active qualified
    researcher (QR) role grant, and only the researcher who submitted the job may read it.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerQueryStatusResponse
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
        )
    ).parsed
