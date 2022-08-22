import json

filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)  # json.load() to read information stored in username.json into the variable username.
    print("Welcome back, " + username + "!")  #