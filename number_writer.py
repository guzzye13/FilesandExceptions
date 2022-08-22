# USING json.dump() AND json.load()

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json' # filename to store the numbers.
with open(filename, 'w') as f_obj:  # open in write mode, allows json to write data to the file.
    json.dump(numbers, f_obj)  # json.dump() to store set of numbers

filename = 'numbers.json'  # make sure to use the same filename
# json.load() to read the list back into memory

with open(filename) as f_obj:  # open it in the read mode
    numbers = json.load(f_obj)  # json.load() to load information, we store it in variable numbers.

print(numbers)