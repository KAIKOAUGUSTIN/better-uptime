import time
import requests

while True:
    try:
        response = requests.get("https://status.kaioaugusto.com/api/push/ViuggxT4wa?status=up&msg=OK&ping=")
        print(f"Heartbeat enviado. Código de status: {response.status_code}")
    except requests.RequestException as e:
        print(f"Ocorreu um erro: {e}")
    time.sleep(20)
    
