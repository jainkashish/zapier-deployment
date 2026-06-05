# Deployment Service

A production-ready REST API for ingesting and serving deployment event data, built with FastAPI + SQLAlchemy + SQLite.

> **Note for AI Agents**: Detailed repository context, architectural patterns, and specialized skills are documented in [AGENTS.md](./AGENTS.md). Please consult this file before performing any modifications.

## Setup

### Prerequisites
- Python 3.11+

### Steps

```bash
# 1. Run the setup script (creates venv, installs deps, seeds data)
chmod +x setup.sh && ./setup.sh

# 2. Activate the virtual environment
source .venv/bin/activate

# 3. Start the server
uvicorn app.main:app --reload
```

The API is now live at **http://localhost:8000**

## Health Check

To verify the service is running:

```bash
curl http://localhost:8000/health
```

---
*For more detailed information on API endpoints, project structure, and configuration, see [TECHNICAL_DETAILS.md](./TECHNICAL_DETAILS.md).*
