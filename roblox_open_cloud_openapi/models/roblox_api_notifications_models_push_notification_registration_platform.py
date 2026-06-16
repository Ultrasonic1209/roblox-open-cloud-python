from enum import Enum


class RobloxApiNotificationsModelsPushNotificationRegistrationPlatform(str, Enum):
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
