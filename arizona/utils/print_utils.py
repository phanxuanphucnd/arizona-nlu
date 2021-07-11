# -*- coding: utf-8 -*-

from arizona.version import __version__

def print_name(name='nlu'):

    if name == 'nlu':
        print("")
        print('\n'.join([
            ' 🅰 🆁 🅸 🆉 🅾 🅽 🅰  🅽 🅻 🆄  ({})'.format(__version__), 
            ''
        ]))
