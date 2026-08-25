import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
SECRET_KEY = os.getenv("SECRET_KEY", "JYOTISH_PRODUCTION_SUPER_SECRET_KEY")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./jyotish.db")
