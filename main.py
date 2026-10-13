
import os
import requests

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("Falta configurar o token do Telegram")

print("Robô iniciado. Token encontrado.")
