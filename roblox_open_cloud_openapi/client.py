import ssl
import sys
from collections.abc import Callable, Coroutine
from http import HTTPStatus
from typing import Any, Literal, TypedDict, cast

import httpx2
from attrs import define, evolve, field
from httpx_limiter import AbstractRateLimiterRepository, AsyncMultiRateLimitedTransport, Rate
from httpx_limiter.pyrate import PyrateAsyncLimiter
from httpx_retries import Retry, RetryTransport

assert not "httpx" in sys.modules, "httpx is not supported"
assert "httpx2" in sys.modules, "httpx2 is required"

sys.modules["httpx"] = sys.modules["httpx2"]
for name, module in list(sys.modules.items()):
    if name.startswith("httpx2.") and module is not None:
        sys.modules.setdefault("httpx." + name.removeprefix("httpx2."), module)


class RobloxRateLimit(TypedDict):
    period: Literal["MINUTE"] | Literal["SECOND"]
    maxInPeriod: int


class AsyncRobloxOpenAPIDefinedRateLimiterRepository(AbstractRateLimiterRepository):
    """Apply different rate limits based on the endpoint being requested, based off endpoint extension "x-roblox-rate-limits"."""

    def get_identifier(self, request: httpx2.Request) -> str:
        """Return the OpenAPI Endpoint ID as the identifier for rate limiting."""
        identifier = cast(str | None, request.extensions.get("openapi-id"))

        return identifier or (request.url.host + request.url.path + ":" + request.method)

    def create_rate(self, request: httpx2.Request) -> Rate:
        extensions = cast(dict[str, Any] | None, request.extensions.get("openapi-extensions"))

        default_ret = Rate.create(magnitude=1000)
        if not extensions:
            return default_ret

        roblox_rate_limits = cast(dict[str, RobloxRateLimit] | None, extensions.get("x-roblox-rate-limits"))

        if not roblox_rate_limits:
            return default_ret

        api_key_limits = roblox_rate_limits.get("perApiKeyOwner")

        if not api_key_limits:
            return default_ret

        magnitude = api_key_limits["maxInPeriod"]
        duration = 60 if api_key_limits["maxInPeriod"] == "MINUTE" else 1

        return Rate.create(magnitude=magnitude, duration=duration)

    def create(self, request: httpx2.Request) -> PyrateAsyncLimiter:
        """Create a rate limiter for the endpoint."""
        rate = self.create_rate(request)

        return PyrateAsyncLimiter.create(rate)


class CSRFHandlingTransport(httpx2.BaseTransport, httpx2.AsyncBaseTransport):
    """
    A transport that handles Roblox's CSRF header flow by automatically retrying requests
    if they are responded with HTTP 403 (Forbidden) along with a new X-CSRF-Token

    in any case, all CSRF-eligible requests are sent with the last recieved X-CSRF-Token
    header injected
    """

    def __init__(self, transport: httpx2.BaseTransport | httpx2.AsyncBaseTransport | None = None):
        if transport is not None:
            self._sync_transport = transport if isinstance(transport, httpx2.BaseTransport) else None
            self._async_transport = transport if isinstance(transport, httpx2.AsyncBaseTransport) else None
        else:
            self._sync_transport = httpx2.HTTPTransport()
            self._async_transport = httpx2.AsyncHTTPTransport()

        self.__X_CSRF_TOKEN = None

    @staticmethod
    def _can_use_csrf(request: httpx2.Request) -> bool:
        """
        Returns whether the request should be subject to this transport's logic
        """

        return request.method in ("POST", "PUT", "PATCH", "DELETE")

    def close(self) -> None:
        """
        Closes this transport.
        """
        if self._sync_transport is not None:
            self._sync_transport.close()

    async def aclose(self) -> None:
        """
        Closes this transport.
        """
        if self._async_transport is not None:
            await self._async_transport.aclose()

    def _handle_request_with_csrf(
        self, request: httpx2.Request, handle_request: Callable[..., httpx2.Response]
    ) -> httpx2.Response:

        if self.__X_CSRF_TOKEN:
            request.headers["X-CSRF-Token"] = self.__X_CSRF_TOKEN

        response = handle_request(request)

        return response

    async def _handle_request_with_csrf_async(
        self, request: httpx2.Request, handle_request: Callable[..., Coroutine[Any, Any, httpx2.Response]]
    ) -> httpx2.Response:

        if self.__X_CSRF_TOKEN:
            request.headers["X-CSRF-Token"] = self.__X_CSRF_TOKEN

        response = await handle_request(request)

        return response

    def handle_request(self, request: httpx2.Request) -> httpx2.Response:
        if self._sync_transport is None:
            raise RuntimeError(
                "This transport was initalised with an underlying AsyncBaseTransport, so it cannot accept synchronous requests"
            )

        if self._can_use_csrf(request):
            response = self._handle_request_with_csrf(request, self._sync_transport.handle_request)

            if x_csrf_token := response.headers.get("X-CSRF-Token"):
                is_new_csrf = x_csrf_token != self.__X_CSRF_TOKEN
                self.__X_CSRF_TOKEN = x_csrf_token
                if is_new_csrf and (response.status_code == HTTPStatus.FORBIDDEN):
                    response = self._handle_request_with_csrf(request, self._sync_transport.handle_request)
        else:
            response = self._sync_transport.handle_request(request)

        return response

    async def handle_async_request(self, request: httpx2.Request) -> httpx2.Response:
        if self._async_transport is None:
            raise RuntimeError(
                "This transport was initalised with an underlying BaseTransport, so it cannot accept asynchronous requests"
            )

        if self._can_use_csrf(request):
            response = await self._handle_request_with_csrf_async(request, self._async_transport.handle_async_request)

            if x_csrf_token := response.headers.get("X-CSRF-Token"):
                is_new_csrf = x_csrf_token != self.__X_CSRF_TOKEN
                self.__X_CSRF_TOKEN = x_csrf_token
                if is_new_csrf and (response.status_code == HTTPStatus.FORBIDDEN):
                    response = await self._handle_request_with_csrf_async(
                        request, self._async_transport.handle_async_request
                    )
        else:
            response = await self._async_transport.handle_async_request(request)

        return response


