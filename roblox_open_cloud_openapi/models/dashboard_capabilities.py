from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_limits import DashboardLimits


T = TypeVar("T", bound="DashboardCapabilities")


@_attrs_define
class DashboardCapabilities:
    """DashboardCapabilities describes what the calling creator may do in a universe
    and the limits the service enforces on writes. Limits can change without a
    client update. Open Cloud credential scopes are enforced separately by API
    Gateway. These booleans describe creator permissions, not credential scopes.

        Attributes:
            universe_id (None | str | Unset): Signed 64-bit integer encoded as a decimal string. Default: '0'.
            can_create (bool | None | Unset): True when the caller may create a new dashboard in this universe. Default:
                False.
            can_edit (bool | None | Unset): True when the caller may change dashboard metadata. Default: False.
            can_publish (bool | None | Unset): True when the caller may replace a dashboard's published document. Default:
                False.
            can_delete (bool | None | Unset): True when the caller may soft-delete a dashboard. Default: False.
            limits (DashboardLimits | None | Unset): DashboardLimits mirrors the write-time caps enforced by this service.
                Values
                are resolved per request, so they reflect the current runtime configuration
                rather than the values present at deploy time. A limit of 0 means the cap is
                disabled and the service does not enforce it.

                Clients should treat these as upper bounds and may apply a stricter
                presentation limit of their own; the effective cap for a client is the
                minimum of the two.
    """

    universe_id: None | str | Unset = "0"
    can_create: bool | None | Unset = False
    can_edit: bool | None | Unset = False
    can_publish: bool | None | Unset = False
    can_delete: bool | None | Unset = False
    limits: DashboardLimits | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_limits import DashboardLimits  # noqa: PLC0415

        universe_id: None | str | Unset
        if isinstance(self.universe_id, Unset):
            universe_id = UNSET
        else:
            universe_id = self.universe_id

        can_create: bool | None | Unset
        if isinstance(self.can_create, Unset):
            can_create = UNSET
        else:
            can_create = self.can_create

        can_edit: bool | None | Unset
        if isinstance(self.can_edit, Unset):
            can_edit = UNSET
        else:
            can_edit = self.can_edit

        can_publish: bool | None | Unset
        if isinstance(self.can_publish, Unset):
            can_publish = UNSET
        else:
            can_publish = self.can_publish

        can_delete: bool | None | Unset
        if isinstance(self.can_delete, Unset):
            can_delete = UNSET
        else:
            can_delete = self.can_delete

        limits: dict[str, Any] | None | Unset
        if isinstance(self.limits, Unset):
            limits = UNSET
        elif isinstance(self.limits, DashboardLimits):
            limits = self.limits.to_dict()
        else:
            limits = self.limits

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if can_create is not UNSET:
            field_dict["canCreate"] = can_create
        if can_edit is not UNSET:
            field_dict["canEdit"] = can_edit
        if can_publish is not UNSET:
            field_dict["canPublish"] = can_publish
        if can_delete is not UNSET:
            field_dict["canDelete"] = can_delete
        if limits is not UNSET:
            field_dict["limits"] = limits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_limits import DashboardLimits  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_universe_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        universe_id = _parse_universe_id(d.pop("universeId", UNSET))

        def _parse_can_create(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_create = _parse_can_create(d.pop("canCreate", UNSET))

        def _parse_can_edit(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_edit = _parse_can_edit(d.pop("canEdit", UNSET))

        def _parse_can_publish(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_publish = _parse_can_publish(d.pop("canPublish", UNSET))

        def _parse_can_delete(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_delete = _parse_can_delete(d.pop("canDelete", UNSET))

        def _parse_limits(data: object) -> DashboardLimits | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                limits_type_0 = DashboardLimits.from_dict(data)

                return limits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardLimits | None | Unset, data)

        limits = _parse_limits(d.pop("limits", UNSET))

        dashboard_capabilities = cls(
            universe_id=universe_id,
            can_create=can_create,
            can_edit=can_edit,
            can_publish=can_publish,
            can_delete=can_delete,
            limits=limits,
        )

        return dashboard_capabilities
