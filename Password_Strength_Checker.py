import re
import math
from collections import Counter

def calculate_entropy(password):
    
    if not password:
        return 0

    char_frequency = Counter(password)
    total_chars = sum(char_frequency.values())
    probs = [freq / total_chars for freq in char_frequency.values()]
    entropy = -sum(p * math.log2(p) for p in probs)

    return entropy * total_chars

def is_common_password(password, common_passwords_set):
    
    return password.lower() in common_passwords_set

def password_strength_checker(password, common_passwords_set):
    
    issues = []

    if len(password) < 8:
        issues.append("Password is too short. Consider making it at least 8 characters long.")
    if not re.search(r'[A-Z]', password):
        issues.append("Password lacks uppercase letters. Consider adding some for complexity.")
    if not re.search(r'[a-z]', password):
        issues.append("Password lacks lowercase letters. Consider adding some for complexity.")
    if not re.search(r'\d', password):
        issues.append("Password lacks digits. Consider adding some for complexity.")
    if not re.search(r'[^a-zA-Z\d]', password):
        issues.append("Password lacks special characters. Consider adding some for complexity.")
    if is_common_password(password, common_passwords_set):
        issues.append("Password is too common. Consider using a more unique password.")

    entropy = calculate_entropy(password)
    if entropy < 30:
        strength = "Weak"
    elif entropy < 50:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, issues

common_passwords_set = {"password", "123456", "123456789", "qwerty","0123456789", "12345678", "111111", "1234567890", "1234567", "password1", "12345"}

user_password = input("Enter your password to check its strength: ")
strength, feedback = password_strength_checker(user_password, common_passwords_set)

print(f"Password Strength: {strength}")
if feedback:
    print("Recommendations to improve your password:")
    for issue in feedback:
        print(f"- {issue}")
else:
    print("Your password is strong. No recommendations needed.")
