def inputnumber(message):
    while True:
        try:
            userInput = float(input(message))
            if userInput <= 0:
                message = "Not a positive number! Try again. \n >> "
            else:
                return userInput
        except ValueError:
            message = "Not a number! Try again. \n >> "

def inputlength():
    length = inputnumber("Enter the length of the square's side: ")
    return length

def inputbase_height():
    base = inputnumber("Enter the base of the triangle: ")
    height = inputnumber("Enter the height of the triangle: ")
    return base, height

def square(length):
    area = length ** 2
    print("The area of the square is: " + str(area) + "\n")

def triangle(base,height):
    area = 0.5 * base * height
    print("The area of the triangle is: " + str(area) + "\n")

def display_menu():
    print("\t===================")
    print("\t MENU")
    print("\t===================")
    print("\t 1) Square \n")
    print("\t 2) Triangle \n")
    print("\t 3) End program \n")

def get_choice():
    choice = inputnumber('Choose the function (1 - 3):')
    if choice in [1, 2, 3]:
        return choice
    else:
        print("Error: Invalid input. Please enter 1, 2 or 3.")

def main():
    while True:
        display_menu()
        choice = get_choice()
        if choice == 3:
            break
        elif choice == 1:
            length = inputlength()
            square(length)
        elif choice == 2:
            base, height = inputbase_height()
            triangle(base,height)

if __name__ == '__main__':
    main()