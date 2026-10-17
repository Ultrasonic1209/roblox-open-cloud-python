from enum import StrEnum


class RobloxApiNotificationsModelsPushNotificationRegistrationPlatform(StrEnum):
    ANDROIDAMAZON = "AndroidAmazon"
    ANDROIDNATIVE = "AndroidNative"
    ANDROIDTENCENTSERVICE = "AndroidTencentService"
    CHROMEONDESKTOP = "ChromeOnDesktop"
    FIREFOXONDESKTOP = "FirefoxOnDesktop"
    IOSNATIVE = "IOSNative"
    IOSPUSHKIT = "IOSPushKit"
    IOSTENCENT = "IOSTencent"

    def __str__(self) -> str:
        return str(self.value)
