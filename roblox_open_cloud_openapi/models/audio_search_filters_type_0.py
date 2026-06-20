from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.music_chart_type import MusicChartType
from ..models.search_audio_type_model import SearchAudioTypeModel
from ..types import UNSET, Unset

T = TypeVar("T", bound="AudioSearchFiltersType0")


@_attrs_define
class AudioSearchFiltersType0:
    """Audio-specific search filter parameters.

    Attributes:
        audio_types (list[SearchAudioTypeModel] | None | Unset): Audio types to include (e.g. Music, SoundEffect)
        min_duration_seconds (int | Unset): The minimum duration for audio in seconds. If included, must be greater than
            or equal to 0.
        max_duration_seconds (int | None | Unset): The maximum duration for audio in seconds. If included, must be
            greater than or equal to 1.
        artist (None | str | Unset): The name of the artist to filter by.
        album (None | str | Unset): The name of the album to filter by.
        include_top_charts (bool | None | Unset): Whether to include top charts in the results.
        music_chart_type (MusicChartType | Unset): Represents which music chart to pull entries from, if any
    """

    audio_types: list[SearchAudioTypeModel] | None | Unset = UNSET
    min_duration_seconds: int | Unset = UNSET
    max_duration_seconds: int | None | Unset = UNSET
    artist: None | str | Unset = UNSET
    album: None | str | Unset = UNSET
    include_top_charts: bool | None | Unset = UNSET
    music_chart_type: MusicChartType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        audio_types: list[str] | None | Unset
        if isinstance(self.audio_types, Unset):
            audio_types = UNSET
        elif isinstance(self.audio_types, list):
            audio_types = []
            for audio_types_type_0_item_data in self.audio_types:
                audio_types_type_0_item = audio_types_type_0_item_data.value
                audio_types.append(audio_types_type_0_item)

        else:
            audio_types = self.audio_types

        min_duration_seconds = self.min_duration_seconds

        max_duration_seconds: int | None | Unset
        if isinstance(self.max_duration_seconds, Unset):
            max_duration_seconds = UNSET
        else:
            max_duration_seconds = self.max_duration_seconds

        artist: None | str | Unset
        if isinstance(self.artist, Unset):
            artist = UNSET
        else:
            artist = self.artist

        album: None | str | Unset
        if isinstance(self.album, Unset):
            album = UNSET
        else:
            album = self.album

        include_top_charts: bool | None | Unset
        if isinstance(self.include_top_charts, Unset):
            include_top_charts = UNSET
        else:
            include_top_charts = self.include_top_charts

        music_chart_type: str | Unset = UNSET
        if not isinstance(self.music_chart_type, Unset):
            music_chart_type = self.music_chart_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if audio_types is not UNSET:
            field_dict["audioTypes"] = audio_types
        if min_duration_seconds is not UNSET:
            field_dict["minDurationSeconds"] = min_duration_seconds
        if max_duration_seconds is not UNSET:
            field_dict["maxDurationSeconds"] = max_duration_seconds
        if artist is not UNSET:
            field_dict["artist"] = artist
        if album is not UNSET:
            field_dict["album"] = album
        if include_top_charts is not UNSET:
            field_dict["includeTopCharts"] = include_top_charts
        if music_chart_type is not UNSET:
            field_dict["musicChartType"] = music_chart_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_audio_types(data: object) -> list[SearchAudioTypeModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                audio_types_type_0 = []
                _audio_types_type_0 = data
                for audio_types_type_0_item_data in _audio_types_type_0:
                    audio_types_type_0_item = SearchAudioTypeModel(audio_types_type_0_item_data)

                    audio_types_type_0.append(audio_types_type_0_item)

                return audio_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SearchAudioTypeModel] | None | Unset, data)

        audio_types = _parse_audio_types(d.pop("audioTypes", UNSET))

        min_duration_seconds = d.pop("minDurationSeconds", UNSET)

        def _parse_max_duration_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_duration_seconds = _parse_max_duration_seconds(d.pop("maxDurationSeconds", UNSET))

        def _parse_artist(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        artist = _parse_artist(d.pop("artist", UNSET))

        def _parse_album(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        album = _parse_album(d.pop("album", UNSET))

        def _parse_include_top_charts(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_top_charts = _parse_include_top_charts(d.pop("includeTopCharts", UNSET))

        _music_chart_type = d.pop("musicChartType", UNSET)
        music_chart_type: MusicChartType | Unset
        if isinstance(_music_chart_type, Unset):
            music_chart_type = UNSET
        else:
            music_chart_type = MusicChartType(_music_chart_type)

        audio_search_filters_type_0 = cls(
            audio_types=audio_types,
            min_duration_seconds=min_duration_seconds,
            max_duration_seconds=max_duration_seconds,
            artist=artist,
            album=album,
            include_top_charts=include_top_charts,
            music_chart_type=music_chart_type,
        )

        return audio_search_filters_type_0
