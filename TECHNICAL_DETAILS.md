# Technical Details - Deployment Service

## Project Structure

```
deployment-service/
├── app/
│   ├── api/v1/endpoints/
│   │   └── deployment_router.py   # HTTP layer
│   ├── core/
│   │   └── config.py              # Settings
│   ├── db/
│   │   └── session.py             # SQLAlchemy engine & session
│   ├── enums/
│   │   └── deployment_status.py   # DeploymentStatus enum
│   ├── exceptions/
│   │   └── base_exception.py      # AppError, DeploymentNotFoundError
│   ├── models/
│   │   └── deployment_model.py    # SQLAlchemy ORM model
│   ├── repositories/
│   │   └── deployment_repository.py # Data access layer
│   ├── schemas/
│   │   └── deployment_schema.py   # Pydantic response models
│   ├── services/
│   │   └── deployment_service.py  # Business logic
│   └── main.py                    # App entrypoint
├── scripts/
│   └── seed_data.py               # Mock data seeder
└── requirements.txt
```

## Endpoints 

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/v1/deployments` | List all deployments (filterable) |
| `GET` | `/api/v1/deployments/{id}` | Get one deployment by ID |
| `GET` | `/health` | Health check |

### Filters for `GET /api/v1/deployments`

| Query Param | Example | Description |
|-------------|---------|-------------|
| `service` | `?service=billing-api` | Filter by service name |
| `status` | `?status=failed` | Filter by status |
| Both | `?service=auth-service&status=success` | Combine filters |

### Example Requests

```bash
# All deployments
curl http://localhost:8000/api/v1/deployments

# Filter by service
curl "http://localhost:8000/api/v1/deployments?service=billing-api"

# Filter by status
curl "http://localhost:8000/api/v1/deployments?status=failed"

# Single deployment
curl http://localhost:8000/api/v1/deployments/deploy_002
```

### Response Shape

**List** (`GET /api/v1/deployments`):
```json
{
  "total": 5,
  "items": [
    {
      "id": "deploy_002",
      "service": "billing-api",
      "status": "failed",
      "duration": 320,
      "timestamp": "2025-04-28T14:32:00Z",
      "commit_sha": "abc123e"
    }
  ]
}
```

**Single** (`GET /api/v1/deployments/{id}`):
```json
{
  "id": "deploy_002",
  "service": "billing-api",
  "status": "failed",
  "duration": 320,
  "timestamp": "2025-04-28T14:32:00Z",
  "commit_sha": "abc123e"
}
```

**Error** (404):
```json
{ "error": "Deployment 'deploy_xyz' not found." }
```

## Interactive API Explorer

Visit **http://localhost:8000/docs** for the Swagger UI to explore and test all endpoints interactively.

## Configuration

Override defaults by creating a `.env` file:

```env
DATABASE_URL=sqlite:///./deployments.db
DEBUG=false
```

## Valid Statuses

`pending` · `running` · `success` · `failed` · `rolled_back`
