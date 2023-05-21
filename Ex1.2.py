# Define a function to get user input for a new password
def get_password_input(message):
    return input(message)

# Define a function to check if the passwords match
def check_passwords_match(password, password_again):
    if password == password_again:
        print("Thank you.")
    elif password.lower() == password_again.lower():
        print("They must be in the same case")
    else:
        print("incorrect")

# Define the main function
def main():
    password = get_password_input("Enter a new password: ")
    password_again = get_password_input("Enter the password again: ")
    check_passwords_match(password, password_again)

if __name__ == "__main__":
    main()