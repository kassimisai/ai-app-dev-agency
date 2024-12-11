from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import Dict, List, Optional
import json

class DataArchitect(BaseTool):
    """
    A tool for designing and managing data infrastructure,
    data models, and data flows.
    """
    
    architecture_config: Dict = Field(
        ...,
        description="Architecture configuration including data sources, models, and requirements"
    )
    
    design_type: str = Field(
        ...,
        description="Type of design: 'infrastructure', 'model', 'pipeline', or 'integration'"
    )
    
    environment: Optional[str] = Field(
        "development",
        description="Target environment: 'development', 'staging', or 'production'"
    )

    def run(self) -> str:
        """
        Designs and manages data architecture based on the specified parameters.
        """
        if self.design_type == "infrastructure":
            return self._design_infrastructure()
        elif self.design_type == "model":
            return self._design_data_model()
        elif self.design_type == "pipeline":
            return self._design_pipeline()
        elif self.design_type == "integration":
            return self._design_integration()
        else:
            return "Invalid design type specified"

    def _design_infrastructure(self) -> str:
        infrastructure = {
            "storage": self._design_storage_layer(),
            "processing": self._design_processing_layer(),
            "serving": self._design_serving_layer(),
            "security": self._design_security_layer()
        }
        
        return json.dumps(infrastructure, indent=2)

    def _design_data_model(self) -> str:
        model = {
            "schemas": self._define_schemas(),
            "relationships": self._define_relationships(),
            "validation": self._define_validation_rules(),
            "documentation": self._create_documentation()
        }
        
        return json.dumps(model, indent=2)

    def _design_pipeline(self) -> str:
        pipeline = {
            "ingestion": self._design_ingestion_layer(),
            "processing": self._design_transformation_layer(),
            "storage": self._design_persistence_layer(),
            "monitoring": self._design_monitoring_layer()
        }
        
        return json.dumps(pipeline, indent=2)

    def _design_integration(self) -> str:
        integration = {
            "connectors": self._design_connectors(),
            "apis": self._design_apis(),
            "sync": self._design_synchronization(),
            "monitoring": self._design_integration_monitoring()
        }
        
        return json.dumps(integration, indent=2)

    def _design_storage_layer(self) -> Dict:
        return {
            "data_warehouse": {
                "type": "snowflake",
                "configuration": {
                    "warehouses": [
                        {
                            "name": "transform_wh",
                            "size": "medium",
                            "auto_suspend": 300,
                            "auto_resume": True
                        },
                        {
                            "name": "serve_wh",
                            "size": "large",
                            "auto_suspend": 300,
                            "auto_resume": True
                        }
                    ],
                    "databases": [
                        {
                            "name": "raw_data",
                            "retention_time": 90
                        },
                        {
                            "name": "processed_data",
                            "retention_time": 365
                        }
                    ]
                }
            },
            "data_lake": {
                "type": "s3",
                "configuration": {
                    "buckets": [
                        {
                            "name": "raw-data",
                            "lifecycle_rules": {
                                "transition_glacier": 180,
                                "expiration": 365
                            }
                        },
                        {
                            "name": "processed-data",
                            "lifecycle_rules": {
                                "transition_glacier": 365,
                                "expiration": 730
                            }
                        }
                    ]
                }
            },
            "operational_db": {
                "type": "postgresql",
                "configuration": {
                    "version": "14",
                    "instance_type": "db.r6g.xlarge",
                    "storage": {
                        "type": "gp3",
                        "size": "500GB",
                        "iops": 3000
                    }
                }
            }
        }

    def _design_processing_layer(self) -> Dict:
        return {
            "batch_processing": {
                "engine": "spark",
                "configuration": {
                    "cluster_type": "emr",
                    "instance_type": "r5.2xlarge",
                    "min_nodes": 3,
                    "max_nodes": 10,
                    "auto_scaling": True
                }
            },
            "stream_processing": {
                "engine": "flink",
                "configuration": {
                    "parallelism": 4,
                    "checkpointing": "exactly_once",
                    "state_backend": "rocksdb",
                    "min_pause": "10s"
                }
            }
        }

    def _design_serving_layer(self) -> Dict:
        return {
            "api_gateway": {
                "type": "rest",
                "endpoints": [
                    {
                        "path": "/data/raw",
                        "methods": ["GET", "POST"],
                        "auth": "iam"
                    },
                    {
                        "path": "/data/processed",
                        "methods": ["GET"],
                        "auth": "iam"
                    }
                ]
            },
            "caching": {
                "engine": "redis",
                "configuration": {
                    "instance_type": "cache.r6g.large",
                    "num_shards": 2,
                    "replicas_per_shard": 1
                }
            }
        }

    def _design_security_layer(self) -> Dict:
        return {
            "encryption": {
                "at_rest": {
                    "type": "kms",
                    "key_rotation": True
                },
                "in_transit": {
                    "type": "tls",
                    "version": "1.3"
                }
            },
            "access_control": {
                "authentication": {
                    "type": "iam",
                    "mfa": True
                },
                "authorization": {
                    "type": "rbac",
                    "roles": ["admin", "analyst", "engineer"]
                }
            }
        }

    def _define_schemas(self) -> Dict:
        return {
            "tables": [
                {
                    "name": "users",
                    "columns": [
                        {"name": "id", "type": "uuid", "primary_key": True},
                        {"name": "email", "type": "varchar(255)", "unique": True},
                        {"name": "created_at", "type": "timestamp"}
                    ],
                    "indexes": ["email"]
                },
                {
                    "name": "events",
                    "columns": [
                        {"name": "id", "type": "uuid", "primary_key": True},
                        {"name": "user_id", "type": "uuid", "foreign_key": "users.id"},
                        {"name": "event_type", "type": "varchar(50)"},
                        {"name": "created_at", "type": "timestamp"}
                    ],
                    "indexes": ["user_id", "event_type"]
                }
            ],
            "views": [
                {
                    "name": "user_events",
                    "query": "SELECT u.*, e.event_type FROM users u JOIN events e ON u.id = e.user_id"
                }
            ]
        }

    def _define_relationships(self) -> List[Dict]:
        return [
            {
                "from": "users.id",
                "to": "events.user_id",
                "type": "one_to_many",
                "on_delete": "cascade"
            },
            {
                "from": "products.id",
                "to": "orders.product_id",
                "type": "one_to_many",
                "on_delete": "restrict"
            }
        ]

    def _define_validation_rules(self) -> Dict:
        return {
            "constraints": {
                "users": {
                    "email": {
                        "format": "email",
                        "required": True
                    },
                    "age": {
                        "type": "integer",
                        "min": 0,
                        "max": 150
                    }
                },
                "orders": {
                    "amount": {
                        "type": "decimal",
                        "min": 0
                    },
                    "status": {
                        "type": "enum",
                        "values": ["pending", "completed", "cancelled"]
                    }
                }
            }
        }

    def _create_documentation(self) -> Dict:
        return {
            "schemas": {
                "format": "markdown",
                "sections": ["tables", "views", "relationships"]
            },
            "data_dictionary": {
                "format": "excel",
                "sheets": ["columns", "constraints", "indexes"]
            }
        }

    def _design_ingestion_layer(self) -> Dict:
        return {
            "batch_ingestion": {
                "sources": [
                    {
                        "type": "database",
                        "connection": "jdbc",
                        "frequency": "daily"
                    },
                    {
                        "type": "file",
                        "format": "parquet",
                        "frequency": "hourly"
                    }
                ]
            },
            "stream_ingestion": {
                "sources": [
                    {
                        "type": "kafka",
                        "topics": ["events", "logs"],
                        "partitions": 6
                    },
                    {
                        "type": "kinesis",
                        "streams": ["clickstream"],
                        "shards": 4
                    }
                ]
            }
        }

    def _design_transformation_layer(self) -> Dict:
        return {
            "data_quality": {
                "validation": True,
                "cleansing": True,
                "deduplication": True
            },
            "transformations": [
                {
                    "type": "normalization",
                    "rules": ["date_standardization", "currency_conversion"]
                },
                {
                    "type": "enrichment",
                    "sources": ["reference_data", "external_apis"]
                }
            ]
        }

    def _design_persistence_layer(self) -> Dict:
        return {
            "storage_formats": {
                "raw": "parquet",
                "processed": "delta"
            },
            "partitioning": {
                "columns": ["date", "region"],
                "strategy": "hive"
            }
        }

    def _design_monitoring_layer(self) -> Dict:
        return {
            "metrics": {
                "latency": True,
                "throughput": True,
                "error_rate": True
            },
            "alerts": {
                "sla_breach": True,
                "data_quality": True,
                "system_health": True
            }
        }

    def _design_connectors(self) -> List[Dict]:
        return [
            {
                "name": "database_connector",
                "type": "jdbc",
                "config": {
                    "driver": "postgresql",
                    "batch_size": 1000,
                    "retry_policy": {
                        "max_retries": 3,
                        "backoff": "exponential"
                    }
                }
            },
            {
                "name": "api_connector",
                "type": "rest",
                "config": {
                    "auth": "oauth2",
                    "rate_limit": 100,
                    "timeout": "30s"
                }
            }
        ]

    def _design_apis(self) -> Dict:
        return {
            "rest_api": {
                "version": "v1",
                "endpoints": [
                    {
                        "path": "/data",
                        "methods": ["GET", "POST"],
                        "rate_limit": 1000
                    }
                ]
            },
            "graphql_api": {
                "version": "v1",
                "schema": "schema.graphql",
                "resolvers": ["Query", "Mutation"]
            }
        }

    def _design_synchronization(self) -> Dict:
        return {
            "strategy": "event-driven",
            "consistency": "eventual",
            "conflict_resolution": "last-write-wins"
        }

    def _design_integration_monitoring(self) -> Dict:
        return {
            "health_checks": {
                "frequency": "1m",
                "timeout": "10s"
            },
            "logging": {
                "level": "info",
                "retention": "30d"
            }
        }


if __name__ == "__main__":
    # Test the DataArchitect tool
    architecture_config = {
        "project": "ai-development-agency",
        "data_sources": ["databases", "apis", "files"],
        "requirements": {
            "scalability": True,
            "real_time": True,
            "security": True
        }
    }
    
    architect = DataArchitect(
        architecture_config=architecture_config,
        design_type="infrastructure",
        environment="development"
    )
    
    print("Testing DataArchitect tool:")
    print(architect.run()) 