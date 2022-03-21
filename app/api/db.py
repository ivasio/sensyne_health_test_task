from pydantic import BaseSettings
import databases
import sqlalchemy


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
print(db_settings.db_url)

database = databases.Database(db_settings.db_url)

metadata = sqlalchemy.MetaData()

readings = sqlalchemy.Table(
    "readings",
    metadata,
    sqlalchemy.Column("reading_uuid", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("patient_uuid", sqlalchemy.String),
    sqlalchemy.Column("recorded_at", sqlalchemy.DateTime),
    sqlalchemy.Column("unit", sqlalchemy.String),
    sqlalchemy.Column("value", sqlalchemy.Float),
)


engine = sqlalchemy.create_engine(db_settings.db_url)
metadata.create_all(engine)
