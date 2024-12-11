from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import Dict, List, Optional
import json

class PipelineAutomator(BaseTool):
    """
    A tool for managing CI/CD pipelines, automation workflows,
    and deployment processes.
    """
    
    pipeline_config: Dict = Field(
        ...,
        description="Pipeline configuration including stages, steps, and requirements"
    )
    
    pipeline_type: str = Field(
        ...,
        description="Type of pipeline: 'build', 'test', 'deploy', or 'release'"
    )
    
    environment: Optional[str] = Field(
        "development",
        description="Target environment: 'development', 'staging', or 'production'"
    )

    def run(self) -> str:
        """
        Manages pipeline operations based on the specified parameters.
        """
        if self.pipeline_type == "build":
            return self._create_build_pipeline()
        elif self.pipeline_type == "test":
            return self._create_test_pipeline()
        elif self.pipeline_type == "deploy":
            return self._create_deploy_pipeline()
        elif self.pipeline_type == "release":
            return self._create_release_pipeline()
        else:
            return "Invalid pipeline type specified"

    def _create_build_pipeline(self) -> str:
        pipeline = {
            "stages": self._define_build_stages(),
            "triggers": self._configure_triggers(),
            "artifacts": self._configure_artifacts(),
            "caching": self._configure_caching()
        }
        
        return json.dumps(pipeline, indent=2)

    def _create_test_pipeline(self) -> str:
        pipeline = {
            "stages": self._define_test_stages(),
            "environments": self._configure_test_environments(),
            "reporting": self._configure_test_reporting(),
            "coverage": self._configure_coverage()
        }
        
        return json.dumps(pipeline, indent=2)

    def _create_deploy_pipeline(self) -> str:
        pipeline = {
            "stages": self._define_deploy_stages(),
            "strategies": self._configure_deploy_strategies(),
            "validation": self._configure_validation(),
            "rollback": self._configure_rollback()
        }
        
        return json.dumps(pipeline, indent=2)

    def _create_release_pipeline(self) -> str:
        pipeline = {
            "stages": self._define_release_stages(),
            "versioning": self._configure_versioning(),
            "changelog": self._generate_changelog(),
            "notifications": self._configure_notifications()
        }
        
        return json.dumps(pipeline, indent=2)

    def _define_build_stages(self) -> List[Dict]:
        return [
            {
                "name": "checkout",
                "steps": [
                    {
                        "action": "git-checkout",
                        "repository": "${REPO_URL}",
                        "branch": "${BRANCH_NAME}"
                    }
                ]
            },
            {
                "name": "dependencies",
                "steps": [
                    {
                        "action": "install-dependencies",
                        "command": "npm install",
                        "cache": True
                    }
                ]
            },
            {
                "name": "build",
                "steps": [
                    {
                        "action": "build-application",
                        "command": "npm run build",
                        "artifacts": ["dist/", "build/"]
                    }
                ]
            }
        ]

    def _configure_triggers(self) -> Dict:
        return {
            "push": {
                "branches": ["main", "develop"],
                "paths": ["src/**", "package.json"]
            },
            "pull_request": {
                "branches": ["main", "develop"],
                "types": ["opened", "synchronize"]
            },
            "schedule": {
                "cron": "0 0 * * *",
                "branches": ["main"]
            }
        }

    def _configure_artifacts(self) -> Dict:
        return {
            "build": {
                "paths": ["dist/**", "build/**"],
                "retention": "30 days"
            },
            "reports": {
                "paths": ["coverage/**", "test-results/**"],
                "retention": "7 days"
            }
        }

    def _configure_caching(self) -> Dict:
        return {
            "dependencies": {
                "paths": ["node_modules/"],
                "key": "npm-${hash:package-lock.json}"
            },
            "build": {
                "paths": [".next/cache/"],
                "key": "next-${hash:package.json}"
            }
        }

    def _define_test_stages(self) -> List[Dict]:
        return [
            {
                "name": "unit-tests",
                "steps": [
                    {
                        "action": "run-tests",
                        "command": "npm run test:unit",
                        "coverage": True
                    }
                ]
            },
            {
                "name": "integration-tests",
                "steps": [
                    {
                        "action": "run-tests",
                        "command": "npm run test:integration",
                        "services": ["database", "cache"]
                    }
                ]
            },
            {
                "name": "e2e-tests",
                "steps": [
                    {
                        "action": "run-tests",
                        "command": "npm run test:e2e",
                        "environment": "test"
                    }
                ]
            }
        ]

    def _configure_test_environments(self) -> Dict:
        return {
            "unit": {
                "type": "container",
                "image": "node:16",
                "variables": {
                    "NODE_ENV": "test"
                }
            },
            "integration": {
                "type": "docker-compose",
                "services": ["app", "db", "cache"],
                "variables": {
                    "DATABASE_URL": "postgresql://test:test@db:5432/test"
                }
            }
        }

    def _configure_test_reporting(self) -> Dict:
        return {
            "junit": {
                "enabled": True,
                "path": "test-results/*.xml"
            },
            "coverage": {
                "enabled": True,
                "path": "coverage/lcov.info",
                "format": "lcov"
            }
        }

    def _configure_coverage(self) -> Dict:
        return {
            "thresholds": {
                "lines": 80,
                "functions": 80,
                "branches": 70
            },
            "exclude": [
                "**/*.test.ts",
                "**/*.spec.ts"
            ]
        }

    def _define_deploy_stages(self) -> List[Dict]:
        return [
            {
                "name": "prepare",
                "steps": [
                    {
                        "action": "validate-config",
                        "files": ["k8s/*.yaml"]
                    }
                ]
            },
            {
                "name": "deploy",
                "steps": [
                    {
                        "action": "deploy-application",
                        "command": "kubectl apply -f k8s/",
                        "environment": self.environment
                    }
                ]
            },
            {
                "name": "verify",
                "steps": [
                    {
                        "action": "health-check",
                        "endpoint": "/health",
                        "timeout": "5m"
                    }
                ]
            }
        ]

    def _configure_deploy_strategies(self) -> Dict:
        return {
            "rolling": {
                "enabled": True,
                "max_surge": "25%",
                "max_unavailable": "25%"
            },
            "canary": {
                "enabled": True,
                "percentage": 10,
                "metrics": ["error_rate", "latency"]
            },
            "blue_green": {
                "enabled": False,
                "switch_method": "manual"
            }
        }

    def _configure_validation(self) -> Dict:
        return {
            "pre_deploy": [
                "config_validation",
                "security_scan",
                "dependency_check"
            ],
            "post_deploy": [
                "health_check",
                "smoke_test",
                "integration_test"
            ]
        }

    def _configure_rollback(self) -> Dict:
        return {
            "automatic": {
                "enabled": True,
                "conditions": [
                    "health_check_failed",
                    "error_rate_exceeded"
                ]
            },
            "manual": {
                "enabled": True,
                "approvers": ["devops-team"]
            }
        }

    def _define_release_stages(self) -> List[Dict]:
        return [
            {
                "name": "version",
                "steps": [
                    {
                        "action": "bump-version",
                        "type": "semver"
                    }
                ]
            },
            {
                "name": "changelog",
                "steps": [
                    {
                        "action": "generate-changelog",
                        "scope": "since-last-release"
                    }
                ]
            },
            {
                "name": "release",
                "steps": [
                    {
                        "action": "create-release",
                        "assets": ["dist/", "changelog.md"]
                    }
                ]
            }
        ]

    def _configure_versioning(self) -> Dict:
        return {
            "strategy": "semver",
            "prefix": "v",
            "source": {
                "type": "git-tag",
                "pattern": "v*.*.*"
            }
        }

    def _generate_changelog(self) -> Dict:
        return {
            "sections": [
                "Features",
                "Bug Fixes",
                "Performance Improvements",
                "Breaking Changes"
            ],
            "commit_types": {
                "feat": "Features",
                "fix": "Bug Fixes",
                "perf": "Performance Improvements"
            }
        }

    def _configure_notifications(self) -> Dict:
        return {
            "channels": {
                "slack": {
                    "enabled": True,
                    "channel": "#releases"
                },
                "email": {
                    "enabled": True,
                    "recipients": ["team@example.com"]
                }
            },
            "events": {
                "started": True,
                "success": True,
                "failure": True
            }
        }


if __name__ == "__main__":
    # Test the PipelineAutomator tool
    pipeline_config = {
        "project": "ai-development-agency",
        "repository": "https://github.com/org/repo",
        "requirements": {
            "automated_tests": True,
            "code_coverage": True,
            "security_scan": True
        }
    }
    
    automator = PipelineAutomator(
        pipeline_config=pipeline_config,
        pipeline_type="build",
        environment="development"
    )
    
    print("Testing PipelineAutomator tool:")
    print(automator.run()) 