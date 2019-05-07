#!/usr/bin/env python

input = open("../sample_data/changedetection.dat", "r")
lines = [ line.strip() for line in  input.readlines() ]
document = lines[:lines.index("/HTML") + 1]
changes = lines[lines.index("/HTML") + 1:]

for change_line in changes:
    change = change_line.split()[1].strip()
    elements = document[document.index(change) + 1:document.index("/" + change)]
    results = [ ]
    while len(elements) > 0:
        element = elements[0]
        results.append(element)
        elements = elements[elements.index("/" + element) + 1:]
    print(" ".join(results))

