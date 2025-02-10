# password_generator.py
import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_numbers=True, use_special=True):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("At least one character type must be selected.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_strength(password):
    """Evaluate the strength of the password."""
    length = len(password)
    
    upper_count = sum(1 for c in password if c.isupper())
    lower_count = sum(1 for c in password if c.islower())
    digit_count = sum(1 for c in password if c.isdigit())
    special_count = sum(1 for c in password if c in string.punctuation)

    upper_percent = (upper_count / length) * 100
    lower_percent = (lower_count / length) * 100
    digit_percent = (digit_count / length) * 100
    special_percent = (special_count / length) * 100
    length_score = (length / 32) * 100

    score = (upper_percent * 0.275) + (lower_percent * 0.175) + (digit_percent * 0.4) + (special_percent * 0.7) + (length_score * 0.75)

    if score <= 50:
        strength = "Weak"
    elif score < 80:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, score
