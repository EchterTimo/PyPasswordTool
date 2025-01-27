'''
widgets (abstractions) for the the cli
'''

from dataclasses import dataclass
from typing import Callable


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
    ask_again: bool = True
    clear_console_before: bool = False
    input_prefix: str = "> "

    def _perform_input(self) -> str:
        '''use the default input func'''
        print(self.question)
        for o in self.options:
            print(f" [{o.value}] {o.description}")
        return input(self.input_prefix)

    def get_option(self) -> Option:
        '''
        let the user decide for an option. returns the options.
        '''
        user_input = self._perform_input()
        for option in self.options:
            if option.value.lower() == user_input.lower():
                return option
        return self.default_option

    def run_option(self) -> None:
        '''
        let the user decide for an option. runs the options function.
        There should be a func for every Option. Including the default case.
        If the func is None no code will be executed
        '''
        option = self.get_option()
        if option:
            option.func()


@dataclass
class IntegerInput:
    ...


@dataclass
class BooleanInput:
    ...
