'''
generate passwords
'''

import random
import string
from dataclasses import dataclass

AMBIGUOUS_CHARACTERS = set(["O", "0", "l", "1", "I", "~", "-", ",", "."])

class Password:
    text: str

    @classmethod
    def generate(
        cls,
        length: int,
        use_lower_case: bool,
        use_upper_case: bool,
        use_digits: bool,
        use_special_characters: bool,
        avoid_ambiguous: bool
    ):
        character_pool: str = ""
        if use_lower_case:
            character_pool += string.ascii_lowercase
        if use_upper_case:
            character_pool += string.ascii_uppercase
        if use_digits:
            character_pool += string.digits
        if use_special_characters:
            character_pool += "!@#$%^&*()-_+=<>?"
        if avoid_ambiguous:
            # overwrite the list and remove ambiguous chars
            characters = ''.join(
                c for c in characters if c not in AMBIGUOUS_CHARACTERS)
        
        return random.sample(characters, length)