import string  # Import the string module to access predefined sets of characters

def check_password_complexity(password):
    # Define sets of characters for each category
    has_uppercase = any(char in string.ascii_uppercase for char in password)  # Check if password has uppercase letters
    has_lowercase = any(char in string.ascii_lowercase for char in password)  # Check if password has lowercase letters
    has_digit = any(char.isdigit() for char in password)  # Check if password has digits
    has_symbol = any(char in string.punctuation for char in password)  # Check if password has symbols

    # Determine which requirements are missing
    missing_requirements = []
    if not has_uppercase:
        missing_requirements.append("Missing A-Z")  # Add message if uppercase letters are missing
    if not has_lowercase:
        missing_requirements.append("Missing a-z")  # Add message if lowercase letters are missing
    if not has_digit:
        missing_requirements.append("Missing 0-9")  # Add message if digits are missing
    if not has_symbol:
        missing_requirements.append("Missing @*$% symbols")  # Add message if symbols are missing

    # Provide feedback to the user based on the missing requirements
    if missing_requirements:
        print("Password is not valid!")  # Inform user that password is not valid
        for req in missing_requirements:
            print(f"- {req}")  # Print each missing requirement
        password_again = input("Enter your password: ")  # Prompt user to enter password again
        check_password_complexity(password_again)  # Recursively check complexity of new password
    else:
        print("Valid Password")  # Inform user that password is valid

# Example usage:
if __name__ == "__main__":
    password = input("Enter your password: ")  # Prompt user to enter a password
    check_password_complexity(password)  # Call the function to check password complexity
