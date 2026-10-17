from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGamesApiModelsResponseRefundPolicy")


@_attrs_define
class RobloxGamesApiModelsResponseRefundPolicy:
    """
    Attributes:
        policy_text (str | Unset): The display text with a placeholder for clients to inject a link, such as:
              "Learn more about policy xyz {linkStart}Learn More{linkEnd}"
        learn_more_base_url (str | Unset): The base URL that the client should redirect to.
        locale (str | Unset): The Roblox selected language locale that the user has presently selected.
        article_id (str | Unset): Zendesk (or similar forum provider) article ID for the client to build a redirect URL.
    """

    policy_text: str | Unset = UNSET
    learn_more_base_url: str | Unset = UNSET
    locale: str | Unset = UNSET
    article_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        policy_text = self.policy_text

        learn_more_base_url = self.learn_more_base_url

        locale = self.locale

        article_id = self.article_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if policy_text is not UNSET:
            field_dict["policyText"] = policy_text
        if learn_more_base_url is not UNSET:
            field_dict["learnMoreBaseUrl"] = learn_more_base_url
        if locale is not UNSET:
            field_dict["locale"] = locale
        if article_id is not UNSET:
            field_dict["articleId"] = article_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        policy_text = d.pop("policyText", UNSET)

        learn_more_base_url = d.pop("learnMoreBaseUrl", UNSET)

        locale = d.pop("locale", UNSET)

        article_id = d.pop("articleId", UNSET)

        roblox_games_api_models_response_refund_policy = cls(
            policy_text=policy_text,
            learn_more_base_url=learn_more_base_url,
            locale=locale,
            article_id=article_id,
        )

        return roblox_games_api_models_response_refund_policy
