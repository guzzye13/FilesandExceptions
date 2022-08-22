# WRITING TO A FILE
filename = 'programming.txt'

with open(filename, 'w') as file_object:  # first argument = name of file we want to open
    # second argument 'w' tells python we want to open the file in write mode.
    file_object.write("I love programming!\n")
    file_object.write("I love creating new games.\n")

# APPENDING TO A FILE
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
