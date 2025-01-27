'''
evaluate passwords
'''

from dataclasses import dataclass
from generate import SPECIAL_CHARACTERS


@dataclass
class PasswordEvaluation:
    '''
    logic for evaluation passwords and provide feedback
    '''

    text: str
    points: str
    suggestions: list[str]

    @staticmethod
    def _get_blacklist(
        file_path: str = "src/services/blacklist.txt"
    ) -> list[str]:
        '''
        read a text file with bad passwords
        '''
        with open(file_path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file]

    @property
    def rating(self) -> str:
        '''
        Get a rating based on the amount of points
        '''
        if self.points < 7:
            return "Weak"
        elif self.points >= 7:
            return "Medium"
        elif self.points > 10:
            return "Strong"

    def __repr__(self):
        '''
        repr for pw that hides the pw and only shows basic information
        '''
        return (f"PasswordEvaluation(points={self.points}, "
                f"rating='{self.rating}', "
                f"suggestions_amount={len(self.suggestions)})")

    @classmethod
    def evaluate(cls, password: str):
        '''
        evaluate the given password
        '''

        suggestions: list[str] = []
        points: int = 0

        # Check length
        if len(password) > 7:
            points += 2
        elif len(password) > 15:
            points += 3
        else:
            suggestions.append(
                "Password should be at least 8 characters long.")

        # Check for uppercase letters
        if not any(char.isupper() for char in password):
            suggestions.append("Include at least one uppercase letter.")
        else:
            points += 1

        # Check for lowercase letters
        if not any(char.lower() for char in password):
            suggestions.append("Include at least one lowercase letter.")
        else:
            points += 1

        # Check for numbers
        if not any(char.isdigit() for char in password):
            suggestions.append("Include at least one number.")
        else:
            points += 2

        # Check for special characters
        if not any(char in SPECIAL_CHARACTERS for char in password):
            suggestions.append(
                f"Include at least one special character (e.g. {
                    ','.join(SPECIAL_CHARACTERS)})")
        else:
            points += 2

        # Check for commonly used passwords (example, extend as needed)
        for forbidden_word in cls._get_blacklist():
            if forbidden_word in password.lower():
                suggestions.append(
                    f"Your password '{password}' should not include '{
                        forbidden_word}'.")

        if " " in password:
            suggestions.append("Avoid using spaces in your password.")

        return PasswordEvaluation(
            text=password,
            points=points,
            suggestions=suggestions
        )


if __name__ == '__main__':
    pw_eval = PasswordEvaluation.evaluate("123password")
    print(pw_eval)
    for sug in pw_eval.suggestions:
        print(sug)
