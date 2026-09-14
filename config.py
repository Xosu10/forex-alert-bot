import os

from dotenv import load_dotenv

load_dotenv()


def _int_env(name, default):
    value = os.environ.get(name, "")
    return int(value) if value else default


DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL", "")

REMINDER_MINUTES_BEFORE = _int_env("REMINDER_MINUTES_BEFORE", 60)
ALERT_MINUTES_BEFORE = _int_env("ALERT_MINUTES_BEFORE", 30)
ACTUAL_CHECK_WINDOW_MINUTES = _int_env("ACTUAL_CHECK_WINDOW_MINUTES", 60)

# Hora (España) a la que se envían el resumen diario y, los lunes, el resumen semanal
SUMMARY_HOUR = _int_env("SUMMARY_HOUR", 1)
