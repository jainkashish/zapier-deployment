from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional

from app.db.session import get_db
from app.enums.deployment_status import DeploymentStatus
from app.schemas.deployment_schema import DeploymentListResponse, DeploymentResponse
from app.services.deployment_service import DeploymentService

router = APIRouter(prefix="/deployments", tags=["Deployments"])


def _get_service(db: Session = Depends(get_db)) -> DeploymentService:
    return DeploymentService(db)


@router.get("", response_model=DeploymentListResponse)
def list_deployments(
    service: Optional[str] = None,
    status: Optional[DeploymentStatus] = None,
    svc: DeploymentService = Depends(_get_service),
):
    """List all deployments with optional filters for service name and status."""
    return svc.list_deployments(service=service, status=status)


@router.get("/{deployment_id}", response_model=DeploymentResponse)
def get_deployment(
    deployment_id: str,
    svc: DeploymentService = Depends(_get_service),
):
    """Retrieve a single deployment by its ID."""
    return svc.get_deployment(deployment_id)
