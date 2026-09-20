"""
CrewAI Enterprise MLOps Telemetry Handler Example
Author: Hasnain Chavhan (@HasnainChavhan)
Description: Integrates custom execution logging and metrics tracking for CrewAI agents.
"""

from typing import Any, Dict

class CrewAIObservabilityHandler:
    def __init__(self, service_name: str = "crewai-agent-service"):
        self.service_name = service_name
        self.metrics_log = []

    def on_agent_start(self, agent_name: str, task_description: str) -> None:
        event = {"event": "agent_start", "agent": agent_name, "task": task_description}
        self.metrics_log.append(event)
        print(f"[Telemetry] Agent '{agent_name}' started task: {task_description}")

    def on_agent_finish(self, agent_name: str, output: Any) -> None:
        event = {"event": "agent_finish", "agent": agent_name, "output": str(output)}
        self.metrics_log.append(event)
        print(f"[Telemetry] Agent '{agent_name}' finished execution.")
