print("Welcome! Enter what you want to calculate.")
calc = input("> ")

try:
    print(eval(calc))
except NameError:
    print("Invalid input: please check your calculation and try again.")
except Exception as e:
    print(f"An error occurred: {e}")