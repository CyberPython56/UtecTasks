from celery import Celery
import requests

app = Celery('tasks', backend='rpc://', broker='amqp://guest@localhost//')


# Выполнение GET-запроса к ip и порту
@app.task
def get_response(ip, port):
    try:
        response = requests.get(f'http://{ip}:{port}')
        if response.status_code > 399:  # Проверка кода ответа
            return f'[Error] {response.reason}'  # Возвращаем причину ошибки
        return response.text
    except Exception as e:
        return f"[Error] {e}"

# celery -A tasks worker --loglevel=INFO
# celery -A tasks flower --broker=amqp://guest:guest@${RABBITMQ_SERVICE_SERVICE_HOST:localhost}:5672//
