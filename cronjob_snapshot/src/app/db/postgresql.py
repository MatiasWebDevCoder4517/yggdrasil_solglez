# Standard Library
from typing import Generator

# External
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker

# Project
from app.config import (
    LOGGER,
    POSTGRESQL_DATABASE,
    POSTGRESQL_PASSWORD,
    POSTGRESQL_PORT,
    POSTGRESQL_SERVER,
    POSTGRESQL_USER,
)


DATABASE_URL = f"postgresql://{POSTGRESQL_USER}:{POSTGRESQL_PASSWORD}@{POSTGRESQL_SERVER}:{POSTGRESQL_PORT}/{POSTGRESQL_DATABASE}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        LOGGER.info("Database session opened.")
        yield db
    except SQLAlchemyError as e:
        LOGGER.error(f"An error occurred in db: {db}")
        LOGGER.debug(e)
    finally:
        db.close()
        LOGGER.info("Database session closed.")
