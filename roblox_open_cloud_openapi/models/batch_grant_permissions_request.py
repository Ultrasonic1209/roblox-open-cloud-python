from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.asset_action import AssetAction
from ..models.subject_type import SubjectType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_grant_request import AssetGrantRequest


T = TypeVar("T", bound="BatchGrantPermissionsRequest")


@_attrs_define
class BatchGrantPermissionsRequest:
    """Request object to grant one permission to multiple assets.

    Attributes:
        subject_type (SubjectType | Unset):
        subject_id (None | str | Unset): The subject ID to grant to. Must be empty for SubjectType 'All'.
        action (AssetAction | Unset): Asset permission actions that can be granted.

            Actions:
            * Invalid - default value, not a valid action.
            * Edit - grants the ability to edit and manage the asset.
            * Use - grants the ability to use the asset.
            * Download - grants the ability to download the asset.
            * CopyFromRcc - grants the ability to copy the asset from RCC, used to enable AssetService:CreatePlaceAsync().
            * UpdateFromRcc - grants the ability to update the asset from RCC, used to enable
            AssetService:UpdatePlaceAsync().

            Valid AssetType - SubjectType - Action combinations:
            * Animation - Group/User/Universe - Use
            * Audio - Group/User/Universe - Use
            * Decal - All/Group/User/Universe - Use
            * Image - All/Group/User/Universe - Use
            * Mesh - All/Group/User/Universe - Use
            * MeshPart - Group/User/Universe - Use
            * Model - User - Edit
              * Group/User/Universe - Use
            * Place - All - Download
              * Universe - CopyFromRcc/UpdateFromRcc
            * Video - Group/User/Universe - Use.
        requests (list[AssetGrantRequest] | None | Unset): Array of asset grant requests. If populated, 'requests' will
            override 'assetIds'.
        asset_ids (list[int] | None | Unset): [Deprecated] The list of asset IDs to grant this permission to. 'requests'
            will be prioritized over this list.
        enable_deep_access_check (bool | Unset): [Do not use] An optional boolean to indicate if a deep access check
            should be done. This is not intended for public use.
    """

    subject_type: SubjectType | Unset = UNSET
    subject_id: None | str | Unset = UNSET
    action: AssetAction | Unset = UNSET
    requests: list[AssetGrantRequest] | None | Unset = UNSET
    asset_ids: list[int] | None | Unset = UNSET
    enable_deep_access_check: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        subject_type: str | Unset = UNSET
        if not isinstance(self.subject_type, Unset):
            subject_type = self.subject_type.value

        subject_id: None | str | Unset
        if isinstance(self.subject_id, Unset):
            subject_id = UNSET
        else:
            subject_id = self.subject_id

        action: str | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        requests: list[dict[str, Any]] | None | Unset
        if isinstance(self.requests, Unset):
            requests = UNSET
        elif isinstance(self.requests, list):
            requests = []
            for requests_type_0_item_data in self.requests:
                requests_type_0_item = requests_type_0_item_data.to_dict()
                requests.append(requests_type_0_item)

        else:
            requests = self.requests

        asset_ids: list[int] | None | Unset
        if isinstance(self.asset_ids, Unset):
            asset_ids = UNSET
        elif isinstance(self.asset_ids, list):
            asset_ids = self.asset_ids

        else:
            asset_ids = self.asset_ids

        enable_deep_access_check = self.enable_deep_access_check

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if subject_type is not UNSET:
            field_dict["subjectType"] = subject_type
        if subject_id is not UNSET:
            field_dict["subjectId"] = subject_id
        if action is not UNSET:
            field_dict["action"] = action
        if requests is not UNSET:
            field_dict["requests"] = requests
        if asset_ids is not UNSET:
            field_dict["assetIds"] = asset_ids
        if enable_deep_access_check is not UNSET:
            field_dict["enableDeepAccessCheck"] = enable_deep_access_check

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_grant_request import AssetGrantRequest

        d = dict(src_dict)
        _subject_type = d.pop("subjectType", UNSET)
        subject_type: SubjectType | Unset
        if isinstance(_subject_type, Unset):
            subject_type = UNSET
        else:
            subject_type = SubjectType(_subject_type)

        def _parse_subject_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject_id = _parse_subject_id(d.pop("subjectId", UNSET))

        _action = d.pop("action", UNSET)
        action: AssetAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = AssetAction(_action)

        def _parse_requests(data: object) -> list[AssetGrantRequest] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                requests_type_0 = []
                _requests_type_0 = data
                for requests_type_0_item_data in _requests_type_0:
                    requests_type_0_item = AssetGrantRequest.from_dict(requests_type_0_item_data)

                    requests_type_0.append(requests_type_0_item)

                return requests_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AssetGrantRequest] | None | Unset, data)

        requests = _parse_requests(d.pop("requests", UNSET))

        def _parse_asset_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                asset_ids_type_0 = cast(list[int], data)

                return asset_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        asset_ids = _parse_asset_ids(d.pop("assetIds", UNSET))

        enable_deep_access_check = d.pop("enableDeepAccessCheck", UNSET)

        batch_grant_permissions_request = cls(
            subject_type=subject_type,
            subject_id=subject_id,
            action=action,
            requests=requests,
            asset_ids=asset_ids,
            enable_deep_access_check=enable_deep_access_check,
        )

        return batch_grant_permissions_request
