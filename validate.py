from .validate_password import ValidatePassword

def validate_password(passwrd):
    a = ValidatePassword(passwrd)
    return a.validate()
