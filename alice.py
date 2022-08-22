#HANDLING THE FILENOTFOUNDERROR EXCEPTION
filename = 'programming.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist"
    print(msg)
else:
    # count the number of words in the file
    words = contents.split()  # split() to produce a list of all the words.
    num_words = len(words)  # len() to examine length, get an approximation of the number
    # of words in the string.
    print("The file " + filename + " has about " + str(num_words) + " words.")