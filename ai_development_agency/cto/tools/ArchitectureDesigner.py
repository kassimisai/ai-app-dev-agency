from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import Dict, List, Optional
import json

class ArchitectureDesigner(BaseTool):
    """
    A tool for designing and validating system architectures, ensuring scalability,
    security, and proper integration of AI/ML components.
    """
    
    project_requirements: Dict = Field(
        ...,
        description="Project requirements including technical specs, scalability needs, and AI/ML components"
    )
    
    design_type: str = Field(
        ...,
        description="Type of architecture design: 'system', 'ai_integration', 'security', or 'infrastructure'"
    )
    
    scalability_level: Optional[str] = Field(
        "medium",
        description="Required scalability level: 'high', 'medium', or 'low'"
    )

    def run(self) -> str:
        """
        Generates architecture design and recommendations based on the specified parameters.
        """
        if self.design_type == "system":
            return self._design_system_architecture()
        elif self.design_type == "ai_integration":
            return self._design_ai_integration()
        elif self.design_type == "security":
            return self._design_security_architecture()
        elif self.design_type == "infrastructure":
            return self._design_infrastructure()
        else:
            return "Invalid design type specified"

    def _design_system_architecture(self) -> str:
        architecture = {
            "system_components": self._define_system_components(),
            "component_interactions": self._define_component_interactions(),
            "data_flow": self._define_data_flow(),
            "scalability_design": self._design_scalability_measures(),
            "technical_stack": self._recommend_tech_stack(),
            "deployment_strategy": self._define_deployment_strategy()
        }
        
        return json.dumps(architecture, indent=2)

    def _design_ai_integration(self) -> str:
        ai_architecture = {
            "ai_components": self._define_ai_components(),
            "model_deployment": self._design_model_deployment(),
            "data_pipeline": self._design_data_pipeline(),
            "integration_points": self._define_integration_points(),
            "performance_optimization": self._design_performance_optimization(),
            "monitoring_strategy": self._define_ai_monitoring()
        }
        
        return json.dumps(ai_architecture, indent=2)

    def _design_security_architecture(self) -> str:
        security = {
            "security_layers": self._define_security_layers(),
            "authentication": self._design_authentication_system(),
            "authorization": self._design_authorization_system(),
            "data_protection": self._define_data_protection(),
            "security_monitoring": self._design_security_monitoring(),
            "compliance_measures": self._define_compliance_measures()
        }
        
        return json.dumps(security, indent=2)

    def _design_infrastructure(self) -> str:
        infrastructure = {
            "cloud_architecture": self._design_cloud_infrastructure(),
            "networking": self._design_network_architecture(),
            "storage_solutions": self._design_storage_solutions(),
            "scaling_strategy": self._define_scaling_strategy(),
            "disaster_recovery": self._design_disaster_recovery(),
            "monitoring_setup": self._design_monitoring_system()
        }
        
        return json.dumps(infrastructure, indent=2)

    def _define_system_components(self) -> List[Dict]:
        return [
            {
                "name": "Frontend Application",
                "type": "Web/Mobile Interface",
                "technology": "React/Flutter",
                "responsibilities": ["User Interface", "State Management", "API Integration"]
            },
            {
                "name": "Backend API",
                "type": "REST/GraphQL API",
                "technology": "FastAPI/Node.js",
                "responsibilities": ["Business Logic", "Data Processing", "Authentication"]
            },
            {
                "name": "AI Service",
                "type": "Machine Learning Service",
                "technology": "Python/TensorFlow",
                "responsibilities": ["Model Inference", "Data Processing", "API Endpoints"]
            },
            {
                "name": "Database Layer",
                "type": "Data Storage",
                "technology": "PostgreSQL/MongoDB",
                "responsibilities": ["Data Storage", "Query Processing", "Data Integrity"]
            }
        ]

    def _define_component_interactions(self) -> List[Dict]:
        return [
            {
                "from": "Frontend",
                "to": "Backend API",
                "protocol": "HTTPS/WSS",
                "data_format": "JSON/Protocol Buffers"
            },
            {
                "from": "Backend API",
                "to": "AI Service",
                "protocol": "gRPC",
                "data_format": "Protocol Buffers"
            },
            {
                "from": "AI Service",
                "to": "Database",
                "protocol": "SQL/MongoDB Protocol",
                "data_format": "BSON/SQL"
            }
        ]

    def _define_data_flow(self) -> List[Dict]:
        return [
            {
                "stage": "Data Input",
                "components": ["Frontend", "API Gateway"],
                "data_type": "User Requests",
                "processing": "Validation & Transformation"
            },
            {
                "stage": "Business Logic",
                "components": ["Backend API", "AI Service"],
                "data_type": "Processed Data",
                "processing": "Business Rules & ML Inference"
            },
            {
                "stage": "Data Storage",
                "components": ["Database", "Cache"],
                "data_type": "Persistent Data",
                "processing": "CRUD Operations"
            }
        ]

    def _design_scalability_measures(self) -> Dict:
        return {
            "horizontal_scaling": {
                "components": ["API Servers", "AI Services"],
                "strategy": "Auto-scaling based on load"
            },
            "vertical_scaling": {
                "components": ["Database"],
                "strategy": "Resource allocation adjustment"
            },
            "caching": {
                "type": "Distributed Cache",
                "technology": "Redis",
                "strategy": "Read-heavy data caching"
            }
        }

    def _recommend_tech_stack(self) -> Dict:
        return {
            "frontend": {
                "framework": "React/Flutter",
                "state_management": "Redux/Provider",
                "ui_components": "Material-UI"
            },
            "backend": {
                "framework": "FastAPI",
                "runtime": "Python 3.9+",
                "api_spec": "OpenAPI 3.0"
            },
            "ai_ml": {
                "framework": "TensorFlow/PyTorch",
                "deployment": "TensorFlow Serving",
                "optimization": "ONNX Runtime"
            },
            "database": {
                "primary": "PostgreSQL",
                "cache": "Redis",
                "analytics": "ClickHouse"
            }
        }

    def _define_deployment_strategy(self) -> Dict:
        return {
            "containerization": {
                "technology": "Docker",
                "orchestration": "Kubernetes"
            },
            "ci_cd": {
                "pipeline": "GitHub Actions",
                "stages": ["Build", "Test", "Deploy"]
            },
            "environments": {
                "development": "Local K8s",
                "staging": "Cloud Dev Cluster",
                "production": "Cloud Prod Cluster"
            }
        }

    def _define_ai_components(self) -> List[Dict]:
        return [
            {
                "name": "Model Service",
                "type": "Inference API",
                "framework": "TensorFlow Serving",
                "scaling": "Horizontal"
            },
            {
                "name": "Feature Store",
                "type": "Feature Management",
                "technology": "Redis/Feast",
                "scaling": "Vertical"
            },
            {
                "name": "Model Monitor",
                "type": "Performance Monitoring",
                "technology": "Prometheus/Grafana",
                "scaling": "Horizontal"
            }
        ]

    def _design_model_deployment(self) -> Dict:
        return {
            "serving_platform": "TensorFlow Serving",
            "deployment_strategy": "Blue-Green",
            "scaling_policy": "CPU/Memory based",
            "version_control": "Model Registry"
        }

    def _design_data_pipeline(self) -> Dict:
        return {
            "ingestion": "Apache Kafka",
            "processing": "Apache Spark",
            "storage": "Delta Lake",
            "monitoring": "Apache Airflow"
        }

    def _define_integration_points(self) -> List[Dict]:
        return [
            {
                "component": "API Gateway",
                "integration_type": "REST/gRPC",
                "security": "OAuth2/JWT"
            },
            {
                "component": "Feature Store",
                "integration_type": "SDK",
                "security": "API Key"
            },
            {
                "component": "Model Monitor",
                "integration_type": "Metrics API",
                "security": "mTLS"
            }
        ]

    def _design_performance_optimization(self) -> Dict:
        return {
            "model_optimization": {
                "quantization": "INT8",
                "pruning": "Magnitude-based",
                "caching": "Feature Cache"
            },
            "inference_optimization": {
                "batch_processing": "Dynamic Batching",
                "hardware_acceleration": "GPU Support",
                "caching": "Prediction Cache"
            }
        }

    def _define_ai_monitoring(self) -> Dict:
        return {
            "metrics": ["Accuracy", "Latency", "Throughput"],
            "alerts": ["Drift Detection", "Performance Degradation"],
            "logging": ["Prediction Logs", "Error Logs"],
            "dashboards": ["Performance", "Quality", "Usage"]
        }

    def _define_security_layers(self) -> List[Dict]:
        return [
            {
                "layer": "Network",
                "components": ["Firewall", "WAF", "DDoS Protection"]
            },
            {
                "layer": "Application",
                "components": ["Authentication", "Authorization", "Input Validation"]
            },
            {
                "layer": "Data",
                "components": ["Encryption", "Access Control", "Audit Logging"]
            }
        ]

    def _design_authentication_system(self) -> Dict:
        return {
            "providers": ["OAuth2", "OIDC"],
            "mfa": "TOTP-based",
            "session_management": "JWT with Redis",
            "password_policy": "NIST Guidelines"
        }

    def _design_authorization_system(self) -> Dict:
        return {
            "model": "RBAC/ABAC",
            "policies": "OPA",
            "enforcement": "API Gateway/Service Mesh",
            "audit": "Detailed Logging"
        }

    def _define_data_protection(self) -> Dict:
        return {
            "encryption": {
                "at_rest": "AES-256",
                "in_transit": "TLS 1.3",
                "key_management": "KMS"
            },
            "backup": {
                "strategy": "Incremental",
                "retention": "30 days",
                "encryption": "Client-side"
            }
        }

    def _design_security_monitoring(self) -> Dict:
        return {
            "siem": "ELK Stack",
            "ids_ips": "Suricata",
            "vulnerability_scanning": "Nessus",
            "compliance_monitoring": "AWS Config"
        }

    def _define_compliance_measures(self) -> Dict:
        return {
            "standards": ["SOC2", "GDPR", "HIPAA"],
            "controls": ["Access Control", "Audit Logging", "Encryption"],
            "documentation": ["Policies", "Procedures", "Training"],
            "auditing": ["Internal", "External", "Continuous"]
        }

    def _design_cloud_infrastructure(self) -> Dict:
        return {
            "provider": "AWS/GCP",
            "compute": ["EKS/GKE", "Lambda/Cloud Functions"],
            "storage": ["S3/GCS", "RDS/Cloud SQL"],
            "networking": ["VPC", "CloudFront/Cloud CDN"]
        }

    def _design_network_architecture(self) -> Dict:
        return {
            "topology": "Hub-and-Spoke",
            "segmentation": ["Public", "Private", "Data"],
            "connectivity": ["VPN", "Direct Connect"],
            "security": ["NACLs", "Security Groups"]
        }

    def _design_storage_solutions(self) -> Dict:
        return {
            "object_storage": "S3/GCS",
            "block_storage": "EBS/Persistent Disk",
            "file_storage": "EFS/Filestore",
            "database": ["RDS", "Cloud SQL"]
        }

    def _define_scaling_strategy(self) -> Dict:
        return {
            "auto_scaling": {
                "triggers": ["CPU", "Memory", "Custom Metrics"],
                "policies": ["Target Tracking", "Step Scaling"]
            },
            "load_balancing": {
                "type": "Application Load Balancer",
                "algorithm": "Least Outstanding Requests"
            }
        }

    def _design_disaster_recovery(self) -> Dict:
        return {
            "strategy": "Pilot Light",
            "rpo": "1 hour",
            "rto": "4 hours",
            "backup": "Cross-region replication"
        }

    def _design_monitoring_system(self) -> Dict:
        return {
            "metrics": ["CloudWatch/Stackdriver", "Prometheus"],
            "logging": ["CloudWatch Logs/Cloud Logging", "ELK Stack"],
            "tracing": ["X-Ray/Cloud Trace", "Jaeger"],
            "alerting": ["SNS/Cloud Pub/Sub", "PagerDuty"]
        }


if __name__ == "__main__":
    # Test the ArchitectureDesigner tool
    test_requirements = {
        "project_type": "AI-powered Web Application",
        "scale": "Medium to Large",
        "users": "100k monthly active users",
        "ai_components": ["Recommendation Engine", "Natural Language Processing"],
        "security_requirements": "SOC2 compliance",
        "performance_requirements": {
            "latency": "< 200ms",
            "availability": "99.9%"
        }
    }
    
    designer = ArchitectureDesigner(
        project_requirements=test_requirements,
        design_type="system",
        scalability_level="high"
    )
    
    print("Testing ArchitectureDesigner tool:")
    print(designer.run()) 