from agency_swarm import Agent
from .tools.ArchitectureDesigner import ArchitectureDesigner
from .tools.TechEvaluator import TechEvaluator

class CTO(Agent):
    """
    CTO Agent responsible for technical strategy, architecture decisions,
    and technology stack selection in the AI Application Development Agency.
    """
    
    def __init__(self):
        super().__init__(
            name="CTO",
            description=(
                "Chief Technology Officer responsible for technical strategy, "
                "architecture decisions, and technology stack selection in the "
                "AI Application Development Agency."
            ),
            instructions="./instructions.md",
            tools=[ArchitectureDesigner, TechEvaluator],
            tools_folder="./tools",
            temperature=0.4,  # Lower temperature for more precise technical decisions
            max_prompt_tokens=25000,
        ) 