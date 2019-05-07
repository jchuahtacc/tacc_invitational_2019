#!/usr/bin/env python

input = open("../sample_data/onboarding.dat", "r")
lines = input.readlines()

users = { }

steps = lines[0].split()[1:]
events = lines[1:]

for event in events:
    tokens = event.split()
    username = tokens[0]
    stepname = tokens[1]
    state = tokens[2]
    if username not in users:
        users[username] = { }
        for step in steps:
            users[username][step] = "INCOMPLETE"
    users[username][stepname] = state.strip()

user_list = [ (username, steps) for username, steps in users.items() ]
user_list.sort(key=lambda item: item[0])

for user in user_list:
    username = user[0]
    output = username + " "
    steps = user[1]
    setup_complete = True
    for step, status in steps.items():
        if status != "COMPLETE":
            setup_complete = False
            output += step + " " + status
            break
    if setup_complete:
        output += "SETUP_COMPLETE"
    print(output)

