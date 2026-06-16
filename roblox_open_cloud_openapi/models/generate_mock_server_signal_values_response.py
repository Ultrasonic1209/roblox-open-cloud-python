from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mock_server_signal_values import MockServerSignalValues


T = TypeVar("T", bound="GenerateMockServerSignalValuesResponse")


@_attrs_define
class GenerateMockServerSignalValuesResponse:
    """Response for generating mock server signal values.

    Attributes:
        example_game_signal_values (list[MockServerSignalValues] | None | Unset): The mock server signal values.
    """

    example_game_signal_values: list[MockServerSignalValues] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        example_game_signal_values: list[dict[str, Any]] | None | Unset
        if isinstance(self.example_game_signal_values, Unset):
            example_game_signal_values = UNSET
        elif isinstance(self.example_game_signal_values, list):
            example_game_signal_values = []
            for example_game_signal_values_type_0_item_data in self.example_game_signal_values:
                example_game_signal_values_type_0_item = example_game_signal_values_type_0_item_data.to_dict()
                example_game_signal_values.append(example_game_signal_values_type_0_item)

        else:
            example_game_signal_values = self.example_game_signal_values

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if example_game_signal_values is not UNSET:
            field_dict["exampleGameSignalValues"] = example_game_signal_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mock_server_signal_values import MockServerSignalValues

        d = dict(src_dict)

        def _parse_example_game_signal_values(data: object) -> list[MockServerSignalValues] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                example_game_signal_values_type_0 = []
                _example_game_signal_values_type_0 = data
                for example_game_signal_values_type_0_item_data in _example_game_signal_values_type_0:
                    example_game_signal_values_type_0_item = MockServerSignalValues.from_dict(
                        example_game_signal_values_type_0_item_data
                    )

                    example_game_signal_values_type_0.append(example_game_signal_values_type_0_item)

                return example_game_signal_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MockServerSignalValues] | None | Unset, data)

        example_game_signal_values = _parse_example_game_signal_values(d.pop("exampleGameSignalValues", UNSET))

        generate_mock_server_signal_values_response = cls(
            example_game_signal_values=example_game_signal_values,
        )

        return generate_mock_server_signal_values_response
