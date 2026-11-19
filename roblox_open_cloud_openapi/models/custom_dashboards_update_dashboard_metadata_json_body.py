from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_metadata_patch import DashboardMetadataPatch


T = TypeVar("T", bound="CustomDashboardsUpdateDashboardMetadataJsonBody")


@_attrs_define
class CustomDashboardsUpdateDashboardMetadataJsonBody:
    """
    Attributes:
        expected_head_etag (None | str | Unset): Required. Enforced for name/description CAS. Ignored for pin-only
            patches;
            those rebase is_pinned onto the current head and do not rewrite other fields. Default: ''.
        patch (DashboardMetadataPatch | None | Unset): DashboardMetadataPatch updates dashboard metadata without
            exposing storage rows.
    """

    expected_head_etag: None | str | Unset = ""
    patch: DashboardMetadataPatch | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_metadata_patch import DashboardMetadataPatch  # noqa: PLC0415

        expected_head_etag: None | str | Unset
        if isinstance(self.expected_head_etag, Unset):
            expected_head_etag = UNSET
        else:
            expected_head_etag = self.expected_head_etag

        patch: dict[str, Any] | None | Unset
        if isinstance(self.patch, Unset):
            patch = UNSET
        elif isinstance(self.patch, DashboardMetadataPatch):
            patch = self.patch.to_dict()
        else:
            patch = self.patch

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if expected_head_etag is not UNSET:
            field_dict["expectedHeadEtag"] = expected_head_etag
        if patch is not UNSET:
            field_dict["patch"] = patch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_metadata_patch import DashboardMetadataPatch  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_expected_head_etag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expected_head_etag = _parse_expected_head_etag(d.pop("expectedHeadEtag", UNSET))

        def _parse_patch(data: object) -> DashboardMetadataPatch | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                patch_type_0 = DashboardMetadataPatch.from_dict(data)

                return patch_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardMetadataPatch | None | Unset, data)

        patch = _parse_patch(d.pop("patch", UNSET))

        custom_dashboards_update_dashboard_metadata_json_body = cls(
            expected_head_etag=expected_head_etag,
            patch=patch,
        )

        return custom_dashboards_update_dashboard_metadata_json_body
