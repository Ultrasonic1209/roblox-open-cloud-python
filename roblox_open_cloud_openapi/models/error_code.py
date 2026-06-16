from enum import Enum


class ErrorCode(str, Enum):
    BADREQUEST = "BadRequest"
    BLOCKED = "Blocked"
    CONFLICT = "Conflict"
    DUPLICATEPRODUCTNAME = "DuplicateProductName"
    INTERNAL = "Internal"
    INVALIDCURSOR = "InvalidCursor"
    INVALIDDESCRIPTION = "InvalidDescription"
    INVALIDDEVELOPERPRODUCTID = "InvalidDeveloperProductId"
    INVALIDIMAGEFILE = "InvalidImageFile"
    INVALIDISFORSALE = "InvalidIsForSale"
    INVALIDNAME = "InvalidName"
    INVALIDPAGENUMBER = "InvalidPageNumber"
    INVALIDPAGESIZE = "InvalidPageSize"
    INVALIDPOSTBODY = "InvalidPostBody"
    INVALIDPRICE = "InvalidPrice"
    INVALIDPRICEINROBUX = "InvalidPriceInRobux"
    INVALIDPRODUCTID = "InvalidProductId"
    INVALIDPRODUCTIDS = "InvalidProductIds"
    INVALIDREGIONALPRICING = "InvalidRegionalPricing"
    INVALIDSHOPID = "InvalidShopId"
    INVALIDSTOREPAGEENABLED = "InvalidStorePageEnabled"
    INVALIDUNIVERSEID = "InvalidUniverseId"
    NOTAUTHENTICATED = "NotAuthenticated"
    NOTFOUND = "NotFound"
    PENDINGPRODUCTSLIMITEXCEEDED = "PendingProductsLimitExceeded"
    PRODUCTRETRIEVALLIMITEXCEEDED = "ProductRetrievalLimitExceeded"
    UNAUTHORIZEDACCESS = "UnauthorizedAccess"
    UNAUTHORIZEDPRODUCTACCESS = "UnauthorizedProductAccess"
    UNAUTHORIZEDUNIVERSEACCESS = "UnauthorizedUniverseAccess"
    UNAVAILABLE = "Unavailable"
    UNKNOWNERROR = "UnknownError"
    UNSUPPORTEDDEVELOPERPRODUCTUPDATE = "UnsupportedDeveloperProductUpdate"

    def __str__(self) -> str:
        return str(self.value)
