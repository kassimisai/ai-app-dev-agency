from agency_swarm import Agent
from .tools.ExperienceDesigner import ExperienceDesigner
from .tools.InterfaceDesigner import InterfaceDesigner

class UIUXDesigner(Agent):
    """
    UI/UX Designer Agent responsible for creating intuitive, accessible,
    and visually appealing user interfaces and experiences.
    """
    
    def __init__(self):
        super().__init__(
            name="UI/UX Designer",
            description=(
                "UI/UX Designer responsible for creating intuitive, accessible, "
                "and visually appealing user interfaces and experiences, ensuring "
                "exceptional user experiences while maintaining brand consistency "
                "and accessibility standards."
            ),
            instructions="./instructions.md",
            tools=[ExperienceDesigner, InterfaceDesigner],
            tools_folder="./tools",
            temperature=0.4,  # Balanced temperature for both creative and precise decisions
            max_prompt_tokens=25000,
        ) 