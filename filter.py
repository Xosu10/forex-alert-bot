def filter_usd_high(events):
    """Se queda solo con los eventos de divisa USD e impacto alto (carpeta roja)."""
    return [e for e in events if e.get("country") == "USD" and e.get("impact") == "High"]
