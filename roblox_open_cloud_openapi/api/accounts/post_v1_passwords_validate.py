import sys
from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_authentication_api_models_password_validation_model import (
    RobloxAuthenticationApiModelsPasswordValidationModel,
)
from ...models.roblox_authentication_api_models_password_validation_response import (
    RobloxAuthenticationApiModelsPasswordValidationResponse,
)


def _get_kwargs(
    *,
    body: RobloxAuthenticationApiModelsPasswordValidationModel
    | RobloxAuthenticationApiModelsPasswordValidationModel
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://auth.roblox.com/v1/passwords/validate",
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            "x-roblox-recommended-alternatives": [
                {
                    "url": "https://auth.roblox.com/v2/passwords/validate",
                    "httpMethod": "POST",
                    "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/accounts#auth_post_v2_passwords_validate",
                }
            ],
        },
        "openapi-id": "post_v1_passwords_validate",
    }

    if isinstance(body, RobloxAuthenticationApiModelsPasswordValidationModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxAuthenticationApiModelsPasswordValidationModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxAuthenticationApiModelsPasswordValidationResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAuthenticationApiModelsPasswordValidationResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxAuthenticationApiModelsPasswordValidationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#auth_post_v1_passwords_validate"
)
def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsPasswordValidationModel
    | RobloxAuthenticationApiModelsPasswordValidationModel
    | Unset = UNSET,
) -> Response[Any | RobloxAuthenticationApiModelsPasswordValidationResponse]:
    """Endpoint for checking if a password is valid.

    Args:
        body (RobloxAuthenticationApiModelsPasswordValidationModel):
        body (RobloxAuthenticationApiModelsPasswordValidationModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsPasswordValidationResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#auth_post_v1_passwords_validate"
)
def sync(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsPasswordValidationModel
    | RobloxAuthenticationApiModelsPasswordValidationModel
    | Unset = UNSET,
) -> Any | RobloxAuthenticationApiModelsPasswordValidationResponse | None:
    """Endpoint for checking if a password is valid.

    Args:
        body (RobloxAuthenticationApiModelsPasswordValidationModel):
        body (RobloxAuthenticationApiModelsPasswordValidationModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsPasswordValidationResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#auth_post_v1_passwords_validate"
)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsPasswordValidationModel
    | RobloxAuthenticationApiModelsPasswordValidationModel
    | Unset = UNSET,
) -> Response[Any | RobloxAuthenticationApiModelsPasswordValidationResponse]:
    """Endpoint for checking if a password is valid.

    Args:
        body (RobloxAuthenticationApiModelsPasswordValidationModel):
        body (RobloxAuthenticationApiModelsPasswordValidationModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsPasswordValidationResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#auth_post_v1_passwords_validate"
)
async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsPasswordValidationModel
    | RobloxAuthenticationApiModelsPasswordValidationModel
    | Unset = UNSET,
) -> Any | RobloxAuthenticationApiModelsPasswordValidationResponse | None:
    """Endpoint for checking if a password is valid.

    Args:
        body (RobloxAuthenticationApiModelsPasswordValidationModel):
        body (RobloxAuthenticationApiModelsPasswordValidationModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsPasswordValidationResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
