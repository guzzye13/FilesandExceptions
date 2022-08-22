print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:  # try block including only the code that might give an error.
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:  # tells python how to respond when ZeroDivisionError arises.
        print("You can't divide by 0.")
    else:  # if successful we use the else block
        print(answer)