from datetime import datetime
from zoneinfo import ZoneInfo

MADRID_TZ = ZoneInfo("Europe/Madrid")


def _local_time(event):
    return datetime.fromisoformat(event["date"]).astimezone(MADRID_TZ).strftime("%d/%m/%Y %H:%M")


def build_message(event, notification_type, now):
    time_str = _local_time(event)

    if notification_type == "before":
        event_time = datetime.fromisoformat(event["date"])
        minutes_left = max(0, round((event_time - now).total_seconds() / 60))
        return (
            f"\U0001F534 USD — Impacto ALTO en {minutes_left} minutos\n\n"
            f"\U0001F4CC {event['title']}\n"
            f"\U0001F552 {time_str} (hora España)\n"
            f"\U0001F4CA Previsión: {event['forecast'] or 'N/D'}   |   Anterior: {event['previous'] or 'N/D'}"
        )

    return (
        f"✅ USD — Dato publicado: {event['title']}\n\n"
        f"\U0001F552 {time_str} (hora España)\n"
        f"\U0001F4CA Real: {event.get('actual') or 'N/D'}   |   Previsión: {event['forecast'] or 'N/D'}   |   Anterior: {event['previous'] or 'N/D'}"
    )
