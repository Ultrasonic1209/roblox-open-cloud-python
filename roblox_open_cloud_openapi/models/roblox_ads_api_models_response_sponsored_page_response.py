from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_ads_api_models_response_sponsored_page_response_page_type import (
    RobloxAdsApiModelsResponseSponsoredPageResponsePageType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAdsApiModelsResponseSponsoredPageResponse")


@_attrs_define
class RobloxAdsApiModelsResponseSponsoredPageResponse:
    """The response model for serving a sponsored game.

    Attributes:
        name (str | Unset): The name of the sponsored page.
        title (str | Unset): The title of the sponsored page.
        logo_image_url (str | Unset): The logo image hash of the sponsored page.
        page_type (RobloxAdsApiModelsResponseSponsoredPageResponsePageType | Unset): The type of the sponsored page.
            ['Event' = 0, 'Sponsored' = 1]
        page_path (str | Unset): The path of the sponsored page.
    """

    name: str | Unset = UNSET
    title: str | Unset = UNSET
    logo_image_url: str | Unset = UNSET
    page_type: RobloxAdsApiModelsResponseSponsoredPageResponsePageType | Unset = UNSET
    page_path: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        title = self.title

        logo_image_url = self.logo_image_url

        page_type: int | Unset = UNSET
        if not isinstance(self.page_type, Unset):
            page_type = self.page_type.value

        page_path = self.page_path

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if title is not UNSET:
            field_dict["title"] = title
        if logo_image_url is not UNSET:
            field_dict["logoImageUrl"] = logo_image_url
        if page_type is not UNSET:
            field_dict["pageType"] = page_type
        if page_path is not UNSET:
            field_dict["pagePath"] = page_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name = d.pop("name", UNSET)

        title = d.pop("title", UNSET)

        logo_image_url = d.pop("logoImageUrl", UNSET)

        _page_type = d.pop("pageType", UNSET)
        page_type: RobloxAdsApiModelsResponseSponsoredPageResponsePageType | Unset
        if isinstance(_page_type, Unset):
            page_type = UNSET
        else:
            page_type = RobloxAdsApiModelsResponseSponsoredPageResponsePageType(_page_type)

        page_path = d.pop("pagePath", UNSET)

        roblox_ads_api_models_response_sponsored_page_response = cls(
            name=name,
            title=title,
            logo_image_url=logo_image_url,
            page_type=page_type,
            page_path=page_path,
        )

        return roblox_ads_api_models_response_sponsored_page_response
