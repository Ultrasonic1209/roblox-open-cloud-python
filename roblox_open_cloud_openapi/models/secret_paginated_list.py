from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.secret import Secret


T = TypeVar("T", bound="SecretPaginatedList")


@_attrs_define
class SecretPaginatedList:
    """Wrapper for the paginated collection output.
    Complies with the REST conventions, containing
    next/previous page, and a data field containing the actual list.

    Needed only to simplify JSON serialization, and can technically
    be AutoMapper-ed from the EaaS or any other data provider.

        Attributes:
            secrets (list[Secret] | None | Unset): Gets the actual list of items to return
            next_page_cursor (None | str | Unset): Gets the cursor where the pagination stopped after fetching `data`.
                `null` if there is no more data available.
            previous_page_cursor (None | str | Unset): Gets the cursor pointing at the previous page. `null` when it's
                the first page.
    """

    secrets: list[Secret] | None | Unset = UNSET
    next_page_cursor: None | str | Unset = UNSET
    previous_page_cursor: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        secrets: list[dict[str, Any]] | None | Unset
        if isinstance(self.secrets, Unset):
            secrets = UNSET
        elif isinstance(self.secrets, list):
            secrets = []
            for secrets_type_0_item_data in self.secrets:
                secrets_type_0_item = secrets_type_0_item_data.to_dict()
                secrets.append(secrets_type_0_item)

        else:
            secrets = self.secrets

        next_page_cursor: None | str | Unset
        if isinstance(self.next_page_cursor, Unset):
            next_page_cursor = UNSET
        else:
            next_page_cursor = self.next_page_cursor

        previous_page_cursor: None | str | Unset
        if isinstance(self.previous_page_cursor, Unset):
            previous_page_cursor = UNSET
        else:
            previous_page_cursor = self.previous_page_cursor

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if secrets is not UNSET:
            field_dict["secrets"] = secrets
        if next_page_cursor is not UNSET:
            field_dict["nextPageCursor"] = next_page_cursor
        if previous_page_cursor is not UNSET:
            field_dict["previousPageCursor"] = previous_page_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.secret import Secret

        d = dict(src_dict)

        def _parse_secrets(data: object) -> list[Secret] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                secrets_type_0 = []
                _secrets_type_0 = data
                for secrets_type_0_item_data in _secrets_type_0:
                    secrets_type_0_item = Secret.from_dict(secrets_type_0_item_data)

                    secrets_type_0.append(secrets_type_0_item)

                return secrets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Secret] | None | Unset, data)

        secrets = _parse_secrets(d.pop("secrets", UNSET))

        def _parse_next_page_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_cursor = _parse_next_page_cursor(d.pop("nextPageCursor", UNSET))

        def _parse_previous_page_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_page_cursor = _parse_previous_page_cursor(d.pop("previousPageCursor", UNSET))

        secret_paginated_list = cls(
            secrets=secrets,
            next_page_cursor=next_page_cursor,
            previous_page_cursor=previous_page_cursor,
        )

        return secret_paginated_list
