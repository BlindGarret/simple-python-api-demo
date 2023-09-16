import os
from typing import Optional

from sqlmodel import create_engine, Session


class Database:
    instance = None
    engine = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.engine = create_engine(
                f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")
        return cls.instance


def get_db_engine():
    return Database().engine


def get_db_session() -> Optional[Session]:
    if Database().engine is None:
        return None
    return Session(Database().engine)
