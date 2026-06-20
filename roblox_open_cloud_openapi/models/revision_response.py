from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conditional_rules_changes_payload import ConditionalRulesChangesPayload
    from ..models.revision_response_changes_type_0 import RevisionResponseChangesType0


T = TypeVar("T", bound="RevisionResponse")


@_attrs_define
class RevisionResponse:
    """Response model for a revision.

    Attributes:
        revision_id (None | str | Unset): The revision ID.
        version (int | Unset): The version number.
        time (datetime.datetime | Unset): The time the revision was created/updated.
        published_by (None | str | Unset): The user ID who published this revision.
        message (None | str | Unset): The message describing the changes.
        deployment_result (None | str | Unset): The deployment result status.
        auto_restore_to_version (int | Unset): The version to auto-restore to, or -1 if not applicable.
        changes (None | RevisionResponseChangesType0 | Unset): The changes in this revision, keyed by entry key.
        conditional_rules_changes (ConditionalRulesChangesPayload | None | Unset): Optional delta for conditional rules
            when this revision touched rules or evaluation order.
    """

    revision_id: None | str | Unset = UNSET
    version: int | Unset = UNSET
    time: datetime.datetime | Unset = UNSET
    published_by: None | str | Unset = UNSET
    message: None | str | Unset = UNSET
    deployment_result: None | str | Unset = UNSET
    auto_restore_to_version: int | Unset = UNSET
    changes: None | RevisionResponseChangesType0 | Unset = UNSET
    conditional_rules_changes: ConditionalRulesChangesPayload | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.conditional_rules_changes_payload import ConditionalRulesChangesPayload
        from ..models.revision_response_changes_type_0 import RevisionResponseChangesType0

        revision_id: None | str | Unset
        if isinstance(self.revision_id, Unset):
            revision_id = UNSET
        else:
            revision_id = self.revision_id

        version = self.version

        time: str | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        published_by: None | str | Unset
        if isinstance(self.published_by, Unset):
            published_by = UNSET
        else:
            published_by = self.published_by

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        deployment_result: None | str | Unset
        if isinstance(self.deployment_result, Unset):
            deployment_result = UNSET
        else:
            deployment_result = self.deployment_result

        auto_restore_to_version = self.auto_restore_to_version

        changes: dict[str, Any] | None | Unset
        if isinstance(self.changes, Unset):
            changes = UNSET
        elif isinstance(self.changes, RevisionResponseChangesType0):
            changes = self.changes.to_dict()
        else:
            changes = self.changes

        conditional_rules_changes: dict[str, Any] | None | Unset
        if isinstance(self.conditional_rules_changes, Unset):
            conditional_rules_changes = UNSET
        elif isinstance(self.conditional_rules_changes, ConditionalRulesChangesPayload):
            conditional_rules_changes = self.conditional_rules_changes.to_dict()
        else:
            conditional_rules_changes = self.conditional_rules_changes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if revision_id is not UNSET:
            field_dict["revisionId"] = revision_id
        if version is not UNSET:
            field_dict["version"] = version
        if time is not UNSET:
            field_dict["time"] = time
        if published_by is not UNSET:
            field_dict["publishedBy"] = published_by
        if message is not UNSET:
            field_dict["message"] = message
        if deployment_result is not UNSET:
            field_dict["deploymentResult"] = deployment_result
        if auto_restore_to_version is not UNSET:
            field_dict["autoRestoreToVersion"] = auto_restore_to_version
        if changes is not UNSET:
            field_dict["changes"] = changes
        if conditional_rules_changes is not UNSET:
            field_dict["conditionalRulesChanges"] = conditional_rules_changes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conditional_rules_changes_payload import ConditionalRulesChangesPayload
        from ..models.revision_response_changes_type_0 import RevisionResponseChangesType0

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_revision_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        revision_id = _parse_revision_id(d.pop("revisionId", UNSET))

        version = d.pop("version", UNSET)

        _time = d.pop("time", UNSET)
        time: datetime.datetime | Unset
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = datetime.datetime.fromisoformat(_time)

        def _parse_published_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        published_by = _parse_published_by(d.pop("publishedBy", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_deployment_result(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deployment_result = _parse_deployment_result(d.pop("deploymentResult", UNSET))

        auto_restore_to_version = d.pop("autoRestoreToVersion", UNSET)

        def _parse_changes(data: object) -> None | RevisionResponseChangesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                changes_type_0 = RevisionResponseChangesType0.from_dict(data)

                return changes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RevisionResponseChangesType0 | Unset, data)

        changes = _parse_changes(d.pop("changes", UNSET))

        def _parse_conditional_rules_changes(data: object) -> ConditionalRulesChangesPayload | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                conditional_rules_changes_type_1 = ConditionalRulesChangesPayload.from_dict(data)

                return conditional_rules_changes_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConditionalRulesChangesPayload | None | Unset, data)

        conditional_rules_changes = _parse_conditional_rules_changes(d.pop("conditionalRulesChanges", UNSET))

        revision_response = cls(
            revision_id=revision_id,
            version=version,
            time=time,
            published_by=published_by,
            message=message,
            deployment_result=deployment_result,
            auto_restore_to_version=auto_restore_to_version,
            changes=changes,
            conditional_rules_changes=conditional_rules_changes,
        )

        return revision_response
