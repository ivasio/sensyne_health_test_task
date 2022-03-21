import databases
import sqlalchemy

DATABASE_URL = "sqlite:///./test.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(DATABASE_URL)

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


engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
