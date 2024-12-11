from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import Dict, List
import json

class ProjectAnalyzer(BaseTool):
    """
    A tool for analyzing project requirements, assessing feasibility, and generating project plans.
    This tool helps the CEO evaluate new projects and create comprehensive project strategies.
    """
    
    project_requirements: Dict = Field(
        ...,
        description="Dictionary containing project requirements including technical specs, timeline, and budget"
    )
    
    analysis_type: str = Field(
        ...,
        description="Type of analysis to perform: 'feasibility', 'resource_planning', or 'risk_assessment'"
    )

    def run(self) -> str:
        """
        Analyzes project requirements and returns a detailed assessment based on the specified analysis type.
        """
        if self.analysis_type == "feasibility":
            return self._analyze_feasibility()
        elif self.analysis_type == "resource_planning":
            return self._analyze_resources()
        elif self.analysis_type == "risk_assessment":
            return self._analyze_risks()
        else:
            return "Invalid analysis type specified"

    def _analyze_feasibility(self) -> str:
        # Analyze technical feasibility
        tech_stack = self.project_requirements.get("tech_stack", {})
        timeline = self.project_requirements.get("timeline", {})
        budget = self.project_requirements.get("budget", {})

        feasibility_score = self._calculate_feasibility_score(tech_stack, timeline, budget)
        
        analysis_result = {
            "feasibility_score": feasibility_score,
            "technical_assessment": self._assess_technical_requirements(tech_stack),
            "timeline_assessment": self._assess_timeline(timeline),
            "budget_assessment": self._assess_budget(budget),
            "recommendations": self._generate_recommendations()
        }
        
        return json.dumps(analysis_result, indent=2)

    def _analyze_resources(self) -> str:
        resources = {
            "development_team": self._calculate_team_requirements(),
            "infrastructure": self._calculate_infrastructure_needs(),
            "timeline": self._generate_timeline(),
            "cost_estimation": self._estimate_costs()
        }
        
        return json.dumps(resources, indent=2)

    def _analyze_risks(self) -> str:
        risks = {
            "technical_risks": self._identify_technical_risks(),
            "timeline_risks": self._identify_timeline_risks(),
            "budget_risks": self._identify_budget_risks(),
            "mitigation_strategies": self._generate_risk_mitigation_strategies()
        }
        
        return json.dumps(risks, indent=2)

    def _calculate_feasibility_score(self, tech_stack: Dict, timeline: Dict, budget: Dict) -> float:
        # Implement scoring logic based on project parameters
        technical_score = self._evaluate_technical_complexity(tech_stack)
        timeline_score = self._evaluate_timeline_feasibility(timeline)
        budget_score = self._evaluate_budget_feasibility(budget)
        
        return (technical_score + timeline_score + budget_score) / 3

    def _assess_technical_requirements(self, tech_stack: Dict) -> Dict:
        return {
            "complexity_level": self._evaluate_technical_complexity(tech_stack),
            "required_expertise": self._identify_required_expertise(tech_stack),
            "potential_challenges": self._identify_technical_challenges(tech_stack)
        }

    def _assess_timeline(self, timeline: Dict) -> Dict:
        return {
            "estimated_duration": timeline.get("duration", "N/A"),
            "critical_path_elements": self._identify_critical_path(),
            "potential_delays": self._identify_potential_delays()
        }

    def _assess_budget(self, budget: Dict) -> Dict:
        return {
            "total_estimated_cost": budget.get("total", "N/A"),
            "cost_breakdown": self._generate_cost_breakdown(),
            "budget_risks": self._identify_budget_risks()
        }

    def _generate_recommendations(self) -> List[str]:
        return [
            "Implement agile development methodology",
            "Set up weekly progress tracking",
            "Establish clear communication channels",
            "Create detailed documentation requirements"
        ]

    def _calculate_team_requirements(self) -> Dict:
        return {
            "developers": {"senior": 2, "mid-level": 3, "junior": 1},
            "designers": {"ui_ux": 1, "graphic": 1},
            "qa_engineers": 2,
            "devops": 1
        }

    def _calculate_infrastructure_needs(self) -> Dict:
        return {
            "cloud_resources": ["compute_instances", "storage", "databases"],
            "development_tools": ["version_control", "ci_cd", "monitoring"],
            "testing_environment": ["staging", "qa", "production"]
        }

    def _generate_timeline(self) -> Dict:
        return {
            "planning_phase": "2 weeks",
            "development_phase": "12 weeks",
            "testing_phase": "4 weeks",
            "deployment_phase": "2 weeks"
        }

    def _estimate_costs(self) -> Dict:
        return {
            "personnel": 120000,
            "infrastructure": 15000,
            "tools_and_licenses": 5000,
            "contingency": 20000
        }

    def _identify_technical_risks(self) -> List[str]:
        return [
            "Integration complexity with existing systems",
            "Performance scalability challenges",
            "Security vulnerabilities",
            "Technical debt accumulation"
        ]

    def _identify_timeline_risks(self) -> List[str]:
        return [
            "Resource availability constraints",
            "Scope creep",
            "Technical challenges",
            "External dependencies"
        ]

    def _identify_budget_risks(self) -> List[str]:
        return [
            "Unexpected technical complications",
            "Resource cost variations",
            "Timeline extensions",
            "Additional infrastructure requirements"
        ]

    def _generate_risk_mitigation_strategies(self) -> Dict[str, List[str]]:
        return {
            "technical": [
                "Regular architecture reviews",
                "Continuous integration testing",
                "Security audits"
            ],
            "timeline": [
                "Buffer time allocation",
                "Regular progress monitoring",
                "Clear milestone definitions"
            ],
            "budget": [
                "Contingency fund allocation",
                "Regular budget reviews",
                "Phased development approach"
            ]
        }

    def _evaluate_technical_complexity(self, tech_stack: Dict) -> float:
        # Implement complexity scoring logic
        return 0.75

    def _evaluate_timeline_feasibility(self, timeline: Dict) -> float:
        # Implement timeline feasibility scoring logic
        return 0.8

    def _evaluate_budget_feasibility(self, budget: Dict) -> float:
        # Implement budget feasibility scoring logic
        return 0.85

    def _identify_required_expertise(self, tech_stack: Dict) -> List[str]:
        return ["AI/ML", "Full-stack development", "DevOps", "Cloud architecture"]

    def _identify_technical_challenges(self, tech_stack: Dict) -> List[str]:
        return ["System integration", "Scalability", "Performance optimization"]

    def _identify_critical_path(self) -> List[str]:
        return ["Architecture design", "Core feature development", "Integration testing"]

    def _identify_potential_delays(self) -> List[str]:
        return ["Resource allocation", "Technical challenges", "External dependencies"]

    def _generate_cost_breakdown(self) -> Dict:
        return {
            "development": "60%",
            "testing": "20%",
            "deployment": "10%",
            "maintenance": "10%"
        }


if __name__ == "__main__":
    # Test the ProjectAnalyzer tool
    test_requirements = {
        "tech_stack": {
            "frontend": ["React", "TypeScript"],
            "backend": ["Python", "FastAPI"],
            "database": ["PostgreSQL"],
            "ai_ml": ["TensorFlow", "PyTorch"]
        },
        "timeline": {
            "duration": "6 months",
            "milestones": ["Planning", "Development", "Testing", "Deployment"]
        },
        "budget": {
            "total": 150000,
            "breakdown": {
                "development": 90000,
                "infrastructure": 30000,
                "contingency": 30000
            }
        }
    }
    
    analyzer = ProjectAnalyzer(
        project_requirements=test_requirements,
        analysis_type="feasibility"
    )
    
    print("Testing ProjectAnalyzer tool:")
    print(analyzer.run()) 