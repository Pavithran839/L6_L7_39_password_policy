def first_character_type(pw):
    if not isinstance(pw, str) or len(pw) == 0:
        return None
    ch = pw[0]
    if ch.isdigit():
        return 'digit'
    if ch.isalpha():
        return 'letter'
    return 'symbol'


def split_credentials(text):
    if not isinstance(text, str) or ':' not in text:
        return None
    user, password = text.split(':', 1)
    return user.strip(), password.strip()


def digit_ratio(pw):
    if not isinstance(pw, str) or len(pw) == 0:
        return None
    return sum(c.isdigit() for c in pw) / len(pw)


def main():
    print("==== Running first_character_type ====")
    user_input = input("Enter a password: ")
    result = first_character_type(user_input)
    print("First Character Type:", result if result else "Invalid input (empty password)")

    print("\n==== Running split_credentials ====")
    user_input = input("Enter user:password (e.g. alice:Secret1): ")
    result = split_credentials(user_input)
    print("User and Password:", result if result else "Invalid format (expected user:password)")

    print("\n==== Running digit_ratio ====")
    user_input = input("Enter a password to measure: ")
    result = digit_ratio(user_input)
    print("Digit Ratio:", result if result is not None else "Invalid input (empty password)")


if __name__ == "__main__":
    main()
