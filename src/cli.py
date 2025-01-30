'''
command line interface for this tool
'''

import art
from utils.widgets import Selector, Option, clear_console
from services.evaluate import PasswordEvaluation, MAX_POINTS
from rich.console import Console
console = Console()

PROJECT_NAME = "PyPasswordTool"
TITLE = art.text2art(PROJECT_NAME, font="small", space=0)


def handle_version_check():
    '''this file handles the version checking'''
    pass  # todo


def pause() -> None:
    '''requires user to press Enter to proceed'''
    input("Press ENTER to continue...")


def menu_evaluate() -> None:
    '''menu for password evaluation'''
    clear_console()
    console.print("[bold]Please enter a password to evaluate.[/bold]")
    password_input = input("Password: ")
    pw = PasswordEvaluation.evaluate(password_input)
    console.print(f"Rating: {pw.rating_colored} ({
                  pw.points} / {MAX_POINTS} Points)")
    print("Suggestions:")
    for sug in pw.suggestions:
        print("- " + sug)
    print()
    pause()


def menu_generate() -> None:
    '''menu for password generation'''
    raise NotImplementedError


def start_cli() -> None:
    '''open the cli loop'''
    handle_version_check()
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
