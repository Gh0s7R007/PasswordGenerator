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
    if length < 8:
        return "Weak"
    elif length < 12:
        return "Medium"
    else:
        return "Strong"

def user_input():
    """Get user-defined parameters for password generation."""
    length = int(input("Enter password length (8 to 32): "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    if length < 8 or length > 32:
        print("Length must be between 8 and 32.")
        return None
    
    return length, use_upper, use_lower, use_numbers, use_special

if __name__ == '__main__':
    params = user_input()
    if params:
        length, use_upper, use_lower, use_numbers, use_special = params
        generated_password = generate_password(length, use_upper, use_lower, use_numbers, use_special)
        strength = password_strength(generated_password)
        
        print(f"Generated Password: {generated_password}")
        print(f"Password Strength: {strength}")