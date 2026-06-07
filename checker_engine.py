def analyze_password(password):
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special_char = False
    special_chars = "!@#$%^&*()-_=+[]{}|;:'\".<>?/"

    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special_char = True

    is_length_ok = len(password) >= 8

    return {
        "is_length_ok": is_length_ok,
        "has_lowercase": has_lowercase,
        "has_uppercase": has_uppercase,
        "has_digit": has_digit,
        "has_special_char": has_special_char,
        "is_strong": is_length_ok and has_lowercase and has_uppercase and has_digit and has_special_char  
    }