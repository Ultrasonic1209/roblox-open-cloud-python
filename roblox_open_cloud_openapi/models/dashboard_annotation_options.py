from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardAnnotationOptions")


@_attrs_define
class DashboardAnnotationOptions:
    """DashboardAnnotationOptions defines annotation controls for a dashboard surface.

    Attributes:
        default_annotation_type_keys (list[str] | None | Unset):
        show_annotations_control (bool | None | Unset):  Default: False.
    """

    default_annotation_type_keys: list[str] | None | Unset = UNSET
    show_annotations_control: bool | None | Unset = False

    def to_dict(self) -> dict[str, Any]:
        default_annotation_type_keys: list[str] | None | Unset
        if isinstance(self.default_annotation_type_keys, Unset):
            default_annotation_type_keys = UNSET
        elif isinstance(self.default_annotation_type_keys, list):
            default_annotation_type_keys = self.default_annotation_type_keys

        else:
            default_annotation_type_keys = self.default_annotation_type_keys

        show_annotations_control: bool | None | Unset
        if isinstance(self.show_annotations_control, Unset):
            show_annotations_control = UNSET
        else:
            show_annotations_control = self.show_annotations_control

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if default_annotation_type_keys is not UNSET:
            field_dict["defaultAnnotationTypeKeys"] = default_annotation_type_keys
        if show_annotations_control is not UNSET:
            field_dict["showAnnotationsControl"] = show_annotations_control

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_default_annotation_type_keys(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                default_annotation_type_keys_type_0 = cast(list[str], data)

                return default_annotation_type_keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        default_annotation_type_keys = _parse_default_annotation_type_keys(d.pop("defaultAnnotationTypeKeys", UNSET))

        def _parse_show_annotations_control(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_annotations_control = _parse_show_annotations_control(d.pop("showAnnotationsControl", UNSET))

        dashboard_annotation_options = cls(
            default_annotation_type_keys=default_annotation_type_keys,
            show_annotations_control=show_annotations_control,
        )

        return dashboard_annotation_options
