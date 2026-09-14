from datetime import datetime
from zoneinfo import ZoneInfo

MADRID_TZ = ZoneInfo("Europe/Madrid")

TRADING_PROCEDURE = (
    "\U0001F4CB **PROCEDIMIENTO OBLIGATORIO**\n\n"
    "**1️⃣ Cerrar la posición 20 minutos antes**\n"
    "**NO** está permitido dejar un trade abierto durante una noticia roja. "
    "Debes **cerrar manualmente todo en ambos lados** (futuros y broker) **20 minutos antes** "
    "de que se publique la noticia.\n"
    "Motivo: la volatilidad de eventos de alto impacto (NFP, CPI, PMI, etc.) no afecta por igual "
    "a futuros y al broker, lo que puede provocar descalibres graves o pérdidas simultáneas en ambas plataformas.\n\n"
    "**2️⃣ Respetar el margen posterior**\n"
    "Espera 20 minutos después de la publicación de la noticia antes de volver a ejecutar cualquier operación.\n\n"
    "**3️⃣ Retomar el trade el mismo día, recalculando la cuenta**\n"
    "Transcurridos los 20 minutos, retoma la operación el mismo día recalculando tus objetivos de "
    "Take Profit (TP) y Stop Loss (SL) según la ganancia o pérdida acumulada antes del cierre pre-noticia:\n"
    "• Día 1: cerraste con +$300 en futuros → nuevo TP $1,200 / nuevo SL $2,300\n"
    "• Día 2: cerraste con -$500 en futuros → nuevo TP $2,000 / nuevo SL $1,500\n"
    "• Día Clave: cerraste con -$100 en futuros → nuevo TP $3,100 / nuevo SL $1,900\n\n"
    "Nota: ajusta las comisiones sumando $1 al TP y restando $1 al SL por cada contrato/unidad ejecutado, "
    "y aplica la regla de los 3 puntos para posicionar los niveles en el broker."
)


def _local_time(event):
    return datetime.fromisoformat(event["date"]).astimezone(MADRID_TZ).strftime("%d/%m/%Y %H:%M")


def build_message(event, notification_type, now):
    time_str = _local_time(event)

    if notification_type == "reminder_1h":
        event_time = datetime.fromisoformat(event["date"])
        minutes_left = max(0, round((event_time - now).total_seconds() / 60))
        return (
            f"\U0001F7E0 USD — Impacto ALTO en {minutes_left} minutos\n\n"
            f"\U0001F4CC {event['title']}\n"
            f"\U0001F552 {time_str} (hora España)\n"
            f"\U0001F4CA Previsión: {event['forecast'] or 'N/D'}   |   Anterior: {event['previous'] or 'N/D'}\n\n"
            f"{TRADING_PROCEDURE}"
        )

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
