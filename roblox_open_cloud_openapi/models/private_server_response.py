from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.game_response import GameResponse
    from ..models.private_server_permissions_response import PrivateServerPermissionsResponse
    from ..models.private_server_subscription_response import PrivateServerSubscriptionResponse
    from ..models.private_server_voice_settings_response import PrivateServerVoiceSettingsResponse


T = TypeVar("T", bound="PrivateServerResponse")


@_attrs_define
class PrivateServerResponse:
    """
    Attributes:
        id (int | Unset):
        name (None | str | Unset):
        game (GameResponse | None | Unset):
        join_code (None | str | Unset):
        active (bool | Unset):
        subscription (None | PrivateServerSubscriptionResponse | Unset):
        permissions (None | PrivateServerPermissionsResponse | Unset):
        voice_settings (None | PrivateServerVoiceSettingsResponse | Unset):
        link (None | str | Unset):
    """

    id: int | Unset = UNSET
    name: None | str | Unset = UNSET
    game: GameResponse | None | Unset = UNSET
    join_code: None | str | Unset = UNSET
    active: bool | Unset = UNSET
    subscription: None | PrivateServerSubscriptionResponse | Unset = UNSET
    permissions: None | PrivateServerPermissionsResponse | Unset = UNSET
    voice_settings: None | PrivateServerVoiceSettingsResponse | Unset = UNSET
    link: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.game_response import GameResponse
        from ..models.private_server_permissions_response import PrivateServerPermissionsResponse
        from ..models.private_server_subscription_response import PrivateServerSubscriptionResponse
        from ..models.private_server_voice_settings_response import PrivateServerVoiceSettingsResponse

        id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        game: dict[str, Any] | None | Unset
        if isinstance(self.game, Unset):
            game = UNSET
        elif isinstance(self.game, GameResponse):
            game = self.game.to_dict()
        else:
            game = self.game

        join_code: None | str | Unset
        if isinstance(self.join_code, Unset):
            join_code = UNSET
        else:
            join_code = self.join_code

        active = self.active

        subscription: dict[str, Any] | None | Unset
        if isinstance(self.subscription, Unset):
            subscription = UNSET
        elif isinstance(self.subscription, PrivateServerSubscriptionResponse):
            subscription = self.subscription.to_dict()
        else:
            subscription = self.subscription

        permissions: dict[str, Any] | None | Unset
        if isinstance(self.permissions, Unset):
            permissions = UNSET
        elif isinstance(self.permissions, PrivateServerPermissionsResponse):
            permissions = self.permissions.to_dict()
        else:
            permissions = self.permissions

        voice_settings: dict[str, Any] | None | Unset
        if isinstance(self.voice_settings, Unset):
            voice_settings = UNSET
        elif isinstance(self.voice_settings, PrivateServerVoiceSettingsResponse):
            voice_settings = self.voice_settings.to_dict()
        else:
            voice_settings = self.voice_settings

        link: None | str | Unset
        if isinstance(self.link, Unset):
            link = UNSET
        else:
            link = self.link

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if game is not UNSET:
            field_dict["game"] = game
        if join_code is not UNSET:
            field_dict["joinCode"] = join_code
        if active is not UNSET:
            field_dict["active"] = active
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if voice_settings is not UNSET:
            field_dict["voiceSettings"] = voice_settings
        if link is not UNSET:
            field_dict["link"] = link

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.game_response import GameResponse
        from ..models.private_server_permissions_response import PrivateServerPermissionsResponse
        from ..models.private_server_subscription_response import PrivateServerSubscriptionResponse
        from ..models.private_server_voice_settings_response import PrivateServerVoiceSettingsResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_game(data: object) -> GameResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                game_type_1 = GameResponse.from_dict(data)

                return game_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GameResponse | None | Unset, data)

        game = _parse_game(d.pop("game", UNSET))

        def _parse_join_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        join_code = _parse_join_code(d.pop("joinCode", UNSET))

        active = d.pop("active", UNSET)

        def _parse_subscription(data: object) -> None | PrivateServerSubscriptionResponse | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subscription_type_1 = PrivateServerSubscriptionResponse.from_dict(data)

                return subscription_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PrivateServerSubscriptionResponse | Unset, data)

        subscription = _parse_subscription(d.pop("subscription", UNSET))

        def _parse_permissions(data: object) -> None | PrivateServerPermissionsResponse | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                permissions_type_1 = PrivateServerPermissionsResponse.from_dict(data)

                return permissions_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PrivateServerPermissionsResponse | Unset, data)

        permissions = _parse_permissions(d.pop("permissions", UNSET))

        def _parse_voice_settings(data: object) -> None | PrivateServerVoiceSettingsResponse | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                voice_settings_type_1 = PrivateServerVoiceSettingsResponse.from_dict(data)

                return voice_settings_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PrivateServerVoiceSettingsResponse | Unset, data)

        voice_settings = _parse_voice_settings(d.pop("voiceSettings", UNSET))

        def _parse_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        link = _parse_link(d.pop("link", UNSET))

        private_server_response = cls(
            id=id,
            name=name,
            game=game,
            join_code=join_code,
            active=active,
            subscription=subscription,
            permissions=permissions,
            voice_settings=voice_settings,
            link=link,
        )

        return private_server_response
