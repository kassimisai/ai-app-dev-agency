from agency_swarm import Agency
from ceo.ceo import CEO
from cto.cto import CTO
from ai_engineer.ai_engineer import AIEngineer
from fullstack_dev.fullstack_dev import FullStackDeveloper
from mobile_dev.mobile_dev import MobileDeveloper
from uiux_designer.uiux_designer import UIUXDesigner
from qa_engineer.qa_engineer import QAEngineer
from devops_engineer.devops_engineer import DevOpsEngineer
from data_engineer.data_engineer import DataEngineer

# Initialize agents
ceo = CEO()
cto = CTO()
ai_engineer = AIEngineer()
fullstack_dev = FullStackDeveloper()
mobile_dev = MobileDeveloper()
uiux_designer = UIUXDesigner()
qa_engineer = QAEngineer()
devops_engineer = DevOpsEngineer()
data_engineer = DataEngineer()

# Create the agency with defined communication flows
agency = Agency(
    [
        ceo,  # CEO is the entry point for communication with users
        [ceo, cto],  # CEO can communicate with CTO
        [ceo, ai_engineer],  # CEO can communicate with AI Engineer
        [ceo, fullstack_dev],  # CEO can communicate with Full-Stack Developer
        [ceo, mobile_dev],  # CEO can communicate with Mobile Developer
        [ceo, uiux_designer],  # CEO can communicate with UI/UX Designer
        [ceo, qa_engineer],  # CEO can communicate with QA Engineer
        [ceo, devops_engineer],  # CEO can communicate with DevOps Engineer
        [ceo, data_engineer],  # CEO can communicate with Data Engineer
        [cto, ai_engineer],  # CTO can communicate with AI Engineer
        [cto, fullstack_dev],  # CTO can communicate with Full-Stack Developer
        [cto, mobile_dev],  # CTO can communicate with Mobile Developer
        [cto, uiux_designer],  # CTO can communicate with UI/UX Designer
        [cto, qa_engineer],  # CTO can communicate with QA Engineer
        [cto, devops_engineer],  # CTO can communicate with DevOps Engineer
        [cto, data_engineer],  # CTO can communicate with Data Engineer
        [ai_engineer, fullstack_dev],  # AI Engineer can communicate with Full-Stack Developer
        [ai_engineer, mobile_dev],  # AI Engineer can communicate with Mobile Developer
        [ai_engineer, uiux_designer],  # AI Engineer can communicate with UI/UX Designer
        [ai_engineer, qa_engineer],  # AI Engineer can communicate with QA Engineer
        [ai_engineer, devops_engineer],  # AI Engineer can communicate with DevOps Engineer
        [ai_engineer, data_engineer],  # AI Engineer can communicate with Data Engineer
        [fullstack_dev, mobile_dev],  # Full-Stack Developer can communicate with Mobile Developer
        [fullstack_dev, uiux_designer],  # Full-Stack Developer can communicate with UI/UX Designer
        [fullstack_dev, qa_engineer],  # Full-Stack Developer can communicate with QA Engineer
        [fullstack_dev, devops_engineer],  # Full-Stack Developer can communicate with DevOps Engineer
        [fullstack_dev, data_engineer],  # Full-Stack Developer can communicate with Data Engineer
        [mobile_dev, uiux_designer],  # Mobile Developer can communicate with UI/UX Designer
        [mobile_dev, qa_engineer],  # Mobile Developer can communicate with QA Engineer
        [mobile_dev, devops_engineer],  # Mobile Developer can communicate with DevOps Engineer
        [mobile_dev, data_engineer],  # Mobile Developer can communicate with Data Engineer
        [uiux_designer, qa_engineer],  # UI/UX Designer can communicate with QA Engineer
        [uiux_designer, devops_engineer],  # UI/UX Designer can communicate with DevOps Engineer
        [uiux_designer, data_engineer],  # UI/UX Designer can communicate with Data Engineer
        [qa_engineer, devops_engineer],  # QA Engineer can communicate with DevOps Engineer
        [qa_engineer, data_engineer],  # QA Engineer can communicate with Data Engineer
        [devops_engineer, data_engineer],  # DevOps Engineer can communicate with Data Engineer
    ],
    shared_instructions="agency_manifesto.md",
    temperature=0.5,
    max_prompt_tokens=25000
)

if __name__ == "__main__":
    agency.run_demo()  # Start the agency in terminal mode 