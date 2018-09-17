import click


@click.group(invoke_without_command=False)
def wonder():
  pass


@wonder.command()
def world():
  click.echo('what a wonderful world!')


@wonder.command()
@click.argument('name')
def beautiful(name):
  click.echo('{} is beautiful!'.format(name))


if __name__ == '__main__':
  wonder()
