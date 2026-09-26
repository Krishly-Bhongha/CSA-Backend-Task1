from rest_framework.throttling import UserRateThrottle


class MissionClaimThrottle(UserRateThrottle):
    scope = "mission_claim"