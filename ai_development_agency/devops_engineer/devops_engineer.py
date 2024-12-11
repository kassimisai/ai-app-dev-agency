from agency_swarm import Agent
from .tools.InfrastructureManager import InfrastructureManager
from .tools.PipelineAutomator import PipelineAutomator

class DevOpsEngineer(Agent):
    """
    DevOps Engineer Agent responsible for implementing and maintaining
    CI/CD pipelines and cloud infrastructure.
    """
    
    def __init__(self):
        super().__init__(
            name="DevOps Engineer",
            description=(
                "DevOps Engineer responsible for implementing and maintaining "
                "continuous integration and deployment pipelines, managing cloud "
                "infrastructure, and ensuring system reliability and scalability."
            ),
            instructions="./instructions.md",
            tools=[InfrastructureManager, PipelineAutomator],
            tools_folder="./tools",
            temperature=0.3,  # Lower temperature for more precise infrastructure decisions
            max_prompt_tokens=25000,
        ) 