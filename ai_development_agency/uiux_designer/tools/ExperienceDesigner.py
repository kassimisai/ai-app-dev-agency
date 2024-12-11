from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import Dict, List, Optional
import json

class ExperienceDesigner(BaseTool):
    """
    A tool for designing user experiences, information architecture,
    and interaction patterns.
    """
    
    design_spec: Dict = Field(
        ...,
        description="Design specifications including user requirements, goals, and constraints"
    )
    
    design_type: str = Field(
        ...,
        description="Type of design needed: 'research', 'architecture', 'interaction', or 'testing'"
    )
    
    platform: Optional[str] = Field(
        "web",
        description="Target platform: 'web', 'mobile', or 'desktop'"
    )

    def run(self) -> str:
        """
        Designs user experiences based on the specified parameters.
        """
        if self.design_type == "research":
            return self._conduct_research()
        elif self.design_type == "architecture":
            return self._design_architecture()
        elif self.design_type == "interaction":
            return self._design_interactions()
        elif self.design_type == "testing":
            return self._design_testing()
        else:
            return "Invalid design type specified"

    def _conduct_research(self) -> str:
        research = {
            "user_research": self._conduct_user_research(),
            "personas": self._create_personas(),
            "journeys": self._map_user_journeys(),
            "requirements": self._analyze_requirements(),
            "insights": self._generate_insights()
        }
        
        return json.dumps(research, indent=2)

    def _design_architecture(self) -> str:
        architecture = {
            "information_structure": self._design_information_structure(),
            "navigation": self._design_navigation(),
            "user_flows": self._create_user_flows(),
            "content_strategy": self._define_content_strategy(),
            "wireframes": self._create_wireframes()
        }
        
        return json.dumps(architecture, indent=2)

    def _design_interactions(self) -> str:
        interactions = {
            "patterns": self._define_interaction_patterns(),
            "behaviors": self._define_behaviors(),
            "feedback": self._design_feedback_system(),
            "animations": self._design_animations(),
            "gestures": self._define_gestures()
        }
        
        return json.dumps(interactions, indent=2)

    def _design_testing(self) -> str:
        testing = {
            "test_plan": self._create_test_plan(),
            "scenarios": self._define_test_scenarios(),
            "metrics": self._define_metrics(),
            "methodology": self._define_methodology(),
            "analysis": self._define_analysis_approach()
        }
        
        return json.dumps(testing, indent=2)

    def _conduct_user_research(self) -> Dict:
        return {
            "methods": [
                "User Interviews",
                "Surveys",
                "Analytics Analysis",
                "Competitor Analysis"
            ],
            "target_users": {
                "primary": "Core user group",
                "secondary": "Occasional users",
                "tertiary": "Administrative users"
            },
            "research_goals": [
                "Understand user needs",
                "Identify pain points",
                "Discover opportunities",
                "Validate assumptions"
            ]
        }

    def _create_personas(self) -> List[Dict]:
        return [
            {
                "name": "Primary Persona",
                "demographics": {
                    "age": "25-34",
                    "occupation": "Professional",
                    "tech_savvy": "High"
                },
                "goals": [
                    "Efficiency in tasks",
                    "Easy navigation",
                    "Quick access to features"
                ],
                "pain_points": [
                    "Complex workflows",
                    "Slow performance",
                    "Unclear feedback"
                ]
            },
            {
                "name": "Secondary Persona",
                "demographics": {
                    "age": "35-50",
                    "occupation": "Manager",
                    "tech_savvy": "Medium"
                },
                "goals": [
                    "Overview of operations",
                    "Team management",
                    "Report generation"
                ],
                "pain_points": [
                    "Limited visibility",
                    "Complex reporting",
                    "Team coordination"
                ]
            }
        ]

    def _map_user_journeys(self) -> List[Dict]:
        return [
            {
                "journey_name": "New User Onboarding",
                "stages": [
                    {
                        "name": "Discovery",
                        "touchpoints": ["Website", "App Store"],
                        "actions": ["Search", "Read Reviews"],
                        "emotions": ["Curious", "Skeptical"]
                    },
                    {
                        "name": "First Use",
                        "touchpoints": ["App", "Tutorial"],
                        "actions": ["Sign Up", "Complete Tutorial"],
                        "emotions": ["Excited", "Sometimes Confused"]
                    }
                ]
            },
            {
                "journey_name": "Daily Usage",
                "stages": [
                    {
                        "name": "Task Initiation",
                        "touchpoints": ["Dashboard", "Quick Actions"],
                        "actions": ["Login", "Select Task"],
                        "emotions": ["Focused", "Goal-oriented"]
                    },
                    {
                        "name": "Task Completion",
                        "touchpoints": ["Task Interface", "Confirmation"],
                        "actions": ["Execute Task", "Review Results"],
                        "emotions": ["Satisfied", "Accomplished"]
                    }
                ]
            }
        ]

    def _analyze_requirements(self) -> Dict:
        return {
            "functional": [
                "User authentication",
                "Data management",
                "Real-time updates",
                "File handling"
            ],
            "non_functional": {
                "performance": "Load time < 3s",
                "accessibility": "WCAG 2.1 AA",
                "usability": "Task completion < 3 steps"
            },
            "constraints": {
                "technical": ["Browser support", "Device compatibility"],
                "business": ["Time to market", "Development resources"]
            }
        }

    def _generate_insights(self) -> Dict:
        return {
            "key_findings": [
                "Users prefer simplified workflows",
                "Mobile access is crucial",
                "Real-time feedback is essential"
            ],
            "opportunities": [
                "Streamline onboarding process",
                "Enhance mobile experience",
                "Implement smart defaults"
            ],
            "recommendations": [
                "Redesign main navigation",
                "Add progress indicators",
                "Improve error messaging"
            ]
        }

    def _design_information_structure(self) -> Dict:
        return {
            "hierarchy": {
                "primary": ["Dashboard", "Projects", "Reports"],
                "secondary": ["Settings", "Profile", "Help"],
                "tertiary": ["Admin", "Analytics", "Archive"]
            },
            "organization": {
                "method": "Task-based",
                "grouping": "User role",
                "labeling": "Clear and concise"
            },
            "relationships": {
                "parent_child": True,
                "cross_references": True,
                "contextual": True
            }
        }

    def _design_navigation(self) -> Dict:
        return {
            "primary_nav": {
                "type": "Top navigation",
                "items": ["Home", "Features", "Reports"],
                "behavior": "Sticky"
            },
            "secondary_nav": {
                "type": "Sidebar",
                "items": ["Settings", "Profile", "Help"],
                "behavior": "Collapsible"
            },
            "mobile_nav": {
                "type": "Bottom tabs",
                "items": ["Home", "Search", "Profile"],
                "behavior": "Fixed"
            }
        }

    def _create_user_flows(self) -> List[Dict]:
        return [
            {
                "flow_name": "User Registration",
                "steps": [
                    {
                        "step": 1,
                        "action": "Enter email",
                        "validation": "Email format",
                        "next": "Step 2"
                    },
                    {
                        "step": 2,
                        "action": "Create password",
                        "validation": "Password strength",
                        "next": "Step 3"
                    }
                ]
            },
            {
                "flow_name": "Content Creation",
                "steps": [
                    {
                        "step": 1,
                        "action": "Select template",
                        "options": ["Blank", "Pre-filled"],
                        "next": "Step 2"
                    },
                    {
                        "step": 2,
                        "action": "Add content",
                        "tools": ["Text editor", "Media upload"],
                        "next": "Step 3"
                    }
                ]
            }
        ]

    def _define_content_strategy(self) -> Dict:
        return {
            "content_types": {
                "text": ["Headers", "Body", "Labels"],
                "media": ["Images", "Videos", "Icons"],
                "data": ["Tables", "Charts", "Lists"]
            },
            "tone_voice": {
                "style": "Professional yet friendly",
                "language": "Clear and concise",
                "terminology": "Industry-standard"
            },
            "content_hierarchy": {
                "primary": "Key actions and information",
                "secondary": "Supporting content",
                "tertiary": "Additional details"
            }
        }

    def _create_wireframes(self) -> Dict:
        return {
            "layouts": {
                "desktop": {
                    "grid": "12-column",
                    "breakpoints": ["1200px", "992px", "768px"]
                },
                "mobile": {
                    "grid": "4-column",
                    "breakpoints": ["576px", "375px"]
                }
            },
            "components": {
                "navigation": ["Header", "Sidebar", "Footer"],
                "content": ["Cards", "Lists", "Forms"],
                "feedback": ["Alerts", "Modals", "Toasts"]
            }
        }

    def _define_interaction_patterns(self) -> Dict:
        return {
            "navigation": {
                "patterns": ["Breadcrumbs", "Tabs", "Dropdown"],
                "behavior": "Consistent across sections"
            },
            "forms": {
                "patterns": ["Inline validation", "Smart defaults"],
                "behavior": "Progressive disclosure"
            },
            "feedback": {
                "patterns": ["Loading states", "Success/Error"],
                "behavior": "Immediate response"
            }
        }

    def _define_behaviors(self) -> Dict:
        return {
            "input": {
                "keyboard": ["Shortcuts", "Tab order"],
                "mouse": ["Hover states", "Click actions"],
                "touch": ["Swipe", "Pinch", "Tap"]
            },
            "system": {
                "loading": ["Progressive", "Skeleton"],
                "errors": ["Inline", "Modal", "Toast"],
                "success": ["Confirmation", "Animation"]
            }
        }

    def _design_feedback_system(self) -> Dict:
        return {
            "visual": {
                "states": ["Hover", "Active", "Disabled"],
                "indicators": ["Progress", "Loading", "Success"]
            },
            "messaging": {
                "types": ["Info", "Warning", "Error"],
                "placement": ["Inline", "Toast", "Modal"]
            }
        }

    def _design_animations(self) -> Dict:
        return {
            "transitions": {
                "page": "Fade",
                "modal": "Scale",
                "list": "Slide"
            },
            "microinteractions": {
                "buttons": "Ripple effect",
                "inputs": "Focus highlight",
                "loading": "Spinner"
            }
        }

    def _define_gestures(self) -> Dict:
        return {
            "touch": {
                "tap": "Primary action",
                "double_tap": "Zoom",
                "long_press": "Context menu"
            },
            "swipe": {
                "horizontal": "Navigation",
                "vertical": "Scroll",
                "diagonal": "Close"
            }
        }

    def _create_test_plan(self) -> Dict:
        return {
            "objectives": [
                "Validate navigation structure",
                "Test task completion",
                "Assess learnability"
            ],
            "methods": [
                "Usability testing",
                "A/B testing",
                "Analytics tracking"
            ],
            "participants": {
                "number": 10,
                "criteria": ["Experience level", "Age group"]
            }
        }

    def _define_test_scenarios(self) -> List[Dict]:
        return [
            {
                "scenario": "New User Registration",
                "tasks": [
                    "Find sign up button",
                    "Complete registration form",
                    "Verify email"
                ],
                "success_criteria": [
                    "Complete within 3 minutes",
                    "No major errors"
                ]
            },
            {
                "scenario": "Content Creation",
                "tasks": [
                    "Create new item",
                    "Add content",
                    "Save and publish"
                ],
                "success_criteria": [
                    "Complete within 5 minutes",
                    "Content saved correctly"
                ]
            }
        ]

    def _define_metrics(self) -> Dict:
        return {
            "quantitative": {
                "task_success": "Completion rate",
                "efficiency": "Time on task",
                "errors": "Error rate"
            },
            "qualitative": {
                "satisfaction": "User feedback",
                "confidence": "Self-reported score",
                "comments": "User observations"
            }
        }

    def _define_methodology(self) -> Dict:
        return {
            "approach": "Mixed methods",
            "data_collection": [
                "Screen recording",
                "Think-aloud protocol",
                "Post-task surveys"
            ],
            "environment": {
                "setting": "Remote/In-person",
                "tools": ["Testing software", "Recording tools"]
            }
        }

    def _define_analysis_approach(self) -> Dict:
        return {
            "data_analysis": {
                "quantitative": ["Statistical analysis", "Metrics comparison"],
                "qualitative": ["Thematic analysis", "Pattern identification"]
            },
            "reporting": {
                "format": ["Executive summary", "Detailed report"],
                "components": ["Findings", "Recommendations", "Action items"]
            }
        }


if __name__ == "__main__":
    # Test the ExperienceDesigner tool
    test_spec = {
        "project": "E-commerce Platform",
        "target_users": {
            "primary": "Online shoppers",
            "secondary": "Store owners"
        },
        "goals": [
            "Improve conversion rate",
            "Enhance user engagement",
            "Streamline checkout process"
        ],
        "constraints": {
            "technical": ["Mobile-first", "Performance"],
            "business": ["Time to market", "Budget"]
        }
    }
    
    designer = ExperienceDesigner(
        design_spec=test_spec,
        design_type="research",
        platform="web"
    )
    
    print("Testing ExperienceDesigner tool:")
    print(designer.run()) 