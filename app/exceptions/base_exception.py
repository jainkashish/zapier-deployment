from http import HTTPStatus


class AppError(Exception):
    """Base application exception."""

    def __init__(self, message: str, status_code: int = HTTPStatus.INTERNAL_SERVER_ERROR):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class DeploymentNotFoundError(AppError):
    def __init__(self, deployment_id: str):
        super().__init__(
            message=f"Deployment '{deployment_id}' not found.",
            status_code=HTTPStatus.NOT_FOUND,
        )
