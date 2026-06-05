# Project Instructions

This repository contains the **Deployment Service**, a FastAPI application for managing deployment records.

## Agent Guidance

All AI agents working on this repository MUST adhere to the instructions and workflows defined in [AGENTS.md](./AGENTS.md).

### Key Directives
- **Consistency**: Maintain the established Repository/Service/Router architectural split.
- **Validation**: Always use the "Deployment Validator" skill defined in `AGENTS.md` before finalizing changes.
- **Documentation**: If adding new features, update `TECHNICAL_DETAILS.md` as well.

## Useful Commands
- **Start Server**: `uvicorn app.main:app --reload`
- **Seed Data**: `python scripts/seed_data.py`
- **Health Check**: `curl http://localhost:8000/health`
