import re

def assess_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Number check
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    # Special character check
    if re.search(r'[\W_]', password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$ etc.).")

    # Strength rating
    if score == 5:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }


# Example usage
password = input("Enter a password: ")
result = assess_password_strength(password)

print(f"\nStrength: {result['strength']} ({result['score']}/5)")
if result["feedback"]:
    print("Suggestions:")
    for f in result["feedback"]:
        print(f"- {f}")
