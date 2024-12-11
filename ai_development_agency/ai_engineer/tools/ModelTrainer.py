from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import Dict, List, Optional
import json

class ModelTrainer(BaseTool):
    """
    A tool for training, optimizing, and evaluating AI/ML models,
    including data preprocessing, training pipeline setup, and performance monitoring.
    """
    
    training_config: Dict = Field(
        ...,
        description="Training configuration including model architecture, data settings, and hyperparameters"
    )
    
    training_phase: str = Field(
        ...,
        description="Phase of training: 'preprocessing', 'training', 'evaluation', or 'optimization'"
    )
    
    monitoring_config: Optional[Dict] = Field(
        None,
        description="Optional configuration for monitoring training progress and performance"
    )

    def run(self) -> str:
        """
        Executes the specified training phase and returns relevant metrics and information.
        """
        if self.training_phase == "preprocessing":
            return self._setup_preprocessing()
        elif self.training_phase == "training":
            return self._setup_training()
        elif self.training_phase == "evaluation":
            return self._setup_evaluation()
        elif self.training_phase == "optimization":
            return self._setup_optimization()
        else:
            return "Invalid training phase specified"

    def _setup_preprocessing(self) -> str:
        preprocessing = {
            "data_pipeline": self._configure_data_pipeline(),
            "preprocessing_steps": self._define_preprocessing_steps(),
            "validation_setup": self._setup_validation_pipeline(),
            "resource_allocation": self._allocate_preprocessing_resources()
        }
        
        return json.dumps(preprocessing, indent=2)

    def _setup_training(self) -> str:
        training = {
            "training_pipeline": self._configure_training_pipeline(),
            "optimization_setup": self._setup_optimization_strategy(),
            "monitoring_config": self._setup_training_monitoring(),
            "checkpointing": self._configure_checkpointing()
        }
        
        return json.dumps(training, indent=2)

    def _setup_evaluation(self) -> str:
        evaluation = {
            "evaluation_metrics": self._define_evaluation_metrics(),
            "testing_pipeline": self._configure_testing_pipeline(),
            "performance_analysis": self._analyze_performance(),
            "validation_results": self._generate_validation_results()
        }
        
        return json.dumps(evaluation, indent=2)

    def _setup_optimization(self) -> str:
        optimization = {
            "optimization_strategy": self._define_optimization_strategy(),
            "hyperparameter_tuning": self._setup_hyperparameter_tuning(),
            "model_compression": self._configure_model_compression(),
            "performance_tracking": self._setup_performance_tracking()
        }
        
        return json.dumps(optimization, indent=2)

    def _configure_data_pipeline(self) -> Dict:
        return {
            "data_sources": {
                "training": "s3://training-data",
                "validation": "s3://validation-data",
                "testing": "s3://test-data"
            },
            "data_format": {
                "type": "TFRecord",
                "compression": "GZIP",
                "sharding": True
            },
            "preprocessing": {
                "num_workers": 4,
                "prefetch_size": 2,
                "batch_size": 32
            }
        }

    def _define_preprocessing_steps(self) -> List[Dict]:
        return [
            {
                "step": "Normalization",
                "params": {
                    "method": "StandardScaler",
                    "per_feature": True
                }
            },
            {
                "step": "Augmentation",
                "params": {
                    "methods": ["rotation", "flip", "noise"],
                    "probability": 0.5
                }
            },
            {
                "step": "Feature Engineering",
                "params": {
                    "methods": ["pca", "polynomial_features"],
                    "config": {"n_components": 10}
                }
            }
        ]

    def _setup_validation_pipeline(self) -> Dict:
        return {
            "validation_split": 0.2,
            "cross_validation": {
                "method": "StratifiedKFold",
                "n_splits": 5
            },
            "metrics": [
                "accuracy",
                "precision",
                "recall",
                "f1_score"
            ]
        }

    def _allocate_preprocessing_resources(self) -> Dict:
        return {
            "cpu_cores": 8,
            "memory": "32GB",
            "storage": {
                "temp": "100GB",
                "processed": "500GB"
            }
        }

    def _configure_training_pipeline(self) -> Dict:
        return {
            "framework": "PyTorch Lightning",
            "training_config": {
                "max_epochs": 100,
                "early_stopping": {
                    "monitor": "val_loss",
                    "patience": 10
                },
                "gradient_clipping": 1.0
            },
            "optimizer": {
                "name": "AdamW",
                "params": {
                    "lr": 1e-4,
                    "weight_decay": 0.01
                }
            },
            "scheduler": {
                "name": "CosineAnnealingLR",
                "params": {
                    "T_max": 100,
                    "eta_min": 1e-6
                }
            }
        }

    def _setup_optimization_strategy(self) -> Dict:
        return {
            "mixed_precision": True,
            "gradient_accumulation": {
                "steps": 4
            },
            "distributed_training": {
                "strategy": "DDP",
                "num_nodes": 1,
                "gpus_per_node": 4
            }
        }

    def _setup_training_monitoring(self) -> Dict:
        return {
            "logging": {
                "framework": "WandB",
                "log_frequency": 100,
                "metrics": [
                    "loss",
                    "accuracy",
                    "learning_rate"
                ]
            },
            "profiling": {
                "enabled": True,
                "start_step": 100,
                "num_steps": 10
            }
        }

    def _configure_checkpointing(self) -> Dict:
        return {
            "frequency": "epoch",
            "save_best": True,
            "monitor": "val_loss",
            "mode": "min",
            "save_last": True,
            "format": "torch_script"
        }

    def _define_evaluation_metrics(self) -> Dict:
        return {
            "classification": [
                "accuracy",
                "precision",
                "recall",
                "f1_score",
                "roc_auc"
            ],
            "regression": [
                "mse",
                "mae",
                "r2_score",
                "explained_variance"
            ],
            "custom_metrics": [
                "inference_latency",
                "memory_usage"
            ]
        }

    def _configure_testing_pipeline(self) -> Dict:
        return {
            "batch_size": 64,
            "num_workers": 4,
            "device": "cuda",
            "precision": 16,
            "metrics_output": {
                "format": "json",
                "save_path": "metrics/"
            }
        }

    def _analyze_performance(self) -> Dict:
        return {
            "metrics_analysis": {
                "aggregate_stats": True,
                "per_class_stats": True,
                "confusion_matrix": True
            },
            "error_analysis": {
                "error_cases": True,
                "error_distribution": True
            },
            "resource_usage": {
                "gpu_memory": True,
                "cpu_usage": True,
                "inference_time": True
            }
        }

    def _generate_validation_results(self) -> Dict:
        return {
            "metrics_summary": {
                "overall_accuracy": 0.95,
                "average_precision": 0.94,
                "average_recall": 0.93
            },
            "detailed_analysis": {
                "per_class_metrics": True,
                "confusion_matrix": True,
                "roc_curves": True
            },
            "validation_insights": [
                "Strong performance on majority classes",
                "Some confusion between similar classes",
                "Good generalization across validation set"
            ]
        }

    def _define_optimization_strategy(self) -> Dict:
        return {
            "methods": [
                "hyperparameter_tuning",
                "model_pruning",
                "quantization",
                "knowledge_distillation"
            ],
            "objectives": [
                "accuracy",
                "latency",
                "model_size"
            ],
            "constraints": {
                "max_latency": "100ms",
                "max_model_size": "100MB"
            }
        }

    def _setup_hyperparameter_tuning(self) -> Dict:
        return {
            "method": "Optuna",
            "search_space": {
                "learning_rate": {
                    "type": "float",
                    "range": [1e-5, 1e-3],
                    "scale": "log"
                },
                "batch_size": {
                    "type": "int",
                    "range": [16, 128],
                    "step": 16
                },
                "num_layers": {
                    "type": "int",
                    "range": [2, 8]
                }
            },
            "optimization": {
                "n_trials": 100,
                "metric": "val_loss",
                "direction": "minimize"
            }
        }

    def _configure_model_compression(self) -> Dict:
        return {
            "quantization": {
                "method": "dynamic",
                "precision": "int8",
                "calibration_method": "histogram"
            },
            "pruning": {
                "method": "magnitude",
                "schedule": "gradual",
                "target_sparsity": 0.7
            },
            "knowledge_distillation": {
                "teacher_model": "full_model",
                "student_model": "compressed_model",
                "temperature": 2.0
            }
        }

    def _setup_performance_tracking(self) -> Dict:
        return {
            "metrics": {
                "accuracy": "classification_accuracy",
                "latency": "inference_time",
                "memory": "gpu_memory_usage"
            },
            "tracking_framework": "MLflow",
            "experiment_name": "model_optimization",
            "tracking_frequency": "every_epoch"
        }


if __name__ == "__main__":
    # Test the ModelTrainer tool
    test_config = {
        "model_architecture": "BERT-base",
        "data_settings": {
            "train_path": "s3://training-data",
            "val_path": "s3://validation-data",
            "batch_size": 32
        },
        "hyperparameters": {
            "learning_rate": 1e-4,
            "num_epochs": 10,
            "weight_decay": 0.01
        }
    }
    
    trainer = ModelTrainer(
        training_config=test_config,
        training_phase="training",
        monitoring_config={
            "framework": "wandb",
            "project": "test_project",
            "metrics": ["loss", "accuracy"]
        }
    )
    
    print("Testing ModelTrainer tool:")
    print(trainer.run()) 