def convert_to_integer(user_input):
    try:
        result = int(user_input)
        return result
    except ValueError:
        return ValueError("The input is not a valid integer.")

user_input = input("Enter a number: ")
try:
    converted_number = convert_to_integer(user_input)
    print(f"The entered number is {converted_number}.")
except ValueError as e:
    print(f"Error: {e}")
