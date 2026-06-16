from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_notification_payload_type import UserNotificationPayloadType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_notification_payload_analytics_data import UserNotificationPayloadAnalyticsData
    from ..models.user_notification_payload_join_experience import UserNotificationPayloadJoinExperience
    from ..models.user_notification_payload_parameters import UserNotificationPayloadParameters


T = TypeVar("T", bound="UserNotificationPayload")


@_attrs_define
class UserNotificationPayload:
    """Details about the notification.

    Attributes:
        type_ (UserNotificationPayloadType | Unset): The type of notification.

            Possible values:

              | Value | Description |
              | --- | --- |
              | TYPE_UNSPECIFIED | The default value. This value is unused. |
              | MOMENT | A notification type representing a moment. | Example: TYPE_UNSPECIFIED.
        message_id (str | Unset): An ID that represents a customizable notification message template
            that you create in Creator Dashboard.

            The message can contain customizable parameters that you can specify
            values for. For example, `Your {egg_name} just hatched` has an
            `egg_name` parameter. See the `parameters` field for more
            information. Example: 5dd7024b-68e3-ac4d-8232-4217f86ca244.
        parameters (UserNotificationPayloadParameters | Unset): A map of parameters used to render a notification
            message template.

            For example, given a template of `Your {egg_name} just hatched.` with
            parameters of `[{"egg_name": {"string_value": "royal egg"}}]`, the
            rendered notification message is: `Your royal egg just hatched.`
        join_experience (UserNotificationPayloadJoinExperience | Unset): A call-to-action that represents joining an
            experience.
        analytics_data (UserNotificationPayloadAnalyticsData | Unset): Data for how analytics are reported.
    """

    type_: UserNotificationPayloadType | Unset = UNSET
    message_id: str | Unset = UNSET
    parameters: UserNotificationPayloadParameters | Unset = UNSET
    join_experience: UserNotificationPayloadJoinExperience | Unset = UNSET
    analytics_data: UserNotificationPayloadAnalyticsData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        message_id = self.message_id

        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        join_experience: dict[str, Any] | Unset = UNSET
        if not isinstance(self.join_experience, Unset):
            join_experience = self.join_experience.to_dict()

        analytics_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.analytics_data, Unset):
            analytics_data = self.analytics_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if join_experience is not UNSET:
            field_dict["joinExperience"] = join_experience
        if analytics_data is not UNSET:
            field_dict["analyticsData"] = analytics_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_notification_payload_analytics_data import UserNotificationPayloadAnalyticsData
        from ..models.user_notification_payload_join_experience import UserNotificationPayloadJoinExperience
        from ..models.user_notification_payload_parameters import UserNotificationPayloadParameters

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: UserNotificationPayloadType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = UserNotificationPayloadType(_type_)

        message_id = d.pop("messageId", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: UserNotificationPayloadParameters | Unset
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = UserNotificationPayloadParameters.from_dict(_parameters)

        _join_experience = d.pop("joinExperience", UNSET)
        join_experience: UserNotificationPayloadJoinExperience | Unset
        if isinstance(_join_experience, Unset):
            join_experience = UNSET
        else:
            join_experience = UserNotificationPayloadJoinExperience.from_dict(_join_experience)

        _analytics_data = d.pop("analyticsData", UNSET)
        analytics_data: UserNotificationPayloadAnalyticsData | Unset
        if isinstance(_analytics_data, Unset):
            analytics_data = UNSET
        else:
            analytics_data = UserNotificationPayloadAnalyticsData.from_dict(_analytics_data)

        user_notification_payload = cls(
            type_=type_,
            message_id=message_id,
            parameters=parameters,
            join_experience=join_experience,
            analytics_data=analytics_data,
        )

        user_notification_payload.additional_properties = d
        return user_notification_payload

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
