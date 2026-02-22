import boto3
from dotenv import load_dotenv
from flask import Blueprint, Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from polyglot.adapters.app_db import mappings as _db_mappings  # noqa: F401
from polyglot.adapters.app_db.settings import Settings as DB_Settings
from polyglot.adapters.app_db.uow import SqlAlchemyUnitOfWork
from polyglot.adapters.http.api import create_api
from polyglot.adapters.http.pages import create_app_pages
from polyglot.adapters.http.settings import Settings as HTTP_Settings
from polyglot.adapters.object_storage import ObjectStorage
from polyglot.adapters.object_storage.settings import Settings as OS_Settings
from polyglot.application.application import TaskService

load_dotenv()


class Settings:
    db = DB_Settings()
    object_storage = OS_Settings()
    http_settings = HTTP_Settings()


class S3:
    s3_client = boto3.client(
        "s3",
        endpoint_url=Settings.object_storage.MINIO_ENDPOINT,
        aws_access_key_id=Settings.object_storage.MINIO_ACCESS_KEY,
        aws_secret_access_key=Settings.object_storage.MINIO_SECRET_KEY,
    )

    object_storage = ObjectStorage(
        s3_client=s3_client,
        bucket_name=Settings.object_storage.MINIO_BUCKET,
        expires_in=Settings.object_storage.PRESIGNED_URL_EXPIRES_IN_SECONDS,
    )


class DB:
    engine = create_engine(Settings.db.database_url)
    session_factory = sessionmaker(bind=engine, expire_on_commit=False)

    @staticmethod
    def uow_factory():
        return SqlAlchemyUnitOfWork(DB.session_factory)


upload_file = TaskService(
    object_storage=S3.object_storage,
    uow_factory=DB.uow_factory,
)

app = Flask(
    __name__,
    template_folder=Settings.http_settings.get_path_templates,
)
app.config.from_mapping(Settings.http_settings.to_flask_config)

bp_api = Blueprint("api", __name__, url_prefix="/api/v1/")
bp_api = create_api(
    bp_api,
    upload_file,
    object_storage=S3.object_storage,
)

bp_pages = Blueprint("pages", __name__, url_prefix="/")
bp_pages = create_app_pages(bp_pages)

app.register_blueprint(bp_api)
app.register_blueprint(bp_pages)
