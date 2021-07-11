# -*- coding: utf-8 -*-

import click

from arizona.nlu.cli import nlu

@click.group()
def entry_point():
    pass

@click.command()
def check_install():
    try:
        print(f"Successfully!")
    except Exception as e:
        print(f"Error: {e}")


# Command: nlu
entry_point.add_command(nlu)

# Command: check
entry_point.add_command(check_install)


if __name__ == '__main__':
    entry_point()