@define
class Client:
    """A class for keeping track of data related to the API

        The following are accepted as keyword arguments and will be used to construct httpx2 Clients internally:

        ``base_url``: The base URL for the API, all requests are made to a relative path to this URL

        ``cookies``: A dictionary of cookies to be sent with every request

        ``headers``: A dictionary of headers to be sent with every request

        ``timeout``: The maximum amount of a time a request can take. API functions will raise
        httpx2.TimeoutException if this is exceeded.

        ``verify_ssl``: Whether or not to verify the SSL certificate of the API server. This should be True in production,
        but can be set to False for testing purposes.

        ``follow_redirects``: Whether or not to follow redirects. Default value is False.

        ``httpx2_args``: A dictionary of additional arguments to be passed to the ``httpx2.Client`` and ``httpx2.AsyncClient`` constructor.


    Attributes:
            raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns
            a status code that was not documented in the source OpenAPI document. Can also be provided as a
            keyword argument to the constructor.
    """

    raise_on_unexpected_status: bool = field(default=False, kw_only=True)
    _base_url: str = field(default="https://apis.roblox.com", kw_only=True, alias="base_url")
    _cookies: dict[str, str] = field(factory=dict, kw_only=True, alias="cookies")

    _headers: dict[str, str] = field(
        factory=dict,
        converter=lambda h: {"User-Agent": "roblox_open_cloud_openapi/0.1.0"} | h,
        kw_only=True,
        alias="headers",
    )
    _timeout: httpx2.Timeout | None = field(default=None, kw_only=True, alias="timeout")
    _verify_ssl: str | bool | ssl.SSLContext = field(default=True, kw_only=True, alias="verify_ssl")
    _follow_redirects: bool = field(default=False, kw_only=True, alias="follow_redirects")
    _httpx2_args: dict[str, Any] = field(factory=dict, kw_only=True, alias="httpx2_args")
    _client: httpx2.Client | None = field(default=None, init=False)
    _async_client: httpx2.AsyncClient | None = field(default=None, init=False)

    def with_headers(self, headers: dict[str, str]) -> "Client":
        """Get a new client matching this one with additional headers"""
        if self._client is not None:
            self._client.headers.update(headers)
        if self._async_client is not None:
            self._async_client.headers.update(headers)
        return evolve(self, headers={**self._headers, **headers})

    def with_cookies(self, cookies: dict[str, str]) -> "Client":
        """Get a new client matching this one with additional cookies"""
        if self._client is not None:
            self._client.cookies.update(cookies)
        if self._async_client is not None:
            self._async_client.cookies.update(cookies)
        return evolve(self, cookies={**self._cookies, **cookies})

    def with_timeout(self, timeout: httpx2.Timeout) -> "Client":
        """Get a new client matching this one with a new timeout configuration"""
        if self._client is not None:
            self._client.timeout = timeout
        if self._async_client is not None:
            self._async_client.timeout = timeout
        return evolve(self, timeout=timeout)

    def set_httpx2_client(self, client: httpx2.Client) -> "Client":
        """Manually set the underlying httpx2.Client

        **NOTE**: This will override any other settings on the client, including cookies, headers, and timeout.
        """
        self._client = client
        return self

    def get_httpx2_client(self) -> httpx2.Client:
        """Get the underlying httpx2.Client, constructing a new one if not previously set"""
        if self._client is None:
            transport = CSRFHandlingTransport(RetryTransport(retry=Retry(total=5, backoff_factor=0.5)))

            self._client = httpx2.Client(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                transport=transport,
                **self._httpx2_args,
            )
        return self._client

    def __enter__(self) -> "Client":
        """Enter a context manager for self.client—you cannot enter twice (see httpx2 docs)"""
        self.get_httpx2_client().__enter__()
        return self

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        """Exit a context manager for internal httpx2.Client (see httpx2 docs)"""
        self.get_httpx2_client().__exit__(*args, **kwargs)

    def set_async_httpx2_client(self, async_client: httpx2.AsyncClient) -> "Client":
        """Manually set the underlying httpx2.AsyncClient

        **NOTE**: This will override any other settings on the client, including cookies, headers, and timeout.
        """
        self._async_client = async_client
        return self

    def get_async_httpx2_client(self) -> httpx2.AsyncClient:
        """Get the underlying httpx2.AsyncClient, constructing a new one if not previously set"""
        if self._async_client is None:
            transport = AsyncMultiRateLimitedTransport(
                repository=AsyncRobloxOpenAPIDefinedRateLimiterRepository(),
                transport=CSRFHandlingTransport(
                    RetryTransport(
                        retry=Retry(total=5, backoff_factor=0.5),
                    )
                ),
            )

            self._async_client = httpx2.AsyncClient(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                transport=transport,
                **self._httpx2_args,
            )
        return self._async_client

    async def __aenter__(self) -> "Client":
        """Enter a context manager for underlying httpx2.AsyncClient—you cannot enter twice (see httpx2 docs)"""
        await self.get_async_httpx2_client().__aenter__()
        return self

    async def __aexit__(self, *args: Any, **kwargs: Any) -> None:
        """Exit a context manager for underlying httpx2.AsyncClient (see httpx2 docs)"""
        await self.get_async_httpx2_client().__aexit__(*args, **kwargs)


