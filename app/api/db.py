import databases
import pytz as pytz
import sqlalchemy
from pydantic import BaseSettings
from sqlalchemy.dialects.postgresql import UUID


class DbSettings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str = 'db'
    POSTGRES_PORT: int = 5432

    @property
    def db_url(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@" \
               f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}"


db_settings = DbSettings()
database = databases.Database(db_settings.db_url)
metadata = sqlalchemy.MetaData()

readings = sqlalchemy.Table(
    "readings",
    metadata,
    sqlalchemy.Column("reading_uuid", UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column("patient_uuid", UUID(as_uuid=True)),
    sqlalchemy.Column("recorded_at", sqlalchemy.DateTime(timezone=pytz.UTC)),
    sqlalchemy.Column("unit", sqlalchemy.String),
    sqlalchemy.Column("value", sqlalchemy.Float),
)


engine = sqlalchemy.create_engine(db_settings.db_url)
metadata.create_all(engine)
