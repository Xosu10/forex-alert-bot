from datetime import datetime
from zoneinfo import ZoneInfo

MADRID_TZ = ZoneInfo("Europe/Madrid")

DIAS_SEMANA = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]


def build_weekly_summary_message(usd_high_events, now_madrid):
    if not usd_high_events:
        return "\U0001F5D3️ Resumen semanal: no hay noticias USD de impacto ALTO esta semana."

    events_sorted = sorted(usd_high_events, key=lambda e: e["date"])

    lines = [
        f"\U0001F5D3️ Resumen semanal: {len(events_sorted)} noticia(s) USD de impacto ALTO esta semana:\n"
    ]
    for event in events_sorted:
        event_time = datetime.fromisoformat(event["date"]).astimezone(MADRID_TZ)
        dia = DIAS_SEMANA[event_time.weekday()]
        lines.append(f"• {dia.capitalize()} {event_time.strftime('%d/%m %H:%M')} — {event['title']}")

    return "\n".join(lines)
