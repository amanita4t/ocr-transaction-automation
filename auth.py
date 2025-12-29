import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def password_strength(password):
    length_rule = len(password) >= 8
    uppercase_rule = bool(re.search(r'[A-Z]', password))
    lowercase_rule = bool(re.search(r'[a-z]', password))
    digit_rule = bool(re.search(r'[0-9]', password))
    special_char_rule = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    if all([length_rule, uppercase_rule, lowercase_rule, digit_rule, special_char_rule]):
        return "Strong"
    elif length_rule and (uppercase_rule or lowercase_rule) and (digit_rule or special_char_rule):
        return "Moderate"
    else:
        return "Weak"


def verify_credentials(sheet, email, password):
    credentials_sheet = sheet.worksheet("user credentials")
    data = credentials_sheet.get_all_values()[1:]
    for row in data:
        if row[0] == email:
            return row[1] == password
    return False


def user_access(sheet):
    while True:
        user_type = input("Are you new user? (y/n): ").lower()
        if user_type in ["y", "n"]:
            break
        print("Please respond with y or n only.")

    if user_type == "y":
        while True:
            email = input("Email address: ")
            if not is_valid_email(email):
                print("Invalid email format.")
                continue

            rows = sheet.worksheet("user credentials").get_all_values()[1:]
            if any(email == row[0] for row in rows):
                print("Account already exists.")
                continue
            break

        while True:
            password = input("Create password: ")
            strength = password_strength(password)
            if strength != "Strong":
                print("Password too weak.")
                continue

            confirm = input("Confirm password: ")
            if password != confirm:
                print("Passwords do not match.")
                continue
            break

        while True:
            username = input("Username: ")
            if username not in [ws.title for ws in sheet.worksheets()]:
                sheet.add_worksheet(title=username, rows=100, cols=26)
                sheet.worksheet("user credentials").append_row([email, password, username])
                print("Signup successful.")
                return username
            print("Username already taken.")

    else:
        while True:
            email = input("Email: ")
            password = input("Password: ")
            if verify_credentials(sheet, email, password):
                rows = sheet.worksheet("user credentials").get_all_values()[1:]
                for row in rows:
                    if row[0] == email:
                        return row[2]
            print("Invalid credentials.")
