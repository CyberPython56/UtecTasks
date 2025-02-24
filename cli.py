import click
from tasks import get_response

@click.command()
@click.argument('ip')
@click.argument('port')
def get_response_task(ip, port):
    res = get_response.delay(ip, port)
    click.echo(f'Задача запущена: {res.id}')


if __name__ == '__main__':
    get_response_task()
