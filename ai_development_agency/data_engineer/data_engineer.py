from agency_swarm import Agent
from .tools.DataArchitect import DataArchitect
from .tools.DataPipelineManager import DataPipelineManager

class DataEngineer(Agent):
    """
    Data Engineer Agent responsible for designing, implementing,
    and maintaining data infrastructure and pipelines.
    """
    
    def __init__(self):
        super().__init__(
            name="Data Engineer",
            description=(
                "Data Engineer responsible for designing, implementing, and "
                "maintaining data infrastructure and pipelines, ensuring efficient "
                "data collection, processing, storage, and accessibility."
            ),
            instructions="./instructions.md",
            tools=[DataArchitect, DataPipelineManager],
            tools_folder="./tools",
            temperature=0.3,  # Lower temperature for more precise data decisions
            max_prompt_tokens=25000,
        ) 