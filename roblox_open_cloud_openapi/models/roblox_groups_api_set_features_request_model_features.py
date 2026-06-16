from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_groups_api_set_features_request_model_features_content_upload import (
    RobloxGroupsApiSetFeaturesRequestModelFeaturesContentUpload,
)
from ..models.roblox_groups_api_set_features_request_model_features_forum_read import (
    RobloxGroupsApiSetFeaturesRequestModelFeaturesForumRead,
)
from ..models.roblox_groups_api_set_features_request_model_features_forum_write import (
    RobloxGroupsApiSetFeaturesRequestModelFeaturesForumWrite,
)
from ..models.roblox_groups_api_set_features_request_model_features_game_ownership_transfer import (
    RobloxGroupsApiSetFeaturesRequestModelFeaturesGameOwnershipTransfer,
)
from ..models.roblox_groups_api_set_features_request_model_features_group_ownership_transfer import (
    RobloxGroupsApiSetFeaturesRequestModelFeaturesGroupOwnershipTransfer,
)
from ..models.roblox_groups_api_set_features_request_model_features_payouts import (
    RobloxGroupsApiSetFeaturesRequestModelFeaturesPayouts,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiSetFeaturesRequestModelFeatures")


@_attrs_define
class RobloxGroupsApiSetFeaturesRequestModelFeatures:
    """Dictionary of features and their desired status.

    Attributes:
        payouts (RobloxGroupsApiSetFeaturesRequestModelFeaturesPayouts | Unset): The desired status of a group feature.
            ['On' = 0, 'Blocked' = 1]
        content_upload (RobloxGroupsApiSetFeaturesRequestModelFeaturesContentUpload | Unset): The desired status of a
            group feature. ['On' = 0, 'Blocked' = 1]
        group_ownership_transfer (RobloxGroupsApiSetFeaturesRequestModelFeaturesGroupOwnershipTransfer | Unset): The
            desired status of a group feature. ['On' = 0, 'Blocked' = 1]
        game_ownership_transfer (RobloxGroupsApiSetFeaturesRequestModelFeaturesGameOwnershipTransfer | Unset): The
            desired status of a group feature. ['On' = 0, 'Blocked' = 1]
        forum_read (RobloxGroupsApiSetFeaturesRequestModelFeaturesForumRead | Unset): The desired status of a group
            feature. ['On' = 0, 'Blocked' = 1]
        forum_write (RobloxGroupsApiSetFeaturesRequestModelFeaturesForumWrite | Unset): The desired status of a group
            feature. ['On' = 0, 'Blocked' = 1]
    """

    payouts: RobloxGroupsApiSetFeaturesRequestModelFeaturesPayouts | Unset = UNSET
    content_upload: RobloxGroupsApiSetFeaturesRequestModelFeaturesContentUpload | Unset = UNSET
    group_ownership_transfer: RobloxGroupsApiSetFeaturesRequestModelFeaturesGroupOwnershipTransfer | Unset = UNSET
    game_ownership_transfer: RobloxGroupsApiSetFeaturesRequestModelFeaturesGameOwnershipTransfer | Unset = UNSET
    forum_read: RobloxGroupsApiSetFeaturesRequestModelFeaturesForumRead | Unset = UNSET
    forum_write: RobloxGroupsApiSetFeaturesRequestModelFeaturesForumWrite | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        payouts: str | Unset = UNSET
        if not isinstance(self.payouts, Unset):
            payouts = self.payouts.value

        content_upload: str | Unset = UNSET
        if not isinstance(self.content_upload, Unset):
            content_upload = self.content_upload.value

        group_ownership_transfer: str | Unset = UNSET
        if not isinstance(self.group_ownership_transfer, Unset):
            group_ownership_transfer = self.group_ownership_transfer.value

        game_ownership_transfer: str | Unset = UNSET
        if not isinstance(self.game_ownership_transfer, Unset):
            game_ownership_transfer = self.game_ownership_transfer.value

        forum_read: str | Unset = UNSET
        if not isinstance(self.forum_read, Unset):
            forum_read = self.forum_read.value

        forum_write: str | Unset = UNSET
        if not isinstance(self.forum_write, Unset):
            forum_write = self.forum_write.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if payouts is not UNSET:
            field_dict["Payouts"] = payouts
        if content_upload is not UNSET:
            field_dict["ContentUpload"] = content_upload
        if group_ownership_transfer is not UNSET:
            field_dict["GroupOwnershipTransfer"] = group_ownership_transfer
        if game_ownership_transfer is not UNSET:
            field_dict["GameOwnershipTransfer"] = game_ownership_transfer
        if forum_read is not UNSET:
            field_dict["ForumRead"] = forum_read
        if forum_write is not UNSET:
            field_dict["ForumWrite"] = forum_write

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _payouts = d.pop("Payouts", UNSET)
        payouts: RobloxGroupsApiSetFeaturesRequestModelFeaturesPayouts | Unset
        if isinstance(_payouts, Unset):
            payouts = UNSET
        else:
            payouts = RobloxGroupsApiSetFeaturesRequestModelFeaturesPayouts(_payouts)

        _content_upload = d.pop("ContentUpload", UNSET)
        content_upload: RobloxGroupsApiSetFeaturesRequestModelFeaturesContentUpload | Unset
        if isinstance(_content_upload, Unset):
            content_upload = UNSET
        else:
            content_upload = RobloxGroupsApiSetFeaturesRequestModelFeaturesContentUpload(_content_upload)

        _group_ownership_transfer = d.pop("GroupOwnershipTransfer", UNSET)
        group_ownership_transfer: RobloxGroupsApiSetFeaturesRequestModelFeaturesGroupOwnershipTransfer | Unset
        if isinstance(_group_ownership_transfer, Unset):
            group_ownership_transfer = UNSET
        else:
            group_ownership_transfer = RobloxGroupsApiSetFeaturesRequestModelFeaturesGroupOwnershipTransfer(
                _group_ownership_transfer
            )

        _game_ownership_transfer = d.pop("GameOwnershipTransfer", UNSET)
        game_ownership_transfer: RobloxGroupsApiSetFeaturesRequestModelFeaturesGameOwnershipTransfer | Unset
        if isinstance(_game_ownership_transfer, Unset):
            game_ownership_transfer = UNSET
        else:
            game_ownership_transfer = RobloxGroupsApiSetFeaturesRequestModelFeaturesGameOwnershipTransfer(
                _game_ownership_transfer
            )

        _forum_read = d.pop("ForumRead", UNSET)
        forum_read: RobloxGroupsApiSetFeaturesRequestModelFeaturesForumRead | Unset
        if isinstance(_forum_read, Unset):
            forum_read = UNSET
        else:
            forum_read = RobloxGroupsApiSetFeaturesRequestModelFeaturesForumRead(_forum_read)

        _forum_write = d.pop("ForumWrite", UNSET)
        forum_write: RobloxGroupsApiSetFeaturesRequestModelFeaturesForumWrite | Unset
        if isinstance(_forum_write, Unset):
            forum_write = UNSET
        else:
            forum_write = RobloxGroupsApiSetFeaturesRequestModelFeaturesForumWrite(_forum_write)

        roblox_groups_api_set_features_request_model_features = cls(
            payouts=payouts,
            content_upload=content_upload,
            group_ownership_transfer=group_ownership_transfer,
            game_ownership_transfer=game_ownership_transfer,
            forum_read=forum_read,
            forum_write=forum_write,
        )

        return roblox_groups_api_set_features_request_model_features
