import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

"""
The BaseSettings class from Pydantic is used to define the settings of our application, like the database url, the minio url, etc.
"""


class Settings(BaseSettings):
    app_name: str = "PropertiesAPI"
    db_host: str = os.getenv("DB_HOST")
    db_username: str = os.getenv("DB_USERNAME")
    db_name: str = os.getenv("DB_NAME")
    db_password: str = os.getenv("DB_PASSWORD")
    db_url: str = (
        "postgresql://"
        + db_username
        + ":"
        + db_password
        + "@"
        + db_host
        + "/"
        + db_name
    )
    minio_access_key: str = os.getenv("MINIO_SECRET_KEY")
    minio_secret_key: str = os.getenv("MINIO_SECRET_CODE")
    minio_url: str = os.getenv("MINIO_URL")
    minio_bucket_name: str = os.getenv("MINIO_BUCKET_NAME")


settings = Settings()
