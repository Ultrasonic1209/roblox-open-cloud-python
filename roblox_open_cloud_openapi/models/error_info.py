from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_info_metadata_type_0 import ErrorInfoMetadataType0


T = TypeVar("T", bound="ErrorInfo")


@_attrs_define
class ErrorInfo:
    """
    Attributes:
        reason (None | str | Unset):
        domain (None | str | Unset):
        metadata (ErrorInfoMetadataType0 | None | Unset):
    """

    reason: None | str | Unset = UNSET
    domain: None | str | Unset = UNSET
    metadata: ErrorInfoMetadataType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.error_info_metadata_type_0 import ErrorInfoMetadataType0  # noqa: PLC0415

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, ErrorInfoMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if reason is not UNSET:
            field_dict["reason"] = reason
        if domain is not UNSET:
            field_dict["domain"] = domain
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_info_metadata_type_0 import ErrorInfoMetadataType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

        def _parse_metadata(data: object) -> ErrorInfoMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = ErrorInfoMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ErrorInfoMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        error_info = cls(
            reason=reason,
            domain=domain,
            metadata=metadata,
        )

        return error_info
