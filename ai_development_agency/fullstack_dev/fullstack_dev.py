from agency_swarm import Agent
from .tools.FrontendDeveloper import FrontendDeveloper
from .tools.BackendDeveloper import BackendDeveloper

class FullStackDeveloper(Agent):
    """
    Full-Stack Developer Agent responsible for implementing both frontend
    and backend components of applications in the AI Application Development Agency.
    """
    
    def __init__(self):
        super().__init__(
            name="Full-Stack Developer",
            description=(
                "Full-Stack Developer responsible for implementing both frontend "
                "and backend components, ensuring seamless integration between "
                "all layers of the system while following best practices."
            ),
            instructions="./instructions.md",
            tools=[FrontendDeveloper, BackendDeveloper],
            tools_folder="./tools",
            temperature=0.4,  # Balanced temperature for both creative and precise decisions
            max_prompt_tokens=25000,
        ) 