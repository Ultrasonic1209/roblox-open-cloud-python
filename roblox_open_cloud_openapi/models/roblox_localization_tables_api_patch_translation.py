from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_localizationtables_localizationtables_v1_change_agent import (
        RobloxLocalizationtablesLocalizationtablesV1ChangeAgent,
    )


T = TypeVar("T", bound="RobloxLocalizationTablesApiPatchTranslation")


@_attrs_define
class RobloxLocalizationTablesApiPatchTranslation:
    """
    Attributes:
        locale (str | Unset):
        translation_text (str | Unset):
        delete (bool | Unset):
        change_agent (RobloxLocalizationtablesLocalizationtablesV1ChangeAgent | Unset):
        updated_time (datetime.datetime | Unset):
    """

    locale: str | Unset = UNSET
    translation_text: str | Unset = UNSET
    delete: bool | Unset = UNSET
    change_agent: RobloxLocalizationtablesLocalizationtablesV1ChangeAgent | Unset = UNSET
    updated_time: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        locale = self.locale

        translation_text = self.translation_text

        delete = self.delete

        change_agent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.change_agent, Unset):
            change_agent = self.change_agent.to_dict()

        updated_time: str | Unset = UNSET
        if not isinstance(self.updated_time, Unset):
            updated_time = self.updated_time.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if locale is not UNSET:
            field_dict["locale"] = locale
        if translation_text is not UNSET:
            field_dict["translationText"] = translation_text
        if delete is not UNSET:
            field_dict["delete"] = delete
        if change_agent is not UNSET:
            field_dict["changeAgent"] = change_agent
        if updated_time is not UNSET:
            field_dict["updatedTime"] = updated_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_localizationtables_localizationtables_v1_change_agent import (
            RobloxLocalizationtablesLocalizationtablesV1ChangeAgent,
        )

        d = dict(src_dict)
        locale = d.pop("locale", UNSET)

        translation_text = d.pop("translationText", UNSET)

        delete = d.pop("delete", UNSET)

        _change_agent = d.pop("changeAgent", UNSET)
        change_agent: RobloxLocalizationtablesLocalizationtablesV1ChangeAgent | Unset
        if isinstance(_change_agent, Unset):
            change_agent = UNSET
        else:
            change_agent = RobloxLocalizationtablesLocalizationtablesV1ChangeAgent.from_dict(_change_agent)

        _updated_time = d.pop("updatedTime", UNSET)
        updated_time: datetime.datetime | Unset
        if isinstance(_updated_time, Unset):
            updated_time = UNSET
        else:
            updated_time = datetime.datetime.fromisoformat(_updated_time)

        roblox_localization_tables_api_patch_translation = cls(
            locale=locale,
            translation_text=translation_text,
            delete=delete,
            change_agent=change_agent,
            updated_time=updated_time,
        )

        return roblox_localization_tables_api_patch_translation
