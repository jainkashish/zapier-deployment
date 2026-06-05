from datetime import datetime

from pydantic import BaseModel

from app.enums.deployment_status import DeploymentStatus


class DeploymentResponse(BaseModel):
    id: str
    service: str
    status: DeploymentStatus
    duration: int
    timestamp: datetime
    commit_sha: str

    model_config = {"from_attributes": True}


class DeploymentListResponse(BaseModel):
    total: int
    items: list[DeploymentResponse]
