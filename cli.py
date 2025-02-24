import click
from tasks import get_response


def correct_ip(ip: str):
    return all(x.isdigit() or x == '.' for x in ip) and len(ip.split('.')) == 4 \
            and all(map(lambda x: 0 <= int(x) <= 255 if ip.find('..') == -1 else False, ip.split('.')))

def correct_port(port: str):
    return all(x.isdigit() for x in port) and 0 <= int(port) <= 65535



@click.command()
@click.argument('ip')
@click.argument('port')
def get_response_task(ip: str, port: str):
    if correct_ip(ip) and correct_port(port):
        res = get_response.delay(ip, port)
        click.echo(f'Задача запущена: {res.id}')
    else:
        click.echo('[Error] Ошибка в корректности аргументов')


# 127.0.0.1
if __name__ == '__main__':
    get_response_task()
