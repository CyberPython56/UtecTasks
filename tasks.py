from celery import Celery
import requests

app = Celery('tasks')

# Выполнение GET-запроса к ip и порту
@app.task
def get_response(ip, port):
    try:
        return f'[OK] {requests.get(f'http://{ip}:{port}').text}'
    except Exception as e:
        return f"[Error] {e}"

