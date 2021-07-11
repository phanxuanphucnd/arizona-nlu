# -*- coding: utf-8 -*-

import logging

from arizona.version import __version__

def init_logger():
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
        level=logging.INFO,
    )

def print_name(name='nlu'):

    if name == 'nlu':
        print("")
        print('\n'.join([
            ' 🅰 🆁 🅸 🆉 🅾 🅽 🅰  🅽 🅻 🆄  ({})'.format(__version__), 
            ''
        ]))