@define
class AuthenticatedClient:
    """A Client which has been authenticated for use on secured endpoints

    The following are accepted as keyword arguments and will be used to construct httpx2 Clients internally:

        ``base_url``: The base URL for the API, all requests are made to a relative path to this URL

        ``cookies``: A dictionary of cookies to be sent with every request

        ``headers``: A dictionary of headers to be sent with every request

        ``timeout``: The maximum amount of a time a request can take. API functions will raise
        httpx2.TimeoutException if this is exceeded.

        ``verify_ssl``: Whether or not to verify the SSL certificate of the API server. This should be True in production,
        but can be set to False for testing purposes.

        ``follow_redirects``: Whether or not to follow redirects. Default value is False.

        ``httpx2_args``: A dictionary of additional arguments to be passed to the ``httpx2.Client`` and ``httpx2.AsyncClient`` constructor.


    Attributes:
            raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns
            a status code that was not documented in the source OpenAPI document. Can also be provided as a
            keyword argument to the constructor.
            token: The token to use for authentication
            prefix: The prefix to use for the Authorization header
            auth_header_name: The name of the Authorization header
    """

    raise_on_unexpected_status: bool = field(default=False, kw_only=True)
    _base_url: str = field(default="https://apis.roblox.com", kw_only=True, alias="base_url")
    _cookies: dict[str, str] = field(factory=dict, kw_only=True, alias="cookies")

    _headers: dict[str, str] = field(
        factory=dict,
        converter=lambda h: {"User-Agent": "roblox_open_cloud_openapi/0.1.0"} | h,
        kw_only=True,
        alias="headers",
    )
    _timeout: httpx2.Timeout | None = field(default=None, kw_only=True, alias="timeout")
    _verify_ssl: str | bool | ssl.SSLContext = field(default=True, kw_only=True, alias="verify_ssl")
    _follow_redirects: bool = field(default=False, kw_only=True, alias="follow_redirects")
    _httpx2_args: dict[str, Any] = field(factory=dict, kw_only=True, alias="httpx2_args")
    _client: httpx2.Client | None = field(default=None, init=False)
    _async_client: httpx2.AsyncClient | None = field(default=None, init=False)

    token: str
    prefix: str = "Bearer"
    auth_header_name: str = "Authorization"

    def with_headers(self, headers: dict[str, str]) -> "AuthenticatedClient":
        """Get a new client matching this one with additional headers"""
        if self._client is not None:
            self._client.headers.update(headers)
        if self._async_client is not None:
            self._async_client.headers.update(headers)
        return evolve(self, headers={**self._headers, **headers})

    def with_cookies(self, cookies: dict[str, str]) -> "AuthenticatedClient":
        """Get a new client matching this one with additional cookies"""
        if self._client is not None:
            self._client.cookies.update(cookies)
        if self._async_client is not None:
            self._async_client.cookies.update(cookies)
        return evolve(self, cookies={**self._cookies, **cookies})

    def with_timeout(self, timeout: httpx2.Timeout) -> "AuthenticatedClient":
        """Get a new client matching this one with a new timeout configuration"""
        if self._client is not None:
            self._client.timeout = timeout
        if self._async_client is not None:
            self._async_client.timeout = timeout
        return evolve(self, timeout=timeout)

    def set_httpx2_client(self, client: httpx2.Client) -> "AuthenticatedClient":
        """Manually set the underlying httpx2.Client

        **NOTE**: This will override any other settings on the client, including cookies, headers, and timeout.
        """
        self._client = client
        return self

    def get_httpx2_client(self) -> httpx2.Client:
        """Get the underlying httpx2.Client, constructing a new one if not previously set"""
        if self._client is None:
            self._headers[self.auth_header_name] = f"{self.prefix} {self.token}" if self.prefix else self.token
            transport = CSRFHandlingTransport(RetryTransport(retry=Retry(total=5, backoff_factor=0.5)))

            self._client = httpx2.Client(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                transport=transport,
                **self._httpx2_args,
            )
        return self._client

    def __enter__(self) -> "AuthenticatedClient":
        """Enter a context manager for self.client—you cannot enter twice (see httpx2 docs)"""
        self.get_httpx2_client().__enter__()
        return self

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        """Exit a context manager for internal httpx2.Client (see httpx2 docs)"""
        self.get_httpx2_client().__exit__(*args, **kwargs)

    def set_async_httpx2_client(self, async_client: httpx2.AsyncClient) -> "AuthenticatedClient":
        """Manually set the underlying httpx2.AsyncClient

        **NOTE**: This will override any other settings on the client, including cookies, headers, and timeout.
        """
        self._async_client = async_client
        return self

    def get_async_httpx2_client(self) -> httpx2.AsyncClient:
        """Get the underlying httpx2.AsyncClient, constructing a new one if not previously set"""
        if self._async_client is None:
            self._headers[self.auth_header_name] = f"{self.prefix} {self.token}" if self.prefix else self.token
            transport = AsyncMultiRateLimitedTransport(
                repository=AsyncRobloxOpenAPIDefinedRateLimiterRepository(),
                transport=CSRFHandlingTransport(
                    RetryTransport(
                        retry=Retry(total=5, backoff_factor=0.5),
                    )
                ),
            )

            self._async_client = httpx2.AsyncClient(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._headers,
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                transport=transport,
                **self._httpx2_args,
            )
        return self._async_client

    async def __aenter__(self) -> "AuthenticatedClient":
        """Enter a context manager for underlying httpx2.AsyncClient—you cannot enter twice (see httpx2 docs)"""
        await self.get_async_httpx2_client().__aenter__()
        return self

    async def __aexit__(self, *args: Any, **kwargs: Any) -> None:
        """Exit a context manager for underlying httpx2.AsyncClient (see httpx2 docs)"""
        await self.get_async_httpx2_client().__aexit__(*args, **kwargs)
