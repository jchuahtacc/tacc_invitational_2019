#!/usr/bin/env python
# coding: utf-8

input = open("../sample_data/allocations.dat", "r")
lines = input.readlines()

def getGigabytes(tokens):
    data = int(tokens[0])
    unit = tokens[1]
    volume = 1
    if unit == 'TERABYTES':
        volume = 1024
    elif unit == 'PETABYTES':
        volume = 1024 * 1024
    return data * volume

for line in lines:
    tokens = [ token.strip() for token in line.split() ]
    system = tokens[0]
    if system in [ 'STAMPEDE2', 'LONESTAR5']:
        nodes = int(tokens[1])
        hours = int(tokens[3])
        jobs = int(tokens[5])
        print(nodes * hours * jobs)
    elif system in [ 'CORRAL', 'RANCH' ]:
        gigabytes = getGigabytes(tokens[1:])
        print(gigabytes)
    elif system == 'HIKARI':
        cores = int(tokens[1])
        nodes = int(tokens[3])
        hours = int(tokens[5])
        jobs = int(tokens[7])
        print(cores * nodes * hours * jobs)
    elif system == 'WRANGLER':
        nodes = int(tokens[1])
        hours = int(tokens[3])
        jobs = int(tokens[5])
        gigabytes = getGigabytes(tokens[7:])
        print(nodes * hours * jobs + gigabytes)

