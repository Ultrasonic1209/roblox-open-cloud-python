from enum import StrEnum


class GetV2UsersUserIdTradableItemsItemTargetTypesItem(StrEnum):
    ANIMATION = "Animation"
    BACKACCESSORY = "BackAccessory"
    CHARACTER = "Character"
    DRESSSKIRTACCESSORY = "DressSkirtAccessory"
    DYNAMICHEAD = "DynamicHead"
    FACE = "Face"
    FACEACCESSORY = "FaceAccessory"
    FRONTACCESSORY = "FrontAccessory"
    GEAR = "Gear"
    HAIRACCESSORY = "HairAccessory"
    HATACCESSORY = "HatAccessory"
    JACKETACCESSORY = "JacketAccessory"
    NECKACCESSORY = "NeckAccessory"
    SHOES = "Shoes"
    SHOULDERACCESSORY = "ShoulderAccessory"
    SWEATERACCESSORY = "SweaterAccessory"
    UNKNOWN = "Unknown"
    WAISTACCESSORY = "WaistAccessory"

    def __str__(self) -> str:
        return str(self.value)
