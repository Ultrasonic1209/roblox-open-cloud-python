from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.experiment_product_type import ExperimentProductType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.in_game_config_experiment_configuration import InGameConfigExperimentConfiguration
    from ..models.matchmaking_experiment_configuration import MatchmakingExperimentConfiguration


T = TypeVar("T", bound="ExperimentConfiguration")


@_attrs_define
class ExperimentConfiguration:
    """Union of per-product experiment configurations. At most one of InGameConfigExperimentConfiguration or
    MatchmakingExperimentConfiguration may be set.

        Attributes:
            product_type (ExperimentProductType | Unset): Type of product the experiment is targeting.

                EXPERIMENT_PRODUCT_TYPE_IN_GAME_CONFIGS

                EXPERIMENT_PRODUCT_TYPE_MATCHMAKING
            in_game_config_experiment_configuration (InGameConfigExperimentConfiguration | None | Unset): Populated when
                ProductType is InGameConfigExperimentConfiguration, null otherwise.
            matchmaking_experiment_configuration (MatchmakingExperimentConfiguration | None | Unset): Populated when
                ProductType is MatchmakingExperimentConfiguration, null otherwise.
    """

    product_type: ExperimentProductType | Unset = UNSET
    in_game_config_experiment_configuration: InGameConfigExperimentConfiguration | None | Unset = UNSET
    matchmaking_experiment_configuration: MatchmakingExperimentConfiguration | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.in_game_config_experiment_configuration import InGameConfigExperimentConfiguration
        from ..models.matchmaking_experiment_configuration import MatchmakingExperimentConfiguration

        product_type: str | Unset = UNSET
        if not isinstance(self.product_type, Unset):
            product_type = self.product_type.value

        in_game_config_experiment_configuration: dict[str, Any] | None | Unset
        if isinstance(self.in_game_config_experiment_configuration, Unset):
            in_game_config_experiment_configuration = UNSET
        elif isinstance(self.in_game_config_experiment_configuration, InGameConfigExperimentConfiguration):
            in_game_config_experiment_configuration = self.in_game_config_experiment_configuration.to_dict()
        else:
            in_game_config_experiment_configuration = self.in_game_config_experiment_configuration

        matchmaking_experiment_configuration: dict[str, Any] | None | Unset
        if isinstance(self.matchmaking_experiment_configuration, Unset):
            matchmaking_experiment_configuration = UNSET
        elif isinstance(self.matchmaking_experiment_configuration, MatchmakingExperimentConfiguration):
            matchmaking_experiment_configuration = self.matchmaking_experiment_configuration.to_dict()
        else:
            matchmaking_experiment_configuration = self.matchmaking_experiment_configuration

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if product_type is not UNSET:
            field_dict["productType"] = product_type
        if in_game_config_experiment_configuration is not UNSET:
            field_dict["inGameConfigExperimentConfiguration"] = in_game_config_experiment_configuration
        if matchmaking_experiment_configuration is not UNSET:
            field_dict["matchmakingExperimentConfiguration"] = matchmaking_experiment_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.in_game_config_experiment_configuration import InGameConfigExperimentConfiguration
        from ..models.matchmaking_experiment_configuration import MatchmakingExperimentConfiguration

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _product_type = d.pop("productType", UNSET)
        product_type: ExperimentProductType | Unset
        if isinstance(_product_type, Unset):
            product_type = UNSET
        else:
            product_type = ExperimentProductType(_product_type)

        def _parse_in_game_config_experiment_configuration(
            data: object,
        ) -> InGameConfigExperimentConfiguration | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                in_game_config_experiment_configuration_type_1 = InGameConfigExperimentConfiguration.from_dict(data)

                return in_game_config_experiment_configuration_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InGameConfigExperimentConfiguration | None | Unset, data)

        in_game_config_experiment_configuration = _parse_in_game_config_experiment_configuration(
            d.pop("inGameConfigExperimentConfiguration", UNSET)
        )

        def _parse_matchmaking_experiment_configuration(
            data: object,
        ) -> MatchmakingExperimentConfiguration | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                matchmaking_experiment_configuration_type_1 = MatchmakingExperimentConfiguration.from_dict(data)

                return matchmaking_experiment_configuration_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MatchmakingExperimentConfiguration | None | Unset, data)

        matchmaking_experiment_configuration = _parse_matchmaking_experiment_configuration(
            d.pop("matchmakingExperimentConfiguration", UNSET)
        )

        experiment_configuration = cls(
            product_type=product_type,
            in_game_config_experiment_configuration=in_game_config_experiment_configuration,
            matchmaking_experiment_configuration=matchmaking_experiment_configuration,
        )

        return experiment_configuration
