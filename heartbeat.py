import time
import requests

while True:
    try:
        response = requests.get("http://192.168.15.11:3001/api/push/lxJtwEUBk0?status=up&msg=OK&ping=")
        print(f"Heartbeat enviado. Código de status: {response.status_code}")
    except requests.RequestException as e:
        print(f"Ocorreu um erro: {e}")
    time.sleep(20)
    
