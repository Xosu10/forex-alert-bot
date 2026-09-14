from datetime import datetime

from config import ACTUAL_CHECK_WINDOW_MINUTES, ALERT_MINUTES_BEFORE


def pending_notifications(event, now):
    """Devuelve qué avisos tocan ahora mismo para este evento: 'before', 'actual', ambos o ninguno."""
    event_time = datetime.fromisoformat(event["date"])
    seconds_until = (event_time - now).total_seconds()
    types = []

    if 0 <= seconds_until <= ALERT_MINUTES_BEFORE * 60:
        types.append("before")

    seconds_since = -seconds_until
    if 0 <= seconds_since <= ACTUAL_CHECK_WINDOW_MINUTES * 60 and event.get("actual"):
        types.append("actual")

    return types
