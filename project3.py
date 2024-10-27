def evaluate_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    number_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(char in "!@#$%^&*(),.?\":{}|<>" for char in password)

    criteria_met = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        number_criteria,
        special_char_criteria
    ])

    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character.")

    strength = "Weak"
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"

    print(f"Password Strength: {strength}")
    if feedback:
        print("Suggestions to improve your password:")
        for suggestion in feedback:
            print(f" - {suggestion}")

def main():
    print("Password Strength Assessment Tool")
    password = input("Enter your password to assess its strength: ")
    evaluate_password_strength(password)

if __name__ == "__main__":
    main()