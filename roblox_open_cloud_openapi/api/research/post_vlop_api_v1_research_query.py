from http import HTTPStatus
from typing import TYPE_CHECKING, Any

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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 10}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 10}}, 'x-roblox-scopes': [{'name': 'research:query'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.internal_controller_http_controller_error_body import InternalControllerHttpControllerErrorBody
from ...models.internal_controller_http_controller_submit_query_request import (
    InternalControllerHttpControllerSubmitQueryRequest,
)
from ...models.internal_controller_http_controller_submit_query_response import (
    InternalControllerHttpControllerSubmitQueryResponse,
)


def _get_kwargs(
    *,
    body: InternalControllerHttpControllerSubmitQueryRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/vlop-api/v1/research/query",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerSubmitQueryResponse | None:
    if response.status_code == 200:
        response_200 = InternalControllerHttpControllerSubmitQueryResponse.from_dict(response.json())

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

    if response.status_code == 429:
        response_429 = InternalControllerHttpControllerErrorBody.from_dict(response.json())

        return response_429

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
) -> Response[InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerSubmitQueryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: InternalControllerHttpControllerSubmitQueryRequest,
) -> Response[InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerSubmitQueryResponse]:
    """Submit a researcher query

     Submits a structured researcher query for asynchronous execution. The caller is authenticated by the
    API Gateway (API key or OAuth2) and must hold an active qualified researcher (QR) role grant; that
    entitlement governs the datasets, fields, and filters they may query. Vetted researcher (VR) data
    access is served through the data clean room, not this API. Returns a job id used to poll the
    query's status and fetch its result once it has completed.

    Args:
        body (InternalControllerHttpControllerSubmitQueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerSubmitQueryResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: InternalControllerHttpControllerSubmitQueryRequest,
) -> InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerSubmitQueryResponse | None:
    """Submit a researcher query

     Submits a structured researcher query for asynchronous execution. The caller is authenticated by the
    API Gateway (API key or OAuth2) and must hold an active qualified researcher (QR) role grant; that
    entitlement governs the datasets, fields, and filters they may query. Vetted researcher (VR) data
    access is served through the data clean room, not this API. Returns a job id used to poll the
    query's status and fetch its result once it has completed.

    Args:
        body (InternalControllerHttpControllerSubmitQueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerSubmitQueryResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: InternalControllerHttpControllerSubmitQueryRequest,
) -> Response[InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerSubmitQueryResponse]:
    """Submit a researcher query

     Submits a structured researcher query for asynchronous execution. The caller is authenticated by the
    API Gateway (API key or OAuth2) and must hold an active qualified researcher (QR) role grant; that
    entitlement governs the datasets, fields, and filters they may query. Vetted researcher (VR) data
    access is served through the data clean room, not this API. Returns a job id used to poll the
    query's status and fetch its result once it has completed.

    Args:
        body (InternalControllerHttpControllerSubmitQueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerSubmitQueryResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: InternalControllerHttpControllerSubmitQueryRequest,
) -> InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerSubmitQueryResponse | None:
    """Submit a researcher query

     Submits a structured researcher query for asynchronous execution. The caller is authenticated by the
    API Gateway (API key or OAuth2) and must hold an active qualified researcher (QR) role grant; that
    entitlement governs the datasets, fields, and filters they may query. Vetted researcher (VR) data
    access is served through the data clean room, not this API. Returns a job id used to poll the
    query's status and fetch its result once it has completed.

    Args:
        body (InternalControllerHttpControllerSubmitQueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalControllerHttpControllerErrorBody | InternalControllerHttpControllerSubmitQueryResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
