from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1ExternalIdentityProviderIdSsoSamlAssertionConsumerServiceBody")


@_attrs_define
class PostV1ExternalIdentityProviderIdSsoSamlAssertionConsumerServiceBody:
    """
    Attributes:
        saml_response (str | Unset):
        relay_state (str | Unset):
    """

    saml_response: str | Unset = UNSET
    relay_state: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        saml_response = self.saml_response

        relay_state = self.relay_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if saml_response is not UNSET:
            field_dict["SAMLResponse"] = saml_response
        if relay_state is not UNSET:
            field_dict["RelayState"] = relay_state

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.saml_response, Unset):
            files.append(("SAMLResponse", (None, str(self.saml_response).encode(), "text/plain")))

        if not isinstance(self.relay_state, Unset):
            files.append(("RelayState", (None, str(self.relay_state).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        saml_response = d.pop("SAMLResponse", UNSET)

        relay_state = d.pop("RelayState", UNSET)

        post_v1_external_identity_provider_id_sso_saml_assertion_consumer_service_body = cls(
            saml_response=saml_response,
            relay_state=relay_state,
        )

        post_v1_external_identity_provider_id_sso_saml_assertion_consumer_service_body.additional_properties = d
        return post_v1_external_identity_provider_id_sso_saml_assertion_consumer_service_body

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
