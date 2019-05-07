#!/usr/bin/env python

input = open("../sample_data/paginator.dat", "r")
lines = input.readlines()

for line in lines:
    tokens = line.split()
    current = int(tokens[0])
    total = int(tokens[1])
    start = current - 2
    end = current + 2
    if start < 1:
        start = 1
    if end > total:
        end = total
    output = " ".join([ str(num) for num in range(start, end + 1, 1)])
    if start > 1:
        output = "... " + output
    if end < total:
        output = output + " ..."
    print(output)
        

