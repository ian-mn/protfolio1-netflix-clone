from pydantic import BaseModel


class Transform:
    def __init__(self, model: BaseModel) -> None:
        self.model = model

    def transform(self, batch: list) -> list[dict]:
        """Transforms rows from PostgreSQL to Elasticsearch bulk actions.

        Args:
        batch (List): List of rows from PostgreSQL.

        Returns:
            list[dict]: Bulk query text.
        """
        batch = [self.model.parse_obj(row) for row in batch]
        bulk_actions = [
            {
                "_index": self.model.__index__,
                "_id": row.id,
                "_source": row.json(ensure_ascii=False),
            }
            for row in batch
        ]
        return bulk_actions
