import logging
from typing import Optional

from sqlalchemy.orm import Session

from app.enums.deployment_status import DeploymentStatus
from app.exceptions.base_exception import DeploymentNotFoundError
from app.repositories.deployment_repository import DeploymentRepository
from app.schemas.deployment_schema import DeploymentListResponse, DeploymentResponse

logger = logging.getLogger(__name__)


class DeploymentService:
    def __init__(self, db: Session):
        self._repo = DeploymentRepository(db)

    def list_deployments(
        self,
        service: Optional[str] = None,
        status: Optional[DeploymentStatus] = None,
    ) -> DeploymentListResponse:
        items = self._repo.get_all(service=service, status=status)
        return DeploymentListResponse(
            total=len(items),
            items=[DeploymentResponse.model_validate(item) for item in items],
        )

    def get_deployment(self, deployment_id: str) -> DeploymentResponse:
        deployment = self._repo.get_by_id(deployment_id)
        if not deployment:
            logger.warning("Deployment not found: %s", deployment_id)
            raise DeploymentNotFoundError(deployment_id)
        return DeploymentResponse.model_validate(deployment)
