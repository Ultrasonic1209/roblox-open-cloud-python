from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.o18_eligibility_tag import O18EligibilityTag
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_response import AgentResponse
    from ..models.generic_currency_response import GenericCurrencyResponse
    from ..models.transaction_details_response import TransactionDetailsResponse


T = TypeVar("T", bound="TransactionResponse")


@_attrs_define
class TransactionResponse:
    """
    Attributes:
        id (int | Unset):
        id_hash (None | str | Unset):
        created (datetime.datetime | Unset):
        is_pending (bool | Unset):
        agent (AgentResponse | None | Unset):
        details (None | TransactionDetailsResponse | Unset):
        currency (GenericCurrencyResponse | None | Unset):
        purchase_token (None | str | Unset):
        o_18_eligibility_tag (None | O18EligibilityTag | Unset):
    """

    id: int | Unset = UNSET
    id_hash: None | str | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    is_pending: bool | Unset = UNSET
    agent: AgentResponse | None | Unset = UNSET
    details: None | TransactionDetailsResponse | Unset = UNSET
    currency: GenericCurrencyResponse | None | Unset = UNSET
    purchase_token: None | str | Unset = UNSET
    o_18_eligibility_tag: None | O18EligibilityTag | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_response import AgentResponse
        from ..models.generic_currency_response import GenericCurrencyResponse
        from ..models.transaction_details_response import TransactionDetailsResponse

        id = self.id

        id_hash: None | str | Unset
        if isinstance(self.id_hash, Unset):
            id_hash = UNSET
        else:
            id_hash = self.id_hash

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        is_pending = self.is_pending

        agent: dict[str, Any] | None | Unset
        if isinstance(self.agent, Unset):
            agent = UNSET
        elif isinstance(self.agent, AgentResponse):
            agent = self.agent.to_dict()
        else:
            agent = self.agent

        details: dict[str, Any] | None | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, TransactionDetailsResponse):
            details = self.details.to_dict()
        else:
            details = self.details

        currency: dict[str, Any] | None | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        elif isinstance(self.currency, GenericCurrencyResponse):
            currency = self.currency.to_dict()
        else:
            currency = self.currency

        purchase_token: None | str | Unset
        if isinstance(self.purchase_token, Unset):
            purchase_token = UNSET
        else:
            purchase_token = self.purchase_token

        o_18_eligibility_tag: None | str | Unset
        if isinstance(self.o_18_eligibility_tag, Unset):
            o_18_eligibility_tag = UNSET
        elif isinstance(self.o_18_eligibility_tag, O18EligibilityTag):
            o_18_eligibility_tag = self.o_18_eligibility_tag.value
        else:
            o_18_eligibility_tag = self.o_18_eligibility_tag

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if id_hash is not UNSET:
            field_dict["idHash"] = id_hash
        if created is not UNSET:
            field_dict["created"] = created
        if is_pending is not UNSET:
            field_dict["isPending"] = is_pending
        if agent is not UNSET:
            field_dict["agent"] = agent
        if details is not UNSET:
            field_dict["details"] = details
        if currency is not UNSET:
            field_dict["currency"] = currency
        if purchase_token is not UNSET:
            field_dict["purchaseToken"] = purchase_token
        if o_18_eligibility_tag is not UNSET:
            field_dict["o18EligibilityTag"] = o_18_eligibility_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_response import AgentResponse
        from ..models.generic_currency_response import GenericCurrencyResponse
        from ..models.transaction_details_response import TransactionDetailsResponse

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_id_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id_hash = _parse_id_hash(d.pop("idHash", UNSET))

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        is_pending = d.pop("isPending", UNSET)

        def _parse_agent(data: object) -> AgentResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                agent_type_1 = AgentResponse.from_dict(data)

                return agent_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentResponse | None | Unset, data)

        agent = _parse_agent(d.pop("agent", UNSET))

        def _parse_details(data: object) -> None | TransactionDetailsResponse | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_1 = TransactionDetailsResponse.from_dict(data)

                return details_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransactionDetailsResponse | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        def _parse_currency(data: object) -> GenericCurrencyResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                currency_type_1 = GenericCurrencyResponse.from_dict(data)

                return currency_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GenericCurrencyResponse | None | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_purchase_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        purchase_token = _parse_purchase_token(d.pop("purchaseToken", UNSET))

        def _parse_o_18_eligibility_tag(data: object) -> None | O18EligibilityTag | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                o_18_eligibility_tag_type_1 = O18EligibilityTag(data)

                return o_18_eligibility_tag_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | O18EligibilityTag | Unset, data)

        o_18_eligibility_tag = _parse_o_18_eligibility_tag(d.pop("o18EligibilityTag", UNSET))

        transaction_response = cls(
            id=id,
            id_hash=id_hash,
            created=created,
            is_pending=is_pending,
            agent=agent,
            details=details,
            currency=currency,
            purchase_token=purchase_token,
            o_18_eligibility_tag=o_18_eligibility_tag,
        )

        return transaction_response
