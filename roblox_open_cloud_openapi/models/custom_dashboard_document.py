from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_dashboard_config import CustomDashboardConfig


T = TypeVar("T", bound="CustomDashboardDocument")


@_attrs_define
class CustomDashboardDocument:
    """CustomDashboardDocument is the dashboard authoring document persisted as the
    latest published content. Draft edits remain local client state until the
    caller sends this document to create or publish a dashboard.

        Attributes:
            schema_version (int | None | Unset):  Default: 0.
            config (CustomDashboardConfig | None | Unset): CustomDashboardConfig is the renderer-owned dashboard authoring
                model. It is
                intentionally a normalized dashboard document rather than a direct mirror of
                Creator Hub RAQI TypeScript config types. Creator Hub adapters may generate
                TS from this proto and map it into the current RAQI renderer.
    """

    schema_version: int | None | Unset = 0
    config: CustomDashboardConfig | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_dashboard_config import CustomDashboardConfig  # noqa: PLC0415

        schema_version: int | None | Unset
        if isinstance(self.schema_version, Unset):
            schema_version = UNSET
        else:
            schema_version = self.schema_version

        config: dict[str, Any] | None | Unset
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, CustomDashboardConfig):
            config = self.config.to_dict()
        else:
            config = self.config

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if schema_version is not UNSET:
            field_dict["schemaVersion"] = schema_version
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_dashboard_config import CustomDashboardConfig  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_schema_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        schema_version = _parse_schema_version(d.pop("schemaVersion", UNSET))

        def _parse_config(data: object) -> CustomDashboardConfig | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = CustomDashboardConfig.from_dict(data)

                return config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CustomDashboardConfig | None | Unset, data)

        config = _parse_config(d.pop("config", UNSET))

        custom_dashboard_document = cls(
            schema_version=schema_version,
            config=config,
        )

        return custom_dashboard_document
