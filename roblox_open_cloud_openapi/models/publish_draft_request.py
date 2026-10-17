from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.deployment_strategy import DeploymentStrategy
from ..types import UNSET, Unset

T = TypeVar("T", bound="PublishDraftRequest")


@_attrs_define
class PublishDraftRequest:
    """Request model for publishing a draft.

    Attributes:
        draft_hash (None | str | Unset): The draft hash for concurrency control. If provided, the publish will fail if
            it doesn't match.
        message (None | str | Unset): The message describing the changes being published.
        deployment_strategy (DeploymentStrategy | Unset): Deployment strategy for publishing configurations.

            Invalid

            GradualRollout

            Immediate
    """

    draft_hash: None | str | Unset = UNSET
    message: None | str | Unset = UNSET
    deployment_strategy: DeploymentStrategy | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        draft_hash: None | str | Unset
        if isinstance(self.draft_hash, Unset):
            draft_hash = UNSET
        else:
            draft_hash = self.draft_hash

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        deployment_strategy: str | Unset = UNSET
        if not isinstance(self.deployment_strategy, Unset):
            deployment_strategy = self.deployment_strategy.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if draft_hash is not UNSET:
            field_dict["draftHash"] = draft_hash
        if message is not UNSET:
            field_dict["message"] = message
        if deployment_strategy is not UNSET:
            field_dict["deploymentStrategy"] = deployment_strategy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_draft_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        draft_hash = _parse_draft_hash(d.pop("draftHash", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        _deployment_strategy = d.pop("deploymentStrategy", UNSET)
        deployment_strategy: DeploymentStrategy | Unset
        if isinstance(_deployment_strategy, Unset):
            deployment_strategy = UNSET
        else:
            deployment_strategy = DeploymentStrategy(_deployment_strategy)

        publish_draft_request = cls(
            draft_hash=draft_hash,
            message=message,
            deployment_strategy=deployment_strategy,
        )

        return publish_draft_request
