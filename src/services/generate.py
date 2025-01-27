'''
generate passwords
'''

import os
import random
import string


from dataclasses import dataclass
import pyperclip

AMBIGUOUS_CHARACTERS = set(["O", "0", "l", "1", "I", "~", "-", ",", "."])
DOWNLOADS_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")
SPECIAL_CHARACTERS = "!@#$%^&*()-_+=<>?"


@dataclass
class Password:
    '''
    Class for creating and exporting passwords
    '''
    text: str

    def copy_to_clipboard(self):
        '''
        Copy the current password to the clipboard
        '''
        pyperclip.copy(self.text)

    @classmethod
    def generate(
        cls,
        use_lower_case: bool,
        use_upper_case: bool,
        use_digits: bool,
        use_special_characters: bool,
        avoid_ambiguous: bool,
        length: int = 8
    ):
        '''
        Generate a password based on the given configuration
        '''
        character_pool: str = ""
        if use_lower_case:
            character_pool += string.ascii_lowercase
        if use_upper_case:
            character_pool += string.ascii_uppercase
        if use_digits:
            character_pool += string.digits
        if use_special_characters:
            character_pool += SPECIAL_CHARACTERS
        if avoid_ambiguous:
            # overwrite the list and remove ambiguous chars
            character_pool = ''.join(
                c for c in character_pool if c not in AMBIGUOUS_CHARACTERS)

        pw_text = ''.join(random.sample(character_pool, length))

        if len(pw_text < 1):
            raise ValueError("Password should be at least one character.")

        return Password(text=pw_text)

    def __str__(self) -> str:
        '''return the current password text'''
        return self.text


@dataclass
class PasswordList:
    '''Util class to hold multiple passwords for exporting purposes'''
    passwords: list[Password]

    def export_as_text_file(self, file_path: str = DOWNLOADS_FOLDER):
        '''Export a list of passwords to a textfile'''
        with open(file_path, "w", encoding="utf-8") as file:
            file.writelines(self.passwords)


if __name__ == '__main__':
    pw = Password.generate(
        length=12,
        use_lower_case=True,
        use_upper_case=True,
        use_digits=True,
        use_special_characters=True,
        avoid_ambiguous=True,
    )
    print(pw.text)
