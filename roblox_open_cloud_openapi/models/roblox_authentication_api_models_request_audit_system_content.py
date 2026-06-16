from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_authentication_api_models_request_audit_system_content_additional_audit_content import (
        RobloxAuthenticationApiModelsRequestAuditSystemContentAdditionalAuditContent,
    )
    from ..models.roblox_authentication_api_models_request_audit_system_content_captured_audit_content import (
        RobloxAuthenticationApiModelsRequestAuditSystemContentCapturedAuditContent,
    )


T = TypeVar("T", bound="RobloxAuthenticationApiModelsRequestAuditSystemContent")


@_attrs_define
class RobloxAuthenticationApiModelsRequestAuditSystemContent:
    """
    Attributes:
        captured_audit_content (RobloxAuthenticationApiModelsRequestAuditSystemContentCapturedAuditContent | Unset):
        additional_audit_content (RobloxAuthenticationApiModelsRequestAuditSystemContentAdditionalAuditContent | Unset):
    """

    captured_audit_content: RobloxAuthenticationApiModelsRequestAuditSystemContentCapturedAuditContent | Unset = UNSET
    additional_audit_content: RobloxAuthenticationApiModelsRequestAuditSystemContentAdditionalAuditContent | Unset = (
        UNSET
    )

    def to_dict(self) -> dict[str, Any]:
        captured_audit_content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.captured_audit_content, Unset):
            captured_audit_content = self.captured_audit_content.to_dict()

        additional_audit_content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_audit_content, Unset):
            additional_audit_content = self.additional_audit_content.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if captured_audit_content is not UNSET:
            field_dict["capturedAuditContent"] = captured_audit_content
        if additional_audit_content is not UNSET:
            field_dict["additionalAuditContent"] = additional_audit_content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_authentication_api_models_request_audit_system_content_additional_audit_content import (
            RobloxAuthenticationApiModelsRequestAuditSystemContentAdditionalAuditContent,
        )
        from ..models.roblox_authentication_api_models_request_audit_system_content_captured_audit_content import (
            RobloxAuthenticationApiModelsRequestAuditSystemContentCapturedAuditContent,
        )

        d = dict(src_dict)
        _captured_audit_content = d.pop("capturedAuditContent", UNSET)
        captured_audit_content: RobloxAuthenticationApiModelsRequestAuditSystemContentCapturedAuditContent | Unset
        if isinstance(_captured_audit_content, Unset):
            captured_audit_content = UNSET
        else:
            captured_audit_content = (
                RobloxAuthenticationApiModelsRequestAuditSystemContentCapturedAuditContent.from_dict(
                    _captured_audit_content
                )
            )

        _additional_audit_content = d.pop("additionalAuditContent", UNSET)
        additional_audit_content: RobloxAuthenticationApiModelsRequestAuditSystemContentAdditionalAuditContent | Unset
        if isinstance(_additional_audit_content, Unset):
            additional_audit_content = UNSET
        else:
            additional_audit_content = (
                RobloxAuthenticationApiModelsRequestAuditSystemContentAdditionalAuditContent.from_dict(
                    _additional_audit_content
                )
            )

        roblox_authentication_api_models_request_audit_system_content = cls(
            captured_audit_content=captured_audit_content,
            additional_audit_content=additional_audit_content,
        )

        return roblox_authentication_api_models_request_audit_system_content
