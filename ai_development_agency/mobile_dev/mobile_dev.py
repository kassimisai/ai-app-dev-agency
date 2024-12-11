from agency_swarm import Agent
from .tools.CrossPlatformDeveloper import CrossPlatformDeveloper
from .tools.NativeDeveloper import NativeDeveloper

class MobileDeveloper(Agent):
    """
    Mobile Developer Agent responsible for creating high-quality,
    performant mobile applications for both iOS and Android platforms.
    """
    
    def __init__(self):
        super().__init__(
            name="Mobile Developer",
            description=(
                "Mobile Developer responsible for creating high-quality, "
                "performant mobile applications for both iOS and Android platforms, "
                "ensuring seamless user experiences and efficient resource usage."
            ),
            instructions="./instructions.md",
            tools=[CrossPlatformDeveloper, NativeDeveloper],
            tools_folder="./tools",
            temperature=0.4,  # Balanced temperature for both creative and precise decisions
            max_prompt_tokens=25000,
        ) 