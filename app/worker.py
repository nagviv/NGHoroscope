import os
from celery import Celery
from celery.schedules import crontab
from datetime import datetime, timezone
from app.config import REDIS_URL

celery_app = Celery("jyotish_tasks", broker=REDIS_URL, backend=REDIS_URL)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Asia/Kolkata",
    enable_utc=True,
    beat_schedule={
        "send-daily-horoscope-morning": {
            "task": "app.worker.dispatch_daily_astrological_digest",
            "schedule": crontab(hour=6, minute=30),
        }
    }
)

@celery_app.task
def dispatch_daily_astrological_digest():
    from app.db import SessionLocal
    from app.models.entities import User, SavedProfile
    from app.services.notification_service import NotificationService

    db = SessionLocal()
    try:
        users = db.query(User).filter(User.notifications_enabled == True).all()
        now = datetime.now(timezone.utc)
        for user in users:
            primary_profile = db.query(SavedProfile).filter(
                SavedProfile.user_id == user.id,
                SavedProfile.relationship_label == "Self"
            ).first()
            if primary_profile:
                NotificationService.send_daily_digest(user, primary_profile, now)
        return {"status": "success", "processed_users": len(users)}
    finally:
        db.close()
