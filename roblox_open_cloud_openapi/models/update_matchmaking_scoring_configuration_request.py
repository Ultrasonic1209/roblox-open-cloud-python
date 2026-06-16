from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_matchmaking_scoring_configuration_request_custom_signal_weights_type_0 import (
        UpdateMatchmakingScoringConfigurationRequestCustomSignalWeightsType0,
    )
    from ..models.update_matchmaking_scoring_configuration_request_matchmaking_signal_weights_type_0 import (
        UpdateMatchmakingScoringConfigurationRequestMatchmakingSignalWeightsType0,
    )


T = TypeVar("T", bound="UpdateMatchmakingScoringConfigurationRequest")


@_attrs_define
class UpdateMatchmakingScoringConfigurationRequest:
    """Request to update a custom matchmaking signal.

    Attributes:
        scoring_configuration_id (None | str | Unset): The ID of the scoring configuration to be updated.
        name (None | str | Unset): Name of the scoring configuration.
        matchmaking_signal_weights (None | Unset |
            UpdateMatchmakingScoringConfigurationRequestMatchmakingSignalWeightsType0): The desired set of weights for each
            matchmaking signal.
        custom_signal_weights (None | Unset | UpdateMatchmakingScoringConfigurationRequestCustomSignalWeightsType0): The
            desired set of weights for custom signals. It is a map from custom signal name to its weight.
    """

    scoring_configuration_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    matchmaking_signal_weights: (
        None | Unset | UpdateMatchmakingScoringConfigurationRequestMatchmakingSignalWeightsType0
    ) = UNSET
    custom_signal_weights: None | Unset | UpdateMatchmakingScoringConfigurationRequestCustomSignalWeightsType0 = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_matchmaking_scoring_configuration_request_custom_signal_weights_type_0 import (
            UpdateMatchmakingScoringConfigurationRequestCustomSignalWeightsType0,
        )
        from ..models.update_matchmaking_scoring_configuration_request_matchmaking_signal_weights_type_0 import (
            UpdateMatchmakingScoringConfigurationRequestMatchmakingSignalWeightsType0,
        )

        scoring_configuration_id: None | str | Unset
        if isinstance(self.scoring_configuration_id, Unset):
            scoring_configuration_id = UNSET
        else:
            scoring_configuration_id = self.scoring_configuration_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        matchmaking_signal_weights: dict[str, Any] | None | Unset
        if isinstance(self.matchmaking_signal_weights, Unset):
            matchmaking_signal_weights = UNSET
        elif isinstance(
            self.matchmaking_signal_weights, UpdateMatchmakingScoringConfigurationRequestMatchmakingSignalWeightsType0
        ):
            matchmaking_signal_weights = self.matchmaking_signal_weights.to_dict()
        else:
            matchmaking_signal_weights = self.matchmaking_signal_weights

        custom_signal_weights: dict[str, Any] | None | Unset
        if isinstance(self.custom_signal_weights, Unset):
            custom_signal_weights = UNSET
        elif isinstance(
            self.custom_signal_weights, UpdateMatchmakingScoringConfigurationRequestCustomSignalWeightsType0
        ):
            custom_signal_weights = self.custom_signal_weights.to_dict()
        else:
            custom_signal_weights = self.custom_signal_weights

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if scoring_configuration_id is not UNSET:
            field_dict["scoringConfigurationId"] = scoring_configuration_id
        if name is not UNSET:
            field_dict["name"] = name
        if matchmaking_signal_weights is not UNSET:
            field_dict["matchmakingSignalWeights"] = matchmaking_signal_weights
        if custom_signal_weights is not UNSET:
            field_dict["customSignalWeights"] = custom_signal_weights

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_matchmaking_scoring_configuration_request_custom_signal_weights_type_0 import (
            UpdateMatchmakingScoringConfigurationRequestCustomSignalWeightsType0,
        )
        from ..models.update_matchmaking_scoring_configuration_request_matchmaking_signal_weights_type_0 import (
            UpdateMatchmakingScoringConfigurationRequestMatchmakingSignalWeightsType0,
        )

        d = dict(src_dict)

        def _parse_scoring_configuration_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scoring_configuration_id = _parse_scoring_configuration_id(d.pop("scoringConfigurationId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_matchmaking_signal_weights(
            data: object,
        ) -> None | Unset | UpdateMatchmakingScoringConfigurationRequestMatchmakingSignalWeightsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                matchmaking_signal_weights_type_0 = (
                    UpdateMatchmakingScoringConfigurationRequestMatchmakingSignalWeightsType0.from_dict(data)
                )

                return matchmaking_signal_weights_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateMatchmakingScoringConfigurationRequestMatchmakingSignalWeightsType0, data)

        matchmaking_signal_weights = _parse_matchmaking_signal_weights(d.pop("matchmakingSignalWeights", UNSET))

        def _parse_custom_signal_weights(
            data: object,
        ) -> None | Unset | UpdateMatchmakingScoringConfigurationRequestCustomSignalWeightsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_signal_weights_type_0 = (
                    UpdateMatchmakingScoringConfigurationRequestCustomSignalWeightsType0.from_dict(data)
                )

                return custom_signal_weights_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateMatchmakingScoringConfigurationRequestCustomSignalWeightsType0, data)

        custom_signal_weights = _parse_custom_signal_weights(d.pop("customSignalWeights", UNSET))

        update_matchmaking_scoring_configuration_request = cls(
            scoring_configuration_id=scoring_configuration_id,
            name=name,
            matchmaking_signal_weights=matchmaking_signal_weights,
            custom_signal_weights=custom_signal_weights,
        )

        return update_matchmaking_scoring_configuration_request
