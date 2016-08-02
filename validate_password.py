"""Password Validator.

Some Rules
------------
- Password must contain 8 charachters.
- Password must contain mix of letters, numbers and special charachters.
- Password must contain atleast 1 letter in upper caps.
- Password must contain atleast 1 number.
- Password must contain atleast one of the following charachters. *()&%$#_@

Some extra rules to be implemented in next release.
---------------------------------------------------
- Password must be changed once in every 30 days.(may be set to a higher value)
- Old password may not be reused.
- Password may not be a word found in standard dictionary of English language.
"""


class ValidatePassword(object):
    """Module for django password validator.

    Utility Used for validation of password strength should be replaced
    in django 1.9 with AUTH_PASSWORD_VALIDATORS.
    """

    __MIN_LENGTH = 8
    __MIN_DIGIT = 1
    __MIN_UPPER = 1
    __MIN_SYMBOL = 1
    __ALLOWED_SYMBOLS = ['*', '(', ')', '&', '%', '$', '#', '_', '@']
    _flag = False

    def __init__(self, password, *args, **kwargs):
        """Constructor for password validator util."""
        self._password = password

    def lenthg_validator(self):
        """Length validator. Min length should be 8."""
        return True if len(self._password) >= self.__MIN_LENGTH else False

    def check_digit(self):
        """Check for digit member if password string."""
        return True if True in map(self.check_int, self._password) else False

    def check_int(self, x):
        """Checking Intger for each element in password via map."""
        return True if x.isdigit() else False

    def validate(self):
        """Validate method for the util to sum up the result."""
        # Check for Length Validation return False if fails.
        self._flag = self.lenthg_validator()
        if not self._flag: return self._flag, "Password is too short."

        # Check for Integer Validation return False if fails.
        if self.__MIN_DIGIT:
            self._flag = self.check_digit()
            if not self._flag: return self._flag, "Password should contain atleast one Integer."

        return True if self._flag else False
