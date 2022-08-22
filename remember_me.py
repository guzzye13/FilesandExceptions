import json

username = input("What is your name? ")  # prompt for username to store

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)   # pass a username and file object to store the username in a file
    print("We'll remember you when you come back, " + username + "!")