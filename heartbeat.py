import time
import requests

while True:
    try:
        response = requests.get("https://uptime.betterstack.com/api/v1/heartbeat/nowwgoPNwDmDEeFNBpgGFAew")
        print(f"Heartbeat enviado. Código de status: {response.status_code}")
    except requests.RequestException as e:
        print(f"Ocorreu um erro: {e}")
    time.sleep(30)  # Aguarda 30 segundos antes de enviar novamente
