from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import Dict, List, Optional
import json

class InfrastructureManager(BaseTool):
    """
    A tool for managing cloud infrastructure, deployments,
    and infrastructure as code.
    """
    
    infra_config: Dict = Field(
        ...,
        description="Infrastructure configuration including cloud provider, resources, and requirements"
    )
    
    operation_type: str = Field(
        ...,
        description="Type of operation: 'provision', 'deploy', 'monitor', or 'maintain'"
    )
    
    environment: Optional[str] = Field(
        "development",
        description="Target environment: 'development', 'staging', or 'production'"
    )

    def run(self) -> str:
        """
        Manages infrastructure operations based on the specified parameters.
        """
        if self.operation_type == "provision":
            return self._provision_infrastructure()
        elif self.operation_type == "deploy":
            return self._deploy_application()
        elif self.operation_type == "monitor":
            return self._monitor_infrastructure()
        elif self.operation_type == "maintain":
            return self._maintain_infrastructure()
        else:
            return "Invalid operation type specified"

    def _provision_infrastructure(self) -> str:
        infrastructure = {
            "cloud_resources": self._provision_cloud_resources(),
            "network": self._configure_network(),
            "security": self._configure_security(),
            "monitoring": self._setup_monitoring()
        }
        
        return json.dumps(infrastructure, indent=2)

    def _deploy_application(self) -> str:
        deployment = {
            "containers": self._deploy_containers(),
            "services": self._configure_services(),
            "routing": self._configure_routing(),
            "scaling": self._configure_scaling()
        }
        
        return json.dumps(deployment, indent=2)

    def _monitor_infrastructure(self) -> str:
        monitoring = {
            "metrics": self._collect_metrics(),
            "logs": self._aggregate_logs(),
            "alerts": self._configure_alerts(),
            "dashboards": self._create_dashboards()
        }
        
        return json.dumps(monitoring, indent=2)

    def _maintain_infrastructure(self) -> str:
        maintenance = {
            "updates": self._apply_updates(),
            "backups": self._manage_backups(),
            "optimization": self._optimize_resources(),
            "cleanup": self._perform_cleanup()
        }
        
        return json.dumps(maintenance, indent=2)

    def _provision_cloud_resources(self) -> Dict:
        return {
            "compute": {
                "type": "kubernetes",
                "clusters": [
                    {
                        "name": f"{self.environment}-cluster",
                        "version": "1.25",
                        "node_pools": [
                            {
                                "name": "general-purpose",
                                "machine_type": "n2-standard-4",
                                "min_nodes": 3,
                                "max_nodes": 10
                            },
                            {
                                "name": "gpu-pool",
                                "machine_type": "n1-standard-8",
                                "accelerator": "nvidia-tesla-t4",
                                "min_nodes": 0,
                                "max_nodes": 4
                            }
                        ]
                    }
                ]
            },
            "storage": {
                "block_storage": {
                    "type": "ssd",
                    "size": "500GB",
                    "iops": 3000
                },
                "object_storage": {
                    "type": "s3",
                    "buckets": ["artifacts", "backups", "media"]
                }
            },
            "database": {
                "type": "managed-postgres",
                "version": "14",
                "size": "db-custom-8-32768",
                "ha": True,
                "backup": {
                    "enabled": True,
                    "retention_days": 7
                }
            }
        }

    def _configure_network(self) -> Dict:
        return {
            "vpc": {
                "name": f"{self.environment}-vpc",
                "cidr": "10.0.0.0/16",
                "subnets": [
                    {
                        "name": "public-1",
                        "cidr": "10.0.1.0/24",
                        "zone": "us-east1-b"
                    },
                    {
                        "name": "private-1",
                        "cidr": "10.0.2.0/24",
                        "zone": "us-east1-c"
                    }
                ]
            },
            "security_groups": [
                {
                    "name": "web-tier",
                    "ingress": [
                        {"port": 80, "source": "0.0.0.0/0"},
                        {"port": 443, "source": "0.0.0.0/0"}
                    ]
                },
                {
                    "name": "app-tier",
                    "ingress": [
                        {"port": 8080, "source": "10.0.1.0/24"}
                    ]
                }
            ],
            "load_balancer": {
                "type": "application",
                "ssl": True,
                "cdn": True
            }
        }

    def _configure_security(self) -> Dict:
        return {
            "iam": {
                "roles": [
                    {
                        "name": "service-account",
                        "permissions": [
                            "storage.objects.get",
                            "logging.write",
                            "monitoring.write"
                        ]
                    }
                ],
                "service_accounts": [
                    {
                        "name": "app-service",
                        "roles": ["service-account"]
                    }
                ]
            },
            "encryption": {
                "at_rest": True,
                "in_transit": True,
                "key_management": "cloud-kms"
            },
            "network_policies": {
                "enabled": True,
                "default_deny": True,
                "allowed_ingress": [
                    {"from": "web-tier", "to": "app-tier"}
                ]
            }
        }

    def _setup_monitoring(self) -> Dict:
        return {
            "metrics": {
                "cpu": True,
                "memory": True,
                "disk": True,
                "network": True
            },
            "logging": {
                "application": True,
                "system": True,
                "audit": True,
                "retention_days": 30
            },
            "alerts": {
                "cpu_threshold": "80%",
                "memory_threshold": "85%",
                "disk_threshold": "90%",
                "error_rate": "1%"
            }
        }

    def _deploy_containers(self) -> List[Dict]:
        return [
            {
                "name": "web-frontend",
                "image": "frontend:latest",
                "replicas": 3,
                "resources": {
                    "cpu": "1",
                    "memory": "2Gi"
                },
                "health_check": {
                    "path": "/health",
                    "port": 80
                }
            },
            {
                "name": "api-backend",
                "image": "backend:latest",
                "replicas": 5,
                "resources": {
                    "cpu": "2",
                    "memory": "4Gi"
                },
                "health_check": {
                    "path": "/api/health",
                    "port": 8080
                }
            }
        ]

    def _configure_services(self) -> Dict:
        return {
            "frontend": {
                "type": "LoadBalancer",
                "ports": [
                    {"name": "http", "port": 80},
                    {"name": "https", "port": 443}
                ],
                "ssl": True
            },
            "backend": {
                "type": "ClusterIP",
                "ports": [
                    {"name": "http", "port": 8080}
                ]
            },
            "cache": {
                "type": "ClusterIP",
                "ports": [
                    {"name": "redis", "port": 6379}
                ]
            }
        }

    def _configure_routing(self) -> Dict:
        return {
            "ingress": {
                "class": "nginx",
                "ssl": True,
                "rules": [
                    {
                        "host": "app.example.com",
                        "http": {
                            "paths": [
                                {
                                    "path": "/",
                                    "service": "frontend"
                                },
                                {
                                    "path": "/api",
                                    "service": "backend"
                                }
                            ]
                        }
                    }
                ]
            },
            "service_mesh": {
                "enabled": True,
                "mtls": True,
                "tracing": True
            }
        }

    def _configure_scaling(self) -> Dict:
        return {
            "horizontal_pod_autoscaling": {
                "frontend": {
                    "min_replicas": 3,
                    "max_replicas": 10,
                    "target_cpu": "70%"
                },
                "backend": {
                    "min_replicas": 5,
                    "max_replicas": 15,
                    "target_cpu": "75%"
                }
            },
            "vertical_pod_autoscaling": {
                "enabled": True,
                "mode": "auto"
            }
        }

    def _collect_metrics(self) -> Dict:
        return {
            "system": {
                "cpu_usage": "45%",
                "memory_usage": "60%",
                "disk_usage": "55%",
                "network_io": "150MB/s"
            },
            "application": {
                "request_rate": "100 rps",
                "error_rate": "0.1%",
                "latency_p95": "200ms",
                "success_rate": "99.9%"
            }
        }

    def _aggregate_logs(self) -> Dict:
        return {
            "sources": {
                "application": True,
                "system": True,
                "security": True
            },
            "storage": {
                "type": "elasticsearch",
                "retention": "30d"
            },
            "analysis": {
                "enabled": True,
                "anomaly_detection": True
            }
        }

    def _configure_alerts(self) -> List[Dict]:
        return [
            {
                "name": "High CPU Usage",
                "condition": "CPU > 80% for 5m",
                "severity": "warning",
                "notification": ["email", "slack"]
            },
            {
                "name": "Service Down",
                "condition": "uptime < 99.9% for 5m",
                "severity": "critical",
                "notification": ["email", "slack", "pager"]
            }
        ]

    def _create_dashboards(self) -> List[Dict]:
        return [
            {
                "name": "System Overview",
                "panels": [
                    "CPU Usage",
                    "Memory Usage",
                    "Disk Usage",
                    "Network IO"
                ]
            },
            {
                "name": "Application Performance",
                "panels": [
                    "Request Rate",
                    "Error Rate",
                    "Latency",
                    "Success Rate"
                ]
            }
        ]

    def _apply_updates(self) -> Dict:
        return {
            "system_updates": {
                "security_patches": True,
                "os_updates": True,
                "scheduled": "weekly"
            },
            "application_updates": {
                "rolling_updates": True,
                "canary_deployments": True
            }
        }

    def _manage_backups(self) -> Dict:
        return {
            "database": {
                "type": "full",
                "frequency": "daily",
                "retention": "30d"
            },
            "files": {
                "type": "incremental",
                "frequency": "hourly",
                "retention": "7d"
            }
        }

    def _optimize_resources(self) -> Dict:
        return {
            "cost_optimization": {
                "idle_resources": "identified",
                "right_sizing": "recommended",
                "reserved_instances": "evaluated"
            },
            "performance_optimization": {
                "caching": "configured",
                "compression": "enabled",
                "query_optimization": "applied"
            }
        }

    def _perform_cleanup(self) -> Dict:
        return {
            "containers": {
                "unused_images": "removed",
                "dangling_volumes": "cleaned"
            },
            "storage": {
                "old_backups": "deleted",
                "temporary_files": "cleaned"
            }
        }


if __name__ == "__main__":
    # Test the InfrastructureManager tool
    infra_config = {
        "cloud_provider": "gcp",
        "region": "us-east1",
        "project": "ai-development-agency",
        "requirements": {
            "high_availability": True,
            "auto_scaling": True,
            "monitoring": True
        }
    }
    
    manager = InfrastructureManager(
        infra_config=infra_config,
        operation_type="provision",
        environment="development"
    )
    
    print("Testing InfrastructureManager tool:")
    print(manager.run()) 