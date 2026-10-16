from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.private_server_subscription_tag import PrivateServerSubscriptionTag
from ..types import UNSET, Unset

T = TypeVar("T", bound="PrivateServerSubscriptionMetadata")


@_attrs_define
class PrivateServerSubscriptionMetadata:
    """
    Attributes:
        private_server_subscription_tags (list[PrivateServerSubscriptionTag] | None | Unset):
    """

    private_server_subscription_tags: list[PrivateServerSubscriptionTag] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        private_server_subscription_tags: list[str] | None | Unset
        if isinstance(self.private_server_subscription_tags, Unset):
            private_server_subscription_tags = UNSET
        elif isinstance(self.private_server_subscription_tags, list):
            private_server_subscription_tags = []
            for private_server_subscription_tags_type_0_item_data in self.private_server_subscription_tags:
                private_server_subscription_tags_type_0_item = private_server_subscription_tags_type_0_item_data.value
                private_server_subscription_tags.append(private_server_subscription_tags_type_0_item)

        else:
            private_server_subscription_tags = self.private_server_subscription_tags

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if private_server_subscription_tags is not UNSET:
            field_dict["privateServerSubscriptionTags"] = private_server_subscription_tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_private_server_subscription_tags(data: object) -> list[PrivateServerSubscriptionTag] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                private_server_subscription_tags_type_0 = []
                _private_server_subscription_tags_type_0 = data
                for private_server_subscription_tags_type_0_item_data in _private_server_subscription_tags_type_0:
                    private_server_subscription_tags_type_0_item = PrivateServerSubscriptionTag(
                        private_server_subscription_tags_type_0_item_data
                    )

                    private_server_subscription_tags_type_0.append(private_server_subscription_tags_type_0_item)

                return private_server_subscription_tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PrivateServerSubscriptionTag] | None | Unset, data)

        private_server_subscription_tags = _parse_private_server_subscription_tags(
            d.pop("privateServerSubscriptionTags", UNSET)
        )

        private_server_subscription_metadata = cls(
            private_server_subscription_tags=private_server_subscription_tags,
        )

        return private_server_subscription_metadata
