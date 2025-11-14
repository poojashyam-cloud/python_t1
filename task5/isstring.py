is_number = lambda s: s.replace('.', '', 1).replace('-', '', 1).isdigit()
if __name__ == "__main__":
    user_input = input("Enter a string: ").strip()

    # Validate and display result
    if is_number(user_input):
        print(f"'{user_input}' is a valid number.")
    else:
        print(f"'{user_input}' is NOT a valid number.")