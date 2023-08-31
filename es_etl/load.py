from backoff import backoff
from elasticsearch import Elasticsearch, helpers
from logger import logger
from pydantic import BaseModel
from queries.indices import INDICES
from settings import get_settings


class Load:
    def __init__(self, model: BaseModel) -> None:
        es_settings = get_settings().es
        url = f"http://{es_settings.host}:{es_settings.port}"
        self.es = Elasticsearch(url, max_retries=0, retry_on_timeout=0)
        self.model = model
        self.__load_index()

    @backoff()
    def __load_index(self) -> None:
        """Loads index into Elasticsearch."""
        index_name = self.model.__index__
        if not self.es.indices.exists(index=index_name):
            logger.info(f"Creating ES index '{index_name}'")
            self.es.indices.create(
                index=index_name,
                mappings=INDICES[index_name]["mappings"],
                settings=INDICES[index_name]["settings"],
            )
        else:
            logger.info(f"ES index '{index_name}' already exists.")

    @backoff()
    def bulk(self, actions: list[dict]) -> None:
        """Bulk loads actions into Elasticsearch.

        Args:
            actions (list[dict]): Bulk query.
        """
        logger.info("Bulk loading to Elasticsearch.")
        logger.info(actions)
        helpers.bulk(self.es, actions)
