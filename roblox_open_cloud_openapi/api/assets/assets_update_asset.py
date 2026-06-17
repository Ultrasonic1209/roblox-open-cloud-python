from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assets_update_asset_body import AssetsUpdateAssetBody
from ...models.ocv1_assets_operation import OCV1AssetsOperation
from ...models.ocv1_assets_status import OCV1AssetsStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    *,
    body: AssetsUpdateAssetBody | Unset = UNSET,
    update_mask: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["updateMask"] = update_mask

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/assets/v1/assets/{asset_id}".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | OCV1AssetsOperation | OCV1AssetsStatus | None:
    if response.status_code == 200:
        response_200 = OCV1AssetsOperation.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = OCV1AssetsStatus.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | OCV1AssetsOperation | OCV1AssetsStatus]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient,
    body: AssetsUpdateAssetBody | Unset = UNSET,
    update_mask: str | Unset = UNSET,
) -> Response[Any | OCV1AssetsOperation | OCV1AssetsStatus]:
    """Updates an asset with provided content and metadata.

     Updates an asset with provided content and metadata, including the description, display name, icon,
    social links, and previews. Currently can only update the content body for **Models**. Icons and
    Previews must be **Image** assets. Icons must have square dimensions.

    Provide the [Asset](#Asset), binary asset file path, and [content type](/cloud/guides/usage-
    assets.md#supported-asset-types-and-limits) in the form data.

    Args:
        asset_id (str):
        update_mask (str | Unset):
        body (AssetsUpdateAssetBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OCV1AssetsOperation | OCV1AssetsStatus]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
        update_mask=update_mask,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    *,
    client: AuthenticatedClient,
    body: AssetsUpdateAssetBody | Unset = UNSET,
    update_mask: str | Unset = UNSET,
) -> Any | OCV1AssetsOperation | OCV1AssetsStatus | None:
    """Updates an asset with provided content and metadata.

     Updates an asset with provided content and metadata, including the description, display name, icon,
    social links, and previews. Currently can only update the content body for **Models**. Icons and
    Previews must be **Image** assets. Icons must have square dimensions.

    Provide the [Asset](#Asset), binary asset file path, and [content type](/cloud/guides/usage-
    assets.md#supported-asset-types-and-limits) in the form data.

    Args:
        asset_id (str):
        update_mask (str | Unset):
        body (AssetsUpdateAssetBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OCV1AssetsOperation | OCV1AssetsStatus
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        body=body,
        update_mask=update_mask,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient,
    body: AssetsUpdateAssetBody | Unset = UNSET,
    update_mask: str | Unset = UNSET,
) -> Response[Any | OCV1AssetsOperation | OCV1AssetsStatus]:
    """Updates an asset with provided content and metadata.

     Updates an asset with provided content and metadata, including the description, display name, icon,
    social links, and previews. Currently can only update the content body for **Models**. Icons and
    Previews must be **Image** assets. Icons must have square dimensions.

    Provide the [Asset](#Asset), binary asset file path, and [content type](/cloud/guides/usage-
    assets.md#supported-asset-types-and-limits) in the form data.

    Args:
        asset_id (str):
        update_mask (str | Unset):
        body (AssetsUpdateAssetBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OCV1AssetsOperation | OCV1AssetsStatus]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
        update_mask=update_mask,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    *,
    client: AuthenticatedClient,
    body: AssetsUpdateAssetBody | Unset = UNSET,
    update_mask: str | Unset = UNSET,
) -> Any | OCV1AssetsOperation | OCV1AssetsStatus | None:
    """Updates an asset with provided content and metadata.

     Updates an asset with provided content and metadata, including the description, display name, icon,
    social links, and previews. Currently can only update the content body for **Models**. Icons and
    Previews must be **Image** assets. Icons must have square dimensions.

    Provide the [Asset](#Asset), binary asset file path, and [content type](/cloud/guides/usage-
    assets.md#supported-asset-types-and-limits) in the form data.

    Args:
        asset_id (str):
        update_mask (str | Unset):
        body (AssetsUpdateAssetBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OCV1AssetsOperation | OCV1AssetsStatus
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            body=body,
            update_mask=update_mask,
        )
    ).parsed
