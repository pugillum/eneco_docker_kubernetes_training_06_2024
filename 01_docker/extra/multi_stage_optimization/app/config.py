import os

PROJECT_NAME = "phresh"
VERSION = "1.0.0"
API_PREFIX = "/api"
POSTGRES_HOST = os.environ.get("PG_HOST", "postgres")
POSTGRES_PORT = os.environ.get("PG_PORT", "5432")
POSTGRES_USER = os.environ.get("PG_USER", "postgres")
POSTGRES_PASSWORD = os.environ.get("PG_PASSWORD")
POSTGRES_DB = os.environ.get("PG_DATABASE", "postgres")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
print(DATABASE_URL)
