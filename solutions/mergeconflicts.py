#!/usr/bin/env python

input = open("../sample_data/mergeconflicts.dat", "r")
lines = input.readlines()

timestamp = 0
branches = {
    "master" : { }
}

master = branches["master"]

for line in lines:
    timestamp += 1
    tokens = [ token.strip() for token in line.split() ]
    if tokens[0] == "COMMIT":
        if tokens[1] not in branches:
            branches[tokens[1]] = { }
        branch = branches[tokens[1]]
        files = tokens[2:]
        for file in files:
            branch[file] = timestamp
    elif tokens[0] == "MERGE":
        automerge = [ ]
        conflicts = [ ]
        branch = branches[tokens[1]]
        for file, timestamp in branch.items():
            if file not in master:
                automerge.append(file)
                master[file] = timestamp
            else:
                if master[file] < timestamp:
                    automerge.append(file)
                    master[file] = timestamp
                else:
                    conflicts.append(file)
        output = ""
        if len(automerge) > 0:
            output = "AUTOMERGE " + " ".join(automerge)
        if len(conflicts) > 0:
            if len(output) > 0:
                output += " "
            output += "CONFLICT " + " ".join(conflicts)
        print(output)
