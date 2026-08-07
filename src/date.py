"""Date functions."""

import datetime


def today_str() -> str:
    """Return the current date in the local timezone as string."""
    return datetime.datetime.now(tz=datetime.UTC).astimezone().strftime("%d-%m-%Y")
