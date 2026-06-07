import secrets
import string

def Generator(length=12, use_uppercase=True, use_special_chars=True, use_digits=True):

    alphabet = string.ascii_lowercase

    if use_uppercase:
        alphabet += string.ascii_uppercase
    if use_digits:
        alphabet += string.digits
    if use_special_chars:
        alphabet += string.punctuation

    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password
