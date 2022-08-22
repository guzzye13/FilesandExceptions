with open('pi_digits.txt') as file_object:  # need to use open() function
    # to do any work with a file.
    # with closes the file once access to it is no longer needed.
    contents = file_object.read()
    print(contents.rstrip())  # rstrip() removes, or strips
    # any whitespace characters from the right side of a string.

# READING LINE BY LINE
filename = 'pi_digits.txt'  # store the name of the file in the variable filename

with open(filename) as file_object:  # file and its contents is store in the variable file_object
    for line in file_object:  # we work through each line in the file by looping over the file object.
        print(line)