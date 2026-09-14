from datetime import datetime
from zoneinfo import ZoneInfo

MADRID_TZ = ZoneInfo("Europe/Madrid")


def events_today(usd_high_events, now_madrid):
    """Filtra los eventos cuya fecha (ya en hora de España) cae en el día de hoy."""
    today = now_madrid.date()
    todays = [
        event
        for event in usd_high_events
        if datetime.fromisoformat(event["date"]).astimezone(MADRID_TZ).date() == today
    ]
    return sorted(todays, key=lambda e: e["date"])


def build_daily_summary_message(today_events, now_madrid):
    date_str = now_madrid.strftime("%d/%m/%Y")

    if not today_events:
        return f"\U0001F4C5 Resumen del día ({date_str}): no hay noticias USD de impacto ALTO hoy."

    lines = [f"\U0001F4C5 Resumen del día ({date_str}): {len(today_events)} noticia(s) USD de impacto ALTO:\n"]
    for event in today_events:
        event_time = datetime.fromisoformat(event["date"]).astimezone(MADRID_TZ)
        lines.append(f"• {event_time.strftime('%H:%M')} — {event['title']}")

    return "\n".join(lines)
