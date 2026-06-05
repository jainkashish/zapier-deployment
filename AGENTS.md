# Agent Context & Skills

This document provides specialized context and workflows for AI agents working on the Deployment Service repository.

## Repository Context

The **Deployment Service** is a FastAPI-based REST API designed for tracking deployment events. It uses:
- **FastAPI**: Web framework.
- **SQLAlchemy**: ORM for database interactions.
- **SQLite**: Local database (default: `deployments.db`).
- **Pydantic**: Data validation and serialization.

### Key Architectural Patterns
- **Repository Pattern**: Data access is abstracted in `app/repositories/`.
- **Service Layer**: Business logic resides in `app/services/`.
- **Router Layer**: HTTP endpoints are defined in `app/api/v1/endpoints/`.
- **Global Exception Handling**: Custom exceptions in `app/exceptions/` are caught and transformed into standard JSON error responses.

## Setup for Agents

When onboarding or performing tasks, ensure the environment is ready:

1.  **Run Setup**: If the environment is not configured, run `./setup.sh`.
2.  **Activation**: Ensure the virtual environment is active: `source .venv/bin/activate`.
3.  **Testing**: Use manual `curl` commands or `pytest` against a running `uvicorn` instance.

## Agent Skill: Deployment Validator

Agents should use this "skill" when adding or modifying deployment-related logic.

### Workflow: Validate Deployment Integrity
1.  **Schema Check**: Ensure any new fields in `DeploymentModel` are reflected in `DeploymentCreate` and `DeploymentRead` schemas in `app/schemas/`.
2.  **Enum Check**: Only use statuses defined in `app/enums/deployment_status.py`.
3.  **Repository Test**: If changing data access, verify `app/repositories/deployment_repository.py` handles the change.
4.  **Integration Test**: Run the server and use `curl` to verify the end-to-end flow.

### Verification Command
```bash
# Verify API health and basic data retrieval
curl -s http://localhost:8000/health && curl -s http://localhost:8000/api/v1/deployments | jq .
```
