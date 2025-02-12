import re

# Make a set of common patterns to avoid
COMMON_PATTERNS = {'123', 'password', 'qwerty', 'abc'}

def check_password_strength(password):
    """Checks password strength based on criteria like length and different characters."""

    # Check length is at least 12 char
    length_criteria = len(password) >= 12
    # Check for at least 1 lowercase char
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    # Check for at least 1 uppercase char
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    # Check for at least 1 digit
    digit_criteria = bool(re.search(r'\d', password))
    # Check for at least 1 special char
    special_char_criteria = bool(re.search(r'[^\w\s]', password))
    # Check for at least 8 different characters by removing duplicates wtih the set function
    unique_chars_criteria = len(set(password)) >= 8

    # Check for common patterns using the set defined above
    common_patterns_check = True
    for pattern in COMMON_PATTERNS:
        if pattern in password.lower():
            common_patterns_check = False
            break

    # Count how many criteria are met
    criteria_met = sum([
        length_criteria,
        lowercase_criteria,
        uppercase_criteria,
        digit_criteria,
        special_char_criteria,
        unique_chars_criteria,
        common_patterns_check
    ])

    # Strength classification
    if criteria_met == 7:
        strength = "Strong 💪"
    elif 5 <= criteria_met < 7:
        strength = "Medium ⚠️"
    else:
        strength = "Weak ❌"

    # Using the criteria variables, give feedback on the password
    feedback = []
    if not length_criteria:
        feedback.append("Make sure password is 12 characters long.")
    if not lowercase_criteria:
        feedback.append("Include lowercase letters.")
    if not uppercase_criteria:
        feedback.append("Include uppercase letters.")
    if not digit_criteria:
        feedback.append("Include digits.")
    if not special_char_criteria:
        feedback.append("Use special characters like (@, #, $, etc.).")
    if not unique_chars_criteria:
        feedback.append("Use multiple characters.")
    if not common_patterns_check:
        feedback.append("Avoid common phrases and patterns like 'password' or '123'.")
    return strength, feedback


def main():
    password = input("Enter your password: ")
    strength, feedback = check_password_strength(password)
    print(f"\nPassword Strength: {strength}\n")
    if feedback:
        print("Suggestions to improve:")
        for item in feedback:
            print(f"   - {item}")


if __name__ == "__main__":
    main()
