from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.custom_signal_type import CustomSignalType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.player_categorical_signal_configuration import PlayerCategoricalSignalConfiguration
    from ..models.player_numerical_signal_configuration import PlayerNumericalSignalConfiguration
    from ..models.server_categorical_signal_configuration import ServerCategoricalSignalConfiguration
    from ..models.server_numerical_signal_configuration import ServerNumericalSignalConfiguration


T = TypeVar("T", bound="CustomSignalConfiguration")


@_attrs_define
class CustomSignalConfiguration:
    """The custom signal configuration using a developer created attribute.

    Attributes:
        name (None | str | Unset): The name of the signal.
        weight (float | None | Unset): The weight of the signal.
        custom_signal_type (CustomSignalType | Unset): The custom signal type.
        player_categorical_signal_configuration (PlayerCategoricalSignalConfiguration | Unset): The player categorical
            signal configuration.
        server_categorical_signal_configuration (ServerCategoricalSignalConfiguration | Unset): The server categorical
            signal configuration.
        server_numerical_signal_configuration (ServerNumericalSignalConfiguration | Unset): The server numerical signal
            configuration.
        player_numerical_signal_configuration (PlayerNumericalSignalConfiguration | Unset): The player numerical signal
            configuration.
        description (None | str | Unset): A text description of the custom signal.
    """

    name: None | str | Unset = UNSET
    weight: float | None | Unset = UNSET
    custom_signal_type: CustomSignalType | Unset = UNSET
    player_categorical_signal_configuration: PlayerCategoricalSignalConfiguration | Unset = UNSET
    server_categorical_signal_configuration: ServerCategoricalSignalConfiguration | Unset = UNSET
    server_numerical_signal_configuration: ServerNumericalSignalConfiguration | Unset = UNSET
    player_numerical_signal_configuration: PlayerNumericalSignalConfiguration | Unset = UNSET
    description: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        weight: float | None | Unset
        if isinstance(self.weight, Unset):
            weight = UNSET
        else:
            weight = self.weight

        custom_signal_type: str | Unset = UNSET
        if not isinstance(self.custom_signal_type, Unset):
            custom_signal_type = self.custom_signal_type.value

        player_categorical_signal_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.player_categorical_signal_configuration, Unset):
            player_categorical_signal_configuration = self.player_categorical_signal_configuration.to_dict()

        server_categorical_signal_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.server_categorical_signal_configuration, Unset):
            server_categorical_signal_configuration = self.server_categorical_signal_configuration.to_dict()

        server_numerical_signal_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.server_numerical_signal_configuration, Unset):
            server_numerical_signal_configuration = self.server_numerical_signal_configuration.to_dict()

        player_numerical_signal_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.player_numerical_signal_configuration, Unset):
            player_numerical_signal_configuration = self.player_numerical_signal_configuration.to_dict()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if weight is not UNSET:
            field_dict["weight"] = weight
        if custom_signal_type is not UNSET:
            field_dict["customSignalType"] = custom_signal_type
        if player_categorical_signal_configuration is not UNSET:
            field_dict["playerCategoricalSignalConfiguration"] = player_categorical_signal_configuration
        if server_categorical_signal_configuration is not UNSET:
            field_dict["serverCategoricalSignalConfiguration"] = server_categorical_signal_configuration
        if server_numerical_signal_configuration is not UNSET:
            field_dict["serverNumericalSignalConfiguration"] = server_numerical_signal_configuration
        if player_numerical_signal_configuration is not UNSET:
            field_dict["playerNumericalSignalConfiguration"] = player_numerical_signal_configuration
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.player_categorical_signal_configuration import PlayerCategoricalSignalConfiguration
        from ..models.player_numerical_signal_configuration import PlayerNumericalSignalConfiguration
        from ..models.server_categorical_signal_configuration import ServerCategoricalSignalConfiguration
        from ..models.server_numerical_signal_configuration import ServerNumericalSignalConfiguration

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_weight(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        weight = _parse_weight(d.pop("weight", UNSET))

        _custom_signal_type = d.pop("customSignalType", UNSET)
        custom_signal_type: CustomSignalType | Unset
        if isinstance(_custom_signal_type, Unset):
            custom_signal_type = UNSET
        else:
            custom_signal_type = CustomSignalType(_custom_signal_type)

        _player_categorical_signal_configuration = d.pop("playerCategoricalSignalConfiguration", UNSET)
        player_categorical_signal_configuration: PlayerCategoricalSignalConfiguration | Unset
        if isinstance(_player_categorical_signal_configuration, Unset):
            player_categorical_signal_configuration = UNSET
        else:
            player_categorical_signal_configuration = PlayerCategoricalSignalConfiguration.from_dict(
                _player_categorical_signal_configuration
            )

        _server_categorical_signal_configuration = d.pop("serverCategoricalSignalConfiguration", UNSET)
        server_categorical_signal_configuration: ServerCategoricalSignalConfiguration | Unset
        if isinstance(_server_categorical_signal_configuration, Unset):
            server_categorical_signal_configuration = UNSET
        else:
            server_categorical_signal_configuration = ServerCategoricalSignalConfiguration.from_dict(
                _server_categorical_signal_configuration
            )

        _server_numerical_signal_configuration = d.pop("serverNumericalSignalConfiguration", UNSET)
        server_numerical_signal_configuration: ServerNumericalSignalConfiguration | Unset
        if isinstance(_server_numerical_signal_configuration, Unset):
            server_numerical_signal_configuration = UNSET
        else:
            server_numerical_signal_configuration = ServerNumericalSignalConfiguration.from_dict(
                _server_numerical_signal_configuration
            )

        _player_numerical_signal_configuration = d.pop("playerNumericalSignalConfiguration", UNSET)
        player_numerical_signal_configuration: PlayerNumericalSignalConfiguration | Unset
        if isinstance(_player_numerical_signal_configuration, Unset):
            player_numerical_signal_configuration = UNSET
        else:
            player_numerical_signal_configuration = PlayerNumericalSignalConfiguration.from_dict(
                _player_numerical_signal_configuration
            )

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        custom_signal_configuration = cls(
            name=name,
            weight=weight,
            custom_signal_type=custom_signal_type,
            player_categorical_signal_configuration=player_categorical_signal_configuration,
            server_categorical_signal_configuration=server_categorical_signal_configuration,
            server_numerical_signal_configuration=server_numerical_signal_configuration,
            player_numerical_signal_configuration=player_numerical_signal_configuration,
            description=description,
        )

        return custom_signal_configuration
