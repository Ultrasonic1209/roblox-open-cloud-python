from enum import Enum


class SubscriptionExpirationDetailsReason(str, Enum):
    EXPIRATION_REASON_UNSPECIFIED = "EXPIRATION_REASON_UNSPECIFIED"
    LAPSED = "LAPSED"
    PRODUCT_DELETED = "PRODUCT_DELETED"
    PRODUCT_INACTIVE = "PRODUCT_INACTIVE"
    SUBSCRIBER_CANCELLED = "SUBSCRIBER_CANCELLED"
    SUBSCRIBER_REFUNDED = "SUBSCRIBER_REFUNDED"

    def __str__(self) -> str:
        return str(self.value)
