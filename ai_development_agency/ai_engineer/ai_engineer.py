from agency_swarm import Agent
from .tools.ModelArchitect import ModelArchitect
from .tools.ModelTrainer import ModelTrainer

class AIEngineer(Agent):
    """
    AI/ML Engineer Agent responsible for designing, developing, and deploying
    artificial intelligence and machine learning solutions in the AI Application
    Development Agency.
    """
    
    def __init__(self):
        super().__init__(
            name="AI Engineer",
            description=(
                "AI/ML Engineer responsible for designing, developing, and deploying "
                "artificial intelligence and machine learning solutions, ensuring "
                "efficiency, scalability, and ethical implementation."
            ),
            instructions="./instructions.md",
            tools=[ModelArchitect, ModelTrainer],
            tools_folder="./tools",
            temperature=0.3,  # Lower temperature for more precise technical decisions
            max_prompt_tokens=25000,
        ) 