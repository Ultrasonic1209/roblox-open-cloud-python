from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation_error_response import OperationErrorResponse
from ...models.update_place_version_notes_request import UpdatePlaceVersionNotesRequest
from ...models.update_place_version_notes_response import UpdatePlaceVersionNotesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    place_id: int,
    version: str,
    *,
    body: UpdatePlaceVersionNotesRequest
    | UpdatePlaceVersionNotesRequest
    | UpdatePlaceVersionNotesRequest
    | UpdatePlaceVersionNotesRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/place-version-history-api/v1/{place_id}/version/{version}/notes".format(
            place_id=quote(str(place_id), safe=""),
            version=quote(str(version), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "EXPERIMENTAL",
                "x-roblox-rate-limits": {"perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100}},
                "x-roblox-scopes": [{"name": "universe.place:write", "targetResourceSpecifier": ""}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "PlaceVersion_UpdatePlaceVersionNotes",
        },
    }

    if isinstance(body, UpdatePlaceVersionNotesRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, UpdatePlaceVersionNotesRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdatePlaceVersionNotesRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, UpdatePlaceVersionNotesRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> OperationErrorResponse | UpdatePlaceVersionNotesResponse | None:
    if response.status_code == 200:
        response_200 = UpdatePlaceVersionNotesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = OperationErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = OperationErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OperationErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = OperationErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[OperationErrorResponse | UpdatePlaceVersionNotesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    place_id: int,
    version: str,
    *,
    client: AuthenticatedClient,
    body: UpdatePlaceVersionNotesRequest
    | UpdatePlaceVersionNotesRequest
    | UpdatePlaceVersionNotesRequest
    | UpdatePlaceVersionNotesRequest
    | Unset = UNSET,
) -> Response[OperationErrorResponse | UpdatePlaceVersionNotesResponse]:
    """Endpoint used to modify the notes of a particular version for a place.

    Args:
        place_id (int):
        version (str):
        body (UpdatePlaceVersionNotesRequest | Unset):
        body (UpdatePlaceVersionNotesRequest | Unset):
        body (UpdatePlaceVersionNotesRequest | Unset):
        body (UpdatePlaceVersionNotesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationErrorResponse | UpdatePlaceVersionNotesResponse]
    """

    kwargs = _get_kwargs(
        place_id=place_id,
        version=version,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    place_id: int,
    version: str,
    *,
    client: AuthenticatedClient,
    body: UpdatePlaceVersionNotesRequest
    | UpdatePlaceVersionNotesRequest
    | UpdatePlaceVersionNotesRequest
    | UpdatePlaceVersionNotesRequest
    | Unset = UNSET,
) -> OperationErrorResponse | UpdatePlaceVersionNotesResponse | None:
    """Endpoint used to modify the notes of a particular version for a place.

    Args:
        place_id (int):
        version (str):
        body (UpdatePlaceVersionNotesRequest | Unset):
        body (UpdatePlaceVersionNotesRequest | Unset):
        body (UpdatePlaceVersionNotesRequest | Unset):
        body (UpdatePlaceVersionNotesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationErrorResponse | UpdatePlaceVersionNotesResponse
    """

    return sync_detailed(
        place_id=place_id,
        version=version,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    place_id: int,
    version: str,
    *,
    client: AuthenticatedClient,
    body: UpdatePlaceVersionNotesRequest
    | UpdatePlaceVersionNotesRequest
    | UpdatePlaceVersionNotesRequest
    | UpdatePlaceVersionNotesRequest
    | Unset = UNSET,
) -> Response[OperationErrorResponse | UpdatePlaceVersionNotesResponse]:
    """Endpoint used to modify the notes of a particular version for a place.

    Args:
        place_id (int):
        version (str):
        body (UpdatePlaceVersionNotesRequest | Unset):
        body (UpdatePlaceVersionNotesRequest | Unset):
        body (UpdatePlaceVersionNotesRequest | Unset):
        body (UpdatePlaceVersionNotesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationErrorResponse | UpdatePlaceVersionNotesResponse]
    """

    kwargs = _get_kwargs(
        place_id=place_id,
        version=version,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    place_id: int,
    version: str,
    *,
    client: AuthenticatedClient,
    body: UpdatePlaceVersionNotesRequest
    | UpdatePlaceVersionNotesRequest
    | UpdatePlaceVersionNotesRequest
    | UpdatePlaceVersionNotesRequest
    | Unset = UNSET,
) -> OperationErrorResponse | UpdatePlaceVersionNotesResponse | None:
    """Endpoint used to modify the notes of a particular version for a place.

    Args:
        place_id (int):
        version (str):
        body (UpdatePlaceVersionNotesRequest | Unset):
        body (UpdatePlaceVersionNotesRequest | Unset):
        body (UpdatePlaceVersionNotesRequest | Unset):
        body (UpdatePlaceVersionNotesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationErrorResponse | UpdatePlaceVersionNotesResponse
    """

    return (
        await asyncio_detailed(
            place_id=place_id,
            version=version,
            client=client,
            body=body,
        )
    ).parsed
