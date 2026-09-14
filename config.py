import os

from dotenv import load_dotenv

load_dotenv()


def _int_env(name, default):
    value = os.environ.get(name, "")
    return int(value) if value else default


DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL", "")

ALERT_MINUTES_BEFORE = _int_env("ALERT_MINUTES_BEFORE", 30)
ACTUAL_CHECK_WINDOW_MINUTES = _int_env("ACTUAL_CHECK_WINDOW_MINUTES", 60)
DAILY_SUMMARY_HOUR = _int_env("DAILY_SUMMARY_HOUR", 8)
