from agency_swarm import Agent
from .tools.ProjectAnalyzer import ProjectAnalyzer
from .tools.TeamCoordinator import TeamCoordinator

class CEO(Agent):
    """
    CEO Agent responsible for strategic planning, team coordination, and project oversight
    in the AI Application Development Agency.
    """
    
    def __init__(self):
        super().__init__(
            name="CEO",
            description=(
                "Chief Executive Officer responsible for strategic planning, "
                "project management, and team coordination in the AI Application "
                "Development Agency."
            ),
            instructions="./instructions.md",
            tools=[ProjectAnalyzer, TeamCoordinator],
            tools_folder="./tools",
            temperature=0.5,
            max_prompt_tokens=25000,
        ) 