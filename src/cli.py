'''
command line interface for this tool
'''

import art

from cli_utils import OptionHandler, Option


def menu_evaluate() -> None:
    raise NotImplementedError


def menu_generate() -> None:
    raise NotImplementedError


def start_cli() -> None:
    '''open the cli loop'''
    art.tprint("PyPasswordTool", font="small", space=0)
    while True:
        handler = OptionHandler([
            Option("1", "Evaluate Password", menu_evaluate),
            Option("2", "Generate Passwords", menu_generate),
            Option("3", "Exit", exit)
        ])
        handler.user_input()


if __name__ == '__main__':
    start_cli()
