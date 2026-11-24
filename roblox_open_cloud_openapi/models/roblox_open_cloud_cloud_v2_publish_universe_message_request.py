from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="RobloxOpenCloudCloudV2PublishUniverseMessageRequest")


@_attrs_define
class RobloxOpenCloudCloudV2PublishUniverseMessageRequest:
    """Publish a message on the specified topic.

    Attributes:
        topic (str): The topic on which to publish the message. Example: my-topic.
        message (str): The message to publish. Example: Hello, world!.
    """

    topic: str
    message: str

    def to_dict(self) -> dict[str, Any]:
        topic = self.topic

        message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "topic": topic,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        topic = d.pop("topic")

        message = d.pop("message")

        roblox_open_cloud_cloud_v2_publish_universe_message_request = cls(
            topic=topic,
            message=message,
        )

        return roblox_open_cloud_cloud_v2_publish_universe_message_request
