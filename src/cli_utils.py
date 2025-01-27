'''
util classes and functions for the cli
'''

from dataclasses import dataclass
from typing import Callable


@dataclass
class Option:
    value: str
    description: str
    action: Callable

    def run(self):
        '''run the linked action'''
        return self.action()


@dataclass
class OptionHandler:
    '''
    abstraction for handling user inputs
    including input validation and action
    '''
    options: list[Option]
    default_option: Option = None

    def user_input(self, user_input: str):
        '''let the user input something'''
        for option in self.options:
            if user_input == option.value:
                option.run()
