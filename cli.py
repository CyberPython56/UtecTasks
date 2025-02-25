import click
from tasks import get_response
from celery.result import AsyncResult


def correct_ip(ip: str):  # Проверка корректности ip
    return all(x.isdigit() or x == '.' for x in ip) and len(ip.split('.')) == 4 and ip.find('..') == -1 \
        and all(0 <= int(x) <= 255 for x in ip.split('.'))


def correct_port(port: str):  # Проверка корректности порта
    return all(x.isdigit() for x in port) and 0 <= int(port) <= 65535


@click.command()
@click.argument('ip')
@click.argument('port')
def get_response_task(ip: str, port: str):  # Основная функция запуска процесса
    if correct_ip(ip) and correct_port(port):
        result = get_response.delay(ip, port)
        click.echo(f'Результат GET-запроса:\n{result.get(timeout=10)}')
    else:
        click.echo('[Error] Ошибка в корректности аргументов')


if __name__ == '__main__':
    get_response_task()
