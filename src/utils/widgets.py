'''
widgets (abstractions) for the the cli
'''

from dataclasses import dataclass
from typing import Callable

import os


def clear_console() -> None:
    '''clears the terminal'''
    os.system("cls")


@dataclass
class Option:
    '''Option for the Selector Widget'''
    value: str
    description: str
    func: Callable = None


@dataclass
class Selector:
    '''Selctor Widget'''
    question: str
    options: list[Option]
    default_option: Option = None
    show_errors: bool = False
    input_prefix: str = "> "

    @property
    def options_values(self) -> list[str]:
        '''return a list of all possible values'''
        return [option.value for option in self.options]

    def _input_loop(self) -> str:
        '''use the default input func'''
        while True:
            clear_console()

            # print the Selection Menu
            print(self.question)
            print()
            for o in self.options:
                print(f" [{o.value}] {o.description}")

            # get the user input
            user_input = input(self.input_prefix)

            # check if the input is allowed
            if user_input in self.options_values:
                break
        return user_input

    def get_option(self) -> Option:
        '''
        let the user decide for an option. returns the options.
        '''
        user_input = self._input_loop()
        for option in self.options:
            if option.value.lower() == user_input.lower():
                return option
        return self.default_option


@dataclass
class IntegerInput:
    ...


@dataclass
class BooleanInput:
    ...
