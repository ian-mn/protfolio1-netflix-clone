from extract import Extract
from load import Load
from logger import logger
from pydantic import BaseModel
from state.state import State
from transform import Transform


class ETL:
    def __init__(self, model: BaseModel) -> None:
        logger.info("Setting connections to PostgreSQL, Redis and Elasticsearch")
        self.model = model
        self.extract = Extract(model)
        self.state = State(model)
        self.transform = Transform(model)
        self.load = Load(model)

    def try_start(self) -> None:
        """Starts ETL process if another process is not running."""
        if self.state.is_running():
            logger.warning("Another process is running")
        else:
            self.state.set_running()
            self.__start()
            self.state.set_finished()

    def __start(self) -> None:
        """Extracts data from PostgreSQL,
        transforms it to bulk query, loads into Elasticsearch."""

        etl_state = self.state.get_etl_state()

        for batch in self.extract.iterbatches(etl_state):
            logger.info(batch)
            bulk_query = self.transform.transform(batch)
            self.load.bulk(bulk_query)

            last_row = batch[-1]
            self.state.set_etl_state(last_row["modified"])
