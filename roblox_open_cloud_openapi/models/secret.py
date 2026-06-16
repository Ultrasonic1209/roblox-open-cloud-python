from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Secret")


@_attrs_define
class Secret:
    """Universe-specific secret, identified by `id`, and belonging to a specific `environment`.

    Attributes:
        id (None | str | Unset): The user-specified secret name. Examples: "aws", "gcp", "discord".

            Static when getting the public key for a universe.

            Must be alphanumeric or underscore, 1-64 characters, not starting with a number.
        secret (None | str | Unset): The binary secret content. Examples: API key content (text), private keys.

            When created, the secret must be encrypted using LibSodium sealed box and encoded in base64 with the universe's
            public key.

            Contains the public key when getting the public key for a universe.
        key_id (None | str | Unset): Encryption key identifier. Identifies the key that was used to encrypt the secret
            content.
        domain (None | str | Unset): The domain wildcard that restricts the purpose of the key.

            You can restrict the URLs callable via HttpService to a specific domain, e.g. "api.example.com" or
            "*.myservice.org".

            An empty or null domain means that the secret is a private key and cannot be transformed with
            addPrefix/addSuffix or sent as a header or URL.

            In order to make the secret accessible for all domains, use "*"
        create_time (None | str | Unset): Date and time when the secret was originally created.
        update_time (None | str | Unset): Date and time when the secret was last updated
    """

    id: None | str | Unset = UNSET
    secret: None | str | Unset = UNSET
    key_id: None | str | Unset = UNSET
    domain: None | str | Unset = UNSET
    create_time: None | str | Unset = UNSET
    update_time: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        secret: None | str | Unset
        if isinstance(self.secret, Unset):
            secret = UNSET
        else:
            secret = self.secret

        key_id: None | str | Unset
        if isinstance(self.key_id, Unset):
            key_id = UNSET
        else:
            key_id = self.key_id

        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        create_time: None | str | Unset
        if isinstance(self.create_time, Unset):
            create_time = UNSET
        else:
            create_time = self.create_time

        update_time: None | str | Unset
        if isinstance(self.update_time, Unset):
            update_time = UNSET
        else:
            update_time = self.update_time

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if secret is not UNSET:
            field_dict["secret"] = secret
        if key_id is not UNSET:
            field_dict["key_id"] = key_id
        if domain is not UNSET:
            field_dict["domain"] = domain
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        secret = _parse_secret(d.pop("secret", UNSET))

        def _parse_key_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_id = _parse_key_id(d.pop("key_id", UNSET))

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

        def _parse_create_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        create_time = _parse_create_time(d.pop("create_time", UNSET))

        def _parse_update_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        update_time = _parse_update_time(d.pop("update_time", UNSET))

        secret = cls(
            id=id,
            secret=secret,
            key_id=key_id,
            domain=domain,
            create_time=create_time,
            update_time=update_time,
        )

        return secret
