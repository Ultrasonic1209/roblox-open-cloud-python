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
from ...types import UNSET, Response

"""
{'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 60}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 60}}, 'x-roblox-scopes': [{'name': 'ad.campaign:write'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.creative import Creative
from ...models.error_envelope import ErrorEnvelope
from ...models.update_creative_request import UpdateCreativeRequest
from ...types import Unset


def _get_kwargs(
    id: str,
    *,
    body: UpdateCreativeRequest,
    group_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["groupId"] = group_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/ads-management/v1/creatives/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Creative | ErrorEnvelope | None:
    if response.status_code == 200:
        response_200 = Creative.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorEnvelope.from_dict(response.json())

        return response_409

    if response.status_code == 429:
        response_429 = ErrorEnvelope.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ErrorEnvelope.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Creative | ErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCreativeRequest,
    group_id: str | Unset = UNSET,
) -> Response[Creative | ErrorEnvelope]:
    """Update a creative

     Archives or unarchives a creative, or changes its associated experience. isArchived=true must be the
    only field in the request; combining it with another field returns 400 without writing. Archiving
    returns 409 if an enabled ad uses the asset; pause or archive that ad first. Set universeId to null
    to clear the association; omitted fields remain unchanged. An empty object returns the current
    creative without writing. The asset is resolved only in the group ads account selected by groupId,
    or the caller's personal account when omitted. Unknown assets and inaccessible accounts return the
    same 404. The caller must have advertising permission for a new experience association.

    Args:
        id (str):
        group_id (str | Unset):
        body (UpdateCreativeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Creative | ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        group_id=group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCreativeRequest,
    group_id: str | Unset = UNSET,
) -> Creative | ErrorEnvelope | None:
    """Update a creative

     Archives or unarchives a creative, or changes its associated experience. isArchived=true must be the
    only field in the request; combining it with another field returns 400 without writing. Archiving
    returns 409 if an enabled ad uses the asset; pause or archive that ad first. Set universeId to null
    to clear the association; omitted fields remain unchanged. An empty object returns the current
    creative without writing. The asset is resolved only in the group ads account selected by groupId,
    or the caller's personal account when omitted. Unknown assets and inaccessible accounts return the
    same 404. The caller must have advertising permission for a new experience association.

    Args:
        id (str):
        group_id (str | Unset):
        body (UpdateCreativeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Creative | ErrorEnvelope
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        group_id=group_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCreativeRequest,
    group_id: str | Unset = UNSET,
) -> Response[Creative | ErrorEnvelope]:
    """Update a creative

     Archives or unarchives a creative, or changes its associated experience. isArchived=true must be the
    only field in the request; combining it with another field returns 400 without writing. Archiving
    returns 409 if an enabled ad uses the asset; pause or archive that ad first. Set universeId to null
    to clear the association; omitted fields remain unchanged. An empty object returns the current
    creative without writing. The asset is resolved only in the group ads account selected by groupId,
    or the caller's personal account when omitted. Unknown assets and inaccessible accounts return the
    same 404. The caller must have advertising permission for a new experience association.

    Args:
        id (str):
        group_id (str | Unset):
        body (UpdateCreativeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Creative | ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        group_id=group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCreativeRequest,
    group_id: str | Unset = UNSET,
) -> Creative | ErrorEnvelope | None:
    """Update a creative

     Archives or unarchives a creative, or changes its associated experience. isArchived=true must be the
    only field in the request; combining it with another field returns 400 without writing. Archiving
    returns 409 if an enabled ad uses the asset; pause or archive that ad first. Set universeId to null
    to clear the association; omitted fields remain unchanged. An empty object returns the current
    creative without writing. The asset is resolved only in the group ads account selected by groupId,
    or the caller's personal account when omitted. Unknown assets and inaccessible accounts return the
    same 404. The caller must have advertising permission for a new experience association.

    Args:
        id (str):
        group_id (str | Unset):
        body (UpdateCreativeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Creative | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            group_id=group_id,
        )
    ).parsed
