"""Envía un mensaje de prueba al webhook configurado en DISCORD_WEBHOOK_URL (archivo .env)."""
from discord_notifier import send_discord_message

send_discord_message(
    "\U0001F9EA Mensaje de prueba del bot de alertas Forex Factory. Si ves esto, el webhook funciona."
)
print("Mensaje de prueba enviado. Revisa tu canal de Discord.")
