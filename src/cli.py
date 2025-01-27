'''
command line interface for this tool
'''

import art
from utils.widgets import Selector, Option

TITLE = art.text2art("PyPasswordTool", font="small", space=0)


def menu_evaluate() -> None:
    '''menu for password evaluation'''
    raise NotImplementedError


def menu_generate() -> None:
    '''menu for password generation'''
    raise NotImplementedError


def start_cli() -> None:
    '''open the cli loop'''
    while True:
        s = Selector(
            question=TITLE + "\nWhat do you want to do?",
            options=[
                Option("1", "Evaluate Password", menu_evaluate),
                Option("2", "Generate Passwords", menu_generate),
                Option("3", "Exit", exit)
            ]
        )
        s.get_option().func()  # run the mapped function


if __name__ == '__main__':
    start_cli()
