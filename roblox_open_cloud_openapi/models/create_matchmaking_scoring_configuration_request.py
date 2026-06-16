from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.matchmaking_scoring_configuration_template import MatchmakingScoringConfigurationTemplate
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_matchmaking_scoring_configuration_request_custom_signal_weights_type_0 import (
        CreateMatchmakingScoringConfigurationRequestCustomSignalWeightsType0,
    )
    from ..models.create_matchmaking_scoring_configuration_request_matchmaking_signal_weights_type_0 import (
        CreateMatchmakingScoringConfigurationRequestMatchmakingSignalWeightsType0,
    )


T = TypeVar("T", bound="CreateMatchmakingScoringConfigurationRequest")


@_attrs_define
class CreateMatchmakingScoringConfigurationRequest:
    """Request to create a matchmaking scoring configuration.

    Attributes:
        universe_id (int | Unset): UniverseId for the new matchmaking scoring configuraiton.
        name (None | str | Unset): Name of the scoring configuration.
        matchmaking_signal_weights (CreateMatchmakingScoringConfigurationRequestMatchmakingSignalWeightsType0 | None |
            Unset): The desired set of weights for each matchmaking signal.
        custom_signal_weights (CreateMatchmakingScoringConfigurationRequestCustomSignalWeightsType0 | None | Unset): The
            desired set of weights for custom signals. It is a map from custom signal name to its weight.
        template (MatchmakingScoringConfigurationTemplate | Unset): A predefined template used for creating matchmaking
            scoring configuration.
    """

    universe_id: int | Unset = UNSET
    name: None | str | Unset = UNSET
    matchmaking_signal_weights: (
        CreateMatchmakingScoringConfigurationRequestMatchmakingSignalWeightsType0 | None | Unset
    ) = UNSET
    custom_signal_weights: CreateMatchmakingScoringConfigurationRequestCustomSignalWeightsType0 | None | Unset = UNSET
    template: MatchmakingScoringConfigurationTemplate | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_matchmaking_scoring_configuration_request_custom_signal_weights_type_0 import (
            CreateMatchmakingScoringConfigurationRequestCustomSignalWeightsType0,
        )
        from ..models.create_matchmaking_scoring_configuration_request_matchmaking_signal_weights_type_0 import (
            CreateMatchmakingScoringConfigurationRequestMatchmakingSignalWeightsType0,
        )

        universe_id = self.universe_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        matchmaking_signal_weights: dict[str, Any] | None | Unset
        if isinstance(self.matchmaking_signal_weights, Unset):
            matchmaking_signal_weights = UNSET
        elif isinstance(
            self.matchmaking_signal_weights, CreateMatchmakingScoringConfigurationRequestMatchmakingSignalWeightsType0
        ):
            matchmaking_signal_weights = self.matchmaking_signal_weights.to_dict()
        else:
            matchmaking_signal_weights = self.matchmaking_signal_weights

        custom_signal_weights: dict[str, Any] | None | Unset
        if isinstance(self.custom_signal_weights, Unset):
            custom_signal_weights = UNSET
        elif isinstance(
            self.custom_signal_weights, CreateMatchmakingScoringConfigurationRequestCustomSignalWeightsType0
        ):
            custom_signal_weights = self.custom_signal_weights.to_dict()
        else:
            custom_signal_weights = self.custom_signal_weights

        template: str | Unset = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if name is not UNSET:
            field_dict["name"] = name
        if matchmaking_signal_weights is not UNSET:
            field_dict["matchmakingSignalWeights"] = matchmaking_signal_weights
        if custom_signal_weights is not UNSET:
            field_dict["customSignalWeights"] = custom_signal_weights
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_matchmaking_scoring_configuration_request_custom_signal_weights_type_0 import (
            CreateMatchmakingScoringConfigurationRequestCustomSignalWeightsType0,
        )
        from ..models.create_matchmaking_scoring_configuration_request_matchmaking_signal_weights_type_0 import (
            CreateMatchmakingScoringConfigurationRequestMatchmakingSignalWeightsType0,
        )

        d = dict(src_dict)
        universe_id = d.pop("universeId", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_matchmaking_signal_weights(
            data: object,
        ) -> CreateMatchmakingScoringConfigurationRequestMatchmakingSignalWeightsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                matchmaking_signal_weights_type_0 = (
                    CreateMatchmakingScoringConfigurationRequestMatchmakingSignalWeightsType0.from_dict(data)
                )

                return matchmaking_signal_weights_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateMatchmakingScoringConfigurationRequestMatchmakingSignalWeightsType0 | None | Unset, data)

        matchmaking_signal_weights = _parse_matchmaking_signal_weights(d.pop("matchmakingSignalWeights", UNSET))

        def _parse_custom_signal_weights(
            data: object,
        ) -> CreateMatchmakingScoringConfigurationRequestCustomSignalWeightsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_signal_weights_type_0 = (
                    CreateMatchmakingScoringConfigurationRequestCustomSignalWeightsType0.from_dict(data)
                )

                return custom_signal_weights_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateMatchmakingScoringConfigurationRequestCustomSignalWeightsType0 | None | Unset, data)

        custom_signal_weights = _parse_custom_signal_weights(d.pop("customSignalWeights", UNSET))

        _template = d.pop("template", UNSET)
        template: MatchmakingScoringConfigurationTemplate | Unset
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = MatchmakingScoringConfigurationTemplate(_template)

        create_matchmaking_scoring_configuration_request = cls(
            universe_id=universe_id,
            name=name,
            matchmaking_signal_weights=matchmaking_signal_weights,
            custom_signal_weights=custom_signal_weights,
            template=template,
        )

        return create_matchmaking_scoring_configuration_request
