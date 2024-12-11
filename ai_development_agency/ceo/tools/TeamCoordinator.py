from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import Dict, List, Optional
import json

class TeamCoordinator(BaseTool):
    """
    A tool for coordinating team assignments, managing resources, and tracking project progress.
    This tool helps the CEO manage team dynamics and ensure efficient project execution.
    """
    
    action_type: str = Field(
        ...,
        description="Type of coordination action: 'assign_task', 'track_progress', 'resource_allocation', or 'performance_review'"
    )
    
    action_parameters: Dict = Field(
        ...,
        description="Parameters specific to the action type (e.g., task details, team member info, etc.)"
    )
    
    priority_level: Optional[str] = Field(
        "medium",
        description="Priority level of the action: 'high', 'medium', or 'low'"
    )

    def run(self) -> str:
        """
        Executes the specified coordination action and returns the result.
        """
        if self.action_type == "assign_task":
            return self._assign_task()
        elif self.action_type == "track_progress":
            return self._track_progress()
        elif self.action_type == "resource_allocation":
            return self._allocate_resources()
        elif self.action_type == "performance_review":
            return self._review_performance()
        else:
            return "Invalid action type specified"

    def _assign_task(self) -> str:
        task_details = self.action_parameters.get("task_details", {})
        assignee = self.action_parameters.get("assignee", "")
        
        assignment = {
            "task_id": self._generate_task_id(),
            "assignee": assignee,
            "task_details": task_details,
            "priority": self.priority_level,
            "status": "assigned",
            "timeline": self._calculate_task_timeline(task_details),
            "dependencies": self._identify_task_dependencies(task_details),
            "resources": self._allocate_task_resources(task_details)
        }
        
        return json.dumps(assignment, indent=2)

    def _track_progress(self) -> str:
        project_id = self.action_parameters.get("project_id", "")
        
        progress_report = {
            "project_id": project_id,
            "overall_progress": self._calculate_overall_progress(),
            "team_progress": self._get_team_progress(),
            "milestones": self._track_milestones(),
            "bottlenecks": self._identify_bottlenecks(),
            "recommendations": self._generate_progress_recommendations()
        }
        
        return json.dumps(progress_report, indent=2)

    def _allocate_resources(self) -> str:
        resource_request = self.action_parameters.get("resource_request", {})
        
        allocation = {
            "allocated_resources": self._process_resource_allocation(resource_request),
            "resource_conflicts": self._identify_resource_conflicts(),
            "optimization_suggestions": self._suggest_resource_optimization(),
            "timeline_impact": self._assess_timeline_impact()
        }
        
        return json.dumps(allocation, indent=2)

    def _review_performance(self) -> str:
        team_member = self.action_parameters.get("team_member", "")
        
        review = {
            "team_member": team_member,
            "performance_metrics": self._calculate_performance_metrics(),
            "achievements": self._list_achievements(),
            "areas_for_improvement": self._identify_improvement_areas(),
            "recommendations": self._generate_performance_recommendations()
        }
        
        return json.dumps(review, indent=2)

    def _generate_task_id(self) -> str:
        # Implementation for generating unique task IDs
        return "TASK-001"

    def _calculate_task_timeline(self, task_details: Dict) -> Dict:
        return {
            "estimated_duration": "2 weeks",
            "start_date": "2024-01-15",
            "end_date": "2024-01-29",
            "milestones": ["Design", "Implementation", "Testing"]
        }

    def _identify_task_dependencies(self, task_details: Dict) -> List[str]:
        return ["Database Setup", "API Development", "Frontend Components"]

    def _allocate_task_resources(self, task_details: Dict) -> Dict:
        return {
            "human_resources": ["Senior Developer", "UI Designer"],
            "technical_resources": ["Development Environment", "Testing Tools"],
            "infrastructure": ["Cloud Resources", "CI/CD Pipeline"]
        }

    def _calculate_overall_progress(self) -> Dict:
        return {
            "percentage_complete": 65,
            "tasks_completed": 12,
            "tasks_remaining": 8,
            "on_track": True
        }

    def _get_team_progress(self) -> Dict:
        return {
            "development": {"complete": 70, "status": "on_track"},
            "design": {"complete": 85, "status": "ahead"},
            "testing": {"complete": 40, "status": "delayed"}
        }

    def _track_milestones(self) -> List[Dict]:
        return [
            {"name": "Planning", "status": "completed", "date": "2024-01-10"},
            {"name": "Development", "status": "in_progress", "date": "2024-02-15"},
            {"name": "Testing", "status": "pending", "date": "2024-03-01"}
        ]

    def _identify_bottlenecks(self) -> List[Dict]:
        return [
            {"area": "Testing", "cause": "Resource constraint", "impact": "high"},
            {"area": "Integration", "cause": "Technical complexity", "impact": "medium"}
        ]

    def _generate_progress_recommendations(self) -> List[str]:
        return [
            "Allocate additional testing resources",
            "Implement automated testing procedures",
            "Schedule daily stand-up meetings",
            "Review and optimize integration process"
        ]

    def _process_resource_allocation(self, resource_request: Dict) -> Dict:
        return {
            "allocated": {
                "developers": 2,
                "designers": 1,
                "infrastructure": "medium_instance"
            },
            "availability": {
                "immediate": True,
                "duration": "3 months"
            }
        }

    def _identify_resource_conflicts(self) -> List[Dict]:
        return [
            {
                "resource": "Senior Developer",
                "conflict_type": "scheduling",
                "affected_projects": ["Project A", "Project B"]
            }
        ]

    def _suggest_resource_optimization(self) -> List[str]:
        return [
            "Implement resource sharing between teams",
            "Utilize cloud resources for scalability",
            "Consider outsourcing non-critical tasks"
        ]

    def _assess_timeline_impact(self) -> Dict:
        return {
            "delay_risk": "low",
            "affected_milestones": ["Testing Phase"],
            "mitigation_suggestions": ["Parallel testing implementation"]
        }

    def _calculate_performance_metrics(self) -> Dict:
        return {
            "productivity": 85,
            "code_quality": 90,
            "collaboration": 88,
            "timeline_adherence": 82
        }

    def _list_achievements(self) -> List[str]:
        return [
            "Completed critical feature ahead of schedule",
            "Improved team collaboration processes",
            "Implemented innovative solution for performance bottleneck"
        ]

    def _identify_improvement_areas(self) -> List[Dict]:
        return [
            {"area": "Documentation", "importance": "high", "impact": "medium"},
            {"area": "Code Reviews", "importance": "medium", "impact": "high"}
        ]

    def _generate_performance_recommendations(self) -> List[str]:
        return [
            "Attend advanced technical training",
            "Take lead in knowledge sharing sessions",
            "Improve documentation practices"
        ]


if __name__ == "__main__":
    # Test the TeamCoordinator tool
    test_parameters = {
        "task_details": {
            "name": "Implement Authentication System",
            "description": "Develop secure user authentication system",
            "requirements": ["OAuth2", "JWT", "Database Integration"],
            "priority": "high"
        },
        "assignee": "Senior Developer"
    }
    
    coordinator = TeamCoordinator(
        action_type="assign_task",
        action_parameters=test_parameters,
        priority_level="high"
    )
    
    print("Testing TeamCoordinator tool:")
    print(coordinator.run()) 