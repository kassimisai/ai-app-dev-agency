from agency_swarm import Agent
from .tools.TestAutomator import TestAutomator
from .tools.QualityAnalyzer import QualityAnalyzer

class QAEngineer(Agent):
    """
    QA Engineer Agent responsible for ensuring the quality, reliability,
    and performance of software applications.
    """
    
    def __init__(self):
        super().__init__(
            name="QA Engineer",
            description=(
                "Quality Assurance Engineer responsible for ensuring the quality, "
                "reliability, and performance of software applications through "
                "comprehensive testing strategies and quality analysis."
            ),
            instructions="./instructions.md",
            tools=[TestAutomator, QualityAnalyzer],
            tools_folder="./tools",
            temperature=0.3,  # Lower temperature for more precise testing decisions
            max_prompt_tokens=25000,
        ) 