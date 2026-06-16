from enum import Enum


class Repository(str, Enum):
    DATA_STORES_CONFIG = "DataStoresConfig"
    EXPERIENCE_USER_CONFIG = "ExperienceUserConfig"
    EXTENDED_SERVICES_CONFIG = "ExtendedServicesConfig"
    IN_EXPERIENCE_CONFIG = "InExperienceConfig"
    LEADERBOARDS_CONFIG = "LeaderboardsConfig"
    RECOMMENDATION_SERVICES_CONFIG = "RecommendationServicesConfig"

    def __str__(self) -> str:
        return str(self.value)
