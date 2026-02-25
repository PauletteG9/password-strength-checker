import re


def check_password_strength(password):
    strength_score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        strength_score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        strength_score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Digit Check
    if re.search(r"[0-9]", password):
        strength_score += 1
    else:
        feedback.append("Add at least one digit.")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_score += 1
    else:
        feedback.append("Add at least one special character.")

    return strength_score, feedback


def main():
    print("🔐 Password Strength Checker")
    password = input("Enter your password: ")

    score, feedback = check_password_strength(password)

    if score == 5:
        print("✅ Strong Password!")
    elif score >= 3:
        print("⚠️ Moderate Password")
    else:
        print("❌ Weak Password")

    if feedback:
        print("\nSuggestions:")
        for tip in feedback:
            print("-", tip)


if __name__ == "__main__":
    main()