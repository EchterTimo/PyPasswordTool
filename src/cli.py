'''
command line interface for this tool
'''

import art
from utils.widgets import Selector, Option


def menu_evaluate() -> None:
    '''menu for password evaluation'''
    raise NotImplementedError


def menu_generate() -> None:
    '''menu for password generation'''
    raise NotImplementedError


def start_cli() -> None:
    '''open the cli loop'''
    art.tprint("PyPasswordTool", font="small", space=0)
    while True:
        s = Selector(
            question="What do you want to do?",
            options=[
                Option("1", "Evaluate Password", menu_evaluate),
                Option("2", "Generate Passwords", menu_generate),
                Option("3", "Exit", exit)
            ]
        )
        s.run_option()


if __name__ == '__main__':
    start_cli()
