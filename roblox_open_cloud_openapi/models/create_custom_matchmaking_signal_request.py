from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_signal_configuration import CustomSignalConfiguration


T = TypeVar("T", bound="CreateCustomMatchmakingSignalRequest")


@_attrs_define
class CreateCustomMatchmakingSignalRequest:
    """Request to create a custom matchmaking signal.

    Attributes:
        scoring_configuration_id (None | str | Unset): The ID of the scoring configuration that has the signal to be
            created.
        signal_configuration (CustomSignalConfiguration | Unset): The custom signal configuration using a developer
            created attribute.
    """

    scoring_configuration_id: None | str | Unset = UNSET
    signal_configuration: CustomSignalConfiguration | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        scoring_configuration_id: None | str | Unset
        if isinstance(self.scoring_configuration_id, Unset):
            scoring_configuration_id = UNSET
        else:
            scoring_configuration_id = self.scoring_configuration_id

        signal_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signal_configuration, Unset):
            signal_configuration = self.signal_configuration.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if scoring_configuration_id is not UNSET:
            field_dict["scoringConfigurationId"] = scoring_configuration_id
        if signal_configuration is not UNSET:
            field_dict["signalConfiguration"] = signal_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_signal_configuration import CustomSignalConfiguration

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_scoring_configuration_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scoring_configuration_id = _parse_scoring_configuration_id(d.pop("scoringConfigurationId", UNSET))

        _signal_configuration = d.pop("signalConfiguration", UNSET)
        signal_configuration: CustomSignalConfiguration | Unset
        if isinstance(_signal_configuration, Unset):
            signal_configuration = UNSET
        else:
            signal_configuration = CustomSignalConfiguration.from_dict(_signal_configuration)

        create_custom_matchmaking_signal_request = cls(
            scoring_configuration_id=scoring_configuration_id,
            signal_configuration=signal_configuration,
        )

        return create_custom_matchmaking_signal_request
