from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import Dict, List, Optional
import json

class DataPipelineManager(BaseTool):
    """
    A tool for managing data pipelines, ETL/ELT workflows,
    and data processing jobs.
    """
    
    pipeline_config: Dict = Field(
        ...,
        description="Pipeline configuration including sources, transformations, and requirements"
    )
    
    pipeline_type: str = Field(
        ...,
        description="Type of pipeline: 'etl', 'elt', 'streaming', or 'batch'"
    )
    
    environment: Optional[str] = Field(
        "development",
        description="Target environment: 'development', 'staging', or 'production'"
    )

    def run(self) -> str:
        """
        Manages data pipeline operations based on the specified parameters.
        """
        if self.pipeline_type == "etl":
            return self._create_etl_pipeline()
        elif self.pipeline_type == "elt":
            return self._create_elt_pipeline()
        elif self.pipeline_type == "streaming":
            return self._create_streaming_pipeline()
        elif self.pipeline_type == "batch":
            return self._create_batch_pipeline()
        else:
            return "Invalid pipeline type specified"

    def _create_etl_pipeline(self) -> str:
        pipeline = {
            "extraction": self._configure_extraction(),
            "transformation": self._configure_transformation(),
            "loading": self._configure_loading(),
            "monitoring": self._configure_monitoring()
        }
        
        return json.dumps(pipeline, indent=2)

    def _create_elt_pipeline(self) -> str:
        pipeline = {
            "extraction": self._configure_extraction(),
            "loading": self._configure_loading(),
            "transformation": self._configure_transformation(),
            "monitoring": self._configure_monitoring()
        }
        
        return json.dumps(pipeline, indent=2)

    def _create_streaming_pipeline(self) -> str:
        pipeline = {
            "ingestion": self._configure_stream_ingestion(),
            "processing": self._configure_stream_processing(),
            "delivery": self._configure_stream_delivery(),
            "monitoring": self._configure_stream_monitoring()
        }
        
        return json.dumps(pipeline, indent=2)

    def _create_batch_pipeline(self) -> str:
        pipeline = {
            "scheduling": self._configure_scheduling(),
            "processing": self._configure_batch_processing(),
            "delivery": self._configure_batch_delivery(),
            "monitoring": self._configure_batch_monitoring()
        }
        
        return json.dumps(pipeline, indent=2)

    def _configure_extraction(self) -> Dict:
        return {
            "sources": [
                {
                    "type": "database",
                    "config": {
                        "type": "postgresql",
                        "connection": {
                            "host": "${DB_HOST}",
                            "port": 5432,
                            "database": "source_db"
                        },
                        "extraction": {
                            "method": "incremental",
                            "key": "updated_at",
                            "batch_size": 10000
                        }
                    }
                },
                {
                    "type": "api",
                    "config": {
                        "url": "${API_URL}",
                        "method": "GET",
                        "headers": {
                            "Authorization": "${API_KEY}"
                        },
                        "pagination": {
                            "type": "offset",
                            "limit": 100
                        }
                    }
                }
            ],
            "validation": {
                "schema_validation": True,
                "data_quality_checks": True
            }
        }

    def _configure_transformation(self) -> Dict:
        return {
            "engine": "spark",
            "config": {
                "master": "yarn",
                "executor_memory": "4g",
                "executor_cores": 2
            },
            "stages": [
                {
                    "name": "data_cleaning",
                    "operations": [
                        "remove_duplicates",
                        "handle_nulls",
                        "standardize_formats"
                    ]
                },
                {
                    "name": "data_enrichment",
                    "operations": [
                        "join_reference_data",
                        "calculate_metrics",
                        "add_derived_columns"
                    ]
                }
            ]
        }

    def _configure_loading(self) -> Dict:
        return {
            "destination": {
                "type": "data_warehouse",
                "config": {
                    "type": "snowflake",
                    "connection": {
                        "account": "${SNOWFLAKE_ACCOUNT}",
                        "warehouse": "LOADING_WH",
                        "database": "PROD_DB"
                    },
                    "loading": {
                        "method": "merge",
                        "key_columns": ["id"],
                        "batch_size": 50000
                    }
                }
            },
            "post_load_validation": {
                "row_count_check": True,
                "data_quality_check": True
            }
        }

    def _configure_monitoring(self) -> Dict:
        return {
            "metrics": {
                "pipeline_metrics": [
                    "records_processed",
                    "processing_time",
                    "error_count"
                ],
                "data_quality_metrics": [
                    "null_percentage",
                    "duplicate_count",
                    "outlier_count"
                ]
            },
            "alerts": {
                "error_threshold": 100,
                "latency_threshold": "30m",
                "notification_channels": [
                    "email",
                    "slack"
                ]
            }
        }

    def _configure_stream_ingestion(self) -> Dict:
        return {
            "source": {
                "type": "kafka",
                "config": {
                    "bootstrap_servers": "${KAFKA_SERVERS}",
                    "topics": ["events", "logs"],
                    "consumer_group": "streaming_pipeline",
                    "auto_offset_reset": "latest"
                }
            },
            "schema_registry": {
                "url": "${SCHEMA_REGISTRY_URL}",
                "compatibility": "BACKWARD"
            }
        }

    def _configure_stream_processing(self) -> Dict:
        return {
            "engine": "flink",
            "config": {
                "parallelism": 4,
                "checkpoint_interval": "1min",
                "state_backend": "rocksdb"
            },
            "operations": [
                {
                    "type": "window",
                    "config": {
                        "type": "sliding",
                        "size": "5min",
                        "slide": "1min"
                    }
                },
                {
                    "type": "aggregation",
                    "config": {
                        "group_by": ["user_id", "event_type"],
                        "metrics": ["count", "sum", "avg"]
                    }
                }
            ]
        }

    def _configure_stream_delivery(self) -> Dict:
        return {
            "sinks": [
                {
                    "type": "elasticsearch",
                    "config": {
                        "hosts": ["${ES_HOST}"],
                        "index": "events-{yyyy-MM-dd}",
                        "bulk_size": 1000
                    }
                },
                {
                    "type": "redis",
                    "config": {
                        "host": "${REDIS_HOST}",
                        "key_pattern": "event:{user_id}",
                        "ttl": "1h"
                    }
                }
            ]
        }

    def _configure_stream_monitoring(self) -> Dict:
        return {
            "metrics": {
                "throughput": True,
                "latency": True,
                "backpressure": True
            },
            "alerts": {
                "lag_threshold": "5min",
                "error_rate_threshold": "1%"
            }
        }

    def _configure_scheduling(self) -> Dict:
        return {
            "scheduler": "airflow",
            "schedule": {
                "frequency": "hourly",
                "start_time": "00:00 UTC",
                "retries": 3,
                "retry_delay": "5min"
            },
            "dependencies": {
                "upstream": ["data_validation"],
                "downstream": ["reporting"]
            }
        }

    def _configure_batch_processing(self) -> Dict:
        return {
            "engine": "spark",
            "config": {
                "master": "yarn",
                "deploy_mode": "cluster",
                "driver_memory": "4g",
                "executor_memory": "8g",
                "executor_cores": 4,
                "num_executors": 10
            },
            "optimization": {
                "partition_columns": ["date", "region"],
                "coalesce_partitions": True,
                "cache_intermediate": True
            }
        }

    def _configure_batch_delivery(self) -> Dict:
        return {
            "destinations": [
                {
                    "type": "s3",
                    "config": {
                        "bucket": "${S3_BUCKET}",
                        "prefix": "processed/",
                        "format": "parquet",
                        "partition_by": ["year", "month", "day"]
                    }
                },
                {
                    "type": "bigquery",
                    "config": {
                        "project": "${GCP_PROJECT}",
                        "dataset": "processed_data",
                        "write_disposition": "WRITE_TRUNCATE",
                        "partition_by": "date"
                    }
                }
            ]
        }

    def _configure_batch_monitoring(self) -> Dict:
        return {
            "metrics": {
                "job_metrics": [
                    "duration",
                    "records_processed",
                    "data_size"
                ],
                "resource_metrics": [
                    "cpu_usage",
                    "memory_usage",
                    "disk_io"
                ]
            },
            "logging": {
                "level": "INFO",
                "retention": "30d",
                "destination": "cloudwatch"
            }
        }


if __name__ == "__main__":
    # Test the DataPipelineManager tool
    pipeline_config = {
        "project": "ai-development-agency",
        "source": {
            "type": "database",
            "name": "production_db"
        },
        "destination": {
            "type": "data_warehouse",
            "name": "analytics_dw"
        },
        "requirements": {
            "frequency": "hourly",
            "latency": "5min",
            "reliability": "99.9%"
        }
    }
    
    manager = DataPipelineManager(
        pipeline_config=pipeline_config,
        pipeline_type="etl",
        environment="development"
    )
    
    print("Testing DataPipelineManager tool:")
    print(manager.run()) 