from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_authentication_api_models_account_upgrade_request_gender import (
    RobloxAuthenticationApiModelsAccountUpgradeRequestGender,
)
from ..models.roblox_authentication_api_models_account_upgrade_request_upgrade_type import (
    RobloxAuthenticationApiModelsAccountUpgradeRequestUpgradeType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsAccountUpgradeRequest")


@_attrs_define
class RobloxAuthenticationApiModelsAccountUpgradeRequest:
    """
    Attributes:
        upgrade_type (RobloxAuthenticationApiModelsAccountUpgradeRequestUpgradeType | Unset):  ['Unknown' = 0, 'Pioneer'
            = 1, 'OAuth' = 2, 'Guest' = 3, 'PioneerU13' = 4]
        username (str | Unset):
        password (str | Unset):
        birthday (datetime.datetime | Unset):
        email (str | Unset):
        gender (RobloxAuthenticationApiModelsAccountUpgradeRequestGender | Unset):
    """

    upgrade_type: RobloxAuthenticationApiModelsAccountUpgradeRequestUpgradeType | Unset = UNSET
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    birthday: datetime.datetime | Unset = UNSET
    email: str | Unset = UNSET
    gender: RobloxAuthenticationApiModelsAccountUpgradeRequestGender | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        upgrade_type: int | Unset = UNSET
        if not isinstance(self.upgrade_type, Unset):
            upgrade_type = self.upgrade_type.value

        username = self.username

        password = self.password

        birthday: str | Unset = UNSET
        if not isinstance(self.birthday, Unset):
            birthday = self.birthday.isoformat()

        email = self.email

        gender: int | Unset = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if upgrade_type is not UNSET:
            field_dict["upgradeType"] = upgrade_type
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if birthday is not UNSET:
            field_dict["birthday"] = birthday
        if email is not UNSET:
            field_dict["email"] = email
        if gender is not UNSET:
            field_dict["gender"] = gender

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _upgrade_type = d.pop("upgradeType", UNSET)
        upgrade_type: RobloxAuthenticationApiModelsAccountUpgradeRequestUpgradeType | Unset
        if isinstance(_upgrade_type, Unset):
            upgrade_type = UNSET
        else:
            upgrade_type = RobloxAuthenticationApiModelsAccountUpgradeRequestUpgradeType(_upgrade_type)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        _birthday = d.pop("birthday", UNSET)
        birthday: datetime.datetime | Unset
        if isinstance(_birthday, Unset):
            birthday = UNSET
        else:
            birthday = datetime.datetime.fromisoformat(_birthday)

        email = d.pop("email", UNSET)

        _gender = d.pop("gender", UNSET)
        gender: RobloxAuthenticationApiModelsAccountUpgradeRequestGender | Unset
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = RobloxAuthenticationApiModelsAccountUpgradeRequestGender(_gender)

        roblox_authentication_api_models_account_upgrade_request = cls(
            upgrade_type=upgrade_type,
            username=username,
            password=password,
            birthday=birthday,
            email=email,
            gender=gender,
        )

        return roblox_authentication_api_models_account_upgrade_request
