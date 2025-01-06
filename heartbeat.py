import time
import requests

# URL do heartbeat
url = "https://uptime.betterstack.com/api/v1/heartbeat/vJP7STeKQL5JKBFHsn2DzDkj"

while True:
    try:
        response = requests.get(url)
        print(f"Heartbeat enviado. Código de status: {response.status_code}")
    except requests.RequestException as e:
        print(f"Ocorreu um erro: {e}")
    time.sleep(30)  # Aguarda 30 segundos antes de enviar novamente
