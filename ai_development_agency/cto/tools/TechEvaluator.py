from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import Dict, List, Optional
import json

class TechEvaluator(BaseTool):
    """
    A tool for evaluating and selecting technologies, frameworks, and tools
    based on project requirements and constraints.
    """
    
    evaluation_context: Dict = Field(
        ...,
        description="Context for evaluation including project requirements, constraints, and preferences"
    )
    
    evaluation_type: str = Field(
        ...,
        description="Type of evaluation: 'framework', 'database', 'cloud_service', 'ai_platform', or 'development_tool'"
    )
    
    comparison_criteria: Optional[List[str]] = Field(
        None,
        description="Specific criteria to focus on during evaluation"
    )

    def run(self) -> str:
        """
        Evaluates technologies based on the specified context and type.
        """
        if self.evaluation_type == "framework":
            return self._evaluate_frameworks()
        elif self.evaluation_type == "database":
            return self._evaluate_databases()
        elif self.evaluation_type == "cloud_service":
            return self._evaluate_cloud_services()
        elif self.evaluation_type == "ai_platform":
            return self._evaluate_ai_platforms()
        elif self.evaluation_type == "development_tool":
            return self._evaluate_development_tools()
        else:
            return "Invalid evaluation type specified"

    def _evaluate_frameworks(self) -> str:
        framework_evaluation = {
            "evaluated_frameworks": self._identify_relevant_frameworks(),
            "comparison_matrix": self._create_comparison_matrix(),
            "performance_analysis": self._analyze_performance_metrics(),
            "community_analysis": self._analyze_community_health(),
            "recommendation": self._generate_framework_recommendation()
        }
        
        return json.dumps(framework_evaluation, indent=2)

    def _evaluate_databases(self) -> str:
        database_evaluation = {
            "evaluated_databases": self._identify_relevant_databases(),
            "scalability_analysis": self._analyze_database_scalability(),
            "performance_metrics": self._analyze_database_performance(),
            "cost_analysis": self._analyze_database_costs(),
            "recommendation": self._generate_database_recommendation()
        }
        
        return json.dumps(database_evaluation, indent=2)

    def _evaluate_cloud_services(self) -> str:
        cloud_evaluation = {
            "evaluated_services": self._identify_relevant_cloud_services(),
            "feature_comparison": self._compare_cloud_features(),
            "pricing_analysis": self._analyze_cloud_pricing(),
            "reliability_metrics": self._analyze_cloud_reliability(),
            "recommendation": self._generate_cloud_recommendation()
        }
        
        return json.dumps(cloud_evaluation, indent=2)

    def _evaluate_ai_platforms(self) -> str:
        ai_evaluation = {
            "evaluated_platforms": self._identify_relevant_ai_platforms(),
            "capability_analysis": self._analyze_ai_capabilities(),
            "integration_assessment": self._assess_ai_integration(),
            "performance_benchmarks": self._analyze_ai_performance(),
            "recommendation": self._generate_ai_platform_recommendation()
        }
        
        return json.dumps(ai_evaluation, indent=2)

    def _evaluate_development_tools(self) -> str:
        tool_evaluation = {
            "evaluated_tools": self._identify_relevant_tools(),
            "feature_comparison": self._compare_tool_features(),
            "integration_analysis": self._analyze_tool_integration(),
            "team_impact": self._assess_team_impact(),
            "recommendation": self._generate_tool_recommendation()
        }
        
        return json.dumps(tool_evaluation, indent=2)

    def _identify_relevant_frameworks(self) -> List[Dict]:
        return [
            {
                "name": "React",
                "category": "Frontend",
                "version": "18.x",
                "key_features": ["Component-based", "Virtual DOM", "Large ecosystem"]
            },
            {
                "name": "FastAPI",
                "category": "Backend",
                "version": "0.100.x",
                "key_features": ["Async support", "Auto OpenAPI docs", "Type hints"]
            },
            {
                "name": "Flutter",
                "category": "Mobile",
                "version": "3.x",
                "key_features": ["Cross-platform", "Hot reload", "Rich widgets"]
            }
        ]

    def _create_comparison_matrix(self) -> Dict:
        return {
            "performance": {
                "React": 9,
                "FastAPI": 9.5,
                "Flutter": 8.5
            },
            "developer_experience": {
                "React": 9,
                "FastAPI": 9,
                "Flutter": 8
            },
            "community_support": {
                "React": 9.5,
                "FastAPI": 8,
                "Flutter": 8.5
            },
            "learning_curve": {
                "React": 7,
                "FastAPI": 8,
                "Flutter": 6
            }
        }

    def _analyze_performance_metrics(self) -> Dict:
        return {
            "load_time": {
                "React": "< 100ms",
                "FastAPI": "< 50ms",
                "Flutter": "< 150ms"
            },
            "memory_usage": {
                "React": "Moderate",
                "FastAPI": "Low",
                "Flutter": "Moderate"
            },
            "scalability": {
                "React": "High",
                "FastAPI": "Very High",
                "Flutter": "High"
            }
        }

    def _analyze_community_health(self) -> Dict:
        return {
            "github_metrics": {
                "stars": {"React": "200k+", "FastAPI": "60k+", "Flutter": "150k+"},
                "contributors": {"React": "1500+", "FastAPI": "300+", "Flutter": "1000+"},
                "issues": {"React": "Low", "FastAPI": "Low", "Flutter": "Medium"}
            },
            "package_metrics": {
                "downloads": {"React": "Millions", "FastAPI": "Millions", "Flutter": "Millions"},
                "release_frequency": {"React": "Regular", "FastAPI": "Regular", "Flutter": "Regular"}
            }
        }

    def _generate_framework_recommendation(self) -> Dict:
        return {
            "recommended_framework": "FastAPI",
            "reasoning": [
                "Best performance metrics",
                "Excellent developer experience",
                "Strong type safety",
                "Growing community support"
            ],
            "considerations": [
                "Team expertise required",
                "Integration complexity",
                "Learning curve for new developers"
            ]
        }

    def _identify_relevant_databases(self) -> List[Dict]:
        return [
            {
                "name": "PostgreSQL",
                "type": "Relational",
                "key_features": ["ACID", "JSON support", "Extensibility"]
            },
            {
                "name": "MongoDB",
                "type": "Document",
                "key_features": ["Scalability", "Flexibility", "Rich queries"]
            },
            {
                "name": "Redis",
                "type": "In-memory",
                "key_features": ["Speed", "Caching", "Data structures"]
            }
        ]

    def _analyze_database_scalability(self) -> Dict:
        return {
            "horizontal_scaling": {
                "PostgreSQL": "Good with replication",
                "MongoDB": "Excellent with sharding",
                "Redis": "Good with cluster mode"
            },
            "vertical_scaling": {
                "PostgreSQL": "Excellent",
                "MongoDB": "Good",
                "Redis": "Limited by memory"
            }
        }

    def _analyze_database_performance(self) -> Dict:
        return {
            "read_performance": {
                "PostgreSQL": "Very Good",
                "MongoDB": "Excellent",
                "Redis": "Outstanding"
            },
            "write_performance": {
                "PostgreSQL": "Good",
                "MongoDB": "Very Good",
                "Redis": "Outstanding"
            }
        }

    def _analyze_database_costs(self) -> Dict:
        return {
            "licensing": {
                "PostgreSQL": "Free",
                "MongoDB": "Community/Enterprise",
                "Redis": "Open Source/Enterprise"
            },
            "operational_costs": {
                "PostgreSQL": "Medium",
                "MongoDB": "Medium-High",
                "Redis": "Medium"
            }
        }

    def _generate_database_recommendation(self) -> Dict:
        return {
            "primary_database": "PostgreSQL",
            "caching_layer": "Redis",
            "reasoning": [
                "Strong ACID compliance",
                "Excellent JSON support",
                "Cost-effective",
                "Rich ecosystem"
            ]
        }

    def _identify_relevant_cloud_services(self) -> List[Dict]:
        return [
            {
                "provider": "AWS",
                "key_services": ["ECS", "RDS", "S3", "Lambda"],
                "strengths": ["Market leader", "Feature-rich", "Global presence"]
            },
            {
                "provider": "GCP",
                "key_services": ["GKE", "Cloud SQL", "Cloud Storage", "Cloud Functions"],
                "strengths": ["AI/ML focus", "Network performance", "Innovation"]
            }
        ]

    def _compare_cloud_features(self) -> Dict:
        return {
            "compute": {
                "AWS": ["EC2", "ECS", "Lambda"],
                "GCP": ["Compute Engine", "GKE", "Cloud Functions"]
            },
            "storage": {
                "AWS": ["S3", "EBS", "EFS"],
                "GCP": ["Cloud Storage", "Persistent Disk", "Filestore"]
            }
        }

    def _analyze_cloud_pricing(self) -> Dict:
        return {
            "compute_costs": {
                "AWS": "Pay per second",
                "GCP": "Pay per second with sustained use discounts"
            },
            "storage_costs": {
                "AWS": "Tiered pricing",
                "GCP": "Tiered pricing with automatic discounts"
            }
        }

    def _analyze_cloud_reliability(self) -> Dict:
        return {
            "uptime_sla": {
                "AWS": "99.99%",
                "GCP": "99.99%"
            },
            "global_presence": {
                "AWS": "25+ regions",
                "GCP": "20+ regions"
            }
        }

    def _generate_cloud_recommendation(self) -> Dict:
        return {
            "recommended_provider": "AWS",
            "reasoning": [
                "Comprehensive service offering",
                "Strong market presence",
                "Extensive documentation",
                "Rich ecosystem"
            ]
        }

    def _identify_relevant_ai_platforms(self) -> List[Dict]:
        return [
            {
                "name": "TensorFlow",
                "type": "ML Framework",
                "key_features": ["Production-ready", "TensorFlow Serving", "TPU support"]
            },
            {
                "name": "PyTorch",
                "type": "ML Framework",
                "key_features": ["Dynamic graphs", "Research-friendly", "TorchServe"]
            }
        ]

    def _analyze_ai_capabilities(self) -> Dict:
        return {
            "model_types": {
                "TensorFlow": ["CNN", "RNN", "Transformers"],
                "PyTorch": ["CNN", "RNN", "Transformers"]
            },
            "deployment_options": {
                "TensorFlow": ["TF Serving", "TF Lite", "TF.js"],
                "PyTorch": ["TorchServe", "ONNX", "Mobile"]
            }
        }

    def _assess_ai_integration(self) -> Dict:
        return {
            "ease_of_integration": {
                "TensorFlow": "Good",
                "PyTorch": "Very Good"
            },
            "deployment_complexity": {
                "TensorFlow": "Medium",
                "PyTorch": "Medium"
            }
        }

    def _analyze_ai_performance(self) -> Dict:
        return {
            "training_speed": {
                "TensorFlow": "Very Good",
                "PyTorch": "Excellent"
            },
            "inference_speed": {
                "TensorFlow": "Excellent",
                "PyTorch": "Very Good"
            }
        }

    def _generate_ai_platform_recommendation(self) -> Dict:
        return {
            "recommended_platform": "TensorFlow",
            "reasoning": [
                "Production-ready features",
                "Excellent deployment options",
                "Strong enterprise support",
                "Comprehensive ecosystem"
            ]
        }

    def _identify_relevant_tools(self) -> List[Dict]:
        return [
            {
                "category": "CI/CD",
                "tools": ["GitHub Actions", "Jenkins", "GitLab CI"],
                "key_features": ["Automation", "Integration", "Scalability"]
            },
            {
                "category": "Monitoring",
                "tools": ["Prometheus", "Grafana", "ELK Stack"],
                "key_features": ["Metrics", "Visualization", "Logging"]
            }
        ]

    def _compare_tool_features(self) -> Dict:
        return {
            "ci_cd": {
                "GitHub Actions": ["Cloud-native", "Easy setup", "GitHub integration"],
                "Jenkins": ["Self-hosted", "Customizable", "Plugin ecosystem"],
                "GitLab CI": ["Integrated", "Container-native", "Auto DevOps"]
            }
        }

    def _analyze_tool_integration(self) -> Dict:
        return {
            "integration_effort": {
                "GitHub Actions": "Low",
                "Jenkins": "High",
                "GitLab CI": "Medium"
            },
            "maintenance_overhead": {
                "GitHub Actions": "Low",
                "Jenkins": "High",
                "GitLab CI": "Medium"
            }
        }

    def _assess_team_impact(self) -> Dict:
        return {
            "learning_curve": {
                "GitHub Actions": "Low",
                "Jenkins": "High",
                "GitLab CI": "Medium"
            },
            "productivity_impact": {
                "GitHub Actions": "High",
                "Jenkins": "Medium",
                "GitLab CI": "High"
            }
        }

    def _generate_tool_recommendation(self) -> Dict:
        return {
            "recommended_tools": {
                "ci_cd": "GitHub Actions",
                "monitoring": "Prometheus + Grafana"
            },
            "reasoning": [
                "Easy integration",
                "Low maintenance overhead",
                "Strong community support",
                "Cost-effective"
            ]
        }


if __name__ == "__main__":
    # Test the TechEvaluator tool
    test_context = {
        "project_type": "AI-powered Web Application",
        "team_size": "Medium (10-20 developers)",
        "budget": "Medium",
        "scalability_requirements": "High",
        "performance_requirements": {
            "latency": "< 200ms",
            "throughput": "10k requests/second"
        },
        "security_requirements": "SOC2 compliance"
    }
    
    evaluator = TechEvaluator(
        evaluation_context=test_context,
        evaluation_type="framework",
        comparison_criteria=["performance", "scalability", "security"]
    )
    
    print("Testing TechEvaluator tool:")
    print(evaluator.run()) 