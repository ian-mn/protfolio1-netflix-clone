from contextlib import contextmanager

import psycopg2
from backoff import backoff_generator
from logger import logger
from psycopg2.extras import DictCursor
from pydantic import BaseModel
from settings import get_settings


class Extract:
    def __init__(self, model: BaseModel) -> None:
        self.pg = get_settings().pg
        self.batch_size = get_settings().batch_size
        self.model = model

    @contextmanager
    def __conn_context(self):
        """PostgreSQL connection context manager."""
        conn = psycopg2.connect(**self.pg.dict(), cursor_factory=DictCursor)
        psycopg2.extras.register_uuid()
        yield conn
        conn.close()

    @backoff_generator()
    def iterbatches(self, etl_state: str):
        """Yields batch from specified table and update date.

        Args:
            params (dict): Dictionary with table name and table state.
        """
        with self.__conn_context() as conn:
            logger.info("Extracting from PostgreSQL.")
            curs = conn.cursor()
            query = self.model.__query__(etl_state)
            curs.execute(query)
            while rows := curs.fetchmany(self.batch_size):
                logger.info(f"Extracted {len(rows)} rows.")
                yield rows
