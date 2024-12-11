from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import Dict, List, Optional
import json

class BackendDeveloper(BaseTool):
    """
    A tool for implementing backend components, APIs, database models,
    and business logic.
    """
    
    api_spec: Dict = Field(
        ...,
        description="API specifications including endpoints, models, and business logic requirements"
    )
    
    development_type: str = Field(
        ...,
        description="Type of development needed: 'api', 'database', 'auth', or 'integration'"
    )
    
    framework: Optional[str] = Field(
        "FastAPI",
        description="Backend framework to use: 'FastAPI', 'Django', or 'Express'"
    )

    def run(self) -> str:
        """
        Implements backend components based on the specified parameters.
        """
        if self.development_type == "api":
            return self._implement_api()
        elif self.development_type == "database":
            return self._implement_database()
        elif self.development_type == "auth":
            return self._implement_auth()
        elif self.development_type == "integration":
            return self._implement_integration()
        else:
            return "Invalid development type specified"

    def _implement_api(self) -> str:
        api = {
            "endpoints": self._design_endpoints(),
            "middleware": self._implement_middleware(),
            "validation": self._implement_validation(),
            "error_handling": self._implement_error_handling(),
            "documentation": self._generate_api_documentation()
        }
        
        return json.dumps(api, indent=2)

    def _implement_database(self) -> str:
        database = {
            "models": self._design_database_models(),
            "migrations": self._setup_migrations(),
            "queries": self._implement_queries(),
            "indexing": self._setup_indexing(),
            "optimization": self._implement_db_optimization()
        }
        
        return json.dumps(database, indent=2)

    def _implement_auth(self) -> str:
        auth = {
            "authentication": self._implement_authentication(),
            "authorization": self._implement_authorization(),
            "security": self._implement_security_measures(),
            "user_management": self._implement_user_management(),
            "session_handling": self._implement_session_handling()
        }
        
        return json.dumps(auth, indent=2)

    def _implement_integration(self) -> str:
        integration = {
            "service_integration": self._implement_service_integration(),
            "data_transformation": self._implement_data_transformation(),
            "error_handling": self._implement_integration_error_handling(),
            "monitoring": self._implement_monitoring(),
            "documentation": self._generate_integration_documentation()
        }
        
        return json.dumps(integration, indent=2)

    def _design_endpoints(self) -> List[Dict]:
        return [
            {
                "path": "/api/v1/users",
                "method": "GET",
                "description": "List users",
                "query_params": ["page", "limit", "sort"],
                "response": {
                    "200": "List[UserSchema]",
                    "400": "ErrorResponse",
                    "401": "UnauthorizedError"
                }
            },
            {
                "path": "/api/v1/users/{user_id}",
                "method": "GET",
                "description": "Get user details",
                "path_params": ["user_id"],
                "response": {
                    "200": "UserSchema",
                    "404": "NotFoundError"
                }
            }
        ]

    def _implement_middleware(self) -> List[Dict]:
        return [
            {
                "name": "Authentication",
                "type": "JWT Verification",
                "config": {
                    "algorithms": ["HS256"],
                    "exclude_paths": ["/auth/login", "/docs"]
                }
            },
            {
                "name": "Rate Limiting",
                "type": "Token Bucket",
                "config": {
                    "rate": "100/minute",
                    "burst": 50
                }
            }
        ]

    def _implement_validation(self) -> Dict:
        return {
            "request_validation": {
                "body": "Pydantic models",
                "query": "Type validation",
                "path": "Parameter validation"
            },
            "response_validation": {
                "enabled": True,
                "schemas": "Response models"
            }
        }

    def _implement_error_handling(self) -> Dict:
        return {
            "global_handler": {
                "enabled": True,
                "logging": True
            },
            "error_types": {
                "validation": "422 Unprocessable Entity",
                "authentication": "401 Unauthorized",
                "authorization": "403 Forbidden",
                "not_found": "404 Not Found",
                "server_error": "500 Internal Server Error"
            }
        }

    def _generate_api_documentation(self) -> Dict:
        return {
            "format": "OpenAPI 3.0",
            "sections": {
                "endpoints": True,
                "models": True,
                "authentication": True
            },
            "examples": {
                "requests": True,
                "responses": True
            }
        }

    def _design_database_models(self) -> List[Dict]:
        return [
            {
                "name": "User",
                "fields": {
                    "id": "UUID, primary_key",
                    "email": "String, unique",
                    "password": "String, hashed",
                    "created_at": "DateTime"
                },
                "relationships": {
                    "profile": "One-to-One",
                    "posts": "One-to-Many"
                }
            },
            {
                "name": "Profile",
                "fields": {
                    "id": "UUID, primary_key",
                    "user_id": "UUID, foreign_key",
                    "name": "String",
                    "bio": "Text"
                }
            }
        ]

    def _setup_migrations(self) -> Dict:
        return {
            "tool": "Alembic",
            "configuration": {
                "auto_generate": True,
                "version_locations": "migrations/versions"
            },
            "commands": {
                "generate": "alembic revision --autogenerate",
                "upgrade": "alembic upgrade head"
            }
        }

    def _implement_queries(self) -> Dict:
        return {
            "orm_queries": {
                "select": "SQLAlchemy queries",
                "join": "Relationship queries",
                "filter": "Conditional queries"
            },
            "optimization": {
                "eager_loading": True,
                "query_caching": True
            }
        }

    def _setup_indexing(self) -> Dict:
        return {
            "indexes": {
                "user_email": "B-tree index",
                "created_at": "B-tree index"
            },
            "constraints": {
                "unique_email": "Unique constraint",
                "foreign_keys": "Referential integrity"
            }
        }

    def _implement_db_optimization(self) -> Dict:
        return {
            "query_optimization": {
                "indexing": True,
                "caching": True
            },
            "connection_pooling": {
                "min_size": 5,
                "max_size": 20
            }
        }

    def _implement_authentication(self) -> Dict:
        return {
            "jwt": {
                "enabled": True,
                "algorithm": "HS256",
                "expiration": "24h"
            },
            "oauth2": {
                "providers": ["Google", "GitHub"],
                "scopes": ["email", "profile"]
            }
        }

    def _implement_authorization(self) -> Dict:
        return {
            "rbac": {
                "enabled": True,
                "roles": ["admin", "user", "guest"]
            },
            "permissions": {
                "resources": ["users", "posts"],
                "actions": ["create", "read", "update", "delete"]
            }
        }

    def _implement_security_measures(self) -> Dict:
        return {
            "password_hashing": {
                "algorithm": "bcrypt",
                "salt_rounds": 12
            },
            "rate_limiting": {
                "enabled": True,
                "rate": "100/minute"
            }
        }

    def _implement_user_management(self) -> Dict:
        return {
            "registration": {
                "email_verification": True,
                "password_validation": True
            },
            "password_reset": {
                "enabled": True,
                "expiration": "1h"
            }
        }

    def _implement_session_handling(self) -> Dict:
        return {
            "session_store": "Redis",
            "configuration": {
                "expiration": "24h",
                "refresh": True
            }
        }

    def _implement_service_integration(self) -> Dict:
        return {
            "external_services": {
                "payment": "Stripe API",
                "email": "SendGrid API",
                "storage": "S3 API"
            },
            "integration_type": {
                "payment": "REST",
                "email": "SMTP",
                "storage": "SDK"
            }
        }

    def _implement_data_transformation(self) -> Dict:
        return {
            "serialization": {
                "request": "JSON serialization",
                "response": "JSON serialization"
            },
            "validation": {
                "input": "Request validation",
                "output": "Response validation"
            }
        }

    def _implement_integration_error_handling(self) -> Dict:
        return {
            "retry_logic": {
                "enabled": True,
                "max_attempts": 3
            },
            "fallback": {
                "enabled": True,
                "strategy": "Circuit Breaker"
            }
        }

    def _implement_monitoring(self) -> Dict:
        return {
            "metrics": {
                "response_time": True,
                "error_rate": True
            },
            "logging": {
                "level": "INFO",
                "format": "JSON"
            }
        }

    def _generate_integration_documentation(self) -> Dict:
        return {
            "api_documentation": {
                "format": "OpenAPI",
                "version": "3.0"
            },
            "integration_guide": {
                "setup": True,
                "examples": True
            }
        }


if __name__ == "__main__":
    # Test the BackendDeveloper tool
    test_spec = {
        "name": "User Management API",
        "version": "v1",
        "endpoints": [
            {
                "path": "/users",
                "methods": ["GET", "POST"],
                "auth_required": True
            },
            {
                "path": "/users/{user_id}",
                "methods": ["GET", "PUT", "DELETE"],
                "auth_required": True
            }
        ],
        "models": {
            "User": {
                "fields": ["id", "email", "name"],
                "relationships": ["Profile"]
            }
        }
    }
    
    developer = BackendDeveloper(
        api_spec=test_spec,
        development_type="api",
        framework="FastAPI"
    )
    
    print("Testing BackendDeveloper tool:")
    print(developer.run()) 