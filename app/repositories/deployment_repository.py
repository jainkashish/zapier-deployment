import logging
from typing import Optional

from sqlalchemy.orm import Session

from app.enums.deployment_status import DeploymentStatus
from app.models.deployment_model import DeploymentModel

logger = logging.getLogger(__name__)


class DeploymentRepository:
    def __init__(self, db: Session):
        self._db = db

    def get_all(
        self,
        service: Optional[str] = None,
        status: Optional[DeploymentStatus] = None,
    ) -> list[DeploymentModel]:
        query = self._db.query(DeploymentModel)
        if service:
            query = query.filter(DeploymentModel.service == service)
        if status:
            query = query.filter(DeploymentModel.status == status)
        results = query.order_by(DeploymentModel.timestamp.desc()).all()
        logger.debug("Fetched %d deployments (service=%s, status=%s)", len(results), service, status)
        return results

    def get_by_id(self, deployment_id: str) -> Optional[DeploymentModel]:
        return self._db.query(DeploymentModel).filter(DeploymentModel.id == deployment_id).first()
