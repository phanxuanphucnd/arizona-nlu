# -*- coding: utf-8 -*-

from arizona.run_cli import entry_point
import click
from click.utils import echo

from arizona.utils.print_utils import print_name

@click.group()
def nlu():
    print_name(name='nlu')
    pass


if __name__ == '__main__':
    nlu()