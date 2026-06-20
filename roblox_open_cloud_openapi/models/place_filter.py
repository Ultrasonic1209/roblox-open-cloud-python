from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlaceFilter")


@_attrs_define
class PlaceFilter:
    """Filter for which versions of a place to restart.

    Attributes:
        versions (list[int] | None | Unset): List of placeVersions to restart. Mutually exclusive with
            ServerManagementService.V2.Models.PlaceFilter.ExcludeCurrentVersion.
        exclude_current_version (bool | None | Unset): If true, all versions except the most recently published will be
            restarted.
            Mutually exclusive with ServerManagementService.V2.Models.PlaceFilter.Versions.
    """

    versions: list[int] | None | Unset = UNSET
    exclude_current_version: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        versions: list[int] | None | Unset
        if isinstance(self.versions, Unset):
            versions = UNSET
        elif isinstance(self.versions, list):
            versions = self.versions

        else:
            versions = self.versions

        exclude_current_version: bool | None | Unset
        if isinstance(self.exclude_current_version, Unset):
            exclude_current_version = UNSET
        else:
            exclude_current_version = self.exclude_current_version

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if versions is not UNSET:
            field_dict["versions"] = versions
        if exclude_current_version is not UNSET:
            field_dict["excludeCurrentVersion"] = exclude_current_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_versions(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                versions_type_0 = cast(list[int], data)

                return versions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        versions = _parse_versions(d.pop("versions", UNSET))

        def _parse_exclude_current_version(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        exclude_current_version = _parse_exclude_current_version(d.pop("excludeCurrentVersion", UNSET))

        place_filter = cls(
            versions=versions,
            exclude_current_version=exclude_current_version,
        )

        return place_filter
