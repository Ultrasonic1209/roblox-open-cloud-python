from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_app_page_platform_notifications_v1_beta_1_stream_page_request_cached_roblox_component_to_template_id import (
        RobloxAppPagePlatformNotificationsV1Beta1StreamPageRequestCachedRobloxComponentToTemplateId,
    )
    from ..models.roblox_app_page_platform_notifications_v1_beta_1_stream_page_request_client_attributes import (
        RobloxAppPagePlatformNotificationsV1Beta1StreamPageRequestClientAttributes,
    )
    from ..models.roblox_app_page_platform_shared_v1_beta_1_client_capabilities import (
        RobloxAppPagePlatformSharedV1Beta1ClientCapabilities,
    )


T = TypeVar("T", bound="RobloxAppPagePlatformNotificationsV1Beta1StreamPageRequest")


@_attrs_define
class RobloxAppPagePlatformNotificationsV1Beta1StreamPageRequest:
    """
    Attributes:
        cursor (str | Unset):
        max_rows (int | Unset):
        notification_id (str | Unset):
        has_notification_id (bool | Unset):
        state (str | Unset):
        has_state (bool | Unset):
        client_capabilities (RobloxAppPagePlatformSharedV1Beta1ClientCapabilities | Unset):
        cached_roblox_component_to_template_id
            (RobloxAppPagePlatformNotificationsV1Beta1StreamPageRequestCachedRobloxComponentToTemplateId | Unset):
        client_attributes (RobloxAppPagePlatformNotificationsV1Beta1StreamPageRequestClientAttributes | Unset):
    """

    cursor: str | Unset = UNSET
    max_rows: int | Unset = UNSET
    notification_id: str | Unset = UNSET
    has_notification_id: bool | Unset = UNSET
    state: str | Unset = UNSET
    has_state: bool | Unset = UNSET
    client_capabilities: RobloxAppPagePlatformSharedV1Beta1ClientCapabilities | Unset = UNSET
    cached_roblox_component_to_template_id: (
        RobloxAppPagePlatformNotificationsV1Beta1StreamPageRequestCachedRobloxComponentToTemplateId | Unset
    ) = UNSET
    client_attributes: RobloxAppPagePlatformNotificationsV1Beta1StreamPageRequestClientAttributes | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cursor = self.cursor

        max_rows = self.max_rows

        notification_id = self.notification_id

        has_notification_id = self.has_notification_id

        state = self.state

        has_state = self.has_state

        client_capabilities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client_capabilities, Unset):
            client_capabilities = self.client_capabilities.to_dict()

        cached_roblox_component_to_template_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cached_roblox_component_to_template_id, Unset):
            cached_roblox_component_to_template_id = self.cached_roblox_component_to_template_id.to_dict()

        client_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client_attributes, Unset):
            client_attributes = self.client_attributes.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if cursor is not UNSET:
            field_dict["Cursor"] = cursor
        if max_rows is not UNSET:
            field_dict["MaxRows"] = max_rows
        if notification_id is not UNSET:
            field_dict["NotificationId"] = notification_id
        if has_notification_id is not UNSET:
            field_dict["HasNotificationId"] = has_notification_id
        if state is not UNSET:
            field_dict["State"] = state
        if has_state is not UNSET:
            field_dict["HasState"] = has_state
        if client_capabilities is not UNSET:
            field_dict["ClientCapabilities"] = client_capabilities
        if cached_roblox_component_to_template_id is not UNSET:
            field_dict["CachedRobloxComponentToTemplateId"] = cached_roblox_component_to_template_id
        if client_attributes is not UNSET:
            field_dict["ClientAttributes"] = client_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_app_page_platform_notifications_v1_beta_1_stream_page_request_cached_roblox_component_to_template_id import (
            RobloxAppPagePlatformNotificationsV1Beta1StreamPageRequestCachedRobloxComponentToTemplateId,  # noqa: PLC0415
        )
        from ..models.roblox_app_page_platform_notifications_v1_beta_1_stream_page_request_client_attributes import (
            RobloxAppPagePlatformNotificationsV1Beta1StreamPageRequestClientAttributes,  # noqa: PLC0415
        )
        from ..models.roblox_app_page_platform_shared_v1_beta_1_client_capabilities import (
            RobloxAppPagePlatformSharedV1Beta1ClientCapabilities,  # noqa: PLC0415
        )

        d = dict(src_dict)
        cursor = d.pop("Cursor", UNSET)

        max_rows = d.pop("MaxRows", UNSET)

        notification_id = d.pop("NotificationId", UNSET)

        has_notification_id = d.pop("HasNotificationId", UNSET)

        state = d.pop("State", UNSET)

        has_state = d.pop("HasState", UNSET)

        _client_capabilities = d.pop("ClientCapabilities", UNSET)
        client_capabilities: RobloxAppPagePlatformSharedV1Beta1ClientCapabilities | Unset
        if isinstance(_client_capabilities, Unset):
            client_capabilities = UNSET
        else:
            client_capabilities = RobloxAppPagePlatformSharedV1Beta1ClientCapabilities.from_dict(_client_capabilities)

        _cached_roblox_component_to_template_id = d.pop("CachedRobloxComponentToTemplateId", UNSET)
        cached_roblox_component_to_template_id: (
            RobloxAppPagePlatformNotificationsV1Beta1StreamPageRequestCachedRobloxComponentToTemplateId | Unset
        )
        if isinstance(_cached_roblox_component_to_template_id, Unset):
            cached_roblox_component_to_template_id = UNSET
        else:
            cached_roblox_component_to_template_id = (
                RobloxAppPagePlatformNotificationsV1Beta1StreamPageRequestCachedRobloxComponentToTemplateId.from_dict(
                    _cached_roblox_component_to_template_id
                )
            )

        _client_attributes = d.pop("ClientAttributes", UNSET)
        client_attributes: RobloxAppPagePlatformNotificationsV1Beta1StreamPageRequestClientAttributes | Unset
        if isinstance(_client_attributes, Unset):
            client_attributes = UNSET
        else:
            client_attributes = RobloxAppPagePlatformNotificationsV1Beta1StreamPageRequestClientAttributes.from_dict(
                _client_attributes
            )

        roblox_app_page_platform_notifications_v1_beta_1_stream_page_request = cls(
            cursor=cursor,
            max_rows=max_rows,
            notification_id=notification_id,
            has_notification_id=has_notification_id,
            state=state,
            has_state=has_state,
            client_capabilities=client_capabilities,
            cached_roblox_component_to_template_id=cached_roblox_component_to_template_id,
            client_attributes=client_attributes,
        )

        return roblox_app_page_platform_notifications_v1_beta_1_stream_page_request
