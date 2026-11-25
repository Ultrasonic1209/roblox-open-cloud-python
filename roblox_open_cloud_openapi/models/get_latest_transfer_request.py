from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.resource import Resource


T = TypeVar("T", bound="GetLatestTransferRequest")


@_attrs_define
class GetLatestTransferRequest:
    """
    Attributes:
        resource (Resource):
    """

    resource: Resource

    def to_dict(self) -> dict[str, Any]:
        resource = self.resource.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "resource": resource,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource import Resource  # noqa: PLC0415

        d = dict(src_dict)
        resource = Resource.from_dict(d.pop("resource"))

        get_latest_transfer_request = cls(
            resource=resource,
        )

        return get_latest_transfer_request
