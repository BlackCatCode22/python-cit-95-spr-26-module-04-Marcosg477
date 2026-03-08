# Worked Exercise 7.1
# This program asks the user for numbers and stores them in a list.
# When the user types "done", it prints the maximum and minimum values.

numbers = []

while True:
    user_input = input("Enter a number (or type 'done'): ")

    if user_input == "done":
        break

    try:
        value = float(user_input)
        numbers.append(value)
    except:
        print("Invalid input")

if len(numbers) > 0:
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
else:
    print("No numbers were entered.")