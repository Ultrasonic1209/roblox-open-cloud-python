from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GenerateUserThumbnailResponse")


@_attrs_define
class GenerateUserThumbnailResponse:
    """Returns the URL for the user's avatar thumbnail.

    Attributes:
        type_ (None | str | Unset): The fully-qualified type of the packed operation response. Mirrors the
            `@type` field the legacy transcoder emitted via `Any.Pack`, kept so clients
            reading `response["@type"]` continue to work. Declared first so it
            serializes before the payload fields.
        image_uri (None | str | Unset): URI for the generated thumbnail.
    """

    type_: None | str | Unset = UNSET
    image_uri: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        image_uri: None | str | Unset
        if isinstance(self.image_uri, Unset):
            image_uri = UNSET
        else:
            image_uri = self.image_uri

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["@type"] = type_
        if image_uri is not UNSET:
            field_dict["imageUri"] = image_uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("@type", UNSET))

        def _parse_image_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_uri = _parse_image_uri(d.pop("imageUri", UNSET))

        generate_user_thumbnail_response = cls(
            type_=type_,
            image_uri=image_uri,
        )

        return generate_user_thumbnail_response
