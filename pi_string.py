filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''  # create a variable, to hold digits of pi.
for line in lines:  # created a for loop to add each line of digits to pi_string
    # removes newline character from each line.
    pi_string += line.strip()

#print(pi_string)  # print the string
#print(len(pi_string))  # print length of the string
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:  # Check if string is in pi_string
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")