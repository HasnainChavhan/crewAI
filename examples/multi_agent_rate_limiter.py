"""
CrewAI Multi-Agent API Rate Limiter
Author: Hasnain Chavhan (@HasnainChavhan)
Description: Throttles concurrent API requests across autonomous CrewAI agents to prevent 429 rate limit errors.
"""

import time

class CrewAIRateLimiter:
    def __init__(self, requests_per_minute: int = 60):
        self.interval = 60.0 / requests_per_minute
        self.last_request_time = 0.0

    def wait_if_needed(self) -> None:
        now = time.time()
        elapsed = now - self.last_request_time
        if elapsed < self.interval:
            time.sleep(self.interval - elapsed)
        self.last_request_time = time.time()
