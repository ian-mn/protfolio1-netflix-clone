import math
from functools import wraps
from time import sleep

from logger import logger
from settings import get_settings


def backoff_generator():
    """Exponential backoff decorator if function fails."""

    def decorator_backoff(func):
        @wraps(func)
        def wrapper_backoff(*args, **kwargs):
            n = 0
            while True:
                try:
                    for i in func(*args, **kwargs):
                        yield i
                    break
                except Exception as e:
                    logger.error(e)
                    backoff_sleep(n)
                    n += 1

        return wrapper_backoff

    return decorator_backoff


def backoff():
    """Exponential backoff decorator if function fails."""

    def decorator_backoff(func):
        @wraps(func)
        def wrapper_backoff(*args, **kwargs):
            n = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.error(e)
                    backoff_sleep(n)
                    n += 1

        return wrapper_backoff

    return decorator_backoff


def backoff_sleep(n) -> None:
    """Sleeps for
    t = start_sleep_time * factor ^ n if t < border_sleep_time
    t = border_sleep_time if t >= border_sleep_time
    """

    settings = get_settings().backoff

    t = settings.start_sleep_time * math.pow(settings.sleep_factor, n)
    if t >= settings.border_sleep_time:
        t = settings.border_sleep_time
    logger.error(f"Backoff for {round(t)} seconds.")
    sleep(t)
