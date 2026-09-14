import requests

FEED_URL = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"


def get_events():
    """Descarga el calendario económico de Forex Factory y lo devuelve como lista de eventos."""
    response = requests.get(FEED_URL, timeout=15)
    response.raise_for_status()
    return response.json()
