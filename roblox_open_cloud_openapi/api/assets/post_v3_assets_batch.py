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
from ...types import UNSET, Response

"""
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.roblox_2_assetdelivery_v3v3_batch_request import Roblox2AssetdeliveryV3V3BatchRequest


def _get_kwargs(
    *,
    body: Roblox2AssetdeliveryV3V3BatchRequest | Roblox2AssetdeliveryV3V3BatchRequest | Unset = UNSET,
    roblox_place_id: int,
    accept_encoding: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Roblox-Place-Id"] = str(roblox_place_id)

    headers["Accept-Encoding"] = accept_encoding

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://assetdelivery.roblox.com/v3/assets/batch",
    }

    if isinstance(body, Roblox2AssetdeliveryV3V3BatchRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, Roblox2AssetdeliveryV3V3BatchRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Roblox2AssetdeliveryV3V3BatchRequest | Roblox2AssetdeliveryV3V3BatchRequest | Unset = UNSET,
    roblox_place_id: int,
    accept_encoding: str,
) -> Response[Any]:
    """
    Args:
        roblox_place_id (int):
        accept_encoding (str):
        body (Roblox2AssetdeliveryV3V3BatchRequest):
        body (Roblox2AssetdeliveryV3V3BatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        roblox_place_id=roblox_place_id,
        accept_encoding=accept_encoding,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Roblox2AssetdeliveryV3V3BatchRequest | Roblox2AssetdeliveryV3V3BatchRequest | Unset = UNSET,
    roblox_place_id: int,
    accept_encoding: str,
) -> Response[Any]:
    """
    Args:
        roblox_place_id (int):
        accept_encoding (str):
        body (Roblox2AssetdeliveryV3V3BatchRequest):
        body (Roblox2AssetdeliveryV3V3BatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        roblox_place_id=roblox_place_id,
        accept_encoding=accept_encoding,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
