"""
Seed script: populates the database with 30+ mock deployment events.
Run once: python scripts/seed_data.py
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from datetime import datetime, timezone, timedelta
from app.db.session import SessionLocal, Base, engine
from app.models.deployment_model import DeploymentModel
from app.enums.deployment_status import DeploymentStatus

Base.metadata.create_all(bind=engine)

EVENTS: list[dict] = [
    # billing-api
    {"id": "deploy_001", "service": "billing-api",     "status": DeploymentStatus.SUCCESS,     "duration": 94,  "commit_sha": "a1b2c3d", "days_ago": 1},
    {"id": "deploy_002", "service": "billing-api",     "status": DeploymentStatus.FAILED,      "duration": 320, "commit_sha": "abc123e", "days_ago": 3},
    {"id": "deploy_003", "service": "billing-api",     "status": DeploymentStatus.RUNNING,     "duration": 60,  "commit_sha": "c3d4e5f", "days_ago": 0},
    {"id": "deploy_004", "service": "billing-api",     "status": DeploymentStatus.ROLLED_BACK, "duration": 210, "commit_sha": "d4e5f6a", "days_ago": 5},
    {"id": "deploy_005", "service": "billing-api",     "status": DeploymentStatus.SUCCESS,     "duration": 85,  "commit_sha": "e5f6a7b", "days_ago": 7},
    # auth-service
    {"id": "deploy_006", "service": "auth-service",    "status": DeploymentStatus.SUCCESS,     "duration": 112, "commit_sha": "f6a7b8c", "days_ago": 2},
    {"id": "deploy_007", "service": "auth-service",    "status": DeploymentStatus.FAILED,      "duration": 450, "commit_sha": "a7b8c9d", "days_ago": 4},
    {"id": "deploy_008", "service": "auth-service",    "status": DeploymentStatus.PENDING,     "duration": 0,   "commit_sha": "b8c9d0e", "days_ago": 0},
    {"id": "deploy_009", "service": "auth-service",    "status": DeploymentStatus.SUCCESS,     "duration": 99,  "commit_sha": "c9d0e1f", "days_ago": 6},
    {"id": "deploy_010", "service": "auth-service",    "status": DeploymentStatus.ROLLED_BACK, "duration": 300, "commit_sha": "d0e1f2a", "days_ago": 10},
    # inventory-service
    {"id": "deploy_011", "service": "inventory-svc",   "status": DeploymentStatus.SUCCESS,     "duration": 75,  "commit_sha": "e1f2a3b", "days_ago": 1},
    {"id": "deploy_012", "service": "inventory-svc",   "status": DeploymentStatus.SUCCESS,     "duration": 80,  "commit_sha": "f2a3b4c", "days_ago": 3},
    {"id": "deploy_013", "service": "inventory-svc",   "status": DeploymentStatus.FAILED,      "duration": 500, "commit_sha": "a3b4c5d", "days_ago": 8},
    {"id": "deploy_014", "service": "inventory-svc",   "status": DeploymentStatus.PENDING,     "duration": 0,   "commit_sha": "b4c5d6e", "days_ago": 0},
    {"id": "deploy_015", "service": "inventory-svc",   "status": DeploymentStatus.SUCCESS,     "duration": 90,  "commit_sha": "c5d6e7f", "days_ago": 12},
    # notification-service
    {"id": "deploy_016", "service": "notification-svc","status": DeploymentStatus.SUCCESS,     "duration": 55,  "commit_sha": "d6e7f8a", "days_ago": 2},
    {"id": "deploy_017", "service": "notification-svc","status": DeploymentStatus.FAILED,      "duration": 280, "commit_sha": "e7f8a9b", "days_ago": 9},
    {"id": "deploy_018", "service": "notification-svc","status": DeploymentStatus.SUCCESS,     "duration": 60,  "commit_sha": "f8a9b0c", "days_ago": 14},
    {"id": "deploy_019", "service": "notification-svc","status": DeploymentStatus.RUNNING,     "duration": 40,  "commit_sha": "a9b0c1d", "days_ago": 0},
    {"id": "deploy_020", "service": "notification-svc","status": DeploymentStatus.SUCCESS,     "duration": 70,  "commit_sha": "b0c1d2e", "days_ago": 20},
    # api-gateway
    {"id": "deploy_021", "service": "api-gateway",     "status": DeploymentStatus.SUCCESS,     "duration": 130, "commit_sha": "c1d2e3f", "days_ago": 1},
    {"id": "deploy_022", "service": "api-gateway",     "status": DeploymentStatus.ROLLED_BACK, "duration": 400, "commit_sha": "d2e3f4a", "days_ago": 6},
    {"id": "deploy_023", "service": "api-gateway",     "status": DeploymentStatus.SUCCESS,     "duration": 110, "commit_sha": "e3f4a5b", "days_ago": 11},
    {"id": "deploy_024", "service": "api-gateway",     "status": DeploymentStatus.FAILED,      "duration": 360, "commit_sha": "f4a5b6c", "days_ago": 15},
    {"id": "deploy_025", "service": "api-gateway",     "status": DeploymentStatus.SUCCESS,     "duration": 120, "commit_sha": "a5b6c7d", "days_ago": 22},
    # user-service
    {"id": "deploy_026", "service": "user-service",    "status": DeploymentStatus.SUCCESS,     "duration": 88,  "commit_sha": "b6c7d8e", "days_ago": 2},
    {"id": "deploy_027", "service": "user-service",    "status": DeploymentStatus.FAILED,      "duration": 510, "commit_sha": "c7d8e9f", "days_ago": 7},
    {"id": "deploy_028", "service": "user-service",    "status": DeploymentStatus.PENDING,     "duration": 0,   "commit_sha": "d8e9f0a", "days_ago": 0},
    {"id": "deploy_029", "service": "user-service",    "status": DeploymentStatus.SUCCESS,     "duration": 95,  "commit_sha": "e9f0a1b", "days_ago": 13},
    {"id": "deploy_030", "service": "user-service",    "status": DeploymentStatus.ROLLED_BACK, "duration": 250, "commit_sha": "f0a1b2c", "days_ago": 18},
    {"id": "deploy_031", "service": "user-service",    "status": DeploymentStatus.SUCCESS,     "duration": 102, "commit_sha": "a1b2c3e", "days_ago": 25},
    {"id": "deploy_032", "service": "billing-api",     "status": DeploymentStatus.SUCCESS,     "duration": 78,  "commit_sha": "b2c3d4f", "days_ago": 30},
]


def seed():
    db = SessionLocal()
    try:
        existing = db.query(DeploymentModel).count()
        if existing:
            print(f"Database already has {existing} records. Skipping seed.")
            return

        now = datetime.now(timezone.utc)
        for event in EVENTS:
            db.add(DeploymentModel(
                id=event["id"],
                service=event["service"],
                status=event["status"],
                duration=event["duration"],
                commit_sha=event["commit_sha"],
                timestamp=now - timedelta(days=event["days_ago"]),
            ))

        db.commit()
        print(f"Seeded {len(EVENTS)} deployment events.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
