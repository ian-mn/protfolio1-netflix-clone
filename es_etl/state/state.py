from datetime import datetime, timezone

from settings import get_settings
from state.storage import JSONStorage, RedisStorage


class State:
    """Provides methods to get and set key, value pair of string and datetime converted to string."""

    DEFAULT_VALUE = datetime(2022, 1, 1, 0, 0, 0, 0, timezone.utc)
    IS_RUNNING_KEY = "is_running"

    def __init__(self, model) -> None:
        self.model = model
        if get_settings().use_redis_storage:
            self.storage = RedisStorage()
        else:
            self.storage = JSONStorage()

    def get_etl_state(self) -> str:
        """Gets ETL state value from storage.
        If key doesn't exist, returns default date.

        Returns:
            str: datetime converted to string.
        """
        value = self.storage.get(self.model.__index__)
        if value:
            return value
        return str(self.DEFAULT_VALUE)

    def set_etl_state(self, value: datetime) -> None:
        """Sets value to a ETL state key. Value is converted to string.

        Args:
            value (datetime): Datetime value.

        Raises:
            ValueError: if key is not string or value is not datetime raises exception.
        """
        if type(value) != datetime:
            raise ValueError
        self.storage.set(self.model.__index__, str(value))

    def is_running(self) -> bool:
        status = self.storage.get(self.IS_RUNNING_KEY)
        if status:
            return status == "True"
        return False

    def set_running(self):
        self.storage.set(self.IS_RUNNING_KEY, "True")

    def set_finished(self):
        self.storage.set(self.IS_RUNNING_KEY, "False")
