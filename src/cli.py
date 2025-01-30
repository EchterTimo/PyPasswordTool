'''
command line interface for this tool
'''

import webbrowser
import art
from colorama import init, Fore, Style

from utils.widgets import Selector, Option, clear_console
from services.evaluate import PasswordEvaluation, MAX_POINTS
from services.update import (
    VersionDetails, determine_version_status, VersionStatus
)

init(autoreset=True)


PROJECT_NAME = "PyPasswordTool"
TITLE = art.text2art(PROJECT_NAME, font="small", space=0)


def handle_version_check():
    '''this file handles the version checking'''
    v = VersionDetails.get()
    if v.fetch_error:
        print("Version check failed")
        print(f"You are currently using {v.current_version}")
        pause()
        return

    status = determine_version_status(v.current_version, v.latest_version)
    if status == VersionStatus.OUTDATED:
        print("A new version is available for this software.")
        print(
            f"{Style.BRIGHT + Fore.RED}{v.current_version}{Style.RESET_ALL}" +
            " -> " +
            f"{Style.BRIGHT + Fore.RED}{v.latest_version}{Style.RESET_ALL}"
        )
        print(v.latest_version_release.html_url)
        input("Do you want to open the url in your web browser")
        choice = input(
            "Do you want to open this link? (y/n): ").strip().lower()
        if choice == "y":
            webbrowser.open(v.latest_version_release.html_url)
            pause()
            return


def pause() -> None:
    '''requires user to press Enter to proceed'''
    input("Press ENTER to continue...")


def menu_evaluate() -> None:
    '''menu for password evaluation'''
    clear_console()
    print(Style.BRIGHT + "Please enter a password to evaluate")
    password_input = input("Password: ")
    pw = PasswordEvaluation.evaluate(password_input)
    print(f"Rating: {pw.rating_colored} ({pw.points} / {MAX_POINTS} Points)")
    print("Suggestions:")
    for sug in pw.suggestions:
        print("- " + sug)
    print()
    pause()


def menu_generate() -> None:
    '''menu for password generation'''
    print("This feature is not available yet.")
    pause()


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
