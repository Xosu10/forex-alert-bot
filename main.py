import logging
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from config import DAILY_SUMMARY_HOUR
from daily_summary import build_daily_summary_message, events_today
from discord_notifier import send_discord_message
from fetch import get_events
from filter import filter_usd_high
from messages import build_message
from notifications import pending_notifications
from storage import build_event_id, init_db, is_notified, mark_notified

MADRID_TZ = ZoneInfo("Europe/Madrid")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger("forex_bot")


def check_daily_summary(usd_high_events, now_utc):
    now_madrid = now_utc.astimezone(MADRID_TZ)
    if now_madrid.hour < DAILY_SUMMARY_HOUR:
        return

    today_key = now_madrid.strftime("%Y-%m-%d")
    if is_notified(today_key, "daily_summary"):
        return

    today_events = events_today(usd_high_events, now_madrid)
    message = build_daily_summary_message(today_events, now_madrid)
    send_discord_message(message)
    mark_notified(today_key, "daily_summary")
    logger.info("Resumen diario enviado (%s eventos hoy)", len(today_events))


def check_event_notifications(usd_high_events, now_utc):
    for event in usd_high_events:
        event_id = build_event_id(event)
        for notification_type in pending_notifications(event, now_utc):
            if is_notified(event_id, notification_type):
                continue

            message = build_message(event, notification_type, now_utc)
            send_discord_message(message)
            mark_notified(event_id, notification_type)
            logger.info("Aviso enviado: %s (%s)", event["title"], notification_type)


def run_cycle():
    now_utc = datetime.now(timezone.utc)
    events = get_events()
    usd_high_events = filter_usd_high(events)

    check_daily_summary(usd_high_events, now_utc)
    check_event_notifications(usd_high_events, now_utc)


def main():
    init_db()
    logger.info("Comprobando calendario económico...")

    try:
        run_cycle()
    except Exception:
        logger.exception("Error en esta comprobación. Se reintentará en la siguiente ejecución programada.")

    logger.info("Comprobación terminada.")


if __name__ == "__main__":
    main()
